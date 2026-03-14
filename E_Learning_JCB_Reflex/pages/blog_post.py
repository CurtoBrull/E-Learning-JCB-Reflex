"""
Página de detalle de artículo del Blog de E-Learning JCB.

Ruta dinámica: /blog/[post_id]
Acceso: Pública
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer


# ---------------------------------------------------------------------------
# Contenido completo de los artículos
# ---------------------------------------------------------------------------

ALL_POSTS = {
    "1": {
        "title": "El futuro del aprendizaje online: IA, personalización y microlearning",
        "category": "Tendencias",
        "category_color": "purple",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "10 marzo 2026",
        "read_time": "8 min",
        "icon": "brain",
        "excerpt": "La educación online está viviendo una revolución silenciosa. La inteligencia artificial ya no es ciencia ficción en el aula virtual.",
        "sections": [
            {
                "heading": "La revolución que nadie vio venir",
                "paragraphs": [
                    "Hace apenas cinco años, el e-learning significaba básicamente vídeos grabados y PDFs descargables. Hoy, la inteligencia artificial está redefiniendo cada aspecto de la experiencia formativa online, desde cómo se diseñan los cursos hasta cómo los consume cada estudiante.",
                    "El cambio no ha sido abrupto, sino gradual, casi imperceptible. Y eso lo hace más poderoso: se ha integrado en las plataformas de forma tan natural que muchos estudiantes ya no distinguen dónde termina el diseño pedagógico humano y dónde empieza la adaptación algorítmica.",
                ],
            },
            {
                "heading": "Personalización: el fin del 'talla única'",
                "paragraphs": [
                    "Durante décadas, la educación —presencial u online— ha funcionado con un modelo de talla única. El mismo temario, el mismo ritmo, la misma evaluación para todos. La IA lo está cambiando radicalmente.",
                    "Los sistemas modernos de aprendizaje adaptativo analizan en tiempo real cómo interactúa cada estudiante con el contenido: qué secciones relee, dónde pausa el vídeo, qué preguntas falla repetidamente. Con esa información, ajustan el orden de los temas, la dificultad de los ejercicios y hasta el formato del contenido (texto, vídeo, ejercicio interactivo) para maximizar la retención.",
                    "El resultado es que dos estudiantes pueden completar el mismo curso por caminos completamente distintos, cada uno adaptado a sus fortalezas y debilidades concretas.",
                ],
            },
            {
                "heading": "Microlearning: aprender en píldoras",
                "paragraphs": [
                    "La atención humana es un recurso limitado. Los estudios de neurociencia cognitiva coinciden en que el cerebro asimila mejor la información en sesiones cortas e intensas que en maratones de estudio. De ahí el auge del microlearning: contenido diseñado para consumirse en menos de 10 minutos.",
                    "Esto no significa simplificar o superficializar el conocimiento. Significa estructurarlo de forma que cada píldora sea completa, aplicable y memorable por sí sola. Una lección de microlearning bien diseñada puede enseñar a configurar un entorno de desarrollo en Docker en 7 minutos con más efectividad que una clase magistral de una hora.",
                    "Combinado con la IA, el microlearning puede entregarse en el momento exacto en que el estudiante lo necesita —justo antes de un ejercicio práctico, por ejemplo— maximizando la transferencia de conocimiento.",
                ],
            },
            {
                "heading": "¿Qué significa esto para E-Learning JCB?",
                "paragraphs": [
                    "En E-Learning JCB estamos monitorizando estas tendencias de cerca. Nuestra hoja de ruta incluye funcionalidades de seguimiento de progreso más granular, recomendaciones de cursos basadas en el perfil del estudiante y lecciones diseñadas específicamente en formato microlearning.",
                    "La educación online del futuro no es solo más conveniente que la presencial. Con las herramientas adecuadas, puede ser más efectiva. Ese es el objetivo que nos guía.",
                ],
            },
        ],
        "tags": ["IA", "E-Learning", "Microlearning", "Personalización", "Tendencias 2026"],
    },
    "2": {
        "title": "Python en 2026: por qué sigue siendo el lenguaje más demandado",
        "category": "Programación",
        "category_color": "blue",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "5 marzo 2026",
        "read_time": "6 min",
        "icon": "code-2",
        "excerpt": "Desde IA hasta automatización web, Python domina los rankings de popularidad año tras año.",
        "sections": [
            {
                "heading": "Un lenguaje diseñado para humanos",
                "paragraphs": [
                    "Guido van Rossum diseñó Python con una filosofía clara: el código se lee muchas más veces de las que se escribe, por lo tanto debe ser legible. Esa decisión de diseño tomada en 1991 sigue siendo hoy la principal razón por la que millones de desarrolladores, científicos, analistas y estudiantes lo eligen como primer lenguaje.",
                    "La sintaxis limpia de Python reduce la carga cognitiva. No necesitas preocuparte por puntos y comas, llaves o declarar tipos (a menos que quieras hacerlo). Puedes centrarte en resolver el problema.",
                ],
            },
            {
                "heading": "El ecosistema que lo hace imparable",
                "paragraphs": [
                    "La popularidad de Python no se explica solo por su sintaxis. PyPI, su repositorio de paquetes, supera los 500.000 proyectos. Hay una librería para prácticamente cualquier tarea imaginable: requests para HTTP, pandas para análisis de datos, FastAPI para APIs REST, TensorFlow y PyTorch para machine learning, Selenium y Playwright para automatización de navegadores.",
                    "Este ecosistema crea un efecto de red poderoso: cuantos más desarrolladores usan Python, más librerías se crean; cuantas más librerías existen, más desarrolladores eligen Python. Es un ciclo que se retroalimenta desde hace más de una década.",
                ],
            },
            {
                "heading": "Python y la inteligencia artificial: una pareja inseparable",
                "paragraphs": [
                    "Si Python domina los rankings en 2026 es en gran parte gracias a la explosión de la IA. El 95% de los modelos de machine learning y deep learning se entrena, evalúa y despliega con herramientas Python. NumPy, pandas, scikit-learn, Hugging Face Transformers... toda la cadena de valor de la IA moderna habla Python.",
                    "Aprender Python hoy no es solo aprender a programar. Es adquirir el idioma que habla la industria tecnológica más dinámica del momento.",
                ],
            },
            {
                "heading": "¿Por dónde empezar?",
                "paragraphs": [
                    "Si estás empezando, lo más importante es no intentar aprenderlo todo a la vez. Python tiene muchas facetas: scripting, web, data science, automatización, IA. Elige una según tus objetivos y profundiza en ella antes de saltar a la siguiente.",
                    "En E-Learning JCB tenemos cursos que te guían desde los conceptos fundamentales hasta proyectos reales, con un enfoque práctico desde el primer día. Porque la mejor forma de aprender a programar es programando.",
                ],
            },
        ],
        "tags": ["Python", "Programación", "Desarrollo", "IA", "Backend"],
    },
    "3": {
        "title": "Cómo estudiar de forma efectiva: la técnica Pomodoro aplicada al e-learning",
        "category": "Productividad",
        "category_color": "green",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "28 febrero 2026",
        "read_time": "5 min",
        "icon": "timer",
        "excerpt": "No se trata de cuántas horas estudias, sino de cómo las aprovechas.",
        "sections": [
            {
                "heading": "El mito de las horas de estudio",
                "paragraphs": [
                    "Cuántas veces has escuchado 'hay que estudiar muchas horas' como si la cantidad fuera la variable que determina el aprendizaje. La realidad, respaldada por décadas de investigación en neurociencia cognitiva, es que la calidad del tiempo de estudio supera sistemáticamente a la cantidad.",
                    "Estudiar 2 horas con plena concentración produce más retención y comprensión que 6 horas con el móvil al lado, interrupciones frecuentes y la mente a medias en otro sitio.",
                ],
            },
            {
                "heading": "Qué es la técnica Pomodoro",
                "paragraphs": [
                    "Francesco Cirillo desarrolló esta técnica en los años 80 usando un temporizador de cocina con forma de tomate (pomodoro en italiano). El método es simple: trabaja con concentración total durante 25 minutos, descansa 5 minutos, y cada 4 ciclos toma un descanso largo de 15-30 minutos.",
                    "La clave no es el tiempo concreto, sino la estructura. El cerebro trabaja mejor cuando sabe que el esfuerzo tiene un límite temporal definido. Saber que 'solo son 25 minutos' reduce la procrastinación y facilita entrar en estado de flujo.",
                ],
            },
            {
                "heading": "Adaptando Pomodoro al e-learning",
                "paragraphs": [
                    "Los cursos online tienen una ventaja enorme sobre los libros de texto: están segmentados en lecciones. Esto hace que sean naturalmente compatibles con la técnica Pomodoro. Algunas recomendaciones prácticas:",
                    "Usa los 25 minutos para completar una o dos lecciones cortas, nunca empieces una lección nueva si te quedan menos de 5 minutos. Durante el descanso de 5 minutos, aléjate de la pantalla: estira, hidráta, mira por la ventana. Después de 4 pomodoros, revisa los conceptos clave de lo que has aprendido antes del descanso largo.",
                    "El descanso largo (15-30 min) es ideal para un repaso espaciado: intenta explicarte a ti mismo lo que has aprendido sin mirar las notas. Si no puedes, sabes qué necesitas repasar.",
                ],
            },
            {
                "heading": "Herramientas recomendadas",
                "paragraphs": [
                    "Hay decenas de aplicaciones Pomodoro, pero las mejores son las más simples. Pomofocus.io es gratuita, funciona en el navegador y permite personalizar los intervalos. Alternativamente, cualquier temporizador físico funciona: el alejamiento del mundo digital durante el estudio es parte del beneficio.",
                    "Lo más importante es la constancia. Dos semanas practicando Pomodoro cambiarán tu relación con el estudio de forma permanente.",
                ],
            },
        ],
        "tags": ["Productividad", "Estudio", "Pomodoro", "Aprendizaje", "Concentración"],
    },
    "4": {
        "title": "MongoDB vs PostgreSQL: ¿cuándo usar cada uno en tus proyectos?",
        "category": "Bases de Datos",
        "category_color": "orange",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "21 febrero 2026",
        "read_time": "7 min",
        "icon": "database",
        "excerpt": "NoSQL o relacional. La respuesta no siempre es obvia.",
        "sections": [
            {
                "heading": "El falso debate",
                "paragraphs": [
                    "Durante años, la comunidad de desarrollo ha debatido MongoDB vs PostgreSQL como si fuera una cuestión de superioridad. La realidad es más pragmática: son herramientas diseñadas para resolver problemas distintos, y la mejor elección depende completamente del contexto de tu proyecto.",
                    "Dicho esto, hay patrones claros que ayudan a tomar la decisión. Vamos a analizarlos.",
                ],
            },
            {
                "heading": "Cuándo elegir PostgreSQL",
                "paragraphs": [
                    "PostgreSQL brilla cuando tus datos tienen estructura predecible y estable, las relaciones entre entidades son complejas y frecuentes (joins), necesitas transacciones ACID estrictas (banca, inventario, reservas), el esquema cambia poco y prefieres validación a nivel de base de datos, o trabajas con datos geoespaciales (PostGIS).",
                    "Un sistema de facturación, una plataforma de reservas de vuelos o un ERP son candidatos naturales para PostgreSQL. La integridad referencial y las transacciones son imprescindibles en esos contextos.",
                ],
            },
            {
                "heading": "Cuándo elegir MongoDB",
                "paragraphs": [
                    "MongoDB es la elección natural cuando el esquema de datos varía entre documentos o evoluciona rápidamente, los datos se leen y escriben como unidades completas (sin necesitar joins frecuentes), necesitas escalar horizontalmente con facilidad, trabajas con datos semi-estructurados (logs, eventos, catálogos de productos con atributos variables), o el equipo prioriza velocidad de desarrollo sobre rigidez del esquema.",
                    "E-Learning JCB usa MongoDB precisamente por esto: los cursos tienen estructuras que varían (algunos tienen vídeos, otros PDFs, otros ejercicios interactivos), los datos de usuarios evolucionan con el producto, y la flexibilidad del esquema nos permite iterar rápido.",
                ],
            },
            {
                "heading": "La respuesta honesta",
                "paragraphs": [
                    "Para la mayoría de aplicaciones web modernas de tamaño medio, ambas bases de datos funcionarán bien. La diferencia real estará en la comodidad del equipo con cada tecnología y en los patrones de acceso a datos de tu aplicación específica.",
                    "Si empiezas un proyecto nuevo y no tienes una razón clara para elegir una sobre otra, PostgreSQL es la opción más conservadora y MongoDB la más flexible. Ambas tienen excelente documentación, comunidad activa y soporte en la nube.",
                ],
            },
        ],
        "tags": ["MongoDB", "PostgreSQL", "Bases de Datos", "NoSQL", "SQL", "Backend"],
    },
    "5": {
        "title": "De cero a desarrollador web: la hoja de ruta en 2026",
        "category": "Guías",
        "category_color": "teal",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "14 febrero 2026",
        "read_time": "10 min",
        "icon": "map",
        "excerpt": "HTML, CSS, JavaScript, frameworks, backend, bases de datos, despliegue… La ruta ordenada y práctica.",
        "sections": [
            {
                "heading": "El problema de la parálisis por análisis",
                "paragraphs": [
                    "Teclea 'cómo aprender desarrollo web' en cualquier buscador y te enfrentarás a centenares de opiniones contradictorias. 'Aprende React primero', 'No, aprende JavaScript puro', 'El backend es más importante', 'Sin HTML sólido no puedes avanzar'...",
                    "La avalancha de opciones paraliza a muchos aspirantes a desarrolladores antes de escribir su primera línea de código. Esta guía te propone una ruta concreta, ordenada y respaldada por la experiencia práctica.",
                ],
            },
            {
                "heading": "Fase 1 — Los fundamentos (1-2 meses)",
                "paragraphs": [
                    "Todo empieza con HTML y CSS. No como paso obligatorio a superar rápido, sino como fundamento real. Aprende HTML semántico (no solo divs), CSS con flexbox y grid, diseño responsive y accesibilidad básica. Construye 3-5 páginas estáticas reales antes de continuar.",
                    "Después, JavaScript. Variables, funciones, arrays, objetos, el DOM, eventos, fetch y promesas. No necesitas dominar el lenguaje completamente, pero sí entender sus conceptos fundamentales antes de tocar cualquier framework.",
                ],
            },
            {
                "heading": "Fase 2 — Frontend moderno (2-3 meses)",
                "paragraphs": [
                    "Con JavaScript sólido, elige un framework frontend. En 2026 las opciones principales son React, Vue y Svelte. React tiene el ecosistema más grande y más oportunidades laborales; Vue tiene la curva de aprendizaje más suave; Svelte compila a JavaScript nativo y es elegante. Elige una y profundiza, no intentes aprender las tres a la vez.",
                    "Construye al menos dos proyectos reales: una SPA que consuma una API pública y un proyecto personal que resuelva un problema real tuyo. Los proyectos en tu portfolio valen más que cualquier certificado.",
                ],
            },
            {
                "heading": "Fase 3 — Backend (2-3 meses)",
                "paragraphs": [
                    "Con el frontend controlado, el backend se aprende mucho más rápido porque ya entiendes cómo se consume. Las opciones más demandadas son Node.js con Express o Fastify, Python con FastAPI o Django, o Go para alto rendimiento.",
                    "Aprende a construir una API REST, gestionar autenticación con JWT, conectarte a una base de datos y desplegar tu aplicación. Aquí es donde muchos proyectos de portfolio pasan de 'demo' a 'aplicación real'.",
                ],
            },
            {
                "heading": "Fase 4 — Despliegue y DevOps básico (1 mes)",
                "paragraphs": [
                    "Saber construir una aplicación y saber desplegarla son habilidades distintas. Aprende Git y GitHub en profundidad (no solo add, commit, push), Docker para containerizar tus aplicaciones y alguna plataforma de despliegue como Railway, Render o Vercel.",
                    "Un proyecto funcionando en una URL real tiene un peso en las entrevistas que ningún repositorio local puede igualar.",
                ],
            },
        ],
        "tags": ["Desarrollo Web", "Frontend", "Backend", "Hoja de Ruta", "Carrera", "Principiantes"],
    },
    "6": {
        "title": "Reflex: construye aplicaciones web full-stack solo con Python",
        "category": "Tecnología",
        "category_color": "violet",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "7 febrero 2026",
        "read_time": "9 min",
        "icon": "layers",
        "excerpt": "¿Y si pudieras crear un frontend reactivo sin tocar JavaScript? Reflex lo hace posible.",
        "sections": [
            {
                "heading": "El problema que Reflex resuelve",
                "paragraphs": [
                    "Los desarrolladores Python que quieren construir aplicaciones web completas se han enfrentado siempre a la misma barrera: el frontend requiere JavaScript. Django o FastAPI gestionan el backend con elegancia, pero en cuanto necesitas interactividad real en el cliente, tienes que cambiar de contexto mental, de lenguaje y de ecosistema.",
                    "Reflex elimina esa fricción. Es un framework Python que te permite construir la interfaz de usuario con componentes Python, gestionar el estado de la aplicación en el servidor y comunicarse con el cliente mediante WebSockets, todo sin escribir una sola línea de JavaScript.",
                ],
            },
            {
                "heading": "Cómo funciona por dentro",
                "paragraphs": [
                    "Reflex compila tus componentes Python a React en tiempo de construcción. El estado de la aplicación vive en el servidor (en Python) y se sincroniza con el cliente a través de una conexión WebSocket persistente. Cuando el usuario interactúa con la interfaz, el evento viaja al servidor, Python actualiza el estado, y solo los cambios necesarios se envían de vuelta al cliente.",
                    "Este modelo tiene ventajas importantes: la lógica de negocio nunca sale del servidor, puedes usar cualquier librería Python directamente en tus event handlers (motor de base de datos, ML, procesamiento de archivos), y el estado es siempre la fuente de verdad.",
                ],
            },
            {
                "heading": "E-Learning JCB está construida con Reflex",
                "paragraphs": [
                    "Esta misma plataforma que estás usando es un ejemplo real de lo que Reflex puede hacer. El dashboard de estudiante, el panel de administración, el buscador de cursos, el sistema de autenticación... todo está escrito en Python puro.",
                    "La experiencia de desarrollo ha sido fluida: una sola base de código, un solo lenguaje, y acceso directo a MongoDB con Motor desde los event handlers del estado. No hay separación artificial entre frontend y backend porque en Reflex no existe esa separación.",
                ],
            },
            {
                "heading": "¿Cuándo tiene sentido usar Reflex?",
                "paragraphs": [
                    "Reflex es ideal para equipos o developers individuales con fuerte background Python que necesitan interfaces de usuario reactivas sin querer invertir tiempo en aprender el ecosistema JavaScript. También es excelente para prototipos rápidos, herramientas internas y aplicaciones de data science que necesitan un frontend.",
                    "No es la elección óptima si necesitas SEO agresivo (el renderizado SSR aún está madurando), si tu equipo es principalmente frontend con dominio de React/Vue, o si necesitas una aplicación mobile nativa.",
                ],
            },
        ],
        "tags": ["Reflex", "Python", "Full-Stack", "Framework", "WebSockets", "React"],
    },
    "7": {
        "title": "Soft skills para developers: las habilidades que nadie te enseña en los cursos",
        "category": "Carrera",
        "category_color": "pink",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "31 enero 2026",
        "read_time": "6 min",
        "icon": "heart-handshake",
        "excerpt": "Comunicación, empatía, gestión del tiempo... El mercado laboral busca desarrolladores completos.",
        "sections": [
            {
                "heading": "El desarrollador completo no es el que más sabe de código",
                "paragraphs": [
                    "Las ofertas de trabajo para desarrolladores listan decenas de tecnologías: React, Node, Docker, AWS, CI/CD... Pero pregunta a cualquier CTO qué diferencia a un developer bueno de uno excelente y raramente mencionarán una tecnología concreta. Hablarán de comunicación, de fiabilidad, de capacidad para resolver problemas ambiguos, de trabajo en equipo.",
                    "Las soft skills no son un complemento opcional. Son el multiplicador que determina si tus hard skills tienen impacto real en un equipo y en un producto.",
                ],
            },
            {
                "heading": "Comunicación técnica: explicar lo complejo de forma simple",
                "paragraphs": [
                    "La capacidad de explicar un problema técnico a alguien no técnico —un cliente, un product manager, un directivo— es extraordinariamente valiosa y escasísima. Requiere entender el problema profundamente (no puedes simplificar lo que no comprendes bien) y ponerse en el lugar del interlocutor.",
                    "Practica esto activamente: explica lo que estás trabajando a alguien fuera del mundo tech. Si no puedes hacerlo, es señal de que tu propio entendimiento necesita refuerzo.",
                ],
            },
            {
                "heading": "Gestión de la incertidumbre",
                "paragraphs": [
                    "El desarrollo de software real está lleno de requisitos ambiguos, cambios de última hora y problemas sin solución obvia. Los developers más valiosos son los que pueden navegar esa incertidumbre sin bloquearse: saben cuándo pedir clarificación, cuándo tomar una decisión y documentarla, y cuándo hacer una pregunta al equipo.",
                    "La alternativa —quedarse paralizado esperando instrucciones perfectas o avanzar en silencio en la dirección equivocada— es mucho más costosa para el equipo.",
                ],
            },
            {
                "heading": "Cómo desarrollar estas habilidades",
                "paragraphs": [
                    "Las soft skills se desarrollan como cualquier otra habilidad: con práctica deliberada y feedback. Algunos ejercicios concretos: escribe en tu blog o en Notion lo que aprendes cada semana (comunicación escrita), participa en code reviews y aprende a dar feedback constructivo (empatía y comunicación), contribuye a proyectos open source (trabajo en equipo distribuido) y presenta tus proyectos en meetups locales aunque sean pequeños (comunicación oral).",
                    "No esperes a tener un trabajo para empezar a desarrollarlas. El mejor momento es durante el aprendizaje.",
                ],
            },
        ],
        "tags": ["Carrera", "Soft Skills", "Comunicación", "Trabajo en Equipo", "Desarrollo Profesional"],
    },
    "8": {
        "title": "Docker para principiantes: contenedores sin miedo",
        "category": "DevOps",
        "category_color": "cyan",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "24 enero 2026",
        "read_time": "8 min",
        "icon": "box",
        "excerpt": "Docker puede parecer intimidante al principio, pero cambia por completo la forma en que desarrollas.",
        "sections": [
            {
                "heading": "¿Por qué Docker importa?",
                "paragraphs": [
                    "'En mi máquina funciona' es uno de los problemas más frustrantes del desarrollo de software. Tu aplicación funciona perfectamente en tu entorno local con Python 3.11, MongoDB 7 y unas dependencias específicas. Luego llegas al servidor de producción con Python 3.9, otra versión de la base de datos y librerías del sistema distintas, y todo se rompe.",
                    "Docker resuelve esto creando contenedores: entornos aislados y reproducibles que incluyen todo lo que tu aplicación necesita para funcionar, independientemente del sistema operativo host. Si funciona en el contenedor en tu máquina, funcionará en cualquier máquina que tenga Docker.",
                ],
            },
            {
                "heading": "Los conceptos clave",
                "paragraphs": [
                    "Imagen: una plantilla inmutable que define el entorno. Contiene el sistema operativo base, las dependencias y tu aplicación. Se define en un Dockerfile.",
                    "Contenedor: una instancia en ejecución de una imagen. Puedes arrancar múltiples contenedores a partir de la misma imagen, cada uno aislado de los demás.",
                    "Dockerfile: el archivo de texto donde describes cómo construir tu imagen paso a paso. FROM (imagen base), RUN (ejecutar comandos), COPY (copiar archivos), CMD (comando de inicio).",
                    "Docker Compose: herramienta para definir y arrancar aplicaciones multi-contenedor (app + base de datos + cache, por ejemplo) con un solo archivo YAML.",
                ],
            },
            {
                "heading": "Tu primer contenedor en 5 minutos",
                "paragraphs": [
                    "Crear un Dockerfile para una aplicación Python básica es sorprendentemente simple. FROM python:3.12-slim, WORKDIR /app, COPY requirements.txt ., RUN pip install -r requirements.txt, COPY . ., CMD [\"python\", \"main.py\"]. Con docker build -t mi-app . construyes la imagen y con docker run mi-app la ejecutas.",
                    "Desde ahí puedes añadir Docker Compose para orquestar tu base de datos junto con tu aplicación, configurar volúmenes para persistir datos y definir variables de entorno de forma segura.",
                ],
            },
            {
                "heading": "Cuándo no usar Docker",
                "paragraphs": [
                    "Docker añade una capa de complejidad. Para scripts simples, proyectos personales pequeños o cuando aprendes un lenguaje nuevo, la fricción inicial puede no merecer la pena. Empieza a usarlo cuando trabajas en equipo, cuando necesitas reproducibilidad entre entornos, o cuando vas a desplegar en producción.",
                    "Una vez que lo incorporas a tu flujo de trabajo, te costará imaginar cómo trabajabas sin él.",
                ],
            },
        ],
        "tags": ["Docker", "DevOps", "Contenedores", "Despliegue", "Backend"],
    },
    "9": {
        "title": "Seguridad web básica: las vulnerabilidades OWASP que todo dev debe conocer",
        "category": "Seguridad",
        "category_color": "red",
        "author": "Javier Curto Brull",
        "author_role": "Fundador & Desarrollador",
        "date": "17 enero 2026",
        "read_time": "7 min",
        "icon": "shield-alert",
        "excerpt": "SQL injection, XSS, CSRF… Los ataques más comunes no son los más sofisticados.",
        "sections": [
            {
                "heading": "La seguridad no es opcional",
                "paragraphs": [
                    "El 43% de los ciberataques van dirigidos a pequeñas empresas y proyectos individuales, precisamente porque suelen tener menos medidas de protección. La buena noticia es que la gran mayoría de los ataques exitosos explotan vulnerabilidades conocidas y bien documentadas que son relativamente sencillas de prevenir.",
                    "OWASP (Open Web Application Security Project) publica periódicamente el Top 10 de vulnerabilidades web más críticas. Conocerlas y saber cómo prevenirlas es conocimiento básico para cualquier desarrollador que ponga código en producción.",
                ],
            },
            {
                "heading": "SQL Injection: el clásico que sigue haciendo daño",
                "paragraphs": [
                    "Ocurre cuando datos de usuario se insertan directamente en consultas SQL sin sanitizar. Un atacante puede manipular la consulta para extraer toda la base de datos, modificar o eliminar datos, o saltarse la autenticación.",
                    "La prevención es simple y no tiene excusas en 2026: usa siempre consultas parametrizadas o prepared statements. Nunca construyas queries concatenando strings con datos de usuario. Los ORMs modernos protegen contra esto por defecto, pero si escribes SQL manual, es tu responsabilidad.",
                ],
            },
            {
                "heading": "XSS: cuando tu web ataca a tus usuarios",
                "paragraphs": [
                    "Cross-Site Scripting ocurre cuando tu aplicación muestra contenido generado por el usuario sin escaparlo correctamente. Un atacante puede inyectar scripts que se ejecutan en el navegador de otros usuarios, robando cookies de sesión, redirigiendo a páginas de phishing o modificando el contenido de la página.",
                    "La prevención: escapa siempre el HTML antes de renderizar datos de usuario. Los frameworks modernos (React, Vue, Reflex) hacen esto automáticamente. El peligro aparece cuando usas dangerouslySetInnerHTML, innerHTML directamente, o generación de HTML manual sin escapado.",
                ],
            },
            {
                "heading": "Autenticación y gestión de contraseñas",
                "paragraphs": [
                    "Nunca almacenes contraseñas en texto plano ni con algoritmos de hash rápidos como MD5 o SHA-1. Usa bcrypt, Argon2 o scrypt, que son lentos por diseño y hacen los ataques de fuerza bruta computacionalmente costosos.",
                    "E-Learning JCB usa bcrypt para todas las contraseñas. Implementa también rate limiting en los endpoints de login para prevenir ataques de fuerza bruta, y considera añadir autenticación de dos factores para cuentas con privilegios.",
                ],
            },
            {
                "heading": "El principio más importante: defensa en profundidad",
                "paragraphs": [
                    "No existe la seguridad perfecta, pero sí existe la seguridad por capas. Valida y sanitiza en el cliente Y en el servidor. Aplica el principio de mínimo privilegio. Mantén dependencias actualizadas. Usa HTTPS siempre. Revisa los permisos de tu base de datos.",
                    "La seguridad no es una feature que añades al final. Es una actitud que aplicas desde el primer commit.",
                ],
            },
        ],
        "tags": ["Seguridad", "OWASP", "SQL Injection", "XSS", "Autenticación", "Web"],
    },
}


# ---------------------------------------------------------------------------
# Estado
# ---------------------------------------------------------------------------

class BlogPostState(rx.State):

    @rx.var
    def post_id(self) -> str:
        return self.router.page.params.get("post_id", "")

    @rx.var
    def found(self) -> bool:
        return self.post_id in ALL_POSTS

    @rx.var
    def post(self) -> dict:
        return ALL_POSTS.get(self.post_id, {})

    @rx.var
    def title(self) -> str:
        return ALL_POSTS.get(self.post_id, {}).get("title", "")

    @rx.var
    def category(self) -> str:
        return ALL_POSTS.get(self.post_id, {}).get("category", "")

    @rx.var
    def category_color(self) -> str:
        return ALL_POSTS.get(self.post_id, {}).get("category_color", "gray")

    @rx.var
    def author(self) -> str:
        return ALL_POSTS.get(self.post_id, {}).get("author", "")

    @rx.var
    def author_role(self) -> str:
        return ALL_POSTS.get(self.post_id, {}).get("author_role", "")

    @rx.var
    def date(self) -> str:
        return ALL_POSTS.get(self.post_id, {}).get("date", "")

    @rx.var
    def read_time(self) -> str:
        return ALL_POSTS.get(self.post_id, {}).get("read_time", "")

    @rx.var
    def sections(self) -> list[dict]:
        return ALL_POSTS.get(self.post_id, {}).get("sections", [])

    @rx.var
    def tags(self) -> list[str]:
        return ALL_POSTS.get(self.post_id, {}).get("tags", [])


# ---------------------------------------------------------------------------
# Componentes
# ---------------------------------------------------------------------------

def tag_badge(tag: str) -> rx.Component:
    return rx.badge(tag, color_scheme="purple", variant="soft", size="1")


def post_section(section: dict) -> rx.Component:
    return rx.vstack(
        rx.heading(section["heading"], size="5", margin_top="0.5em"),
        *[
            rx.text(p, size="3", color=rx.color("gray", 11), line_height="1.9")
            for p in section["paragraphs"]
        ],
        spacing="3",
        align_items="start",
        width="100%",
    )


def blog_post_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.cond(
                BlogPostState.found,
                # Artículo encontrado
                rx.vstack(
                    # Breadcrumb
                    rx.hstack(
                        rx.link(
                            rx.hstack(rx.icon("arrow-left", size=14), rx.text("Blog", size="2"), spacing="1"),
                            href="/blog",
                            color=rx.color("gray", 10),
                            _hover={"color": rx.color("purple", 9)},
                        ),
                        rx.text("/", size="2", color=rx.color("gray", 7)),
                        rx.text(BlogPostState.category, size="2", color=rx.color("gray", 10)),
                        spacing="2",
                        align_items="center",
                        margin_bottom="1em",
                    ),
                    # Cabecera del artículo
                    rx.vstack(
                        rx.badge(
                            BlogPostState.category,
                            color_scheme=BlogPostState.category_color,
                            size="2",
                            variant="soft",
                        ),
                        rx.heading(
                            BlogPostState.title,
                            size="8",
                            line_height="1.3",
                        ),
                        rx.hstack(
                            rx.box(
                                rx.icon("user", size=14, color="white"),
                                background=rx.color("purple", 9),
                                padding="0.3em",
                                border_radius="50%",
                                width="30px",
                                height="30px",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                flex_shrink="0",
                            ),
                            rx.vstack(
                                rx.text(BlogPostState.author, size="2", weight="medium"),
                                rx.text(BlogPostState.author_role, size="1", color=rx.color("gray", 10)),
                                spacing="0",
                                align_items="start",
                            ),
                            rx.box(width="1px", height="24px", background=rx.color("gray", 5)),
                            rx.hstack(
                                rx.icon("calendar", size=13, color=rx.color("gray", 9)),
                                rx.text(BlogPostState.date, size="2", color=rx.color("gray", 10)),
                                spacing="1",
                                align_items="center",
                            ),
                            rx.hstack(
                                rx.icon("clock", size=13, color=rx.color("gray", 9)),
                                rx.text(BlogPostState.read_time, size="2", color=rx.color("gray", 10)),
                                spacing="1",
                                align_items="center",
                            ),
                            spacing="3",
                            align_items="center",
                            flex_wrap="wrap",
                        ),
                        spacing="4",
                        align_items="start",
                        width="100%",
                    ),
                    rx.divider(),
                    # Cuerpo del artículo
                    rx.vstack(
                        rx.foreach(
                            BlogPostState.sections,
                            post_section,
                        ),
                        spacing="4",
                        align_items="start",
                        width="100%",
                    ),
                    rx.divider(),
                    # Tags
                    rx.vstack(
                        rx.text("Etiquetas", size="2", weight="bold", color=rx.color("gray", 10)),
                        rx.flex(
                            rx.foreach(BlogPostState.tags, tag_badge),
                            wrap="wrap",
                            gap="2",
                        ),
                        spacing="2",
                        align_items="start",
                        width="100%",
                    ),
                    # Volver al blog
                    rx.center(
                        rx.link(
                            rx.button(
                                rx.hstack(rx.icon("arrow-left", size=16), rx.text("Volver al Blog"), spacing="2"),
                                variant="soft",
                                color_scheme="purple",
                                size="3",
                            ),
                            href="/blog",
                        ),
                        margin_top="1em",
                        width="100%",
                    ),
                    spacing="6",
                    align_items="start",
                    width="100%",
                    padding_y="2em",
                ),
                # Artículo no encontrado
                rx.center(
                    rx.vstack(
                        rx.icon("file-x", size=64, color=rx.color("gray", 7)),
                        rx.heading("Artículo no encontrado", size="6"),
                        rx.text("El artículo que buscas no existe o ha sido eliminado.", color=rx.color("gray", 10)),
                        rx.link(
                            rx.button("Volver al Blog", color_scheme="purple"),
                            href="/blog",
                        ),
                        align_items="center",
                        spacing="4",
                        padding_y="6em",
                    ),
                    width="100%",
                ),
            ),
            max_width="780px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
            padding_bottom="4em",
        ),
        footer(),
        width="100%",
    )
