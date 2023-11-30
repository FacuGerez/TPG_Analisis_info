from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from ticket_model import TicketCreate, TicketUpdate
from ticket_service import TicketService

router = APIRouter(
    prefix="/product/{product_id}/version/{version_id}/ticket",
    tags=["ticket"],
)


@router.post("/client/{client_id}")
async def create_ticket(version_id: int, client_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    ticket_new = service_ticket.create_ticket(ticket, version_id, client_id)
    return ticket_new


@router.get("/")
async def get_tickets(version_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.get_tickets(version_id)


@router.get("/{ticket_id}")
async def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.get_ticket(ticket_id)


@router.get("/{ticket_title}")
async def get_ticket_by_title(ticket_title: str, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.get_ticket_by_title(ticket_title)


@router.put("/{ticket_id}")
async def update_ticket(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.update_ticket(ticket_id, ticket)


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.delete_ticket(ticket_id)
