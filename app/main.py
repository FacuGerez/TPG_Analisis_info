from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.client import router as r_client
from controllers.ticket import router as r_ticket
from controllers.product import router as r_product
from app.database.database import engine, Base


Base.metadata.create_all(bind=engine)
app = FastAPI()


# Routers
app.include_router(r_ticket)
app.include_router(r_client)
app.include_router(r_product)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hola fastapi"}
