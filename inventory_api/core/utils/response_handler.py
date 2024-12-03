from typing import Coroutine
from fastapi import HTTPException

def response_handler_sync(response):
  if response["status"] != "success":
    raise HTTPException(status_code=response["status_code"], detail=response["detail"])
  
  return response

async def response_handler(data: Coroutine):
  response = await data
  
  if response["status"] != "success":
    raise HTTPException(status_code=response["status_code"], detail=response["detail"])
  
  return response