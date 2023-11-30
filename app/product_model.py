from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    nroDeProducto: int

    class Config:
        orm_mode = True
