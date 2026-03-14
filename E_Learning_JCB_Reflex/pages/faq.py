"""
Página de Preguntas Frecuentes (FAQ) de E-Learning JCB.

Ruta: /faq
Acceso: Pública
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer


# ---------------------------------------------------------------------------
# Datos de las preguntas frecuentes
# ---------------------------------------------------------------------------

FAQ_CATEGORIES = [
    {
        "icon": "user",
        "color": "purple",
        "title": "Cuenta y Registro",
        "questions": [
            {
                "q": "¿Cómo me registro en la plataforma?",
                "a": "Haz clic en 'Registrarse' en la barra de navegación. Rellena el formulario con tu nombre, email y contraseña. Recibirás acceso inmediato a la plataforma como estudiante.",
            },
            {
                "q": "¿Puedo cambiar mi contraseña?",
                "a": "Sí. Desde tu perfil (icono de usuario en la barra superior) encontrarás la opción para actualizar tu contraseña en cualquier momento.",
            },
            {
                "q": "¿Cómo me convierto en instructor?",
                "a": "Contacta con el equipo de administración a través del formulario de contacto o escríbenos a admin@elearningjcb.com. Evaluaremos tu perfil y te asignaremos el rol de instructor.",
            },
            {
                "q": "¿Puedo tener más de un rol?",
                "a": "Actualmente cada cuenta tiene un único rol: estudiante, instructor o administrador. Si necesitas cambiar tu rol, contacta con administración.",
            },
        ],
    },
    {
        "icon": "book-open",
        "color": "blue",
        "title": "Cursos y Contenido",
        "questions": [
            {
                "q": "¿Cómo me inscribo en un curso?",
                "a": "Navega al catálogo de cursos, selecciona el que te interese y pulsa el botón 'Inscribirse'. Si el curso es gratuito, el acceso es inmediato.",
            },
            {
                "q": "¿Los cursos tienen fecha de caducidad?",
                "a": "No. Una vez inscrito, tienes acceso ilimitado al curso durante el tiempo que la plataforma esté activa.",
            },
            {
                "q": "¿Puedo descargar el contenido para verlo offline?",
                "a": "Actualmente el contenido está disponible exclusivamente online a través de la plataforma. Estamos trabajando en funcionalidades de descarga para versiones futuras.",
            },
            {
                "q": "¿Los cursos tienen certificado al finalizar?",
                "a": "Estamos desarrollando el sistema de certificados. Próximamente podrás obtener un certificado de finalización para compartir en LinkedIn y otras redes profesionales.",
            },
            {
                "q": "¿Con qué frecuencia se actualizan los cursos?",
                "a": "Cada instructor es responsable de mantener su contenido actualizado. Los cursos se revisan periódicamente para garantizar que reflejan el estado actual de la tecnología.",
            },
        ],
    },
    {
        "icon": "credit-card",
        "color": "green",
        "title": "Pagos y Precios",
        "questions": [
            {
                "q": "¿Cuánto cuestan los cursos?",
                "a": "El precio varía según el curso. Algunos son completamente gratuitos. El precio de cada curso se muestra claramente en su página de detalle antes de inscribirte.",
            },
            {
                "q": "¿Qué métodos de pago aceptáis?",
                "a": "Actualmente estamos integrando el sistema de pagos. Por el momento, muchos cursos están disponibles de forma gratuita durante el período de lanzamiento.",
            },
            {
                "q": "¿Hay política de devolución?",
                "a": "Ofrecemos devolución completa en los 7 días siguientes a la compra si no has completado más del 20% del contenido del curso. Contacta con soporte para gestionar tu solicitud.",
            },
        ],
    },
    {
        "icon": "monitor",
        "color": "orange",
        "title": "Aspectos Técnicos",
        "questions": [
            {
                "q": "¿Qué navegadores son compatibles?",
                "a": "La plataforma funciona correctamente en Chrome, Firefox, Edge y Safari (versiones recientes). Recomendamos mantener tu navegador actualizado para la mejor experiencia.",
            },
            {
                "q": "¿Puedo acceder desde el móvil?",
                "a": "Sí. La plataforma es completamente responsive y está optimizada para dispositivos móviles y tablets.",
            },
            {
                "q": "¿Qué velocidad de internet necesito?",
                "a": "Para ver vídeos con fluidez recomendamos al menos 5 Mbps. Para contenido de texto e imágenes cualquier conexión estable es suficiente.",
            },
            {
                "q": "He encontrado un error en la plataforma, ¿cómo lo reporto?",
                "a": "Usa el formulario de contacto describiendo el error, el navegador que usas y los pasos para reproducirlo. Nuestro equipo técnico lo revisará lo antes posible.",
            },
        ],
    },
    {
        "icon": "users",
        "color": "pink",
        "title": "Para Instructores",
        "questions": [
            {
                "q": "¿Cómo creo un curso?",
                "a": "Desde tu dashboard de instructor, pulsa '+ Crear Curso' o ve a 'Mis Cursos'. Rellena el formulario con título, descripción, nivel y precio. El curso quedará publicado inmediatamente.",
            },
            {
                "q": "¿Puedo editar un curso ya publicado?",
                "a": "Sí. Desde la página 'Mis Cursos' puedes editar cualquier curso en cualquier momento sin que los estudiantes pierdan su progreso.",
            },
            {
                "q": "¿Cómo veo las estadísticas de mis cursos?",
                "a": "En tu dashboard de instructor encontrarás un resumen. Para datos detallados accede a la sección 'Estadísticas' del menú lateral.",
            },
            {
                "q": "¿Los instructores reciben remuneración?",
                "a": "Estamos definiendo el modelo de reparto de ingresos. Contacta con administración para conocer las condiciones actuales.",
            },
        ],
    },
]


# ---------------------------------------------------------------------------
# Componentes
# ---------------------------------------------------------------------------

def faq_item(question: str, answer: str) -> rx.Component:
    return rx.accordion.item(
        header=rx.hstack(
            rx.icon("circle-help", size=16, color=rx.color("gray", 10)),
            rx.text(question, size="3", weight="medium"),
            spacing="2",
            align_items="center",
        ),
        content=rx.box(
            rx.text(answer, size="2", color=rx.color("gray", 11), line_height="1.7"),
            padding_left="1.6em",
            padding_bottom="0.5em",
        ),
        value=question,
    )


def faq_category(icon: str, color: str, title: str, questions: list[dict]) -> rx.Component:
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
                *[faq_item(q["q"], q["a"]) for q in questions],
                collapsible=True,
                width="100%",
                variant="ghost",
            ),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def hero_section() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.box(
                rx.icon("circle-help", size=40, color="white"),
                background=rx.color("purple", 9),
                padding="1.1em",
                border_radius="20px",
                box_shadow=f"0 8px 32px {rx.color('purple', 6)}",
            ),
            margin_bottom="0.5em",
        ),
        rx.heading(
            "Preguntas Frecuentes",
            size="9",
            text_align="center",
            background=f"linear-gradient(135deg, {rx.color('purple', 10)}, {rx.color('blue', 10)})",
            background_clip="text",
            color="transparent",
        ),
        rx.text(
            "Encuentra respuesta a las dudas más habituales sobre la plataforma",
            size="4",
            color=rx.color("gray", 11),
            text_align="center",
            max_width="600px",
        ),
        rx.link(
            rx.button(
                rx.hstack(
                    rx.icon("mail", size=16),
                    rx.text("¿No encuentras tu respuesta? Contáctanos"),
                    spacing="2",
                ),
                variant="soft",
                color_scheme="purple",
                size="2",
            ),
            href="/contact",
        ),
        align_items="center",
        spacing="4",
        padding_y="3em",
        width="100%",
    )


def faq_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            hero_section(),
            rx.vstack(
                *[
                    faq_category(
                        cat["icon"],
                        cat["color"],
                        cat["title"],
                        cat["questions"],
                    )
                    for cat in FAQ_CATEGORIES
                ],
                spacing="5",
                width="100%",
            ),
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
                            rx.text("¿Tienes otra pregunta?", size="4", weight="bold"),
                            rx.text(
                                "Nuestro equipo estará encantado de ayudarte. Escríbenos a través del formulario de contacto.",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="1",
                            align_items="start",
                        ),
                        rx.link(
                            rx.button("Contactar", color_scheme="purple", size="2"),
                            href="/contact",
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
