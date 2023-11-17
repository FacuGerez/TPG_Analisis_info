from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    version: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    nroDeProducto: int
    state: str

    class Config:
        orm_mode = True
