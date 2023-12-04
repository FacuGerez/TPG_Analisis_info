from behave import given, when, then
from fastapi import status, HTTPException
from unittest.mock import MagicMock
from app.ticket_model import TicketCreate, TicketUpdate
from app.ticket_service import TicketService

TICKET_DATA = {
    "title": "Cant save an operation",
    "severity": "s1",
    "priority": "alta",
    "description": "when I try to save an operation, there is an error"
}
DB = MagicMock()


@given('a support employee wants to log a ticket and fills out all required fields')
def step_impl(context):
    ticket: dict = TICKET_DATA.copy()
    context.ticket_data = ticket
    pass


@given('a support employee wants to register a ticket and does not provide a description')
def step_impl(context):
    ticket: dict = TICKET_DATA.copy()
    ticket["description"] = ""
    context.ticket_data = ticket
    pass


@given('a support employee wants to register a ticket and does not select a severity')
def step_impl(context):
    ticket: dict = TICKET_DATA.copy()
    ticket["severity"] = ""
    context.ticket_data = ticket
    pass


@given('a support employee wants to register a ticket and does not select a priority')
def step_impl(context):
    ticket: dict = TICKET_DATA.copy()
    ticket["priority"] = ""
    context.ticket_data = ticket
    pass


@given(
    'a support employee wants to update some allowed field(s) of a ticket (severity, priority, status, name, '
    'description)')
def step_impl(context):
    context.idTicket = GetTicketNew()
    ticket: dict = TICKET_DATA.copy()
    ticket["priority"] = "baja"
    ticket["severity"] = "s2"
    ticket["description"] = "new description"
    ticket["state"] = "Finished"
    context.ticket_data = ticket
    pass


@given('a support employee wants to update some allowed field(s) of a ticket and does not provide a description')
def step_impl(context):
    context.idTicket = GetTicketNew()
    ticket: dict = TICKET_DATA.copy()
    ticket["priority"] = "baja"
    ticket["severity"] = "s2"
    ticket["description"] = ""
    ticket["state"] = "Finished"
    context.ticket_data = ticket
    pass


@given('a support employee wants to update some allowed field(s) of a ticket and does not select a severity')
def step_impl(context):
    context.idTicket = GetTicketNew()
    ticket: dict = TICKET_DATA.copy()
    ticket["priority"] = "baja"
    ticket["severity"] = ""
    ticket["description"] = "new description"
    ticket["state"] = "Finished"
    context.ticket_data = ticket
    pass


@given('a support employee wants to update some allowed field(s) of a ticket and does not select a priority')
def step_impl(context):
    context.idTicket = GetTicketNew()
    ticket: dict = TICKET_DATA.copy()
    ticket["priority"] = ""
    ticket["severity"] = "s2"
    ticket["description"] = "new description"
    ticket["state"] = "Finished"
    context.ticket_data = ticket
    pass


@given('a support employee wants to delete a ticket')
def step_impl(context):
    context.idTicket = GetTicketNew()
    pass

@when('they want to record the complaint in a ticket')
def step_impl(context):
    context.ticket_service = TicketService(DB)
    pass


@when('they choose to change them and you try to apply this')
def step_impl(context):
    context.ticket_service = TicketService(DB)
    pass

@when('you decide to delete the ticket')
def step_impl(context):
    context.ticket_service = TicketService(DB)
    pass

@then('the ticket is created successfully')
def step_impl(context):
    context.created_ticket = context.ticket_service.create_ticket(TicketCreate(**context.ticket_data), version_id=1,
                                                                  client_id=1)
    assert context.created_ticket is not None, "Se produjo un error al crear el ticket"
    pass


@then('the employee is informed that a description needs to be added and is asked to complete it')
def step_impl(context):
    try:
        context.ticket_service.create_ticket(TicketCreate(**context.ticket_data), version_id=1,
                                             client_id=1)
    except HTTPException as e:
        assert e.detail == "Debe ingresar una descripción"
        assert e.status_code == status.HTTP_204_NO_CONTENT
    pass


@then('the employee is informed that a severity needs to be selected and is asked to select it')
def step_impl(context):
    try:
        context.ticket_service.create_ticket(TicketCreate(**context.ticket_data), version_id=1,
                                             client_id=1)
    except HTTPException as e:
        assert e.detail == "Debe seleccionar una severidad correcta"
        assert e.status_code == status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    pass


@then('the employee is informed that a priority needs to be selected and is asked to select it')
def step_impl(context):
    try:
        context.ticket_service.create_ticket(TicketCreate(**context.ticket_data), version_id=1,
                                             client_id=1)
    except HTTPException as e:
        assert e.detail == "Debe seleccionar una prioridad correcta"
        assert e.status_code == status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    pass


@then('the ticket is update successfully')
def step_impl(context):
    assert context.ticket_service.update_ticket(context.idTicket, TicketUpdate(
        **context.ticket_data)) is not None, "Se produjo un error al actualizar el ticket"
    pass


@then('the employee is informed that it is necessary not to leave the description empty')
def step_impl(context):
    try:
        context.ticket_service.update_ticket(context.idTicket, TicketUpdate(**context.ticket_data))
    except HTTPException as e:
        assert e.detail == "Debe ingresar una descripción"
        assert e.status_code == status.HTTP_204_NO_CONTENT
    pass


@then('the employee is informed that a severity needs to be selected')
def step_impl(context):
    try:
        context.ticket_service.update_ticket(context.idTicket, TicketUpdate(**context.ticket_data))
    except HTTPException as e:
        assert e.detail == "Debe seleccionar una severidad correcta"
        assert e.status_code == status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    pass


@then('the employee is informed that a priority needs to be selected')
def step_impl(context):
    try:
        context.ticket_service.update_ticket(context.idTicket, TicketUpdate(**context.ticket_data))
    except HTTPException as e:
        assert e.detail == "Debe seleccionar una prioridad correcta"
        assert e.status_code == status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    pass

@then('the ticket is deleted successfully.')
def step_impl(context):
    assert context.ticket_service.delete_ticket(context.idTicket)
    pass

def GetTicketNew() -> int:
    return TicketService(DB).create_ticket(TicketCreate(**TICKET_DATA), 1, 1).id
