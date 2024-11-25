from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

# URL de conexión a la base de datos
DATABASE_URL = "postgresql://kavak_user:kavak_password@kavakchallenge-db-1:5432/kavak_db"

# Configuración de SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        # Manejo de errores durante la sesión
        print(f"Error en la sesión de base de datos: {e}")
        raise
    finally:
        db.close()

# Validar conexión inicial a la base de datos (opcional)
def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))  # Usar `text` para consultas SQL
        print("Conexión a la base de datos exitosa.")
    except SQLAlchemyError as e:
        print(f"Error al conectar con la base de datos: {e}")
        raise
