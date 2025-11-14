"""E-Learning JCB Platform - Main application file."""

import reflex as rx
from rxconfig import config
from E_Learning_JCB_Reflex.pages.index import index
from E_Learning_JCB_Reflex.pages.courses import courses_page

# Configuración de la aplicación
app = rx.App()

# Registro de rutas
app.add_page(index)
app.add_page(courses_page, route="/courses")
