from fastapi import APIRouter, status

from utils import response_handler
from services.notify_service import NotifyDependency

route = APIRouter()

@route.get("/")
async def list_notifications(notify_service: NotifyDependency):
    return notify_service.list_notifications()