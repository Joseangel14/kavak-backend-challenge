from pydantic import BaseModel
from typing import Optional, List
from app.schemas.credit_application import CreditApplicationResponse  # Importa el esquema de CreditApplicationResponse

class BuyerBase(BaseModel):
    """Base model para atributos compartidos entre los esquemas."""
    name: str
    age: int
    income: float
    credit_score: int
    occupation: str

class BuyerCreate(BuyerBase):
    """Esquema para crear un nuevo Buyer."""
    pass

class BuyerUpdate(BaseModel):
    """Esquema para actualizar un Buyer."""
    name: Optional[str]
    age: Optional[int]
    income: Optional[float]
    credit_score: Optional[int]
    occupation: Optional[str]

class BuyerResponse(BuyerBase):
    """Esquema para la respuesta de un Buyer, incluye relaciones."""
    id: int
    credit_applications: List[CreditApplicationResponse] = []  # Incluye solicitudes de crédito relacionadas

    class Config:
        from_attributes = True  # Sustituye a orm_mode en Pydantic v2
