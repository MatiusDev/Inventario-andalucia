from typing import Awaitable, Callable
from fastapi import Request, HTTPException
from starlette.types import ASGIApp
from fastapi_auth_jwt import JWTAuthenticationMiddleware

class CookieSessionMiddleware(JWTAuthenticationMiddleware):
  def __init__(
    self, 
    app: ASGIApp,
    backend,
    exclude_urls = None
  ):
    super().__init__(app, backend=backend, exclude_urls=exclude_urls or [])
  
  async def dispatch(
    self, request: Request, call_next: Callable[[Request], Awaitable]
  ):
    if request.method == "OPTIONS":
        return await call_next(request)
    
    request_url_path = request.url.path
    if any(
      url in request_url_path
      for url in self.exclude_urls + self._default_excluded_urls
    ):
      return await call_next(request)

    try:
        if "session" in request.cookies:
          token = request.cookies["session"]
        else:
          token = self.extract_token_from_request(request)
        user = await self.backend.authenticate(token)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found.")
    except Exception as exc:
        return self._handle_authentication_exception(request, exc)

    request.state.user = user
    return await call_next(request)