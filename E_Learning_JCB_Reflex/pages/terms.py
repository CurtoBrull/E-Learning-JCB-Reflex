"""
Página de Términos y Condiciones de E-Learning JCB.

Ruta: /terms
Acceso: Pública
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer

LAST_UPDATED = "14 de marzo de 2026"

SECTIONS = [
    {
        "icon": "file-text",
        "color": "blue",
        "title": "1. Aceptación de los términos",
        "items": [
            "Al acceder y utilizar la plataforma E-Learning JCB, aceptas quedar vinculado por los presentes Términos y Condiciones, así como por nuestra Política de Privacidad y Política de Cookies.",
            "Si no estás de acuerdo con alguno de estos términos, te rogamos que no utilices la plataforma.",
            "Nos reservamos el derecho a modificar estos términos en cualquier momento. Los cambios serán efectivos desde su publicación. El uso continuado de la plataforma implica la aceptación de los términos actualizados.",
        ],
    },
    {
        "icon": "users",
        "color": "purple",
        "title": "2. Registro y cuenta de usuario",
        "items": [
            "Para acceder a los cursos debes crear una cuenta proporcionando información veraz, completa y actualizada.",
            "Eres responsable de mantener la confidencialidad de tu contraseña y de todas las actividades que ocurran bajo tu cuenta.",
            "Debes notificarnos inmediatamente cualquier uso no autorizado de tu cuenta o cualquier otra brecha de seguridad.",
            "Nos reservamos el derecho de suspender o cancelar cuentas que incumplan estos términos, sin previo aviso.",
            "Debes tener al menos 14 años para registrarte. Los menores de 14 años necesitan el consentimiento expreso de sus padres o tutores.",
        ],
    },
    {
        "icon": "book-open",
        "color": "green",
        "title": "3. Uso del servicio",
        "items": [
            "Puedes acceder al contenido de los cursos en los que estés inscrito para uso personal y no comercial.",
            "No está permitido compartir tu cuenta con terceros ni proporcionar acceso al contenido a personas no inscritas.",
            "Queda prohibido reproducir, distribuir, modificar o crear obras derivadas del contenido de los cursos sin autorización expresa.",
            "No puedes usar la plataforma para actividades ilegales, fraudulentas o que perjudiquen a otros usuarios.",
            "El scraping automatizado, la ingeniería inversa o cualquier intento de acceder a datos no públicos de la plataforma está expresamente prohibido.",
        ],
    },
    {
        "icon": "presentation",
        "color": "orange",
        "title": "4. Instructores y contenido",
        "items": [
            "Los instructores son responsables de la veracidad, calidad y actualización del contenido que publican.",
            "Al publicar contenido en la plataforma, el instructor garantiza que posee los derechos necesarios sobre dicho contenido.",
            "E-Learning JCB se reserva el derecho de revisar, modificar o retirar cualquier contenido que incumpla estos términos o la legislación aplicable.",
            "Los instructores no pueden publicar contenido ofensivo, discriminatorio, violento, obsceno o que viole derechos de terceros.",
            "La plataforma puede establecer acuerdos de reparto de ingresos con instructores, regulados en un contrato específico.",
        ],
    },
    {
        "icon": "credit-card",
        "color": "yellow",
        "title": "5. Pagos y reembolsos",
        "items": [
            "Los precios de los cursos se muestran claramente antes de la inscripción e incluyen los impuestos aplicables.",
            "El pago se procesa de forma segura a través de los proveedores de pago integrados en la plataforma.",
            "Ofrecemos reembolso completo en los 7 días siguientes a la compra, siempre que no se haya completado más del 20% del contenido.",
            "Para solicitar un reembolso, contacta con soporte en pagos@elearningjcb.com indicando el número de pedido.",
            "Los cursos gratuitos no generan derecho a reembolso económico.",
        ],
    },
    {
        "icon": "copyright",
        "color": "red",
        "title": "6. Propiedad intelectual",
        "items": [
            "Todo el contenido de la plataforma (diseño, código, textos, imágenes, logotipos) es propiedad de E-Learning JCB o de sus licenciantes.",
            "El contenido de los cursos es propiedad de los instructores respectivos, salvo acuerdo en contrario.",
            "Queda prohibida cualquier reproducción total o parcial sin autorización escrita previa.",
            "Las marcas, logos y nombres comerciales de E-Learning JCB son propiedad exclusiva de la plataforma.",
        ],
    },
    {
        "icon": "alert-triangle",
        "color": "gray",
        "title": "7. Limitación de responsabilidad",
        "items": [
            "La plataforma se ofrece 'tal cual', sin garantías de disponibilidad ininterrumpida ni ausencia de errores.",
            "E-Learning JCB no se hace responsable de los daños indirectos, incidentales o consecuentes derivados del uso o imposibilidad de uso de la plataforma.",
            "La responsabilidad máxima de E-Learning JCB no superará el importe abonado por el usuario en los 12 meses previos al evento que originó el daño.",
            "No somos responsables del contenido publicado por instructores o usuarios, aunque nos comprometemos a actuar con diligencia ante denuncias fundadas.",
        ],
    },
    {
        "icon": "scale",
        "color": "teal",
        "title": "8. Legislación aplicable",
        "items": [
            "Estos términos se rigen por la legislación española y de la Unión Europea.",
            "Para cualquier controversia derivada del uso de la plataforma, las partes se someten a los Juzgados y Tribunales de Madrid, con renuncia expresa a cualquier otro fuero.",
            "Si alguna cláusula de estos términos resultara nula o inaplicable, el resto de las cláusulas permanecerán en vigor.",
            "La versión en español de estos términos prevalece sobre cualquier traducción en caso de discrepancia.",
        ],
    },
    {
        "icon": "mail",
        "color": "blue",
        "title": "9. Contacto",
        "items": [
            "Para cualquier consulta sobre estos términos, puedes escribirnos a legal@elearningjcb.com.",
            "También puedes usar el formulario de contacto disponible en /contact.",
            "Intentaremos responder a todas las consultas en un plazo máximo de 5 días hábiles.",
        ],
    },
]


def terms_section(icon: str, color: str, title: str, items: list[str]) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=18, color="white"),
                    background=rx.color(color, 9),
                    padding="0.5em",
                    border_radius="9px",
                    flex_shrink="0",
                ),
                rx.heading(title, size="4"),
                spacing="3",
                align_items="center",
            ),
            rx.vstack(
                *[
                    rx.hstack(
                        rx.box(
                            width="6px",
                            height="6px",
                            border_radius="50%",
                            background=rx.color(color, 9),
                            flex_shrink="0",
                            margin_top="7px",
                        ),
                        rx.text(item, size="2", color=rx.color("gray", 11), line_height="1.8"),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    )
                    for item in items
                ],
                spacing="2",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def terms_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.center(
                    rx.box(
                        rx.icon("file-text", size=40, color="white"),
                        background=rx.color("blue", 9),
                        padding="1.1em",
                        border_radius="20px",
                        box_shadow=f"0 8px 32px {rx.color('blue', 6)}",
                    ),
                    margin_bottom="0.5em",
                ),
                rx.heading(
                    "Términos y Condiciones",
                    size="9",
                    text_align="center",
                    background=f"linear-gradient(135deg, {rx.color('blue', 10)}, {rx.color('purple', 10)})",
                    background_clip="text",
                    color="transparent",
                ),
                rx.text(
                    f"Última actualización: {LAST_UPDATED}",
                    size="2",
                    color=rx.color("gray", 10),
                    text_align="center",
                ),
                rx.text(
                    "Por favor, lee detenidamente estos términos antes de utilizar la plataforma E-Learning JCB. El acceso y uso de la plataforma implica la aceptación de las condiciones descritas a continuación.",
                    size="3",
                    color=rx.color("gray", 11),
                    text_align="center",
                    max_width="700px",
                ),
                align_items="center",
                spacing="4",
                padding_y="3em",
                width="100%",
            ),
            rx.vstack(
                *[
                    terms_section(s["icon"], s["color"], s["title"], s["items"])
                    for s in SECTIONS
                ],
                spacing="4",
                width="100%",
            ),
            max_width="860px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
            padding_bottom="4em",
        ),
        footer(),
        width="100%",
    )
