from fastapi import APIRouter, HTTPException, status
from version_model import Version

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
    Version(id=22, version="7.8.45806", product_id=3),
    Version(id=23, version="3.14.229773.06", product_id=4),
    Version(id=24, version="3.14.229773.07", product_id=4),
    Version(id=25, version="3.14.229773.08", product_id=4),
    Version(id=26, version="3.14.229773.09", product_id=4),
    Version(id=27, version="3.14.229773.10", product_id=4),
    Version(id=28, version="3.14.229773.01", product_id=4),
    Version(id=29, version="3.15.499315.02", product_id=4),
    Version(id=30, version="12.1.5335185.01", product_id=5),
    Version(id=31, version="12.1.5335185.02", product_id=5),
    Version(id=32, version="12.1.5335185.03", product_id=5),
    Version(id=33, version="12.1.5335185.04", product_id=5),
    Version(id=34, version="12.1.5335185.05", product_id=5),
    Version(id=35, version="12.1.5335185.06", product_id=5),
    Version(id=36, version="12.1.5335185.07", product_id=5),
    Version(id=37, version="7.8.45801", product_id=6),
    Version(id=38, version="7.8.45802", product_id=6),
    Version(id=39, version="7.8.45803", product_id=6),
    Version(id=40, version="7.8.45804", product_id=6),
    Version(id=41, version="7.8.45805", product_id=6),
    Version(id=42, version="3.14.229773.05", product_id=7),
    Version(id=43, version="3.14.229773.06", product_id=7),
    Version(id=44, version="3.14.229773.07", product_id=7),
    Version(id=45, version="3.14.229773.08", product_id=7),
    Version(id=46, version="3.14.229773.09", product_id=7),
    Version(id=47, version="3.14.229773.10", product_id=7),
    Version(id=48, version="3.14.229773.01", product_id=7),
    Version(id=49, version="3.15.499315.02", product_id=7),
    Version(id=50, version="12.1.5335185.01", product_id=8),
    Version(id=51, version="12.1.5335185.02", product_id=8),
    Version(id=52, version="12.1.5335185.03", product_id=8),
    Version(id=53, version="12.1.5335185.04", product_id=8),
    Version(id=54, version="12.1.5335185.05", product_id=8),
    Version(id=55, version="12.1.5335185.06", product_id=8),
    Version(id=56, version="12.1.5335185.07", product_id=8),
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
