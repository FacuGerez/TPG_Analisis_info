from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tickets = relationship("Ticket", back_populates="owner")
