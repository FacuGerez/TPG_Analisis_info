from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from ticket_model import TicketCreate, TicketUpdate
from ticket_service import TicketService
from assignment_service import AssignmentService

router = APIRouter(
    prefix="/product/{product_id}/version/{version_id}/ticket",
    tags=["ticket"],
)


@router.post("/client/{client_id}")
async def create_ticket(version_id: int, client_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.create_ticket(ticket, version_id, client_id)


@router.get("/")
async def get_tickets_by_version(version_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.get_tickets(version_id)


@router.get("/{ticket_id}")
async def get_ticket_by_id(ticket_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.get_ticket(ticket_id)


@router.put("/{ticket_id}")
async def update_ticket(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.update_ticket(ticket_id, ticket)


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    service_assigment: AssignmentService = AssignmentService(db)

    service_assigment.delete_by_ticket(ticket_id)
    return service_ticket.delete_ticket(ticket_id)
