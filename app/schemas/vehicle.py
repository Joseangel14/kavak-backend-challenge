from pydantic import BaseModel, ConfigDict
from typing import Optional  # Importar Optional para compatibilidad con Python 3.9

# Base para evitar redundancia entre esquemas
class VehicleBase(BaseModel):
    brand: str
    model: str
    year: int
    price: float

    # Configuración para compatibilidad con Pydantic v2
    model_config = ConfigDict(from_attributes=True)

# Esquema para creación de vehículos
class VehicleCreate(VehicleBase):
    pass

# Esquema para actualización de vehículos
class VehicleUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    price: Optional[float] = None

    # Configuración para compatibilidad con Pydantic v2
    model_config = ConfigDict(from_attributes=True)

# Esquema para respuesta
class VehicleResponse(VehicleBase):
    id: int  # Incluye el identificador en las respuestas
