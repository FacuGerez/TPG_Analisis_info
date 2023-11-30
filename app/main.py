from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from client_controller import router as r_client
from ticket_controller import router as r_ticket
from assignment_controller import router as r_assignment
from product_controller import router as r_product
from db import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI(
    tags=["root"],
)

# Routers
app.include_router(r_ticket)
app.include_router(r_assignment)
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
    return {"detail": "Aca va la redireccion al modulo de soporte o al de proyecto"}
