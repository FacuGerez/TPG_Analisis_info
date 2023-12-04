from sqlalchemy import Column, Integer
from app.db import Base


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer)
    task_id = Column(Integer)
