from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import ticket


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints
app.include_router(ticket.router)
#crear ticket