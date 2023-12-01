from fastapi import APIRouter, HTTPException, status
from version_model import Version

router = APIRouter(
    prefix="/product/{product_id}/version",
    tags=["version"],
)

list_versions = [
    Version(id=1, version="3.14.04", product_id=1),
    Version(id=2, version="3.14.05", product_id=1),
    Version(id=3, version="3.14.06", product_id=1),
    Version(id=4, version="3.14.07", product_id=1),
    Version(id=5, version="3.14.08", product_id=1),
    Version(id=6, version="3.14.09", product_id=1),
    Version(id=7, version="3.14.10", product_id=1),
    Version(id=8, version="3.14.01", product_id=1),
    Version(id=9, version="3.15.02", product_id=1),
    Version(id=10, version="12.1.01", product_id=2),
    Version(id=11, version="12.1.02", product_id=2),
    Version(id=12, version="12.1.03", product_id=2),
    Version(id=13, version="12.1.04", product_id=2),
    Version(id=14, version="12.1.05", product_id=2),
    Version(id=15, version="12.1.06", product_id=2),
    Version(id=16, version="12.1.07", product_id=2),
    Version(id=17, version="7.8.01", product_id=3),
    Version(id=18, version="7.8.02", product_id=3),
    Version(id=19, version="7.8.03", product_id=3),
    Version(id=20, version="7.8.04", product_id=3),
    Version(id=21, version="7.8.05", product_id=3),
    Version(id=22, version="7.8.06", product_id=3)
]


@router.get("/")
async def versions(product_id: int):
    final_list: list[Version] = []
    for v in list_versions:
        if v.product_id == product_id:
            final_list.append(v)
    return final_list


@router.post("/{version_id}")
async def version(version_id: int):
    for v in list_versions:
        if v.id == version_id:
            return v
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No se encontro la version deseada")
