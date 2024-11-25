from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.credit_application import CreditApplication as CreditApplicationModel
from app.models.buyer import Buyer
from app.models.vehicle import Vehicle
from app.schemas.credit_application import CreditApplicationCreate, CreditApplicationResponse
from app.db import get_db
from fastapi.security import OAuth2PasswordBearer
from app.security.auth import decode_access_token

router = APIRouter()

# Configurar esquema de OAuth2 para obtener el token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/", response_model=CreditApplicationResponse)
def create_credit_application(
    application: CreditApplicationCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_application = CreditApplicationModel(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@router.get("/{application_id}", response_model=CreditApplicationResponse)
def get_credit_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(CreditApplicationModel).filter(CreditApplicationModel.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Credit application not found")
    return application

@router.delete("/{application_id}", response_model=dict)
def delete_credit_application(application_id: int, db: Session = Depends(get_db)):
    db_application = db.query(CreditApplicationModel).filter(CreditApplicationModel.id == application_id).first()
    if not db_application:
        raise HTTPException(status_code=404, detail="Credit application not found")
    db.delete(db_application)
    db.commit()
    return {"message": f"Credit application with ID {application_id} deleted successfully"}
