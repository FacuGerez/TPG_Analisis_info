from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from App.controllers import client
from App.database.database import SessionLocal, engine, Base
from controllers import ticket
from controllers import product

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routers
app.include_router(ticket.router)
app.include_router(client.router)
app.include_router(product.router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
