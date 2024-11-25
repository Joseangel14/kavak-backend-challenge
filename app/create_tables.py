from app.db import Base, engine
from app.models.vehicle import Vehicle

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
