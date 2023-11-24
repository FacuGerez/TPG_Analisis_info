from fastapi import APIRouter

router = APIRouter(
    tags=["client"],
    responses={404: {"description": "Not found"}},
)


@router.get("/product/{product_id}/client")
async def clients():
    return {"message": "Aca van todos los clientes"}
