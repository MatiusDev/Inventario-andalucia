from typing import Awaitable, Callable
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from starlette.types import ASGIApp

class CheckOriginMiddleware(BaseHTTPMiddleware):
  def __init__(self, app: ASGIApp, allowed_origins: set) -> None:
    self.allowed_origins = allowed_origins
    super().__init__(app)
    
  async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    host = request.headers.get("host")
    if '*' not in self.allowed_origins:
      if host not in self.allowed_origins:
        content = { "error": "IP origen no permitida", "status": "fail" }
      return JSONResponse(content=content, status_code=403)
    
    response = await call_next(request)
    return response