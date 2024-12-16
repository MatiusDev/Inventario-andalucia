from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

# Configuraciones
from core.config.environtments_config import environment_config
from core.config.openapi_config import custom_openapi

# Middlewares
from core.middlewares.cookie_session_middleware import CookieSessionMiddleware

# Rutas de API
from core.router.routes import routes

load_dotenv()

config = environment_config()

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=config["origins"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.add_middleware(
  CookieSessionMiddleware,
  backend=config["auth"],
  exclude_urls=["api/auth/health", "/api/auth/login", "/api/auth/sign-up"]
)

app.include_router(routes, prefix="/api")

app.openapi_schema = custom_openapi(app)