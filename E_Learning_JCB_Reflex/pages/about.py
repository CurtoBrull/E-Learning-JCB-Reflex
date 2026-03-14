"""
Página 'Sobre Nosotros' de E-Learning JCB.

Muestra información de la plataforma y estadísticas reales de la BD.

Ruta: /about
Acceso: Pública
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer
from E_Learning_JCB_Reflex.states.about_state import AboutState


# ---------------------------------------------------------------------------
# Componentes reutilizables
# ---------------------------------------------------------------------------

def stat_card(value: rx.Var | str, label: str, icon: str, color: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.box(
                rx.icon(icon, size=28, color="white"),
                background=rx.color(color, 9),
                padding="0.75em",
                border_radius="14px",
                margin_bottom="0.5em",
            ),
            rx.text(value, size="8", weight="bold", color=rx.color(color, 11)),
            rx.text(label, size="2", color=rx.color("gray", 10), text_align="center"),
            align_items="center",
            spacing="1",
        ),
        width="100%",
        text_align="center",
    )


def value_card(icon: str, color: str, title: str, description: str) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.box(
                rx.icon(icon, size=22, color="white"),
                background=rx.color(color, 9),
                padding="0.6em",
                border_radius="10px",
                flex_shrink="0",
            ),
            rx.vstack(
                rx.text(title, size="3", weight="bold"),
                rx.text(description, size="2", color=rx.color("gray", 10)),
                spacing="1",
                align_items="start",
            ),
            spacing="4",
            align_items="start",
            width="100%",
        ),
        width="100%",
    )


def team_card(name: str, role: str, description: str, avatar_icon: str, color: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.box(
                rx.icon(avatar_icon, size=32, color="white"),
                background=rx.color(color, 9),
                padding="1em",
                border_radius="50%",
                width="72px",
                height="72px",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.text(name, size="4", weight="bold"),
            rx.badge(role, color_scheme=color, size="1", variant="soft"),
            rx.text(
                description,
                size="2",
                color=rx.color("gray", 10),
                text_align="center",
            ),
            align_items="center",
            spacing="2",
            padding="0.5em",
        ),
        width="100%",
        text_align="center",
    )


def section_heading(title: str, subtitle: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size="7", text_align="center"),
        rx.text(
            subtitle,
            size="3",
            color=rx.color("gray", 10),
            text_align="center",
            max_width="600px",
        ),
        align_items="center",
        spacing="2",
        width="100%",
    )


def category_tag(name: str) -> rx.Component:
    return rx.badge(name, color_scheme="purple", variant="soft", size="2")


# ---------------------------------------------------------------------------
# Secciones
# ---------------------------------------------------------------------------

def hero_section() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.box(
                rx.icon("graduation-cap", size=48, color="white"),
                background=rx.color("purple", 9),
                padding="1.2em",
                border_radius="24px",
                box_shadow=f"0 8px 32px {rx.color('purple', 6)}",
            ),
            margin_bottom="1em",
        ),
        rx.heading(
            "E-Learning JCB",
            size="9",
            text_align="center",
            background=f"linear-gradient(135deg, {rx.color('purple', 10)}, {rx.color('blue', 10)})",
            background_clip="text",
            color="transparent",
        ),
        rx.text(
            "La plataforma de aprendizaje online diseñada para impulsar tu carrera en tecnología",
            size="5",
            color=rx.color("gray", 11),
            text_align="center",
            max_width="700px",
        ),
        rx.hstack(
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("book-open", size=18),
                        rx.text("Ver Cursos"),
                        spacing="2",
                    ),
                    color_scheme="purple",
                    size="3",
                ),
                href="/courses",
            ),
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("users", size=18),
                        rx.text("Nuestros Instructores"),
                        spacing="2",
                    ),
                    variant="soft",
                    size="3",
                ),
                href="/instructors",
            ),
            spacing="3",
            flex_wrap="wrap",
            justify_content="center",
        ),
        align_items="center",
        spacing="5",
        padding_y="4em",
        width="100%",
    )


def stats_section() -> rx.Component:
    return rx.vstack(
        section_heading(
            "La plataforma en números",
            "Datos reales extraídos directamente de nuestra base de datos",
        ),
        rx.cond(
            AboutState.loading,
            rx.center(rx.spinner(size="3"), padding="2em"),
            rx.grid(
                stat_card(AboutState.total_courses.to_string(), "Cursos disponibles", "graduation-cap", "purple"),
                stat_card(AboutState.total_instructors.to_string(), "Instructores expertos", "user-check", "blue"),
                stat_card(AboutState.total_students.to_string(), "Estudiantes registrados", "users", "green"),
                stat_card(AboutState.total_lessons.to_string(), "Lecciones en total", "play-circle", "orange"),
                stat_card(AboutState.total_enrollments.to_string(), "Matriculaciones activas", "book-open", "red"),
                stat_card(AboutState.categories.length().to_string(), "Áreas de conocimiento", "layers", "yellow"),
                columns=rx.breakpoints(initial="2", sm="3", lg="6"),
                spacing="4",
                width="100%",
            ),
        ),
        align_items="center",
        spacing="6",
        width="100%",
        padding="2em",
        background=rx.color("gray", 2),
        border_radius="16px",
    )


def mission_section() -> rx.Component:
    return rx.grid(
        rx.vstack(
            rx.heading("Nuestra Misión", size="6"),
            rx.text(
                "En E-Learning JCB creemos que el conocimiento tecnológico no debe tener barreras. "
                "Nacimos con el propósito de democratizar el acceso a formación de calidad en "
                "programación, inteligencia artificial, bases de datos y desarrollo web, ofreciendo "
                "cursos impartidos por profesionales activos del sector.",
                size="3",
                color=rx.color("gray", 11),
                line_height="1.8",
            ),
            rx.text(
                "Cada curso está diseñado para que puedas aprender a tu propio ritmo, "
                "con contenido práctico y actualizado que podrás aplicar desde el primer día.",
                size="3",
                color=rx.color("gray", 11),
                line_height="1.8",
            ),
            align_items="start",
            spacing="4",
        ),
        rx.vstack(
            rx.heading("Nuestra Visión", size="6"),
            rx.text(
                "Convertirnos en la plataforma de referencia en habla hispana para la formación "
                "técnica online, conectando a miles de profesionales con los instructores más "
                "cualificados del sector IT.",
                size="3",
                color=rx.color("gray", 11),
                line_height="1.8",
            ),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("check-circle", size=16, color=rx.color("green", 9)),
                        rx.text("Contenido actualizado y relevante", size="2"),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("check-circle", size=16, color=rx.color("green", 9)),
                        rx.text("Instructores con experiencia real en el sector", size="2"),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("check-circle", size=16, color=rx.color("green", 9)),
                        rx.text("Aprendizaje flexible a tu ritmo", size="2"),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("check-circle", size=16, color=rx.color("green", 9)),
                        rx.text("Comunidad activa de estudiantes", size="2"),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("check-circle", size=16, color=rx.color("green", 9)),
                        rx.text("Certificados reconocidos por la industria", size="2"),
                        spacing="2",
                    ),
                    align_items="start",
                    spacing="2",
                ),
                background=rx.color("green", 2),
                border=f"1px solid {rx.color('green', 5)}",
                border_radius="12px",
                padding="1.2em",
            ),
            align_items="start",
            spacing="4",
        ),
        columns=rx.breakpoints(initial="1", md="2"),
        spacing="8",
        width="100%",
    )


def values_section() -> rx.Component:
    return rx.vstack(
        section_heading(
            "Nuestros Valores",
            "Los principios que guían todo lo que hacemos",
        ),
        rx.grid(
            value_card("lightbulb", "yellow", "Innovación", "Adoptamos las últimas tecnologías y metodologías pedagógicas para ofrecerte la mejor experiencia de aprendizaje."),
            value_card("shield-check", "green", "Calidad", "Cada curso pasa por un proceso de revisión riguroso para garantizar que el contenido es preciso, claro y aplicable."),
            value_card("heart", "red", "Pasión", "Tanto instructores como el equipo de E-Learning JCB sentimos una profunda pasión por la tecnología y la educación."),
            value_card("users", "blue", "Comunidad", "Fomentamos un entorno de aprendizaje colaborativo donde estudiantes e instructores crecen juntos."),
            value_card("globe", "purple", "Accesibilidad", "Creemos que la formación de calidad debe estar al alcance de todos, sin importar dónde estés."),
            value_card("trending-up", "orange", "Crecimiento", "Nos comprometemos con el desarrollo profesional continuo de cada uno de nuestros estudiantes."),
            columns=rx.breakpoints(initial="1", sm="2", lg="3"),
            spacing="4",
            width="100%",
        ),
        align_items="center",
        spacing="6",
        width="100%",
    )


def categories_section() -> rx.Component:
    return rx.vstack(
        section_heading(
            "Áreas de Conocimiento",
            "Tecnologías y disciplinas que encontrarás en nuestra plataforma",
        ),
        rx.cond(
            AboutState.categories.length() > 0,
            rx.flex(
                rx.foreach(
                    AboutState.categories,
                    category_tag,
                ),
                flex_wrap="wrap",
                gap="2",
                justify_content="center",
            ),
            rx.spinner(size="2"),
        ),
        align_items="center",
        spacing="5",
        width="100%",
    )


def team_section() -> rx.Component:
    return rx.vstack(
        section_heading(
            "Quiénes somos",
            "El equipo detrás de E-Learning JCB",
        ),
        # Fila 1: Javier centrado — card grande destacada
        rx.center(
            rx.card(
                rx.vstack(
                    rx.image(
                        src="/images/jcb/JCB_Tanque.png",
                        width="200px",
                        height="200px",
                        border_radius="50%",
                        object_fit="cover",
                        border=f"4px solid {rx.color('purple', 8)}",
                        box_shadow=f"0 8px 32px {rx.color('purple', 5)}",
                    ),
                    rx.text("Javier Curto Brull", size="6", weight="bold"),
                    rx.badge("Fundador & Desarrollador", color_scheme="purple", size="2", variant="soft"),
                    rx.text(
                        "Desarrollador full-stack apasionado por la educación tecnológica. "
                        "Creó E-Learning JCB para democratizar el acceso a la formación IT de calidad, "
                        "combinando su experiencia en desarrollo web con su vocación docente.",
                        size="3",
                        color=rx.color("gray", 10),
                        text_align="center",
                        max_width="420px",
                    ),
                    rx.hstack(
                        rx.badge(rx.hstack(rx.icon("code", size=14), rx.text("Python · Reflex"), spacing="1"), color_scheme="purple", variant="outline", size="1"),
                        rx.badge(rx.hstack(rx.icon("database", size=14), rx.text("MongoDB"), spacing="1"), color_scheme="green", variant="outline", size="1"),
                        spacing="2",
                        justify_content="center",
                        flex_wrap="wrap",
                    ),
                    align_items="center",
                    spacing="3",
                    padding="1.5em",
                ),
                width="100%",
                max_width="520px",
                text_align="center",
                box_shadow=f"0 4px 24px {rx.color('purple', 4)}",
                border=f"1px solid {rx.color('purple', 5)}",
            ),
            width="100%",
        ),
        # Fila 2: Instructores + Comunidad formando la base del triángulo
        rx.grid(
            team_card(
                "Equipo de Instructores",
                "9 Expertos del Sector",
                "Profesionales activos de la industria con años de experiencia en sus áreas, comprometidos con transmitir conocimiento real y aplicable.",
                "users",
                "blue",
            ),
            team_card(
                "Comunidad JCB",
                "Estudiantes y Alumni",
                "Una comunidad creciente de estudiantes que aprenden, comparten y crecen juntos en su camino hacia el desarrollo profesional en tecnología.",
                "heart",
                "green",
            ),
            columns=rx.breakpoints(initial="1", sm="2"),
            spacing="4",
            width="100%",
            max_width="720px",
        ),
        align_items="center",
        spacing="6",
        width="100%",
    )


def tech_row(badge_label: str, color: str, icon: str, description: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.icon(icon, size=16, color="white"),
            background=rx.color(color, 9),
            padding="0.4em",
            border_radius="8px",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.badge(badge_label, color_scheme=color, size="1", variant="soft"),
            rx.text(description, size="2", color=rx.color("gray", 10)),
            spacing="0",
            align_items="start",
        ),
        spacing="3",
        align_items="center",
        width="100%",
    )


def tech_section() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Tecnología que nos impulsa", size="6"),
            rx.text(
                "E-Learning JCB está construida con tecnologías modernas y robustas "
                "para garantizar la mejor experiencia de usuario.",
                size="3",
                color=rx.color("gray", 10),
            ),
            rx.divider(),
            tech_row("Reflex", "purple", "zap", "Framework Python full-stack para construir aplicaciones web reactivas sin escribir JavaScript."),
            tech_row("Python", "blue", "code-2", "Lenguaje principal del backend: lógica de negocio, servicios, modelos y estados de la aplicación."),
            tech_row("MongoDB Atlas", "green", "database", "Base de datos NoSQL en la nube que almacena cursos, usuarios, lecciones e inscripciones."),
            tech_row("Motor (Async)", "orange", "activity", "Driver asíncrono de MongoDB para Python, permite operaciones de base de datos sin bloquear el servidor."),
            tech_row("Radix UI", "red", "layout", "Sistema de componentes UI accesibles y personalizables que dan forma a toda la interfaz visual."),
            tech_row("Bun", "yellow", "rocket", "Runtime y bundler ultra-rápido utilizado por Reflex para compilar y servir el frontend."),
            spacing="4",
            width="100%",
            align_items="start",
        ),
        width="100%",
    )


def cta_section() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.icon("rocket", size=40, color=rx.color("purple", 9)),
            rx.heading("¿Listo para empezar?", size="7", text_align="center"),
            rx.text(
                "Únete a la comunidad de E-Learning JCB y da el siguiente paso en tu carrera tecnológica.",
                size="4",
                color=rx.color("gray", 10),
                text_align="center",
                max_width="500px",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "Crear cuenta gratis",
                        color_scheme="purple",
                        size="3",
                    ),
                    href="/register",
                ),
                rx.link(
                    rx.button(
                        "Ver cursos",
                        variant="soft",
                        size="3",
                    ),
                    href="/courses",
                ),
                spacing="3",
                flex_wrap="wrap",
                justify_content="center",
            ),
            align_items="center",
            spacing="4",
            padding="2em",
        ),
        width="100%",
        background=rx.color("purple", 2),
        border=f"1px solid {rx.color('purple', 5)}",
    )


# ---------------------------------------------------------------------------
# Página principal
# ---------------------------------------------------------------------------

def about_page() -> rx.Component:
    return rx.box(
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background_image="url(/images/bg/background_login.webp)",
            background_size="cover",
            background_position="center",
            opacity="0.07",
            z_index="-1",
        ),
        rx.vstack(
            navbar(),
            rx.container(
                rx.vstack(
                    hero_section(),
                    stats_section(),
                    mission_section(),
                    values_section(),
                    categories_section(),
                    team_section(),
                    tech_section(),
                    cta_section(),
                    spacing="8",
                    width="100%",
                    padding_y="2em",
                ),
                max_width="1200px",
                padding_x=["4", "6", "8"],
                margin_x="auto",
                on_mount=AboutState.load_stats,
            ),
            footer(),
            width="100%",
            spacing="0",
        ),
        width="100%",
        position="relative",
    )
