from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

# Configuraciones
from config.environtments_config import environment_config
# from services.auth_service import AuthService as AuthBackend

# Middlewares
# from fastapi_auth_jwt import JWTAuthenticationMiddleware

# Rutas de API
from router.routes import routes

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
# app.add_middleware(
#   JWTAuthenticationMiddleware,
#   backend=AuthBackend(),
#   exclude_urls=["/auth/sign-up", "/auth/login"]
# )

app.include_router(routes, prefix="/api")


