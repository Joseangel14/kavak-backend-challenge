from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.credit_application import CreditApplication

class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    income = Column(Float, nullable=False)
    credit_score = Column(Integer, nullable=False)
    occupation = Column(String, nullable=False)

    # Relación inversa con CreditApplication
    credit_applications = relationship("CreditApplication", back_populates="buyer")
