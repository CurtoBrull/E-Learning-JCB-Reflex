"""E-Learning JCB Platform - Main application file."""

import reflex as rx
from rxconfig import config
from E_Learning_JCB_Reflex.pages.index import index
from E_Learning_JCB_Reflex.pages.courses import courses_page
from E_Learning_JCB_Reflex.pages.course_detail import course_detail_page
from E_Learning_JCB_Reflex.pages.instructors import instructors_page
from E_Learning_JCB_Reflex.pages.instructor_detail import instructor_detail_page
from E_Learning_JCB_Reflex.pages.contact import contact_page
from E_Learning_JCB_Reflex.pages.login import login_page
from E_Learning_JCB_Reflex.pages.register import register_page
from E_Learning_JCB_Reflex.pages.student_dashboard import student_dashboard_page
from E_Learning_JCB_Reflex.pages.instructor_dashboard import instructor_dashboard_page
from E_Learning_JCB_Reflex.pages.admin_dashboard import admin_dashboard_page

# Configuración de la aplicación
app = rx.App()

# Registro de rutas públicas
app.add_page(index)
app.add_page(courses_page, route="/courses")
app.add_page(course_detail_page, route="/courses/[course_id]")
app.add_page(instructors_page, route="/instructors")
app.add_page(instructor_detail_page, route="/instructors/[instructor_id]")
app.add_page(contact_page, route="/contact")
app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register")

# Registro de rutas protegidas - Dashboards
app.add_page(student_dashboard_page, route="/student/dashboard")
app.add_page(instructor_dashboard_page, route="/instructor/dashboard")
app.add_page(admin_dashboard_page, route="/admin/dashboard")
