# app/api/v1/api.py
from fastapi import APIRouter
from app.api.v1.endpoints import auth # Agi banayeko auth module layout taneko

api_router = APIRouter()

# Main entry connection line logic integration
# Auth section ko counters haru hub router network node vitra push gareko
api_router.include_router(auth.router)