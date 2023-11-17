from fastapi import APIRouter, HTTPException, status

from product_model import Product

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

list_products = [
    Product(nroDeProducto=1, name="SIU-guarani", state="Finalizado", version="12.01"),
    Product(nroDeProducto=2, name="Gestion-de-Molinetes", state="En Proceso", version="3.14.05"),
    Product(nroDeProducto=3, name="Gestion-de-Molinetes", state="En Proceso", version="3.14.18"),
    Product(nroDeProducto=4, name="??", state="En Pausa", version="12.01"),
    Product(nroDeProducto=5, name="??", state="Finalizado", version="12.01"),
    Product(nroDeProducto=6, name="??", state="Correccion de Errores", version="12.01")
]


@router.get("/")
async def products():
    return list_products


@router.post("/{product_id}")
async def product(product_id: int):
    product_deseado = filter(lambda p: p.id == product_id, list_products)
    print(product_deseado)
    if product_deseado is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No se encontro el producto deseado")
    return product_deseado
