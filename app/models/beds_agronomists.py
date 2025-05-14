from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class BedAgronomist(Base):
    __tablename__ = "beds_agronomists"

    id = Column(Integer, primary_key=True)
    agronomist_id = Column(Integer, ForeignKey("agronomist.id"))
    bed_id = Column(Integer, ForeignKey("beds.id"))

    agronomist = relationship("Agronomist", back_populates="beds")
    bed = relationship("Bed", back_populates="agronomists")
