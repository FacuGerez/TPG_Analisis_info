from fastapi import APIRouter

router = APIRouter()

@router.get("/tickets")
async def tickets():
    return {"message": "Hello World"}