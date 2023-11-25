from sqlalchemy.orm import Session
from ticket_table import Ticket


class TicketRepository:
    def __init__(self, db: Session):
        self.db: Session = db

    def get_ticket(self, ticket_id: int) -> Ticket:
        return self.db.query(Ticket).get(ticket_id)

    def get_tickets(self, product_id: int) -> list[
        Ticket]:  # skip: int = 0, limit: int = 100 para poner un limite
        return self.db.query(Ticket).filter(Ticket.product_id == product_id).all()

    #Por si implementamos busqueda por titulo
    def get_tickets_by_title(self, title: str) -> list[Ticket]: 
        return self.db.query(Ticket).filter(Ticket.title == title).all()

    def save_tickets(self, ticket: Ticket) -> Ticket:
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def delete(self, ticket: Ticket):
        self.db.delete(ticket)
        self.db.commit()
        return None
