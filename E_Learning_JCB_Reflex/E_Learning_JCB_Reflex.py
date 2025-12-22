"""
E-Learning JCB Platform - Archivo principal de la aplicación.

Este es el punto de entrada de la aplicación Reflex. Define la aplicación principal
y registra todas las rutas (páginas) disponibles en el sistema.

Estructura de rutas:
===================

RUTAS PÚBLICAS (accesibles sin autenticación):
- / : Página de inicio
- /courses : Catálogo de cursos
- /courses/[course_id] : Detalle de un curso específico
- /instructors : Listado de instructores
- /instructors/[instructor_id] : Detalle de un instructor
- /contact : Formulario de contacto
- /login : Página de inicio de sesión
- /register : Página de registro de usuarios

RUTAS PROTEGIDAS - Dashboards (requieren autenticación):
- /student/dashboard : Dashboard para estudiantes
- /instructor/dashboard : Dashboard para instructores
- /admin/dashboard : Dashboard para administradores

RUTAS PROTEGIDAS - Gestión de perfil:
- /profile : Página de perfil de usuario (todos los roles autenticados)

RUTAS PROTEGIDAS - Administración (solo admin):
- /admin/users : Gestión de usuarios
- /admin/courses : Gestión de cursos

Notas:
- Las rutas con [param] son rutas dinámicas (ej: /courses/[course_id])
- La protección de rutas se maneja en cada página usando componentes de /components/protected.py
- La configuración adicional de la app está en rxconfig.py
"""

import reflex as rx
from rxconfig import config

# Importar todas las páginas de la aplicación
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
from E_Learning_JCB_Reflex.pages.profile import profile_page
from E_Learning_JCB_Reflex.pages.user_management import user_management_page
from E_Learning_JCB_Reflex.pages.course_management import course_management_page


# Crear la aplicación principal de Reflex
app = rx.App()


# ============================================================================
# REGISTRO DE RUTAS PÚBLICAS
# ============================================================================
# Estas rutas son accesibles para todos los usuarios, sin necesidad de autenticación

app.add_page(index)  # Página de inicio - ruta: /
app.add_page(courses_page, route="/courses")  # Catálogo de cursos
app.add_page(course_detail_page, route="/courses/[course_id]")  # Detalle del curso (ruta dinámica)
app.add_page(instructors_page, route="/instructors")  # Listado de instructores
app.add_page(instructor_detail_page, route="/instructors/[instructor_id]")  # Detalle del instructor
app.add_page(contact_page, route="/contact")  # Formulario de contacto
app.add_page(login_page, route="/login")  # Inicio de sesión
app.add_page(register_page, route="/register")  # Registro de nuevos usuarios


# ============================================================================
# REGISTRO DE RUTAS PROTEGIDAS - DASHBOARDS
# ============================================================================
# Estas rutas requieren autenticación y están protegidas según el rol del usuario

app.add_page(student_dashboard_page, route="/student/dashboard")  # Dashboard de estudiante
app.add_page(instructor_dashboard_page, route="/instructor/dashboard")  # Dashboard de instructor
app.add_page(admin_dashboard_page, route="/admin/dashboard")  # Dashboard de administrador


# ============================================================================
# REGISTRO DE RUTAS PROTEGIDAS - PERFIL DE USUARIO
# ============================================================================
# Ruta accesible para cualquier usuario autenticado

app.add_page(profile_page, route="/profile")  # Perfil de usuario


# ============================================================================
# REGISTRO DE RUTAS PROTEGIDAS - ADMINISTRACIÓN
# ============================================================================
# Estas rutas están restringidas solo para usuarios con rol "admin"

app.add_page(user_management_page, route="/admin/users")  # Gestión de usuarios (CRUD)
app.add_page(course_management_page, route="/admin/courses")  # Gestión de cursos (CRUD)
