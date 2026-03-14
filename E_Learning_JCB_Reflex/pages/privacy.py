"""
Página de Política de Privacidad de E-Learning JCB.

Ruta: /privacy
Acceso: Pública
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer

LAST_UPDATED = "14 de marzo de 2026"

SECTIONS = [
    {
        "icon": "info",
        "color": "blue",
        "title": "1. Responsable del tratamiento",
        "content": [
            ("Identidad", "E-Learning JCB, proyecto de Javier Curto Brull."),
            ("Email de contacto", "privacidad@elearningjcb.com"),
            ("Domicilio", "Madrid, España"),
            ("Finalidad", "Gestionar el acceso a la plataforma de formación online y prestar los servicios contratados."),
        ],
        "type": "table",
    },
    {
        "icon": "database",
        "color": "purple",
        "title": "2. Datos que recopilamos",
        "content": [
            "Datos de registro: nombre completo, dirección de correo electrónico y contraseña (almacenada de forma hasheada con bcrypt).",
            "Datos de perfil: foto de avatar y cualquier información adicional que el usuario decida añadir voluntariamente.",
            "Datos de uso: cursos en los que te inscribes, progreso de aprendizaje y actividad dentro de la plataforma.",
            "Datos técnicos: dirección IP, tipo de navegador y sistema operativo, recogidos de forma automática durante el acceso.",
            "Comunicaciones: mensajes enviados a través del formulario de contacto.",
        ],
        "type": "list",
    },
    {
        "icon": "target",
        "color": "green",
        "title": "3. Finalidad del tratamiento",
        "content": [
            "Crear y gestionar tu cuenta de usuario en la plataforma.",
            "Permitir la inscripción en cursos y el seguimiento del progreso formativo.",
            "Enviar comunicaciones relacionadas con el servicio (confirmaciones, actualizaciones de cursos).",
            "Mejorar la plataforma mediante el análisis del uso y detección de errores.",
            "Cumplir con las obligaciones legales aplicables.",
        ],
        "type": "list",
    },
    {
        "icon": "scale",
        "color": "orange",
        "title": "4. Base jurídica",
        "content": [
            ("Ejecución de contrato", "El tratamiento es necesario para prestarte el servicio de formación online que has solicitado al registrarte."),
            ("Interés legítimo", "Análisis de uso para la mejora continua de la plataforma."),
            ("Consentimiento", "Para el envío de comunicaciones comerciales o newsletters, cuando lo hayas aceptado expresamente."),
            ("Obligación legal", "Conservación de datos contables y fiscales según la legislación española."),
        ],
        "type": "table",
    },
    {
        "icon": "clock",
        "color": "yellow",
        "title": "5. Conservación de los datos",
        "content": [
            "Los datos de cuenta se conservan mientras mantengas tu cuenta activa en la plataforma.",
            "Tras la eliminación de la cuenta, los datos se suprimen en un plazo máximo de 30 días, salvo obligación legal de conservación.",
            "Los datos de transacciones económicas se conservan durante 5 años conforme a la normativa fiscal.",
            "Los logs técnicos se eliminan automáticamente pasados 90 días.",
        ],
        "type": "list",
    },
    {
        "icon": "share-2",
        "color": "red",
        "title": "6. Comunicación de datos a terceros",
        "content": [
            "No vendemos ni cedemos tus datos personales a terceros con fines comerciales.",
            "Podemos compartir datos con proveedores de servicios técnicos (hosting, email transaccional) que actúan como encargados del tratamiento bajo contrato.",
            "Podemos revelar información cuando sea requerido por ley o autoridad competente.",
            "En caso de fusión o adquisición de la plataforma, los usuarios serán notificados con antelación.",
        ],
        "type": "list",
    },
    {
        "icon": "shield-check",
        "color": "teal",
        "title": "7. Tus derechos",
        "content": [
            ("Acceso", "Puedes solicitar una copia de los datos personales que tenemos sobre ti."),
            ("Rectificación", "Puedes corregir datos inexactos o incompletos desde tu perfil o contactando con nosotros."),
            ("Supresión", "Puedes solicitar la eliminación de tus datos cuando ya no sean necesarios para los fines recogidos."),
            ("Oposición", "Puedes oponerte al tratamiento basado en interés legítimo."),
            ("Portabilidad", "Puedes solicitar tus datos en formato estructurado y legible por máquina."),
            ("Limitación", "Puedes solicitar la limitación del tratamiento en determinadas circunstancias."),
        ],
        "type": "table",
    },
    {
        "icon": "lock",
        "color": "gray",
        "title": "8. Seguridad de los datos",
        "content": [
            "Las contraseñas se almacenan exclusivamente en forma hasheada mediante bcrypt, nunca en texto plano.",
            "La comunicación entre el navegador y el servidor se realiza mediante protocolos seguros (HTTPS/WSS).",
            "El acceso a la base de datos está restringido y protegido por credenciales seguras.",
            "Realizamos revisiones periódicas de seguridad para detectar y corregir posibles vulnerabilidades.",
        ],
        "type": "list",
    },
    {
        "icon": "mail",
        "color": "blue",
        "title": "9. Contacto y reclamaciones",
        "content": [
            "Para ejercer tus derechos o resolver cualquier duda sobre privacidad, escríbenos a privacidad@elearningjcb.com.",
            "También puedes usar el formulario de contacto disponible en /contact.",
            "Si consideras que el tratamiento de tus datos no es conforme a la normativa, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (www.aepd.es).",
        ],
        "type": "list",
    },
]


def policy_section(icon: str, color: str, title: str, content, section_type: str) -> rx.Component:
    if section_type == "list":
        body = rx.vstack(
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
                for item in content
            ],
            spacing="2",
            width="100%",
        )
    else:
        body = rx.vstack(
            *[
                rx.hstack(
                    rx.text(label, size="2", weight="bold", min_width="160px", color=rx.color("gray", 12)),
                    rx.text(value, size="2", color=rx.color("gray", 11), line_height="1.7"),
                    spacing="3",
                    align_items="start",
                    width="100%",
                )
                for label, value in content
            ],
            spacing="3",
            width="100%",
        )

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
            body,
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def privacy_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.center(
                    rx.box(
                        rx.icon("shield", size=40, color="white"),
                        background=rx.color("blue", 9),
                        padding="1.1em",
                        border_radius="20px",
                        box_shadow=f"0 8px 32px {rx.color('blue', 6)}",
                    ),
                    margin_bottom="0.5em",
                ),
                rx.heading(
                    "Política de Privacidad",
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
                    "En E-Learning JCB nos comprometemos a proteger tu privacidad y a tratar tus datos personales con total transparencia, en cumplimiento del Reglamento General de Protección de Datos (RGPD) y la Ley Orgánica 3/2018 de Protección de Datos Personales (LOPDGDD).",
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
                    policy_section(
                        s["icon"], s["color"], s["title"], s["content"], s["type"]
                    )
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
