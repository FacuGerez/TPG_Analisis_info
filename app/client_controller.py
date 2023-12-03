from requests import Session
from fastapi import APIRouter, status

router = APIRouter(
    prefix="/client",
    tags=["client"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "No se encontraron los clientes"}},
)


@router.get("/")
def clients():
    with Session() as sess:
        response = sess.get(
            "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes")
        return response.json()
