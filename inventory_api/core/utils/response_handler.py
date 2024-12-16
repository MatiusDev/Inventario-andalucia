from typing import Coroutine
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import os

async def response_handler(data):
  if isinstance(data, Coroutine):
    response = await data
  else:
    response = data

  if response["status"] != "success":
    raise HTTPException(status_code=response["status_code"], detail=f"Error: {response['detail']}")
  
  cookie = response.get("cookie")
  if (cookie != "close" 
      and cookie != None):
    if os.getenv("ENVIRONMENT") == "development":
      json_response = JSONResponse(
        content={
          "message": response["message"], 
          "status": response["status"],
          "token": cookie["value"]
        }
      )
    else:
      json_response = JSONResponse(
        content={
          "message": response["message"], 
          "status": response["status"]
        }
      )
    # Configura la cookie en la respuesta JSON
    json_response.set_cookie(
      key=cookie.get("key"),
      value=cookie.get("value"),
      httponly=cookie.get("httponly", True),
      secure=cookie.get("secure", True),
      samesite=cookie.get("samesite", "None"),
      path=cookie.get("path", "/"),
      max_age=cookie.get("max_age"),
    )
    return json_response
  elif cookie == "close":
    json_response = JSONResponse(
      content={
        "message": response["message"], 
        "status": response["status"]
      }
    )
    json_response.delete_cookie(
        key="session",
        path="/",
        domain=None,
        samesite="None",
        secure=True,
        httponly=True,
    )
    return json_response
  else:
    return response