from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.models.buyer import Buyer as BuyerModel
from app.models.credit_application import CreditApplication
from app.schemas.buyer import BuyerCreate, BuyerUpdate, BuyerResponse
from app.db import get_db
from fastapi.security import OAuth2PasswordBearer
from app.security.auth import decode_access_token

router = APIRouter()

# Configurar esquema de OAuth2 para obtener el token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/", response_model=BuyerResponse)
def create_buyer(
    buyer: BuyerCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_buyer = BuyerModel(**buyer.dict())
    db.add(db_buyer)
    db.commit()
    db.refresh(db_buyer)
    return db_buyer

@router.get("/", response_model=list[BuyerResponse])
def read_buyers(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    buyers = db.query(BuyerModel).offset(skip).limit(limit).all()
    return buyers

@router.put("/{buyer_id}", response_model=BuyerResponse)
def update_buyer(
    buyer_id: int,
    buyer: BuyerUpdate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_buyer = db.query(BuyerModel).filter(BuyerModel.id == buyer_id).first()
    if not db_buyer:
        raise HTTPException(status_code=404, detail="Buyer not found")
    for key, value in buyer.dict(exclude_unset=True).items():
        setattr(db_buyer, key, value)
    db.commit()
    db.refresh(db_buyer)
    return db_buyer

@router.delete("/{buyer_id}", response_model=dict)
def delete_buyer(
    buyer_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    db_buyer = db.query(BuyerModel).filter(BuyerModel.id == buyer_id).first()
    if not db_buyer:
        raise HTTPException(status_code=404, detail="Buyer not found")
    db.delete(db_buyer)
    db.commit()
    return {"message": f"Buyer with ID {buyer_id} deleted successfully"}

# Rutas adicionales: listar compradores con solicitudes de crédito
@router.get("/with-credit-applications", response_model=list[dict])
def get_buyers_with_credit_applications(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    username = decode_access_token(token)  # Validar el token
    buyers = db.query(BuyerModel).options(joinedload(BuyerModel.credit_applications)).all()
    result = []
    for buyer in buyers:
        result.append({
            "id": buyer.id,
            "name": buyer.name,
            "age": buyer.age,
            "income": buyer.income,
            "credit_score": buyer.credit_score,
            "occupation": buyer.occupation,
            "credit_applications": [
                {
                    "id": ca.id,
                    "vehicle_id": ca.vehicle_id,
                    "approved_limit": ca.approved_limit,
                    "status": ca.status
                } for ca in buyer.credit_applications
            ]
        })
    return result
