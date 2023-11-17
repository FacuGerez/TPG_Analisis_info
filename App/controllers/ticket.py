from fastapi import APIRouter

router = APIRouter(
    prefix="/ticket",
    tags=["ticket"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def tickets():
    return {"message": "Hello World"}


@router.post("/")
async def create_ticket():
    return {"message": "Hello World"}


@router.get("/{ticket_id}")
async def get_ticket(ticket_id: int):
    return {"message": "Hello World"}


@router.put("/{ticket_id}")
async def update_ticket(ticket_id: int):
    return {"message": "Hello World"}


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: int):
    return {"message": "Hello World"}
