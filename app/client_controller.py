from fastapi import APIRouter

router = APIRouter(
    prefix="/client",
    tags=["client"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def clients():
    return {"message": "Aca van todos los clientes"}
