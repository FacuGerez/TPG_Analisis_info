from fastapi import APIRouter, HTTPException, status

from product_model import Product

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

list_products = [
    Product(nroDeProducto=1, name="SIU-guarani"),
    Product(nroDeProducto=2, name="Gestion-de-Molinetes"),
    Product(nroDeProducto=3, name="League of legends"),
    Product(nroDeProducto=4, name="Canva"),
    Product(nroDeProducto=5, name="Aerolineas Emperador"),
    Product(nroDeProducto=6, name="Paint en rosita"),
    Product(nroDeProducto=7, name="Sistema de gestios contable"),
    Product(nroDeProducto=8, name="Convertidor de archivos"),
]


@router.get("/")
async def products():
    return list_products


@router.get("/{product_id}")
async def product(product_id: int):
    for p in list_products:
        if p.nroDeProducto == product_id:
            return p
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No se encontro el producto deseado")
