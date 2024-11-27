from typing import Awaitable, Callable
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from starlette.types import ASGIApp

class CheckAuthTokenMiddleware(BaseHTTPMiddleware):
  def __init__(self, app: ASGIApp) -> None:
    super().__init__(app)
    
  async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    return await call_next(request)