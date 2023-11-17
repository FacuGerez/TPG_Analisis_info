from fastapi import APIRouter

router = APIRouter(
    prefix="/task",
    tags=["task"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def tasks():
    return {"message": "Hello World"}


@router.post("/")
async def create_task():
    return {"message": "Hello World"}


@router.get("/{task_id}")
async def get_task(task_id: int):
    return {"message": "Hello World"}


@router.put("/{task_id}")
async def update_task(task_id: int):
    return {"message": "Hello World"}


@router.delete("/{task_id}")
async def delete_task(task_id: int):
    return {"message": "Hello World"}
