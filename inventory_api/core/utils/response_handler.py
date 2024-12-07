from typing import Coroutine
from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def response_handler(data):
  if isinstance(data, Coroutine):
    response = await data
  else:
    response = data

  if response["status"] != "success":
    raise HTTPException(status_code=response["status_code"], detail=f"Error: {response['detail']}")
  
  if hasattr(response, "cookie"):
    response = JSONResponse(
      content={ "message": data["message"], "status": data["status"] },
      headers={"Set-Cookie": data["cookie"]}
    )
    return response

  return response