from fastapi import APIRouter, HTTPException, status

from product_model import Product

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

list_products = [
    Product(nroDeProducto=1, name="SIU-guarani", version="12.01"),
    Product(nroDeProducto=2, name="Gestion-de-Molinetes", version="3.14.05"),
    Product(nroDeProducto=3, name="Gestion-de-Molinetes", version="3.14.18"),
    Product(nroDeProducto=4, name="??", version="12.01"),
    Product(nroDeProducto=5, name="??",  version="12.01"),
    Product(nroDeProducto=6, name="??", version="12.01")
]


@router.get("/")
async def products():
    return list_products


@router.post("/{product_id}")
async def product(product_id: int):
    for p in list_products:
        if p.nroDeProducto == product_id:
            return p
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No se encontro el producto deseado")
