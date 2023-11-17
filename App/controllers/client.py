from fastapi import APIRouter

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/clients")
async def clients():
    return {"message": "Aca van todos los clientes"}
