from fastapi import APIRouter
from app.services.query_services import ask_database

router = APIRouter()

@router.get("/query")
def query(q: str):
    return ask_database(q)
