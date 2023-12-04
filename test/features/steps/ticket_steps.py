from behave import given, when, then
from unittest.mock import MagicMock
from app.ticket_model import TicketCreate
from app.ticket_service import TicketService


@given('a support employee wants to log a ticket and fills out all required fields')
def step_impl(context):


    context.ticket_data = {
        "title": "Cant save an operation",
        "severity": "s1",
        "priority": "alta",
        "description": "when I try to save an operation, there is an error"
    }
    pass

@when('they want to record the complaint in a ticket')
def step_impl(context):

    context.db = MagicMock()
    context.ticket_service = TicketService(context.db)
    context.created_ticket = context.ticket_service.create_ticket(TicketCreate(**context.ticket_data), version_id=1, client_id=1)

    pass

@then('the ticket is created successfully')
def step_impl(context):
    assert context.created_ticket is not None, "Se produjo un error al crear el ticket"
    pass
