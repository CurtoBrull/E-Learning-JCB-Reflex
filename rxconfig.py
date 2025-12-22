import reflex as rx
import os

# Detectar si estamos en producción
is_production = os.getenv("ENVIRONMENT") == "production"

config = rx.Config(
    app_name="E_Learning_JCB_Reflex",

    # Configuración de backend
    backend_port=int(os.getenv("BACKEND_PORT", "8000")),

    # Configuración de frontend
    frontend_port=int(os.getenv("FRONTEND_PORT", "3000")),

    # API URL para producción (Render usa HTTPS)
    api_url=os.getenv("API_URL", "http://localhost:8000") if not is_production else os.getenv("API_URL"),

    # Habilitar CORS para producción
    cors_allowed_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
        os.getenv("FRONTEND_URL", ""),
    ] if is_production else ["*"],

    # Configuración de WebSockets para producción
    # Asegurar que los WebSockets funcionen con HTTPS en Render
    backend_host="0.0.0.0",  # Escuchar en todas las interfaces

    # Plugins
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)