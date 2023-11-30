from pydantic import BaseModel


class VersionBase(BaseModel):
    version: str


class VersionCreate(VersionBase):
    pass


class Version(VersionBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True
