from behave import given, when, then, step
from app.ticket_service import TicketService
from app.ticket_model import TicketCreate

@given('a support employee wants to log a ticket and fills out all required fields')
def step_impl(context):
    """
    context.ticket_service = TicketService()
    context.ticket_data = {
        "title": "Cant save an operation",
        "severity": "s1",
        "priority": "alta",
        "description": "when I try to save an operation, there is an error"
    }"""
    pass

@when('they want to record the complaint in a ticket')
def step_impl(context):
    """
    context.ticket_create = TicketCreate(**context.ticket_data)
    context.created_ticket = context.ticket_service.create_ticket(context.ticket_create, version_id=1, client_id=1)
    """
    pass

@then('the ticket is created successfully')
def step_impl(context):
    #assert context.created_ticket is not None, "Se produjo un error al crear el ticket"
    pass
