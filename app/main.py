from app.routes.vehicle_routes import router as vehicle_router
from app.routes.feedback_routes import router as feedback_router
from app.routes.buyer_routes import router as buyer_router
from app.routes.credit_application_routes import router as credit_application_router
from app.db import Base, engine, test_connection  # Importa test_connection
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.security.auth import create_access_token
from app.security.users import authenticate_user
from seed_data import seed_vehicles_and_feedback, seed_buyers_and_credit_applications  # Importa la función de llenado para vehículos y feedback
from contextlib import asynccontextmanager

# Usar asynccontextmanager para manejar el ciclo de vida de la aplicación
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Verificar conexión a la base de datos
    print("Verificando conexión a la base de datos...")
    test_connection()  # Llama a la función para validar la conexión
    print("Conexión a la base de datos exitosa.")

    # Crear tablas al iniciar
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("¡Tablas creadas con éxito!")

    # Llenar la base de datos con datos iniciales
    print("Insertando datos iniciales...")
    seed_vehicles_and_feedback()
    seed_buyers_and_credit_applications()
    print("¡Datos iniciales insertados con éxito!")

    yield  # Aquí se mantiene la aplicación activa

# Crear la aplicación FastAPI
app = FastAPI(lifespan=lifespan)

# Endpoint para obtener el token JWT
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Registrar las rutas protegidas con JWT
app.include_router(vehicle_router, prefix="/vehicles")
app.include_router(feedback_router, prefix="/feedback")
app.include_router(buyer_router, prefix="/buyers")
app.include_router(credit_application_router, prefix="/credit_applications")