from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.client_controller import router as r_client
from app.ticket_controller import router as r_ticket
from app.assignment_controller import router as r_assignment
from app.product_controller import router as r_product
from app.version_controller import router as r_version
from app.db import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI(
    tags=["root"],
)


@app.get("/")
async def root():
    return {"detail": "Aca va la redireccion al modulo de soporte o al de proyecto"}


# Routers
app.include_router(r_product)
app.include_router(r_version)
app.include_router(r_client)
app.include_router(r_ticket)
app.include_router(r_assignment)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
