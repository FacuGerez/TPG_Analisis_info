from fastapi import HTTPException
from sqlalchemy.orm import Session

from ticket_model import TicketCreate
from ticket_repository import TicketRepository
from ticket_table import Ticket


class TicketService:
    def __init__(self, db: Session):
        self.ticket_repository: TicketRepository = TicketRepository(db)

    def get_tickets(self, product_id: int) -> list[[Ticket]]:
        return self.ticket_repository.get_tickets(product_id)

    def get_ticket(self, ticket_id: int) -> Ticket:
        return self.ticket_repository.get_ticket(ticket_id)

    def create_ticket(self, ticket: TicketCreate, product_id: int, client_id: int) -> Ticket:
        ticket_data = ticket.dict()
        ticket_data.update({
            "client_id": client_id,
            "product_id": product_id
        })
        ticket_nuevo = Ticket(**ticket_data)
        return self.ticket_repository.save_tickets(ticket_nuevo)

    def update_ticket(self, ticket_id: int, ticket: TicketCreate):
        ticket_actualizable = self.ticket_repository.get_ticket(ticket_id)
        if ticket_actualizable is None:
            raise HTTPException(status_code=400, detail="El ticket no fue encontrado")
        ticket_actualizable.state = ticket.state
        ticket_actualizable.priority = ticket.priority
        ticket_actualizable.severity = ticket.severity
        ticket_actualizable.title = ticket.title
        return self.ticket_repository.save_tickets(ticket_actualizable)

    def delete_ticket(self, ticket_id: int):
        ticket_eliminable = self.ticket_repository.get_ticket(ticket_id)
        if ticket_eliminable is None:
            raise HTTPException(status_code=404, detail="El ticket no fue encontrado")
        return self.ticket_repository.delete(ticket_eliminable)
