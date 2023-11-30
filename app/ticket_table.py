from sqlalchemy import Column, Integer, String

from db import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    state = Column(String)
    severity = Column(String)
    priority = Column(String)
    date_creacion = Column(String)

    client_id = Column(Integer)
    product_id = Column(Integer, index=True)

