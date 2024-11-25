from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    date = Column(Date, nullable=False)  # Campo para la fecha del feedback

    # Relación inversa con Vehicle
    vehicle = relationship("Vehicle", back_populates="feedback")
