from fastapi import APIRouter

router = APIRouter(
    prefix="/client",
    tags=["client"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def clients():
    return {"message": "Hello World"}

@router.post("/")
async def create_client():
    return {"message": "Hello World"}

@router.get("/{client_id}")
async def get_client(client_id: int):
    return {"message": "Hello World"}

@router.put("/{client_id}")
async def update_client(client_id: int):
    return {"message": "Hello World"}

@router.delete("/{client_id}")
async def delete_client(client_id: int):
    return {"message": "Hello World"}

@router.get("/{client_id}/tickets")
async def get_client_tickets(client_id: int):
    return {"message": "Hello World"}