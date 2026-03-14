"""
Página de Blog de E-Learning JCB.

Ruta: /blog
Acceso: Pública
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer


# ---------------------------------------------------------------------------
# Datos del blog
# ---------------------------------------------------------------------------

FEATURED_POST = {
    "id": "1",
    "title": "El futuro del aprendizaje online: IA, personalización y microlearning",
    "excerpt": "La educación online está viviendo una revolución silenciosa. La inteligencia artificial ya no es ciencia ficción en el aula virtual: personaliza itinerarios, detecta dificultades y adapta el ritmo a cada estudiante. Te contamos cómo estas tendencias están reshaping el e-learning tal y como lo conocemos.",
    "category": "Tendencias",
    "category_color": "purple",
    "author": "Javier Curto Brull",
    "author_role": "Fundador & Desarrollador",
    "date": "10 marzo 2026",
    "read_time": "8 min",
    "icon": "brain",
    "gradient": f"linear-gradient(135deg, #7c3aed, #2563eb)",
}

POSTS = [
    {
        "id": "2",
        "title": "Python en 2026: por qué sigue siendo el lenguaje más demandado",
        "excerpt": "Desde IA hasta automatización web, Python domina los rankings de popularidad año tras año. Analizamos qué lo hace tan versátil y qué aprende quien empieza desde cero.",
        "category": "Programación",
        "category_color": "blue",
        "author": "Javier Curto Brull",
        "date": "5 marzo 2026",
        "read_time": "6 min",
        "icon": "code-2",
    },
    {
        "id": "3",
        "title": "Cómo estudiar de forma efectiva: la técnica Pomodoro aplicada al e-learning",
        "excerpt": "No se trata de cuántas horas estudias, sino de cómo las aprovechas. La técnica Pomodoro adaptada a cursos online puede multiplicar tu retención y reducir la fatiga mental.",
        "category": "Productividad",
        "category_color": "green",
        "author": "Javier Curto Brull",
        "date": "28 febrero 2026",
        "read_time": "5 min",
        "icon": "timer",
    },
    {
        "id": "4",
        "title": "MongoDB vs PostgreSQL: ¿cuándo usar cada uno en tus proyectos?",
        "excerpt": "NoSQL o relacional. La respuesta no siempre es obvia. Comparamos ambas tecnologías con casos de uso reales para que puedas tomar la decisión correcta en tu próximo proyecto.",
        "category": "Bases de Datos",
        "category_color": "orange",
        "author": "Javier Curto Brull",
        "date": "21 febrero 2026",
        "read_time": "7 min",
        "icon": "database",
    },
    {
        "id": "5",
        "title": "De cero a desarrollador web: la hoja de ruta en 2026",
        "excerpt": "HTML, CSS, JavaScript, frameworks, backend, bases de datos, despliegue… La cantidad de tecnologías puede abrumar. Te presentamos una ruta de aprendizaje ordenada y práctica.",
        "category": "Guías",
        "category_color": "teal",
        "author": "Javier Curto Brull",
        "date": "14 febrero 2026",
        "read_time": "10 min",
        "icon": "map",
    },
    {
        "id": "6",
        "title": "Reflex: construye aplicaciones web full-stack solo con Python",
        "excerpt": "¿Y si pudieras crear un frontend reactivo sin tocar JavaScript? Reflex lo hace posible. Exploramos su arquitectura, sus ventajas y cuándo tiene sentido usarlo sobre alternativas tradicionales.",
        "category": "Tecnología",
        "category_color": "violet",
        "author": "Javier Curto Brull",
        "date": "7 febrero 2026",
        "read_time": "9 min",
        "icon": "layers",
    },
    {
        "id": "7",
        "title": "Soft skills para developers: las habilidades que nadie te enseña en los cursos",
        "excerpt": "Comunicación, empatía, gestión del tiempo y trabajo en equipo. El mercado laboral busca desarrolladores completos, no solo buenos codificadores. Descubre cómo cultivar estas competencias.",
        "category": "Carrera",
        "category_color": "pink",
        "author": "Javier Curto Brull",
        "date": "31 enero 2026",
        "read_time": "6 min",
        "icon": "heart-handshake",
    },
    {
        "id": "8",
        "title": "Docker para principiantes: contenedores sin miedo",
        "excerpt": "Docker puede parecer intimidante al principio, pero cambia por completo la forma en que desarrollas y despliegas aplicaciones. Guía práctica para empezar desde cero.",
        "category": "DevOps",
        "category_color": "cyan",
        "author": "Javier Curto Brull",
        "date": "24 enero 2026",
        "read_time": "8 min",
        "icon": "box",
    },
    {
        "id": "9",
        "title": "Seguridad web básica: las vulnerabilidades OWASP que todo dev debe conocer",
        "excerpt": "SQL injection, XSS, CSRF… Los ataques más comunes no son los más sofisticados. Aprende a identificarlos y a proteger tus aplicaciones con buenas prácticas desde el primer día.",
        "category": "Seguridad",
        "category_color": "red",
        "author": "Javier Curto Brull",
        "date": "17 enero 2026",
        "read_time": "7 min",
        "icon": "shield-alert",
    },
]

CATEGORIES = ["Todos", "Programación", "Tendencias", "Productividad", "Bases de Datos", "Guías", "Tecnología", "Carrera", "DevOps", "Seguridad"]


# ---------------------------------------------------------------------------
# Estado
# ---------------------------------------------------------------------------

class BlogState(rx.State):
    selected_category: str = "Todos"

    def set_category(self, category: str):
        self.selected_category = category


# ---------------------------------------------------------------------------
# Componentes
# ---------------------------------------------------------------------------

def category_tab(label: str) -> rx.Component:
    return rx.button(
        label,
        on_click=BlogState.set_category(label),
        variant=rx.cond(BlogState.selected_category == label, "solid", "soft"),
        color_scheme="purple",
        size="2",
        radius="full",
        cursor="pointer",
    )


def featured_post_card(post: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            # Header visual con gradiente
            rx.box(
                rx.center(
                    rx.vstack(
                        rx.box(
                            rx.icon(post["icon"], size=48, color="white"),
                            opacity="0.9",
                        ),
                        rx.badge(
                            post["category"],
                            color_scheme=post["category_color"],
                            size="2",
                            variant="solid",
                        ),
                        spacing="3",
                        align_items="center",
                    ),
                    height="100%",
                ),
                background=post["gradient"],
                border_radius="12px",
                height="200px",
                width="100%",
                margin_bottom="1em",
            ),
            rx.hstack(
                rx.badge("Artículo destacado", color_scheme="yellow", size="1", variant="soft"),
                rx.badge(
                    rx.hstack(rx.icon("clock", size=12), rx.text(post["read_time"]), spacing="1"),
                    color_scheme="gray",
                    size="1",
                    variant="soft",
                ),
                spacing="2",
            ),
            rx.heading(post["title"], size="6", line_height="1.4"),
            rx.text(
                post["excerpt"],
                size="3",
                color=rx.color("gray", 11),
                line_height="1.7",
            ),
            rx.hstack(
                rx.hstack(
                    rx.box(
                        rx.icon("user", size=14, color="white"),
                        background=rx.color("purple", 9),
                        padding="0.3em",
                        border_radius="50%",
                        width="28px",
                        height="28px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text(post["author"], size="2", weight="medium"),
                        rx.text(post["author_role"], size="1", color=rx.color("gray", 10)),
                        spacing="0",
                        align_items="start",
                    ),
                    spacing="2",
                    align_items="center",
                ),
                rx.spacer(),
                rx.text(post["date"], size="2", color=rx.color("gray", 10)),
                width="100%",
                align_items="center",
            ),
            rx.link(
                rx.button(
                    rx.hstack(rx.text("Leer artículo"), rx.icon("arrow-right", size=16), spacing="2"),
                    color_scheme="purple",
                    size="2",
                    width="100%",
                ),
                href=f"/blog/{post['id']}",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def post_card(post: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            # Icono + categoría
            rx.hstack(
                rx.box(
                    rx.icon(post["icon"], size=22, color="white"),
                    background=rx.color(post["category_color"], 9),
                    padding="0.55em",
                    border_radius="10px",
                    flex_shrink="0",
                ),
                rx.spacer(),
                rx.badge(
                    rx.hstack(rx.icon("clock", size=11), rx.text(post["read_time"]), spacing="1"),
                    color_scheme="gray",
                    size="1",
                    variant="soft",
                ),
                width="100%",
                align_items="center",
            ),
            rx.badge(post["category"], color_scheme=post["category_color"], size="1", variant="soft"),
            rx.heading(post["title"], size="4", line_height="1.4"),
            rx.text(
                post["excerpt"],
                size="2",
                color=rx.color("gray", 10),
                line_height="1.7",
                # Limitar a ~3 líneas
            ),
            rx.spacer(),
            rx.hstack(
                rx.text(post["author"], size="1", color=rx.color("gray", 10)),
                rx.spacer(),
                rx.text(post["date"], size="1", color=rx.color("gray", 9)),
                width="100%",
            ),
            rx.link(
                rx.button(
                    rx.hstack(rx.text("Leer más"), rx.icon("arrow-right", size=14), spacing="2"),
                    variant="soft",
                    color_scheme=post["category_color"],
                    size="1",
                    width="100%",
                ),
                href=f"/blog/{post['id']}",
                width="100%",
            ),
            spacing="3",
            width="100%",
            height="100%",
        ),
        width="100%",
        height="100%",
    )


def newsletter_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.box(
                    rx.icon("mail", size=28, color="white"),
                    background=rx.color("purple", 9),
                    padding="0.8em",
                    border_radius="14px",
                ),
                margin_bottom="0.5em",
            ),
            rx.heading("Suscríbete al newsletter", size="5", text_align="center"),
            rx.text(
                "Recibe cada semana los mejores artículos sobre tecnología, programación y aprendizaje directamente en tu bandeja de entrada.",
                size="2",
                color=rx.color("gray", 10),
                text_align="center",
                max_width="500px",
            ),
            rx.hstack(
                rx.input(
                    placeholder="tu@email.com",
                    size="3",
                    flex="1",
                    min_width="200px",
                ),
                rx.button(
                    "Suscribirme",
                    color_scheme="purple",
                    size="3",
                ),
                spacing="2",
                flex_wrap="wrap",
                justify_content="center",
                width="100%",
            ),
            rx.text(
                "Sin spam. Cancela cuando quieras.",
                size="1",
                color=rx.color("gray", 9),
            ),
            align_items="center",
            spacing="4",
            padding="1em",
            width="100%",
        ),
        background=f"linear-gradient(135deg, {rx.color('purple', 2)}, {rx.color('blue', 2)})",
        border=f"1px solid {rx.color('purple', 5)}",
        width="100%",
    )


def hero_section() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.box(
                rx.icon("newspaper", size=40, color="white"),
                background=rx.color("purple", 9),
                padding="1.1em",
                border_radius="20px",
                box_shadow=f"0 8px 32px {rx.color('purple', 6)}",
            ),
            margin_bottom="0.5em",
        ),
        rx.heading(
            "Blog E-Learning JCB",
            size="9",
            text_align="center",
            background=f"linear-gradient(135deg, {rx.color('purple', 10)}, {rx.color('blue', 10)})",
            background_clip="text",
            color="transparent",
        ),
        rx.text(
            "Artículos sobre programación, tecnología, productividad y el mundo del aprendizaje online",
            size="4",
            color=rx.color("gray", 11),
            text_align="center",
            max_width="600px",
        ),
        align_items="center",
        spacing="4",
        padding_y="3em",
        width="100%",
    )


def blog_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            hero_section(),
            # Artículo destacado
            featured_post_card(FEATURED_POST),
            # Filtro por categorías
            rx.vstack(
                rx.heading("Todos los artículos", size="6", margin_top="1em"),
                rx.flex(
                    *[category_tab(cat) for cat in CATEGORIES],
                    wrap="wrap",
                    gap="2",
                    width="100%",
                ),
                spacing="4",
                width="100%",
                margin_top="2em",
            ),
            # Grid de posts
            rx.grid(
                *[post_card(p) for p in POSTS],
                columns=rx.breakpoints(initial="1", sm="2", lg="3"),
                spacing="4",
                width="100%",
                margin_top="1.5em",
            ),
            # Newsletter
            rx.box(newsletter_card(), margin_top="3em", width="100%"),
            max_width="1100px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
            padding_bottom="4em",
        ),
        footer(),
        width="100%",
    )
