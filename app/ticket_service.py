from fastapi import HTTPException
from sqlalchemy.orm import Session
from ticket_model import TicketCreate, TicketUpdate
from ticket_repository import TicketRepository
from ticket_table import Ticket
from datetime import datetime


class TicketService:
    def __init__(self, db: Session):
        self.ticket_repository: TicketRepository = TicketRepository(db)

    def get_tickets(self, version_id: int) -> list[Ticket]:
        return self.ticket_repository.get_tickets(version_id)

    def get_ticket(self, ticket_id: int) -> Ticket:
        return self.ticket_repository.get_ticket(ticket_id)

    def get_ticket_by_title(self, ticket_title: str) -> list[Ticket]:
        return self.ticket_repository.get_tickets_by_title(ticket_title)

    def create_ticket(self, ticket: TicketCreate, version_id: int, client_id: int) -> Ticket:
        ticket_data = ticket.dict()

        if ticket_data["severity"] not in ["S1", "S2", "S3", "S4"]:
            raise HTTPException(status_code=400, detail="Debe seleccionar una severidad correcta")
        if ticket_data["priority"] not in ["Alta", "Media", "Baja"]:
            raise HTTPException(status_code=400, detail="Debe seleccionar una prioridad correcta")
        if ticket_data["description"] == "":
            raise HTTPException(status_code=400, detail="Debe ingresar una descripción")

        ticket_data.update({
            "client_id": client_id,
            "version_id": version_id,
            "state": "Abierto",
            "date_creacion": datetime.now().strftime("Fecha : %d / %m / %Y , Horario : %H:%M:%S")
        })
        ticket_nuevo = Ticket(**ticket_data)
        return self.ticket_repository.save_tickets(ticket_nuevo)

    def update_ticket(self, ticket_id: int, ticket: TicketUpdate):
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
