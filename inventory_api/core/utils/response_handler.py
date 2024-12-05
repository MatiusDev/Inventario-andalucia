from typing import Coroutine
from fastapi import HTTPException

async def response_handler(data):
  if isinstance(data, Coroutine):
    response = await data
  else:
    response = data

  if response["status"] != "success":
    raise HTTPException(status_code=response["status_code"], detail=f"Error: {response['detail']}")

  return response