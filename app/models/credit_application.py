from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.credit_application import CreditApplication

class CreditApplication(Base):
    __tablename__ = "credit_applications"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("buyers.id"), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    approved_limit = Column(Float, nullable=True)
    status = Column(String, default="Pending")

    # Relaciones
    buyer = relationship("Buyer", back_populates="credit_applications")  # Relación con Buyer
    vehicle = relationship("Vehicle", back_populates="credit_applications")  # Relación con Vehicle
