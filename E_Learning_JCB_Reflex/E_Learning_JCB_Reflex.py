"""E-Learning JCB Platform - Main application file."""

import reflex as rx
from rxconfig import config
from E_Learning_JCB_Reflex.pages.index import index
from E_Learning_JCB_Reflex.pages.courses import courses_page
from E_Learning_JCB_Reflex.pages.course_detail import course_detail_page
from E_Learning_JCB_Reflex.pages.instructors import instructors_page
from E_Learning_JCB_Reflex.pages.instructor_detail import instructor_detail_page
from E_Learning_JCB_Reflex.pages.contact import contact_page

# Configuración de la aplicación
app = rx.App()

# Registro de rutas
app.add_page(index)
app.add_page(courses_page, route="/courses")
app.add_page(course_detail_page, route="/courses/[course_id]")
app.add_page(instructors_page, route="/instructors")
app.add_page(instructor_detail_page, route="/instructors/[instructor_id]")
app.add_page(contact_page, route="/contact")
