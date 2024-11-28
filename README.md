# **Kavak Backend Challenge**

Este proyecto implementa un modelo de predicción de aprobación de créditos utilizando **FastAPI** como framework principal, **PostgreSQL** como base de datos, y **scikit-learn** para el entrenamiento del modelo de machine learning. La solución está completamente **dockerizada** para garantizar la portabilidad y la facilidad de despliegue.

## Funcionalidades Implementadas

- **Estructura Backend con FastAPI**:
   Endpoints CRUD para administrar Buyers, Vehicles, Credit Applications y Feedback.
   Validaciones de datos utilizando Pydantic.
- **Entrenamiento de un modelo de Machine Learning**:
   Modelo entrenado para predecir la aprobación de créditos (Approved, Denied) basado en las características del comprador y el vehículo.
   Almacenamiento del modelo en formato .joblib.
- **Autenticación con JWT**: La aplicación incluye un sistema de autenticación basado en JWT para proteger los endpoints. Solo los usuarios autenticados pueden acceder a ciertas funcionalidades.
- **Base de datos relacional**:
   Uso de PostgreSQL para almacenar datos estructurados.
   Datos iniciales predefinidos cargados mediante un script de seed.
- **Dockerización**:Todo el proyecto se puede ejecutar en cualquier entorno utilizando Docker.
- **Pruebas Unitarias**: Se incluyen pruebas básicas para validar la funcionalidad de los endpoints.
- **Interactive API Documentation**: Documentación Swagger y ReDoc generada automáticamente.

---

## Características del Modelo de Machine Learning

- **Entrenamiento**: 
  - Modelo: **Random Forest Classifier**.
  - Características utilizadas:
    - `income`: Ingresos del comprador.
    - `credit_score`: Puntuación crediticia.
    - `age`: Edad del comprador.
    - `vehicle_price`: Precio del vehículo.
    - `occupation`: Ocupación del comprador.
  - Variable objetivo:
    - `status`: Aprobado (`1`) o Denegado (`0`).
  - Datos de entrenamiento y prueba divididos al 80/20.

---

## Requisitos

- **Python 3.9+**
- **Docker y Docker Compose**
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- **PostgreSQL**
- Bibliotecas principales:
  - `FastAPI`
  - `scikit-learn`
  - `SQLAlchemy`
  - `Pandas`
  - `Joblib`

---

## Instrucciones para Configuración y Ejecución

# 1. **Clonar el Repositorio**
git clone <URL_DEL_REPOSITORIO>

cd <NOMBRE_DEL_REPOSITORIO>

# 2. Configurar el Entorno
⚠️ **Este paso ya no es necesario.**  
Las credenciales de conexión a la base de datos están configuradas directamente en el archivo docker-compose.yml. No necesitas crear un archivo .env adicional.

**Detalles de configuración ya integrados:**
- **Usuario:** kavak_user
- **Contraseña:** kavak_password
- **Host:** kavakchallenge-db-1 (interno al contenedor Docker)
- **Puerto:** 5432 (puerto estándar de PostgreSQL)
- **Base de datos:** kavak_db

Puedes continuar directamente con la siguiente sección.


**Instalar las dependencias necesarias**:
pip install -r requirements.txt

# 3. **Ejecutar con Docker**:
docker-compose up --build

# 4. **Acceso a la Documentación Autogenerada**
La aplicación incluye documentación autogenerada para consultar todos los endpoints disponibles, sus métodos, parámetros y respuestas.

- **API Documentation (Swagger):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
  Aquí encontrarás una interfaz interactiva para probar y explorar todos los endpoints de la API.

- **API Documentation (ReDoc):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
  Esta vista ofrece una documentación estructurada con detalles de todos los endpoints disponibles en la API.


# 5. **¿Cómo entrenar el modelo?**:
python machine_learning/train_model.py

---
# **Project Architecture**

```
/KAVAKCHALLENGE
├── app/
│   ├── main.py                   # Application entry point
│   ├── db.py                     # Database configuration and session management
│   ├── config.py
│   ├── create_tables.py
│   ├── models/                   # Database models
│   │   ├── __init__.py
│   │   ├── buyer.py
│   │   ├── credit_application.py
│   │   ├── vehicle.py
│   │   └── feedback.py
│   ├── routes/                   # API endpoints
│   │   ├── __init__.py
│   │   ├── buyer_routes.py
│   │   ├── credit_application_routes.py
│   │   ├── vehicle_routes.py
│   │   └── feedback_routes.py
│   ├── schemas/                   # API endpoints
│   │   ├── __init__.py
│   │   ├── buyer.py
│   │   ├── credit_application.py
│   │   ├── vehicle.py
│   │   └── feedback.py
│   ├── security/                   # API endpoints
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── users.py
│   ├── tests/                    # Test cases
│   │   ├── __init__.py
│   │   └── test_endpoints.py
├── machine_learning/  
│   ├── train_model.py            # Script to train the model
│   └── credit_model.joblib       # Trained model
├── seed_data_files/              # Initial project data
│   ├── __init__.py
│   ├── buyers_data.py
│   ├── credit_applications_data.py
│   ├── feedback_data.py
│   └── vehicles_data.joblib
├── docker-compose.yml            # Docker Compose configuration
├── Dockerfile                    # Dockerfile for the application
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation
```
---

## **Autenticación con JWT**
La aplicación incluye un sistema de autenticación basado en JWT para proteger los endpoints. Solo los usuarios autenticados pueden acceder a ciertas funcionalidades.

**Endpoint para obtener un token JWT**:
POST /token: Permite a los usuarios autenticarse con credenciales (nombre de usuario y contraseña) y recibir un token JWT en respuesta.

# **Configuración en Postman**
# 1. **Obtener el Token JWT**
**Crear una nueva solicitud en Postman**:
- Método: POST
- URL: http://<tu-servidor>/token
- Configurar el cuerpo de la solicitud:

Selecciona la opción Body -> x-www-form-urlencoded.
- Añade las siguientes claves y valores:
- username: testuser (usuario registrado)
- password: password123 
- Enviar la solicitud:
   Haz clic en el botón Send.
Si las credenciales son correctas, recibirás un token en la respuesta, similar a:
json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

# 2. **Usar el Token en Otros Métodos Protegidos**
**Crear una nueva solicitud en Postman**:

Método: Elige el método correspondiente al endpoint (GET, POST, PUT, DELETE, etc.).
URL: http://127.0.0.1:8000/<endpoint>/

Añadir el token en los encabezados:
- Ve a la pestaña Headers.
- Añade el encabezado:
      Key: Authorization
      Value: Bearer <tu_token> (reemplaza <tu_token> con el token obtenido anteriormente).
- Enviar la solicitud:
- Configura los parámetros del cuerpo si es necesario (por ejemplo, en un POST o PUT).
- Haz clic en Send.

---

## **API Endpoints**

## **Vehicles**
- `POST /vehicles/`: Add a new vehicle.
- `GET /vehicles/`: Retrieve a list of vehicles.
- `GET /vehicles/with-feedback/`: Retrieve a list of vehicles with feedback.
- `PUT /vehicles/{id}`: Update vehicle details.
- `DELETE /vehicles/{id}`: Remove a vehicle from inventory.

## **Feedback**
- `POST /feedback/`: Submit feedback for a vehicle.
- `GET /feedback/`: Retrieve feedback for all vehicles.

## **Buyers**
- `POST /buyers/`: Add a new buyer.
- `GET /buyers/`: Retrieve a list of buyers.
- `GET /buyers/{id}`: Retrieve details of a specific buyer.
- `GET /buyers/with-credit-applications/`: Retrieve a list of buyers with credit application.
- `PUT /buyers/{id}`: Update buyer details.
- `DELETE /buyers/{id}`: Remove a buyer.

## **Credit Applications**
- `POST /credit_applications/`: Submit a new credit application.
- `GET /credit_applications/`: Retrieve a list of credit applications.
- `GET /credit_applications/{id}`: Retrieve details of a specific credit application.
- `PUT /credit_applications/{id}`: Update credit application details.
- `DELETE /credit_applications/{id}`: Remove a credit application.

---

## **Futuras Implementaciones**

- Implementar filtros avanzados y opciones de ordenamiento en las consultas de vehículos.
- Desarrollar una interfaz frontend, potencialmente con React, para mejorar la interacción de los usuarios.
- Integrar funcionalidades de Machine Learning adicionales, como recomendaciones personalizadas o análisis predictivo más detallado.

---

