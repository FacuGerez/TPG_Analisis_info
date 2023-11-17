from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from ticket_model import TicketCreate, Ticket
from ticket_service import TicketService

router = APIRouter()


@router.post("/product/{product_id}/client/{client_id}/ticket")
async def create_ticket(product_id: int, client_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    ticket_new = service_ticket.create_ticket(ticket, product_id, client_id)
    return ticket_new


@router.get("/product/{product_id}/tickets")
async def get_tickets(product_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.get_tickets(product_id)


@router.get("/product/{product_id}/ticket/{ticket_id}")
async def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.get_ticket(ticket_id)


@router.put("/product/{product_id}/ticket/{ticket_id}")
async def update_ticket(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.update_ticket(ticket_id, ticket)


@router.delete("/product/{product_id}/ticket/{ticket_id}")
async def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.delete_ticket(ticket_id)
