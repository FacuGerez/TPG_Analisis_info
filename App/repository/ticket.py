from sqlalchemy.orm import Session
from ..database.ticket import Ticket


# from ..model.ticket import .

class TicketRepository:
    def __init__(self, db: Session):
        self.db: Session = db

    def get_ticket(self, ticket_id: int):
        return self.db.query(Ticket).get(ticket_id)

    def get_tickets(self):  # skip: int = 0, limit: int = 100 para poner un limite
        return self.db.query(Ticket).all()

    def save_tickets(self, ticket: Ticket):
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def delete(self, ticket: Ticket):
        self.db.delete(ticket)
        self.db.commit()
        return None
