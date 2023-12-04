from sqlalchemy.orm import Session
from app.ticket_table import Ticket


class TicketRepository:
    def __init__(self, db: Session):
        self.db: Session = db

    def get_ticket(self, ticket_id: int) -> Ticket:
        return self.db.query(Ticket).get(ticket_id)

    def get_tickets(self, version_id: int) -> list[Ticket]:  # skip: int = 0, limit: int = 100 para poner un limite
        return self.db.query(Ticket).filter(Ticket.version_id == version_id).all()

    def save_tickets(self, ticket: Ticket) -> Ticket:
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def delete(self, ticket: Ticket):
        self.db.delete(ticket)
        self.db.commit()
        return True
