from typing import Awaitable, Callable
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from starlette.types import ASGIApp

import os

class CheckOriginMiddleware(BaseHTTPMiddleware):
  def __init__(self, app: ASGIApp, allowed_origins: list) -> None:
    self.allowed_origins = allowed_origins
    super().__init__(app)
    
  async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    origin = request.headers.get("origin")
    
    if os.getenv("ENVIRONMENT") == "development" and origin is None:
      return await call_next(request)
    
    if origin not in self.allowed_origins:
      content = { "error": "IP origen no permitida", "status": "fail" }
      return JSONResponse(content=content, status_code=403)
    # Retorno el response para que siga con las demás validaciones
    return await call_next(request)