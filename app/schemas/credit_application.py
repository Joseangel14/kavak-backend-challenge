from pydantic import BaseModel
from typing import Optional

class CreditApplicationCreate(BaseModel):
    buyer_id: int
    vehicle_id: int

class CreditApplicationResponse(BaseModel):
    id: int
    buyer_id: int
    vehicle_id: int
    approved_limit: Optional[float] = None  # Puede ser null inicialmente
    status: str = "Pending"  # Valor predeterminado en la base de datos

    class Config:
        from_attributes = True
