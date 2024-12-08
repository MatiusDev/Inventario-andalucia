from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
  if app.openapi_schema:
    return app.openapi_schema
  
  title = app.title
  version = app.version
  description = app.description
  
  openapi_schema = get_openapi(
    title=title,
    version=version,
    description=description,
    routes=app.routes
  )
  
  openapi_schema["components"]["securitySchemes"] = {
    "BearerAuth": {
      "type": "http",
      "scheme": "bearer",
      "bearerFormat": "JWT"
    }
  }
  
  for path, methods in openapi_schema["paths"].items():
    for method in methods:
      if (not path.startswith("/api/auth/login") 
        and not path.startswith("/api/auth/sign-up")):
        methods[method]["security"] = [{"BearerAuth": []}]
      else:
        methods[method].pop("security", None)        
  return openapi_schema