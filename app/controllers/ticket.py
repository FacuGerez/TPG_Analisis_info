from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from ..model.ticket import TicketCreate, Ticket
from ..service.ticket import TicketService

router = APIRouter()


@router.post("/product/{product_id}/client/{client_id}/ticket", response_model=Ticket)
async def create_ticket(product_id: int, client_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    ticket_new = service_ticket.create_ticket(ticket, product_id, client_id)
    return ticket_new


@router.get("/product/{product_id}/tickets", response_model=list[[Ticket]])
async def get_tickets(product_id: int, db: Session = Depends(get_db)):
    service_ticket: TicketService = TicketService(db)
    return service_ticket.get_tickets(product_id)


@router.get("/product/{product_id}/ticket/{ticket_id}", response_model=[Ticket])
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
