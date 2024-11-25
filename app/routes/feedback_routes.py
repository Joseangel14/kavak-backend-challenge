from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.feedback import Feedback as FeedbackModel
from app.models.vehicle import Vehicle as VehicleModel
from app.schemas.feedback import FeedbackCreate, FeedbackResponse, FeedbackUpdate
from app.db import get_db
from fastapi.security import OAuth2PasswordBearer
from app.security.auth import decode_access_token

router = APIRouter()

# Configurar esquema de OAuth2 para obtener el token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/", response_model=FeedbackResponse)
def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    # Verificar si el vehículo existe
    vehicle = db.query(VehicleModel).filter(VehicleModel.id == feedback.vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db_feedback = FeedbackModel(**feedback.model_dump())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

@router.get("/", response_model=list[FeedbackResponse])
def read_feedback(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    feedbacks = db.query(FeedbackModel).offset(skip).limit(limit).all()
    return feedbacks

@router.put("/{feedback_id}", response_model=FeedbackResponse)
def update_feedback(
    feedback_id: int,
    feedback: FeedbackUpdate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_feedback = db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id).first()
    if not db_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")

    # Actualizar solo los campos proporcionados
    for key, value in feedback.model_dump(exclude_unset=True).items():
        setattr(db_feedback, key, value)
    
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

@router.delete("/{feedback_id}")
def delete_feedback(
    feedback_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_feedback = db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id).first()
    if not db_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")

    db.delete(db_feedback)
    db.commit()
    return {"message": "Feedback deleted successfully"}
