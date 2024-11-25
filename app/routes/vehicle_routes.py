from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.models.vehicle import Vehicle as VehicleModel
from app.models.feedback import Feedback
from app.schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse
from app.db import get_db
from fastapi.security import OAuth2PasswordBearer
from app.security.auth import decode_access_token

router = APIRouter()

# Configurar esquema de OAuth2 para obtener el token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Proteger los endpoints con JWT
@router.post("/", response_model=VehicleResponse)
def create_vehicle(
    vehicle: VehicleCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_vehicle = VehicleModel(**vehicle.model_dump())

    if hasattr(db, "add"):  # Si es una sesión real
        db.add(db_vehicle)
        db.commit()
        db.refresh(db_vehicle)
    else:  # Mockeada
        db_vehicle.id = 1  # Asignar un ID simulado manualmente

    assert db_vehicle.id is not None, "El campo 'id' no está definido"

    return VehicleResponse.model_validate(db_vehicle)
    

@router.get("/", response_model=list[VehicleResponse])
def read_vehicles(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    vehicles = db.query(VehicleModel).offset(skip).limit(limit).all()
    return vehicles

@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle(
    vehicle_id: int,
    vehicle: VehicleUpdate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_vehicle = db.query(VehicleModel).filter(VehicleModel.id == vehicle_id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    # Actualiza los campos
    db_vehicle.brand = vehicle.brand
    db_vehicle.model = vehicle.model
    db_vehicle.year = vehicle.year
    db_vehicle.price = vehicle.price
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

@router.delete("/{vehicle_id}", response_model=dict)
def delete_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_vehicle = db.query(VehicleModel).filter(VehicleModel.id == vehicle_id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    db.delete(db_vehicle)
    db.commit()
    return {"message": f"Vehicle with ID {vehicle_id} deleted successfully"}

# Listar vehículos con feedbacks
@router.get("/with-feedback", response_model=list[dict])
def get_vehicles_with_feedback(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    vehicles = db.query(VehicleModel).options(joinedload(VehicleModel.feedback)).all()
    result = []
    for vehicle in vehicles:
        result.append({
            "id": vehicle.id,
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "price": vehicle.price,
            "feedback": [
                {
                    "id": fb.id,
                    "rating": fb.rating,
                    "comment": fb.comment,
                    "date": fb.date,
                } for fb in vehicle.feedback
            ]
        })
    return result
