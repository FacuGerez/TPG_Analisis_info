from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.ticket_model import TicketCreate, TicketUpdate
from app.ticket_repository import TicketRepository
from app.ticket_table import Ticket
from datetime import datetime


class TicketService:
    def __init__(self, db: Session):
        self.ticket_repository: TicketRepository = TicketRepository(db)

    def get_tickets(self, version_id: int) -> list[Ticket]:
        return self.ticket_repository.get_tickets(version_id)

    def get_ticket(self, ticket_id: int) -> Ticket:
        ticket: Ticket = self.ticket_repository.get_ticket(ticket_id)
        if ticket is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No se encontro el ticket deseado")
        return ticket

    def create_ticket(self, ticket: TicketCreate, version_id: int, client_id: int) -> Ticket:
        ticket_data = ticket.dict()

        if ticket_data["severity"] not in ["s1", "s2", "s3", "s4"]:
            raise HTTPException(status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail="Debe seleccionar una severidad "
                                                                                      "correcta")
        if ticket_data["priority"] not in ["alta", "media", "baja"]:
            raise HTTPException(status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail="Debe seleccionar una prioridad "
                                                                                      "correcta")
        if ticket_data["description"] == "":
            raise HTTPException(status.HTTP_204_NO_CONTENT, detail="Debe ingresar una descripción")

        ticket_data.update({
            "client_id": client_id,
            "version_id": version_id,
            "state": "Abierto",
            "date_creacion": datetime.now().strftime("Fecha : %d / %m / %Y , Horario : %H:%M:%S")
        })
        ticket_nuevo = Ticket(**ticket_data)
        return self.ticket_repository.save_tickets(ticket_nuevo)

    def update_ticket(self, ticket_id: int, ticket: TicketUpdate) -> Ticket:
        ticket_actualizable: Ticket = self.get_ticket(ticket_id)
        ticket_actualizable.state = ticket.state
        ticket_actualizable.priority = ticket.priority
        ticket_actualizable.severity = ticket.severity
        ticket_actualizable.title = ticket.title
        return self.ticket_repository.save_tickets(ticket_actualizable)

    def delete_ticket(self, ticket_id: int):
        ticket_eliminable: Ticket = self.get_ticket(ticket_id)
        return self.ticket_repository.delete(ticket_eliminable)
