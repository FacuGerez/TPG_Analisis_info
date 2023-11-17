from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from App.database.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    severity = Column(String)
    priority = Column(String)
    state = Column(String)
    client_id = Column(Integer)
    product_id = Column(Integer, index=True)
