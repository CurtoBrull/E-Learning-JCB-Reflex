"""
Página de Documentación de E-Learning JCB.

Ruta: /docs
Acceso: Pública
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer


# ---------------------------------------------------------------------------
# Estructura de la documentación
# ---------------------------------------------------------------------------

DOCS_SECTIONS = [
    {
        "id": "inicio-rapido",
        "icon": "zap",
        "color": "yellow",
        "title": "Inicio Rápido",
        "items": [
            {
                "title": "Crear tu cuenta",
                "content": [
                    "Ve a la página de registro haciendo clic en 'Registrarse' en la barra de navegación.",
                    "Rellena el formulario con tu nombre completo, dirección de email y una contraseña segura.",
                    "Pulsa 'Crear cuenta' y accederás directamente a la plataforma como estudiante.",
                    "Desde tu perfil podrás completar tus datos personales y subir una foto.",
                ],
            },
            {
                "title": "Explorar el catálogo",
                "content": [
                    "Navega a la sección 'Cursos' desde el menú principal.",
                    "Usa el buscador para filtrar por título, descripción o nivel del curso.",
                    "Haz clic en cualquier curso para ver su descripción completa, instructor y contenido.",
                    "Pulsa 'Inscribirse' para unirte al curso y comenzar a aprender.",
                ],
            },
            {
                "title": "Tu dashboard de estudiante",
                "content": [
                    "Accede a tu dashboard desde el menú de usuario (esquina superior derecha).",
                    "Aquí verás tus cursos inscritos, progreso y estadísticas personales.",
                    "El panel muestra el número de cursos en progreso y completados.",
                    "Haz clic en cualquier curso para continuar donde lo dejaste.",
                ],
            },
        ],
    },
    {
        "id": "estudiantes",
        "icon": "graduation-cap",
        "color": "blue",
        "title": "Guía del Estudiante",
        "items": [
            {
                "title": "Inscribirse en un curso",
                "content": [
                    "Desde el catálogo de cursos, selecciona el curso que te interese.",
                    "En la página de detalle verás la descripción, nivel (principiante/intermedio/avanzado) y precio.",
                    "Pulsa el botón 'Inscribirse'. Si el curso es gratuito, el acceso es inmediato.",
                    "El curso aparecerá en tu dashboard bajo 'Mis Cursos'.",
                ],
            },
            {
                "title": "Ver el contenido de un curso",
                "content": [
                    "Desde tu dashboard, haz clic en el curso que quieras continuar.",
                    "El visor de curso muestra las lecciones disponibles en el panel lateral.",
                    "Avanza por las lecciones a tu propio ritmo sin fecha de caducidad.",
                    "Tu progreso se guarda automáticamente.",
                ],
            },
            {
                "title": "Gestionar tu perfil",
                "content": [
                    "Accede al perfil desde el icono de usuario en la barra de navegación.",
                    "Puedes actualizar tu nombre, email y foto de perfil.",
                    "Para cambiar la contraseña, usa la opción correspondiente en la sección de seguridad.",
                    "Los cambios se guardan al pulsar 'Guardar cambios'.",
                ],
            },
        ],
    },
    {
        "id": "instructores",
        "icon": "presentation",
        "color": "purple",
        "title": "Guía del Instructor",
        "items": [
            {
                "title": "Crear un curso",
                "content": [
                    "Desde tu dashboard de instructor, pulsa '+ Crear Curso' o ve a 'Mis Cursos'.",
                    "Rellena el formulario: título, descripción, nivel (principiante/intermedio/avanzado), categoría y precio.",
                    "Opcionalmente añade una URL de imagen de portada para el curso.",
                    "Pulsa 'Guardar' — el curso queda publicado inmediatamente en el catálogo.",
                ],
            },
            {
                "title": "Editar y eliminar cursos",
                "content": [
                    "Ve a 'Mis Cursos' desde el menú lateral de tu dashboard.",
                    "En la tabla de cursos, usa el icono de lápiz para editar un curso existente.",
                    "Para eliminar un curso, usa el icono de papelera. Se pedirá confirmación antes de borrar.",
                    "Al eliminar un curso, los estudiantes perderán el acceso al mismo.",
                ],
            },
            {
                "title": "Ver estadísticas",
                "content": [
                    "Accede a la sección 'Estadísticas' desde el menú de tu dashboard.",
                    "Verás KPIs globales: estudiantes totales, ingresos, valoración media y cursos activos.",
                    "La gráfica de barras muestra la evolución mensual de ingresos.",
                    "La tabla de cursos detalla métricas individuales por curso.",
                ],
            },
            {
                "title": "Convertirse en instructor",
                "content": [
                    "El rol de instructor lo asigna el administrador de la plataforma.",
                    "Contacta con el equipo a través del formulario en /contact o por email.",
                    "Una vez asignado el rol, tu dashboard cambiará automáticamente al de instructor.",
                    "No es necesario crear una cuenta nueva.",
                ],
            },
        ],
    },
    {
        "id": "administracion",
        "icon": "shield",
        "color": "red",
        "title": "Panel de Administración",
        "items": [
            {
                "title": "Gestión de usuarios",
                "content": [
                    "Desde /admin/users puedes ver todos los usuarios registrados.",
                    "Puedes cambiar el rol de cualquier usuario (student, instructor, admin).",
                    "También puedes activar, desactivar o eliminar cuentas.",
                    "El buscador permite filtrar por nombre, email o rol.",
                ],
            },
            {
                "title": "Gestión de cursos",
                "content": [
                    "Desde /admin/courses puedes ver y gestionar todos los cursos de la plataforma.",
                    "Los administradores pueden editar o eliminar cualquier curso independientemente del instructor.",
                    "Útil para moderar contenido y mantener la calidad del catálogo.",
                ],
            },
            {
                "title": "Estadísticas globales",
                "content": [
                    "Accede a /admin/stats para ver métricas globales de la plataforma.",
                    "Datos de usuarios activos, inscripciones totales, cursos publicados e ingresos.",
                    "Información útil para la toma de decisiones sobre la plataforma.",
                ],
            },
        ],
    },
    {
        "id": "tecnologia",
        "icon": "code",
        "color": "green",
        "title": "Stack Tecnológico",
        "items": [
            {
                "title": "Frontend y Backend — Reflex",
                "content": [
                    "E-Learning JCB está construida con Reflex (Python full-stack framework).",
                    "Todo el código, tanto el servidor como la interfaz, está escrito en Python.",
                    "Reflex compila el frontend a React automáticamente.",
                    "Comunicación en tiempo real mediante WebSockets.",
                ],
            },
            {
                "title": "Base de datos — MongoDB",
                "content": [
                    "Los datos se almacenan en MongoDB, base de datos NoSQL orientada a documentos.",
                    "El driver Motor permite operaciones asíncronas eficientes.",
                    "Las colecciones principales son: users, courses, categories.",
                    "Los identificadores son ObjectId de MongoDB, convertidos a string en la capa de aplicación.",
                ],
            },
            {
                "title": "Autenticación y seguridad",
                "content": [
                    "Las contraseñas se almacenan hasheadas con bcrypt.",
                    "El sistema de roles (RBAC) controla el acceso a cada sección: student, instructor, admin.",
                    "Las rutas protegidas usan HOCs (Higher-Order Components) de Reflex.",
                    "Las sesiones se gestionan mediante el estado de Reflex en el servidor.",
                ],
            },
        ],
    },
]


# ---------------------------------------------------------------------------
# Componentes
# ---------------------------------------------------------------------------

def doc_item(title: str, content: list[str]) -> rx.Component:
    return rx.accordion.item(
        header=rx.text(title, size="3", weight="medium"),
        content=rx.vstack(
            *[
                rx.hstack(
                    rx.box(
                        width="6px",
                        height="6px",
                        border_radius="50%",
                        background=rx.color("purple", 9),
                        flex_shrink="0",
                        margin_top="6px",
                    ),
                    rx.text(step, size="2", color=rx.color("gray", 11), line_height="1.7"),
                    spacing="3",
                    align_items="start",
                    width="100%",
                )
                for step in content
            ],
            spacing="2",
            padding_left="0.5em",
            padding_bottom="0.75em",
            width="100%",
        ),
        value=title,
    )


def doc_section(icon: str, color: str, title: str, items: list[dict]) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=20, color="white"),
                    background=rx.color(color, 9),
                    padding="0.55em",
                    border_radius="10px",
                    flex_shrink="0",
                ),
                rx.heading(title, size="5"),
                spacing="3",
                align_items="center",
            ),
            rx.accordion.root(
                *[doc_item(item["title"], item["content"]) for item in items],
                collapsible=True,
                width="100%",
                variant="ghost",
            ),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def sidebar_link(icon: str, color: str, title: str, section_id: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.box(
                rx.icon(icon, size=14, color="white"),
                background=rx.color(color, 9),
                padding="0.3em",
                border_radius="6px",
                flex_shrink="0",
            ),
            rx.text(title, size="2"),
            spacing="2",
            align_items="center",
        ),
        href=f"#",
        color=rx.color("gray", 11),
        _hover={"color": rx.color("purple", 10)},
        text_decoration="none",
    )


def hero_section() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.box(
                rx.icon("book", size=40, color="white"),
                background=rx.color("purple", 9),
                padding="1.1em",
                border_radius="20px",
                box_shadow=f"0 8px 32px {rx.color('purple', 6)}",
            ),
            margin_bottom="0.5em",
        ),
        rx.heading(
            "Documentación",
            size="9",
            text_align="center",
            background=f"linear-gradient(135deg, {rx.color('purple', 10)}, {rx.color('blue', 10)})",
            background_clip="text",
            color="transparent",
        ),
        rx.text(
            "Todo lo que necesitas saber para sacar el máximo partido a E-Learning JCB",
            size="4",
            color=rx.color("gray", 11),
            text_align="center",
            max_width="600px",
        ),
        rx.hstack(
            rx.link(
                rx.button(
                    rx.hstack(rx.icon("zap", size=16), rx.text("Inicio Rápido"), spacing="2"),
                    color_scheme="purple",
                    size="2",
                ),
                href="/register",
            ),
            rx.link(
                rx.button(
                    rx.hstack(rx.icon("circle-help", size=16), rx.text("FAQ"), spacing="2"),
                    variant="soft",
                    size="2",
                ),
                href="/faq",
            ),
            spacing="3",
        ),
        align_items="center",
        spacing="4",
        padding_y="3em",
        width="100%",
    )


def docs_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            hero_section(),
            # Índice rápido
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon("list", size=18, color=rx.color("purple", 9)),
                        rx.text("Índice de contenidos", size="3", weight="bold"),
                        spacing="2",
                    ),
                    rx.grid(
                        *[
                            sidebar_link(s["icon"], s["color"], s["title"], s["id"])
                            for s in DOCS_SECTIONS
                        ],
                        columns=rx.breakpoints(initial="1", sm="2", md="3"),
                        spacing="3",
                        width="100%",
                    ),
                    spacing="3",
                    width="100%",
                ),
                margin_bottom="2em",
                width="100%",
            ),
            # Secciones de documentación
            rx.vstack(
                *[
                    doc_section(s["icon"], s["color"], s["title"], s["items"])
                    for s in DOCS_SECTIONS
                ],
                spacing="5",
                width="100%",
            ),
            # CTA final
            rx.center(
                rx.card(
                    rx.hstack(
                        rx.box(
                            rx.icon("message-circle", size=24, color="white"),
                            background=rx.color("purple", 9),
                            padding="0.7em",
                            border_radius="12px",
                            flex_shrink="0",
                        ),
                        rx.vstack(
                            rx.text("¿No encuentras lo que buscas?", size="4", weight="bold"),
                            rx.text(
                                "Consulta las preguntas frecuentes o contacta con nuestro equipo de soporte.",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="1",
                            align_items="start",
                        ),
                        rx.vstack(
                            rx.link(
                                rx.button("Ver FAQ", color_scheme="purple", size="2"),
                                href="/faq",
                            ),
                            rx.link(
                                rx.button("Contactar", variant="soft", size="2"),
                                href="/contact",
                            ),
                            spacing="2",
                        ),
                        spacing="4",
                        align_items="center",
                        flex_wrap="wrap",
                    ),
                    width="100%",
                ),
                width="100%",
                margin_top="2em",
            ),
            max_width="900px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
            padding_bottom="4em",
        ),
        footer(),
        width="100%",
    )
