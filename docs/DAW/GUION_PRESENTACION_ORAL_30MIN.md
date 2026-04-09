# E-Learning JCB — Guion de Presentación Oral (30 minutos)
> Texto completo para leer/adaptar · ~130 palabras/minuto · ~3.900 palabras totales

---

## ESTRUCTURA RÁPIDA

| Bloque | Tema | Tiempo |
|--------|------|--------|
| 1 | Introducción y contexto | 3 min |
| 2 | Arquitectura general del sistema | 4 min |
| 3 | La base de datos: MongoDB y modelos | 4 min |
| 4 | Autenticación y sistema de roles | 5 min |
| 5 | Los estados de Reflex: el backend | 5 min |
| 6 | Páginas y componentes: el frontend | 4 min |
| 7 | Demo de funcionalidades destacadas | 3 min |
| 8 | Conclusiones y próximos pasos | 2 min |

---

---

# BLOQUE 1 — INTRODUCCIÓN Y CONTEXTO
**⏱ 3 minutos · ~390 palabras**

---

Buenos días a todos.

Voy a presentaros **E-Learning JCB**, una plataforma de formación online que he desarrollado íntegramente en Python. Y cuando digo íntegramente en Python, lo digo en serio: no hay ni una sola línea de JavaScript escrita manualmente en este proyecto. Todo el código, tanto el servidor como la interfaz de usuario, está en Python.

Sé que eso suena extraño. Normalmente cuando construimos una aplicación web, el frontend es JavaScript o TypeScript —React, Vue, Angular— y el backend es Python, Java, Node... Son dos mundos separados, con dos lenguajes, dos entornos de desarrollo, dos formas de pensar.

**E-Learning JCB rompe esa dicotomía.** Y lo hace gracias a **Reflex**, un framework open-source que compila código Python en una aplicación React + FastAPI de forma automática. Tú escribes Python puro, Reflex genera el frontend en React y el backend en FastAPI por debajo. Tú no ves ese código generado: solo ves Python.

¿Por qué este proyecto? Tres razones principales.

La primera: quería demostrar que Python es suficiente para construir una aplicación web profesional y completa. No un prototipo, no un tutorial de diez páginas: una plataforma real con autenticación, múltiples roles de usuario, operaciones CRUD, búsqueda en tiempo real y dashboards diferenciados.

La segunda: quería trabajar con MongoDB en un contexto real. No con datos de ejemplo, sino con una base de datos de producción en MongoDB Atlas, con documentos complejos y relaciones reales entre colecciones.

La tercera: el resultado final tiene que ser algo útil. Una plataforma de e-learning, similar en concepto a Udemy o Platzi, donde estudiantes se inscriben en cursos, instructores crean y gestionan contenido, y administradores controlan todo el sistema.

Antes de entrar en detalle, os dejo algunas cifras para tener la escala del proyecto en mente:

- **39 archivos Python** en total
- **30 páginas web** accesibles desde el navegador
- **33 rutas registradas** en la aplicación
- **10 clases de estado** que gestionan toda la lógica
- **4 servicios** que se comunican con la base de datos
- **~18.000 líneas de código** Python

Empecemos por cómo está organizado todo esto.

---

---

# BLOQUE 2 — ARQUITECTURA GENERAL DEL SISTEMA
**⏱ 4 minutos · ~520 palabras**

---

Cuando diseñé la arquitectura de E-Learning JCB, seguí un patrón en capas inspirado en MVC —Modelo, Vista, Controlador—, pero adaptado al paradigma reactivo de Reflex.

Hay **cinco capas bien diferenciadas**, y cada una tiene una responsabilidad clara.

La capa más alta es el **navegador**. El usuario abre Chrome, Safari, lo que sea. Lo que ve es React —pero ese React lo ha generado Reflex automáticamente a partir de mi código Python. No lo he escrito yo.

La segunda capa son las **páginas y componentes**: treinta archivos Python en la carpeta `/pages/` que definen qué ve el usuario en cada URL. Y cinco componentes reutilizables en `/components/` —la barra de navegación, el footer, las tarjetas de cursos— que se usan en varias páginas.

La tercera capa son los **estados**. Esta es la capa clave en Reflex. Los estados son clases Python que almacenan los datos y definen las acciones del usuario. Hay diez estados en el proyecto. Cuando el usuario hace clic en un botón, se ejecuta un método del estado. Cuando el estado cambia, la UI se actualiza automáticamente. Todo via WebSocket.

La cuarta capa son los **servicios**. Cuatro módulos Python que encapsulan todas las operaciones con MongoDB. Los estados llaman a los servicios; los servicios hablan con la base de datos. Los servicios no saben nada de la UI. Eso permite testear la lógica sin necesitar el frontend.

Y la quinta capa es **MongoDB Atlas**: la base de datos en la nube con cuatro colecciones —usuarios, cursos, contactos y categorías.

El **archivo de entrada** del proyecto es `E_Learning_JCB_Reflex.py`. Su función es muy simple: registrar todas las rutas de la aplicación.

```python
app = rx.App()
app.add_page(index_page, route="/")
app.add_page(courses_page, route="/courses")
app.add_page(course_detail_page, route="/courses/[course_id]")
app.add_page(admin_dashboard_page, route="/admin/dashboard")
# ... 33 rutas en total
```

Hay dos tipos de rutas. Las **rutas públicas** son accesibles sin autenticación: la portada, el catálogo de cursos, el blog, los instructores. Las **rutas protegidas** requieren login y, además, verifican el rol del usuario: el panel de administrador solo es accesible para admins, el dashboard de instructor solo para instructores.

Un detalle técnico interesante: las rutas con corchetes como `/courses/[course_id]` son **rutas dinámicas**. Reflex extrae automáticamente el parámetro de la URL y lo inyecta en el estado. Cuando visito `/courses/abc123`, Reflex pone `course_id = "abc123"` en el estado y la página carga el curso correcto de MongoDB.

En cuanto al stack tecnológico:
- **Python 3.14** como único lenguaje
- **Reflex 0.8.24** como framework full-stack
- **MongoDB Atlas** como base de datos en la nube
- **Motor 3.7** como driver asíncrono para MongoDB —las operaciones no bloquean el servidor
- **bcrypt** para el hash seguro de contraseñas
- **Granian** como servidor HTTP asíncrono, más rápido que uvicorn
- **Redis** para sincronizar el estado entre sesiones y pestañas

---

---

# BLOQUE 3 — LA BASE DE DATOS: MONGODB Y LOS MODELOS
**⏱ 4 minutos · ~520 palabras**

---

¿Por qué MongoDB y no una base de datos relacional como PostgreSQL?

La respuesta está en la naturaleza del contenido. Un curso de programación tiene lecciones con código. Un curso de diseño tiene lecciones con imágenes. Un curso de música tiene lecciones con audio. Con SQL, cada variación requeriría nuevas tablas y JOINs costosos. Con MongoDB, un curso es simplemente un **documento JSON flexible**: tiene exactamente los campos que necesita, nada más.

El proyecto usa **cuatro colecciones**.

La colección `users` almacena estudiantes, instructores y administradores en una misma colección. El campo `role` distingue entre ellos. Los instructores tienen además un subdocumento `instructorProfile` con su bio y especialidad.

La colección `courses` es la más compleja. Cada curso lleva embebidos sus propias lecciones y reseñas, porque siempre se consultan junto al curso. Pero las referencias a estudiantes e instructores son solo ObjectIDs, porque esos datos se consultan también de forma independiente.

Este es el **patrón de diseño más importante** de la base de datos: **embedding vs referencing**. Si los datos siempre se leen juntos, los embedo dentro del documento. Si los datos se leen también por separado, guardo solo el ID y hago una consulta adicional cuando los necesito.

La colección `contacts` almacena los mensajes del formulario de contacto. Y `categories` almacena las categorías de cursos que el administrador puede gestionar.

Los **modelos Python** en la carpeta `/models/` son clases que mapean esos documentos a objetos Python. El más relevante es el método `from_dict()`, que convierte un documento de MongoDB en un objeto Python:

```python
@classmethod
def from_dict(cls, data: dict) -> "Course":
    course = cls()
    course.id = str(data.get("_id", ""))
    course.title = data.get("title", "")
    course.students = [str(s) for s in data.get("students", [])]
    return course
```

¿Por qué ese `str()` en todos los IDs? MongoDB almacena los identificadores como tipo `ObjectId`, no como string. Si no los convierto, cuando comparo en Python `"abc123" == ObjectId("abc123")` el resultado es `False`. Ese es el tipo de bug difícil de detectar que aparece en producción un viernes por la tarde. El `from_dict()` convierte todo a string al cargar los datos, eliminando el problema de raíz.

Los **servicios** en `/services/` encapsulan todas las operaciones con la base de datos. Son funciones `async` que el estado llama cuando necesita datos:

```python
async def get_popular_courses(limit: int = 6) -> list[Course]:
    db = MongoDB.get_db()
    cursor = db["courses"].find({}).sort("studentsEnrolled", -1).limit(limit)
    docs = await cursor.to_list(length=limit)
    return [Course.from_dict(doc) for doc in docs]
```

La palabra clave `async` y el `await` son esenciales aquí. Motor —el driver de MongoDB— es completamente asíncrono. Esto significa que mientras esperamos que MongoDB responda, el servidor puede atender otras peticiones. No hay bloqueos.

---

---

# BLOQUE 4 — AUTENTICACIÓN Y SISTEMA DE ROLES
**⏱ 5 minutos · ~650 palabras**

---

La autenticación es uno de los sistemas más críticos de cualquier plataforma. Si falla, cualquiera puede acceder a cualquier cosa. En E-Learning JCB hay tres tipos de usuario con capacidades muy distintas.

El **estudiante** puede ver el catálogo, inscribirse en cursos, acceder al contenido de los cursos en los que está inscrito y dejar valoraciones.

El **instructor** puede crear y editar sus propios cursos, ver cuántos alumnos tiene inscritos en cada uno, y acceder a sus estadísticas de rendimiento.

El **administrador** tiene acceso total: gestión de todos los usuarios, todos los cursos, todas las categorías, y la configuración del sistema.

El corazón de todo esto es `AuthState`, el estado base del que heredan todos los demás estados de la aplicación:

```python
class AuthState(rx.State):
    is_authenticated: bool = False
    current_user: dict = {}

    @rx.var
    def user_role(self) -> str:
        return self.current_user.get("role", "")

    @rx.var
    def is_user_admin(self) -> bool:
        return self.user_role == "admin"
```

El `@rx.var` es un decorador especial de Reflex. Marca una propiedad como **computada**: se recalcula automáticamente cada vez que `current_user` cambia. No hay que llamarla manualmente. El frontend siempre tiene el valor correcto.

El **flujo de login** tiene cinco pasos bien definidos.

Primero, se busca el usuario en MongoDB por email. Si no existe, error de credenciales —sin especificar cuál es incorrecto, por seguridad.

Segundo, se verifica la contraseña usando bcrypt. Más sobre esto en un momento.

Tercero, si todo es correcto, se guarda el usuario en el estado: `self.current_user = {...}`, `self.is_authenticated = True`.

Cuarto, se redirige al usuario a su dashboard correspondiente según su rol.

```python
if user.role == "admin":
    return rx.redirect("/admin/dashboard")
elif user.role == "instructor":
    return rx.redirect("/instructor/dashboard")
else:
    return rx.redirect("/student/dashboard")
```

Quinto, el estado `is_authenticated = True` ya está visible en toda la aplicación porque AuthState es el estado base. La navbar cambia, el menú cambia, las rutas protegidas se desbloquean.

Hablemos de **bcrypt**. Las contraseñas nunca se guardan en texto plano en la base de datos. Eso sería un desastre de seguridad: si alguien obtiene acceso a la base de datos, obtiene todas las contraseñas de todos los usuarios.

bcrypt aplica un algoritmo de hash que es prácticamente imposible de revertir. Además, añade un "salt" —un valor aleatorio— antes de hashear, por lo que dos usuarios con la misma contraseña tienen hashes completamente diferentes. Esto bloquea los ataques de "rainbow table", que son listas precomputadas de hashes comunes.

```python
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()
    # 'micontraseña123' → '$2b$12$KNk/wJ9JRlmqYhxVu97hg...'

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())
```

La verificación no necesita conocer el salt porque bcrypt lo embebe dentro del propio hash.

Para la **protección de rutas**, uso Higher Order Components en `/components/protected.py`:

```python
def admin_only(component: rx.Component) -> rx.Component:
    return rx.cond(
        AuthState.is_user_admin,
        component,           # Admin: ve el contenido
        access_denied_view() # Otros: pantalla de acceso denegado
    )
```

Y en cada página protegida:

```python
def admin_dashboard_page():
    return admin_only(
        rx.box(navbar(), admin_dashboard_content(), footer())
    )
```

`rx.cond()` funciona en el **frontend**. El navegador recibe ambos componentes y muestra el correcto según el estado actual. La protección real del backend está en los servicios: si el estado no lo permite, las operaciones de MongoDB nunca se ejecutan.

---

---

# BLOQUE 5 — LOS ESTADOS DE REFLEX: EL CORAZÓN DEL BACKEND
**⏱ 5 minutos · ~650 palabras**

---

Si hay un concepto central en Reflex que hay que entender, es el **State**.

Un State en Reflex es una clase Python que hace tres cosas: almacena los datos que la UI necesita mostrar, define las acciones que el usuario puede ejecutar, y se sincroniza automáticamente con el frontend vía WebSocket.

Cuando un atributo del estado cambia, todos los componentes UI que lo usan se actualizan solos. No hay que escribir código de sincronización. No hay fetch, no hay callbacks, no hay useState de React. Solo Python.

Los diez estados del proyecto forman una **jerarquía de herencia** que tiene `AuthState` en la cima:

```
rx.State
    └── AuthState
            ├── EnrollmentState
            ├── InstructorDashboardState
            ├── InstructorCourseState
            ├── AdminDashboardState
            ├── CourseManagementState
            └── UserManagementState
```

Al heredar de `AuthState`, cualquier estado hijo tiene acceso directo a `self.current_user`, `self.is_authenticated` y los vars computados de rol. No hay que pasarlos como parámetros ni duplicar código.

Veamos `CourseState`, que gestiona la búsqueda en tiempo real de cursos:

```python
class CourseState(rx.State):
    courses: list[dict] = []
    search_query: str = ""

    @rx.var
    def filtered_courses(self) -> list[dict]:
        if not self.search_query:
            return self.courses
        query = self.search_query.lower()
        return [
            c for c in self.courses
            if query in c.get("title", "").lower()
            or query in c.get("description", "").lower()
        ]

    def set_search_query(self, value: str):
        self.search_query = value
```

El `@rx.var` `filtered_courses` se recalcula automáticamente cada vez que `search_query` cambia. En la UI solo hay que conectar el input al handler:

```python
rx.input(
    on_change=CourseState.set_search_query,
),
rx.foreach(
    CourseState.filtered_courses,
    course_card
)
```

El usuario escribe una letra, `set_search_query` se ejecuta, `filtered_courses` se recalcula, la lista de cursos se actualiza. Sin recargar la página. Sin llamadas adicionales al servidor.

Ahora `InstructorCourseState`, que gestiona el CRUD de cursos:

```python
async def save_course(self):
    if self.is_editing:
        await update_course(self.editing_course_id, data)
    else:
        course_id = await create_course(data)
        await self._add_course_to_instructor(course_id)

async def _add_course_to_instructor(self, course_id: str):
    db = MongoDB.get_db()
    await db["users"].update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"coursesCreated": ObjectId(course_id)}}
    )
```

El operador `$addToSet` de MongoDB es interesante: añade el elemento al array solo si no existe ya. Evita duplicados de forma atómica, sin necesitar una consulta previa para verificar.

Un problema técnico real que encontré y resolví: **el doble `on_mount`**. En modo desarrollo, Reflex llama a `on_mount` dos veces por el StrictMode de React. Eso causaba que el formulario de crear curso se abriera y se volviera a cerrar inmediatamente.

La solución fue usar un flag `auto_open_form` y comprobar también el estado actual de `show_form`:

```python
async def load_my_courses(self):
    if self.auto_open_form and not self.show_form:
        self.open_create_form()     # Primera llamada: abrir
        self.auto_open_form = False
    elif self.auto_open_form and self.show_form:
        self.auto_open_form = False  # Segunda llamada: ignorar
```

Este tipo de bugs —donde el mismo código correcto se ejecuta dos veces— son los más difíciles de diagnosticar porque el código parece correcto. La clave fue entender el comportamiento de React StrictMode e implementar idempotencia en el handler.

`EnrollmentState` gestiona las inscripciones con dos operaciones atómicas en MongoDB: añade el curso al array `enrolledCourses` del usuario, y añade el usuario al array `students` del curso. Ambas con `$addToSet` para garantizar consistencia.

---

---

# BLOQUE 6 — PÁGINAS Y COMPONENTES: EL FRONTEND
**⏱ 4 minutos · ~520 palabras**

---

En Reflex, una página es simplemente una función Python que retorna componentes UI. Esos componentes se compilan a JSX/React automáticamente. El resultado es HTML, CSS y JavaScript estándar en el navegador, pero nosotros nunca vemos ese código.

Los **cinco componentes reutilizables** del proyecto son la navbar, el footer, las tarjetas de cursos, el formulario de contacto y los componentes de protección de rutas.

La **tarjeta de curso** es un buen ejemplo de cómo funciona la UI en Reflex:

```python
def course_card(course: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.image(src=course["thumbnail"], height="200px"),
            rx.heading(course["title"], size="4"),
            rx.text(course["description"], no_of_lines=3),
            rx.hstack(
                rx.badge(
                    course["level"],
                    color_scheme=rx.match(
                        course["level"],
                        ("beginner", "green"),
                        ("intermediate", "blue"),
                        ("advanced", "purple"),
                        "gray"
                    )
                ),
                rx.text(f"€{course['price']}", color="green"),
            )
        ),
        href=f"/courses/{course['id']}",
    )
```

`rx.match()` es el equivalente del `switch/case` en la UI. No podemos usar `if/else` de Python normal con valores del estado, porque esos valores solo se conocen en el navegador en tiempo de ejecución, no en Python en tiempo de compilación. `rx.match()` genera la lógica condicional en el frontend.

La **navbar** es el componente más complejo porque muestra cosas diferentes según si el usuario está autenticado y cuál es su rol:

```python
def user_menu() -> rx.Component:
    return rx.cond(
        AuthState.is_authenticated,
        rx.menu.root(
            rx.menu.trigger(rx.text(AuthState.user_name)),
            rx.menu.content(
                rx.cond(
                    AuthState.is_user_admin,
                    rx.menu.item("Panel Admin", on_click=rx.redirect("/admin/dashboard")),
                    rx.fragment()  # Nada si no es admin
                ),
                rx.menu.item("Mi Perfil", on_click=rx.redirect("/profile")),
                rx.menu.item("Cerrar Sesión", on_click=AuthState.logout, color="red"),
            )
        ),
        rx.hstack(
            rx.link("Iniciar Sesión", href="/login"),
            rx.button("Registrarse", on_click=rx.redirect("/register")),
        )
    )
```

`rx.cond()` con dos variantes: si está autenticado, menú con opciones de usuario; si no, botones de login y registro. Y dentro del menú, otro `rx.cond()` que muestra el enlace al panel de admin solo si el usuario es admin.

El **diseño responsive** se implementa con `rx.breakpoints()`:

```python
rx.grid(
    columns=rx.breakpoints(
        initial="1",   # Móvil: 1 columna
        sm="2",        # Tablet: 2 columnas
        md="3",        # Escritorio: 3 columnas
        lg="4",        # Pantalla grande: 4 columnas
    ),
    gap="4",
)
```

Una sola línea de Python, y el grid se adapta a cualquier tamaño de pantalla. Reflex genera los media queries de CSS correspondientes automáticamente.

La plataforma tiene **páginas de contenido** —blog, FAQ, documentación, términos, cookies, política de privacidad— y **páginas funcionales** con lógica real: dashboards, gestión de usuarios, gestión de cursos, visor de lecciones. En total, treinta páginas accesibles desde el navegador.

---

---

# BLOQUE 7 — FUNCIONALIDADES DESTACADAS
**⏱ 3 minutos · ~390 palabras**

---

Quiero destacar cinco funcionalidades que demuestran la amplitud del proyecto.

**Primera: el visor de cursos**. La página `/courses/[course_id]/view` funciona como un reproductor de cursos tipo Udemy. Tiene un sidebar izquierdo con el índice de lecciones, un panel central con el contenido de la lección actual, y el progreso se guarda en MongoDB por lección. El estudiante puede navegar entre lecciones y retomar donde lo dejó.

**Segunda: los dashboards diferenciados**. Cada rol tiene su propio dashboard.

El dashboard de **administrador** muestra estadísticas globales: total de usuarios, cursos, inscripciones, ingresos. Tiene acceso directo a la gestión de usuarios, cursos y categorías. Los cambios que hace el admin se reflejan inmediatamente en la base de datos.

El dashboard de **instructor** muestra sus cursos activos, cuántos estudiantes tiene cada uno, y métricas de rendimiento. Desde ahí puede crear un nuevo curso con un clic.

El dashboard de **estudiante** muestra los cursos en los que está inscrito, el progreso en cada uno, y recomendaciones de nuevos cursos.

**Tercera: la búsqueda en tiempo real**. Ya la hemos visto en el código, pero en la práctica es: el usuario empieza a escribir en el buscador, y los resultados se filtran instantáneamente. Sin botón de buscar, sin llamada al servidor, sin recarga de página. La var computada `filtered_courses` hace todo el trabajo.

**Cuarta: el CRUD completo de cursos para instructores**. Desde la página `/instructor/courses`, el instructor puede crear cursos nuevos, editar los existentes, eliminarlos con confirmación mediante un dialog de alerta, y ver cuántos alumnos tiene cada curso. El formulario maneja tanto la creación como la edición con el mismo código, distinguiéndolos por el flag `is_editing`.

**Quinta: estadísticas reales desde MongoDB**. La página `/about` no usa datos hardcodeados. Consulta MongoDB en tiempo de carga:

```python
self.total_courses = len(courses)
self.total_lessons = sum(len(c.get("lessons", [])) for c in courses)
self.total_enrollments = sum(len(c.get("students", [])) for c in courses)
self.total_instructors = len([u for u in users if u["role"] == "instructor"])
```

Los números que ve el usuario en "Sobre Nosotros" son los números reales de la base de datos en ese momento.

---

---

# BLOQUE 8 — CONCLUSIONES Y PRÓXIMOS PASOS
**⏱ 2 minutos · ~260 palabras**

---

Repasemos lo que hemos visto hoy.

Hemos construido una plataforma de e-learning completa usando exclusivamente Python. Sin JavaScript manual. Sin frameworks frontend separados. Un solo lenguaje para todo el stack.

La combinación de **Reflex + MongoDB + bcrypt** ha demostrado ser eficaz para este tipo de proyecto:

- **Velocidad de desarrollo**: un solo lenguaje para todo elimina el cambio de contexto constante entre frontend y backend.
- **Coherencia del código**: toda la lógica, tanto de UI como de negocio, sigue los mismos patrones Python.
- **Seguridad**: autenticación con bcrypt, roles bien definidos, rutas protegidas, contraseñas nunca en texto plano.
- **Escalabilidad**: MongoDB crece horizontalmente; Reflex compila a React optimizado para producción.

Los **patrones de diseño** aplicados son: Repository Pattern en los servicios, State Pattern en los estados, Component Pattern en la UI, y Higher Order Components para la protección de rutas.

En cuanto a **próximos pasos**:
- Integración con Stripe para pagos online
- Sistema de notificaciones en tiempo real
- Exámenes y certificados automáticos
- Analítica avanzada con gráficos de progreso
- Recomendaciones personalizadas con IA
- Deploy a producción en Reflex Cloud o con Docker

La reflexión final es esta: **Python es suficiente**. Suficiente para construir una aplicación web profesional, escalable y segura. No necesitamos dos lenguajes, dos equipos, dos formas de pensar. Reflex demuestra que el ecosistema Python puede cubrir el stack completo de una aplicación moderna.

Muchas gracias. Quedo abierto a preguntas.

---

---

# APÉNDICE — RESPUESTAS A PREGUNTAS FRECUENTES

**¿No es más lento que usar React directamente?**
En producción, Reflex compila a React optimizado. La diferencia de rendimiento es mínima para este tipo de aplicación. La ganancia en velocidad de desarrollo es enorme.

**¿Se puede usar SQL en lugar de MongoDB?**
Sí. Reflex funciona con cualquier base de datos. MongoDB se eligió por la flexibilidad de esquema para cursos con estructura variable.

**¿Cómo se hace el deploy?**
Reflex tiene su propio servicio en la nube, Reflex Cloud, o se puede dockerizar para desplegar en cualquier VPS.

**¿Es seguro para producción?**
La autenticación y el hash de contraseñas son sólidos. Para producción habría que añadir HTTPS, rate limiting y validación de entrada más estricta.

**¿Qué fue lo más difícil de desarrollar?**
El sistema de estados con herencia y el bug del doble `on_mount` en Reflex. Entender cómo el estado reactivo se sincroniza con el frontend requiere cambiar la forma de pensar respecto al desarrollo web tradicional.

---

*Guion oral para presentación de 30 minutos — E-Learning JCB*
*~3.900 palabras · ~130 palabras/minuto · 30 minutos*
