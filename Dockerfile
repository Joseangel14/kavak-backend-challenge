FROM python:3.9-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar y configurar dependencias de Python
COPY requirements.txt ./requirements.txt

# Instalar las dependencias de Python y corregir bcrypt
RUN pip install --no-cache-dir -r requirements.txt \
    && pip uninstall -y bcrypt \
    && pip install bcrypt==4.0.1

# Copiar el resto del proyecto
COPY . .

# Asegurar que Python use el directorio correcto para las importaciones
ENV PYTHONPATH=/app

# Variable de entorno para distinguir entre entornos (producción o pruebas)
ENV TESTING=0

# Comando por defecto para iniciar la aplicación
CMD ["sh", "-c", "if [ \"$TESTING\" = \"1\" ]; then pytest; else python seed_data.py && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload; fi"]
