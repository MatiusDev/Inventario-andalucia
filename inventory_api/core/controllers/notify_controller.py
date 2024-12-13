from fastapi import APIRouter, status

from core.utils import response_handler
from core.services.notify_service import SNotifyDependency

route = APIRouter()

@route.get("/")
async def list_notifications(notify_service: SNotifyDependency):
    return notify_service.list_notifications()