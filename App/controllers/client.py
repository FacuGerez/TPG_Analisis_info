from fastapi import APIRouter

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/product/{product_id}/clients")
async def clients():
    return {"message": "Aca van todos los clientes"}
