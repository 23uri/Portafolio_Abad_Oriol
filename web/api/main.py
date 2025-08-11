from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web.api.routes.contact_route import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)