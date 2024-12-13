from fastapi import APIRouter, status

from utils import response_handler
from services.notify_service import SNotifyDependency

route = APIRouter()

@route.get("/")
async def list_notifications(notify_service: SNotifyDependency):
    return notify_service.list_notifications()