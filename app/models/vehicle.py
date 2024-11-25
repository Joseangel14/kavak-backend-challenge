from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.credit_application import CreditApplication

class Vehicle(Base):
    __tablename__ = "vehicles"

    # Definición de columnas
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False, index=True)  # Agregado nullable=False
    model = Column(String, nullable=False, index=True)  # Agregado nullable=False
    year = Column(Integer, nullable=False, index=True)  # Agregado nullable=False
    price = Column(Float, nullable=False)              # Agregado nullable=False

    # Relación con Feedback
    feedback = relationship("Feedback", back_populates="vehicle", cascade="all, delete-orphan")
    
    # Relación con CreditApplication
    credit_applications = relationship("CreditApplication", back_populates="vehicle")