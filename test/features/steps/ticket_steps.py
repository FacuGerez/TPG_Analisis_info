from behave import given, when, then
from fastapi import status, HTTPException
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


@given('a support employee wants to register a ticket and does not provide a description')
def step_impl(context):
    context.ticket_data = {
        "title": "Cant save an operation",
        "severity": "s1",
        "priority": "alta",
        "description": ""
    }
    pass


@given('a support employee wants to register a ticket and does not select a severity')
def step_impl(context):
    context.ticket_data = {
        "title": "Cant save an operation",
        "severity": "",
        "priority": "alta",
        "description": "when I try to save an operation, there is an error"
    }
    pass


@given('a support employee wants to register a ticket and does not select a priority')
def step_impl(context):
    context.ticket_data = {
        "title": "Cant save an operation",
        "severity": "s1",
        "priority": "",
        "description": "when I try to save an operation, there is an error"
    }
    pass


@when('they want to record the complaint in a ticket')
def step_impl(context):
    context.db = MagicMock()
    context.ticket_service = TicketService(context.db)

    pass


@then('the ticket is created successfully')
def step_impl(context):
    context.created_ticket = context.ticket_service.create_ticket(TicketCreate(**context.ticket_data), version_id=1,
                                                                  client_id=1)
    assert context.created_ticket is not None, "Se produjo un error al crear el ticket"
    pass


@then('he employee is informed that a description needs to be added and is asked to complete it')
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
