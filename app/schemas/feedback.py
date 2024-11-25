from pydantic import BaseModel, ConfigDict
from typing import Optional

class FeedbackCreate(BaseModel):
    vehicle_id: int
    rating: int
    comment: str

class FeedbackResponse(BaseModel):
    id: int
    vehicle_id: int
    rating: int
    comment: str

    # Uso de ConfigDict en lugar de class Config
    model_config = ConfigDict(from_attributes=True)

class FeedbackUpdate(BaseModel):
    rating: Optional[int]
    comment: Optional[str]

    # Uso de ConfigDict en lugar de class Config
    model_config = ConfigDict(from_attributes=True)

