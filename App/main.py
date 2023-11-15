from fastapi import FastAPI
from controllers import ticket

app = FastAPI()
app.include_router(ticket.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}