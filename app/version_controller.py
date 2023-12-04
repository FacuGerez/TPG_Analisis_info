from fastapi import APIRouter, HTTPException, status
from app.version_model import Version

router = APIRouter(
    prefix="/version",
    tags=["version"],
)

list_versions = [
    Version(id=1, version="3.14.229773.04", product_id=1),
    Version(id=2, version="3.14.229773.05", product_id=1),
    Version(id=3, version="3.14.229773.06", product_id=1),
    Version(id=4, version="3.14.229773.07", product_id=1),
    Version(id=5, version="3.14.229773.08", product_id=1),
    Version(id=6, version="3.14.229773.09", product_id=1),
    Version(id=7, version="3.14.229773.10", product_id=1),
    Version(id=8, version="3.14.229773.01", product_id=1),
    Version(id=9, version="3.15.499315.02", product_id=1),
    Version(id=10, version="12.1.5335185.01", product_id=2),
    Version(id=11, version="12.1.5335185.02", product_id=2),
    Version(id=12, version="12.1.5335185.03", product_id=2),
    Version(id=13, version="12.1.5335185.04", product_id=2),
    Version(id=14, version="12.1.5335185.05", product_id=2),
    Version(id=15, version="12.1.5335185.06", product_id=2),
    Version(id=16, version="12.1.5335185.07", product_id=2),
    Version(id=17, version="7.8.45801", product_id=3),
    Version(id=18, version="7.8.45802", product_id=3),
    Version(id=19, version="7.8.45803", product_id=3),
    Version(id=20, version="7.8.45804", product_id=3),
    Version(id=21, version="7.8.45805", product_id=3),
    Version(id=22, version="7.8.45806", product_id=3)
]


@router.get("/product/{product_id}")
async def versions(product_id: int):
    final_list: list[Version] = []
    for v in list_versions:
        if v.product_id == product_id:
            final_list.append(v)
    return final_list


@router.get("/{version_id}")
async def version(version_id: int):
    for v in list_versions:
        if v.id == version_id:
            return v
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No se encontro la version deseada")
