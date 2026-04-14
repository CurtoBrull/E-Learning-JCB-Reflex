# E-Learning JCB — Guion de Presentación Oral (30 minutos)
> Texto completo para leer/adaptar · ~130 palabras/minuto · ~3.900 palabras totales
> Incluye módulos FOL (Formación y Orientación Laboral) y EMPRESA e Iniciativa Emprendedora

---

## ESTRUCTURA RÁPIDA

| Bloque | Tema | Módulo | Tiempo |
|--------|------|--------|--------|
| 1 | Introducción y contexto del proyecto | DAW | 2 min |
| 2 | Mercado, oportunidad y modelo de negocio | EMPRESA | 4 min |
| 3 | Viabilidad: técnica, económica y legal | FOL + EMPRESA | 4 min |
| 4 | Arquitectura general del sistema | DAW | 3 min |
| 5 | La base de datos: MongoDB y modelos | DAW | 3 min |
| 6 | Autenticación y sistema de roles | DAW | 4 min |
| 7 | Los estados de Reflex: el backend | DAW | 4 min |
| 8 | Páginas, componentes y funcionalidades | DAW | 4 min |
| 9 | Conclusiones, ayudas y próximos pasos | FOL + DAW | 2 min |

---

---

# BLOQUE 1 — INTRODUCCIÓN Y CONTEXTO
**⏱ 2 minutos · ~260 palabras**

---

Buenos días a todos.

Voy a presentaros **E-Learning JCB**, una plataforma de formación online construida íntegramente en Python. Y cuando digo íntegramente en Python, lo digo en serio: no hay ni una sola línea de JavaScript escrita manualmente. Todo el código —servidor e interfaz de usuario— está escrito en un único lenguaje.

Esto es posible gracias a **Reflex**, un framework open-source que compila código Python en una aplicación React + FastAPI automáticamente. Escribes Python puro; Reflex genera el frontend y el backend por debajo.

El proyecto cubre el stack completo de una plataforma real: autenticación con roles, operaciones CRUD, búsqueda en tiempo real y dashboards diferenciados para estudiantes, instructores y administradores.

Para tener la escala en mente:

- **39 archivos Python**, **0 líneas de JavaScript manual**
- **30 páginas web**, **33 rutas registradas**
- **10 clases de estado** gestionando toda la lógica
- **~18.000 líneas de código**

Pero antes de entrar en el código, necesito explicar **por qué** existe este proyecto y si tiene sentido económico y legal construirlo. Eso es lo que veremos en los próximos bloques.

---

---

# BLOQUE 2 — MERCADO, OPORTUNIDAD Y MODELO DE NEGOCIO
**⏱ 4 minutos · ~520 palabras · Módulo: EMPRESA**

---

## El contexto del mercado

El e-learning no es una moda pasajera. Es uno de los sectores con mayor crecimiento sostenido de la última década.

Según el informe *Global E-Learning Market 2025* de Research and Markets:

- El mercado global facturó **$315 mil millones** en 2023.
- La proyección para 2026 es de **$457 mil millones**.
- La tasa de crecimiento anual compuesta es del **13,7%**, muy por encima del PIB medio global.

En España, el mercado factura **€2.1 mil millones** anuales y crece a ritmo similar. El 76% de las empresas españolas ya ha adoptado formación online, y el 89% de los estudiantes universitarios usa plataformas de e-learning de forma complementaria.

## Las oportunidades identificadas

He identificado tres segmentos de mercado con potencial real para este proyecto.

**El primero es el mercado de formación técnica.** En España hay 120.000 profesionales IT, y el 68% busca formación online por flexibilidad. El ticket medio por curso es de 49€ a 199€, con una frecuencia de 3 a 4 cursos por año. Proyección conservadora para el primer año: **13.860€** con 100 estudiantes activos.

**El segundo es el mercado corporativo B2B.** Hay 2,9 millones de PYMEs en España, y el 23% busca plataformas de e-learning propias. El presupuesto medio anual por empresa es de 2.000€ a 5.000€. Con solo 5 empresas cliente, el primer año genera **12.000€**.

**El tercero es el marketplace de instructores.** Con 20 instructores activos y 50 ventas mensuales a una comisión del 25%, el primer año produce **14.850€**.

## El análisis de competencia

Los principales competidores directos son Udemy, Coursera, Domestika y Platzi.

Udemy domina con un 35% de cuota de mercado, pero su principal debilidad es la saturación de contenido y la baja calidad de algunos cursos. Coursera apunta al mercado académico premium, dejando desatendido el segmento de formación técnica accesible. Domestika tiene muy buena UX pero un catálogo limitado a creativos. Platzi tiene comunidad sólida pero orientada a Latinoamérica.

La oportunidad está en el nicho de **formación técnica de calidad**, con contenido verificado, UX optimizada y precios accesibles para el mercado español.

## El modelo de negocio

El modelo está estructurado en tres fuentes de ingresos:

1. **Modelo Freemium**: cursos básicos gratuitos para atraer usuarios, cursos premium de 49€ a 99€.
2. **Comisiones por ventas**: la plataforma retiene un 25-30% de cada venta de instructor.
3. **Suscripciones corporativas**: acceso ilimitado para empresas a partir de 200€/mes.

El **punto de equilibrio** es de solo **24 ventas al año** —2 cursos vendidos al mes—, un umbral muy accesible en cualquiera de los tres segmentos.

---

---

# BLOQUE 3 — VIABILIDAD: TÉCNICA, ECONÓMICA Y LEGAL
**⏱ 4 minutos · ~520 palabras · Módulo: FOL + EMPRESA**

---

## La forma jurídica: autónomo

Para el lanzamiento del proyecto se ha optado por la figura del **trabajador autónomo** —persona física empresario individual—. Las razones son claras:

- **Coste de constitución cero**: el alta es gratuita, no hay capital mínimo.
- **Gestión simplificada**: contabilidad más sencilla, sin Registro Mercantil.
- **Flexibilidad total**: se puede cesar la actividad en cualquier momento.
- **Tarifa plana de Seguridad Social**: los primeros doce meses, la cuota es de solo **80€/mes** en lugar de los ~303€ habituales. Eso supone un ahorro de **2.676€ el primer año**.

La única desventaja relevante es la responsabilidad ilimitada —el patrimonio personal responde de las deudas—, pero en un negocio digital con costes bajos, ese riesgo es mínimo.

Si el negocio supera los **40.000€ de beneficios anuales**, está previsto el cambio a Sociedad Limitada, que es fiscalmente más eficiente a partir de ese umbral.

## Obligaciones fiscales

Como autónomo que presta servicios digitales en España, las obligaciones fiscales son tres.

**IVA al 21%**: declaración trimestral mediante el Modelo 303, más el resumen anual (Modelo 390). En servicios digitales a consumidores finales españoles, se aplica siempre el 21%.

**IRPF**: declaración trimestral (Modelo 130) bajo el régimen de estimación directa simplificada. El tipo progresivo va del 15% al 47% sobre el beneficio neto. Para un beneficio neto de 11.400€ en el primer año, el IRPF es de aproximadamente **720€**.

**Cuota de Seguridad Social (RETA)**: 80€/mes el primer año por tarifa plana. A partir del segundo año, la cuota se calcula por rendimientos netos, con un mínimo de ~230€/mes.

## Marco legal del proyecto

El proyecto cumple con tres normativas clave.

**RGPD** —Reglamento General de Protección de Datos—: los datos de usuarios se almacenan en MongoDB Atlas con cifrado AES-256 en reposo y TLS en tránsito. Existe política de privacidad accesible, formulario de contacto con consentimiento explícito, y cookies con gestión de preferencias. La plataforma incluye páginas de política de privacidad, términos y condiciones, y política de cookies.

**LSSI** —Ley de Servicios de la Sociedad de la Información—: el servicio está identificado legalmente, los precios son visibles antes de la compra, y existe proceso de contratación electrónica documentado.

**Propiedad intelectual**: el código fuente se publica bajo **licencia MIT**, compatible con uso comercial. Los contenidos de los cursos son propiedad de los instructores que los crean. Las dependencias del proyecto usan licencias Apache 2.0, MIT y PSF, todas compatibles con el uso comercial.

## Viabilidad económica resumida

| Concepto | Valor |
|----------|-------|
| Coste de desarrollo (Año 1) | 13.190€ |
| Coste operativo anual | 4.376€ |
| Punto de equilibrio | 24 ventas/año |
| Ingresos Año 1 (realista) | 13.761€ |
| ROI Año 1 sin coste desarrollo | +18% a +506% |
| **Viabilidad global** | **89% — PROYECTO VIABLE** |

---

---

# BLOQUE 4 — ARQUITECTURA GENERAL DEL SISTEMA
**⏱ 3 minutos · ~390 palabras · Módulo: DAW**

---

La arquitectura de E-Learning JCB sigue un patrón en capas inspirado en MVC, adaptado al paradigma reactivo de Reflex.

Hay **cinco capas diferenciadas**:

El **navegador** ejecuta React —generado por Reflex desde Python. El usuario ve HTML, CSS y JavaScript estándar, pero yo nunca los escribí.

Las **páginas y componentes** son treinta archivos Python que definen qué ve el usuario en cada URL, más cinco componentes reutilizables —navbar, footer, tarjetas de cursos—.

Los **estados** son la capa central de Reflex. Diez clases Python que almacenan datos y definen las acciones del usuario. Cuando el estado cambia, la UI se actualiza sola vía WebSocket.

Los **servicios** son cuatro módulos Python que encapsulan todas las operaciones con MongoDB. Los estados llaman a los servicios; los servicios no saben nada de la UI.

Y **MongoDB Atlas** en la nube, con cuatro colecciones: usuarios, cursos, contactos y categorías.

El archivo de entrada registra las 33 rutas:

```python
app = rx.App()
app.add_page(index_page, route="/")
app.add_page(courses_page, route="/courses")
app.add_page(course_detail_page, route="/courses/[course_id]")
app.add_page(admin_dashboard_page, route="/admin/dashboard")
```

Las rutas con corchetes como `[course_id]` son **rutas dinámicas**: Reflex extrae el parámetro de la URL e inyecta su valor en el estado automáticamente.

El stack completo: **Python 3.14 + Reflex 0.8.24 + MongoDB Atlas + Motor async + bcrypt + Granian + Redis**.

---

---

# BLOQUE 5 — LA BASE DE DATOS: MONGODB Y LOS MODELOS
**⏱ 3 minutos · ~390 palabras · Módulo: DAW**

---

¿Por qué MongoDB? Porque los cursos tienen estructura variable: algunos tienen vídeos, otros textos, otros evaluaciones. Con SQL necesitaría nuevas tablas y JOINs costosos para cada variación. Con MongoDB, un curso es un **documento JSON flexible** con exactamente los campos que necesita.

El proyecto usa **cuatro colecciones**: `users`, `courses`, `contacts` y `categories`.

La colección `courses` aplica el patrón de diseño más importante: **embedding vs referencing**.

Las **lecciones y reseñas** están embebidas dentro del curso porque siempre se leen juntas con él. Las **referencias a estudiantes e instructores** son solo ObjectIDs porque esos datos se consultan también de forma independiente.

Los modelos Python convierten documentos MongoDB en objetos Python con el método `from_dict()`:

```python
@classmethod
def from_dict(cls, data: dict) -> "Course":
    course = cls()
    course.id = str(data.get("_id", ""))
    course.students = [str(s) for s in data.get("students", [])]
    return course
```

El `str()` es crítico: MongoDB almacena IDs como tipo `ObjectId`, no como string. Sin esa conversión, `"abc123" == ObjectId("abc123")` devuelve `False` —un bug silencioso que aparece en producción.

Los servicios son funciones `async` que encapsulan las operaciones:

```python
async def get_popular_courses(limit: int = 6) -> list[Course]:
    db = MongoDB.get_db()
    cursor = db["courses"].find({}).sort("studentsEnrolled", -1).limit(limit)
    return [Course.from_dict(doc) for doc in await cursor.to_list(length=limit)]
```

`async`/`await` con Motor garantiza que mientras MongoDB responde, el servidor atiende otras peticiones. Sin bloqueos.

---

---

# BLOQUE 6 — AUTENTICACIÓN Y SISTEMA DE ROLES
**⏱ 4 minutos · ~520 palabras · Módulo: DAW**

---

La autenticación es el sistema más crítico. En E-Learning JCB hay tres roles con capacidades muy distintas.

El **estudiante** se inscribe en cursos, accede al contenido y deja valoraciones.
El **instructor** crea y gestiona sus cursos, ve estadísticas de rendimiento.
El **administrador** tiene control total: usuarios, cursos, categorías, configuración.

El corazón es `AuthState`:

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

El `@rx.var` marca una propiedad como **computada**: se recalcula automáticamente cuando `current_user` cambia. El frontend siempre tiene el valor correcto sin código de sincronización.

El **flujo de login** tiene cinco pasos:

1. Buscar usuario en MongoDB por email. Si no existe: error genérico —sin especificar cuál campo es incorrecto, por seguridad.
2. Verificar contraseña con bcrypt.
3. Guardar usuario en estado: `self.current_user = {...}`, `self.is_authenticated = True`.
4. Redirigir según rol: `/admin/dashboard`, `/instructor/dashboard` o `/student/dashboard`.
5. El cambio de estado se propaga a toda la app: navbar, menús, rutas protegidas.

**bcrypt**: las contraseñas nunca se guardan en texto plano. bcrypt aplica un hash irreversible con salt aleatorio integrado:

```python
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()
    # 'micontraseña' → '$2b$12$KNk/wJ9JRlmq...'

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())
```

Esto bloquea los ataques de rainbow table: aunque la base de datos sea comprometida, los hashes no son revertibles.

La **protección de rutas** usa Higher Order Components:

```python
def admin_only(component: rx.Component) -> rx.Component:
    return rx.cond(
        AuthState.is_user_admin,
        component,            # Admin: ve el contenido
        access_denied_view()  # Otros: pantalla de error
    )

# En la página:
def admin_dashboard_page():
    return admin_only(rx.box(navbar(), admin_content(), footer()))
```

`rx.cond()` funciona en el frontend. La protección real del backend está en los servicios: si el estado no lo permite, las operaciones de MongoDB no se ejecutan.

---

---

# BLOQUE 7 — LOS ESTADOS DE REFLEX: EL BACKEND
**⏱ 4 minutos · ~520 palabras · Módulo: DAW**

---

El **State** es el concepto central de Reflex. Una clase Python que almacena datos, define acciones y se sincroniza con el frontend vía WebSocket automáticamente.

Los diez estados forman una jerarquía de herencia con `AuthState` en la cima:

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

Los estados hijos heredan acceso directo a `self.current_user` y `self.is_authenticated` sin duplicar código.

**CourseState** gestiona la búsqueda en tiempo real:

```python
class CourseState(rx.State):
    courses: list[dict] = []
    search_query: str = ""

    @rx.var
    def filtered_courses(self) -> list[dict]:
        if not self.search_query:
            return self.courses
        query = self.search_query.lower()
        return [c for c in self.courses
                if query in c.get("title", "").lower()
                or query in c.get("description", "").lower()]

    def set_search_query(self, value: str):
        self.search_query = value
```

El usuario escribe → `set_search_query` se ejecuta → `filtered_courses` se recalcula → la lista se actualiza. Sin llamadas al servidor. Sin recargar la página.

**InstructorCourseState** gestiona el CRUD de cursos:

```python
async def save_course(self):
    if self.is_editing:
        await update_course(self.editing_course_id, data)
    else:
        course_id = await create_course(data)
        await db["users"].update_one(
            {"_id": ObjectId(user_id)},
            {"$addToSet": {"coursesCreated": ObjectId(course_id)}}
        )
```

`$addToSet` de MongoDB añade al array solo si el elemento no existe, evitando duplicados de forma atómica.

Un bug real que resolví: **el doble `on_mount`**. En desarrollo, Reflex llama a `on_mount` dos veces por el StrictMode de React. El formulario se abría y se cerraba inmediatamente. La solución fue idempotencia con un flag:

```python
async def load_my_courses(self):
    if self.auto_open_form and not self.show_form:
        self.open_create_form()      # Primera llamada: abrir
        self.auto_open_form = False
    elif self.auto_open_form and self.show_form:
        self.auto_open_form = False  # Segunda llamada: ignorar
```

Este tipo de bug —código correcto ejecutado dos veces— es el más difícil de diagnosticar. La clave fue entender el ciclo de vida de React StrictMode.

---

---

# BLOQUE 8 — PÁGINAS, COMPONENTES Y FUNCIONALIDADES
**⏱ 4 minutos · ~520 palabras · Módulo: DAW**

---

En Reflex, una página es una función Python que retorna componentes UI compilados automáticamente a JSX/React.

La **navbar** muestra opciones distintas según el estado del usuario:

```python
def user_menu() -> rx.Component:
    return rx.cond(
        AuthState.is_authenticated,
        rx.menu.root(
            rx.menu.trigger(rx.text(AuthState.user_name)),
            rx.menu.content(
                rx.cond(AuthState.is_user_admin,
                    rx.menu.item("Panel Admin", on_click=rx.redirect("/admin/dashboard")),
                    rx.fragment()
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

El **diseño responsive** usa `rx.breakpoints()`:

```python
rx.grid(
    columns=rx.breakpoints(
        initial="1",  # Móvil: 1 columna
        sm="2",       # Tablet: 2 columnas
        md="3",       # Escritorio: 3 columnas
        lg="4",       # Pantalla grande: 4 columnas
    ),
    gap="4",
)
```

Una sola línea genera los media queries de CSS automáticamente.

Quiero destacar **cinco funcionalidades** que demuestran la amplitud del proyecto.

**El visor de cursos** funciona como Udemy: sidebar con índice de lecciones, panel central con el contenido, progreso guardado por lección en MongoDB.

**Los dashboards diferenciados**: el de administrador muestra estadísticas globales y acceso a gestión de usuarios, cursos y categorías. El de instructor muestra sus cursos y KPIs. El de estudiante muestra los cursos inscritos y el progreso individual.

**La búsqueda en tiempo real**: el usuario escribe, los resultados se filtran al instante mediante la var computada `filtered_courses`. Cero llamadas al servidor.

**El CRUD de cursos para instructores**: crear, editar, eliminar con confirmación mediante dialog de alerta, y ver alumnos inscritos. El mismo formulario maneja creación y edición distinguiéndolos por el flag `is_editing`.

**Las estadísticas reales**: la página `/about` consulta MongoDB en tiempo de carga para mostrar datos reales —total de cursos, lecciones, inscripciones, instructores activos—. No hay datos hardcodeados.

---

---

# BLOQUE 9 — CONCLUSIONES, AYUDAS Y PRÓXIMOS PASOS
**⏱ 2 minutos · ~260 palabras · Módulo: FOL + DAW**

---

## Ayudas para el lanzamiento

El proyecto tiene acceso a ayudas reales que reducen el riesgo financiero del primer año:

- **Tarifa plana de autónomos**: 80€/mes los primeros 12 meses. Ahorro de **2.676€**.
- **Kit Digital** (Red.es): hasta **1.500€** para digitalización de autónomos.
- **Almería Emprende** (Junta de Andalucía): hasta **3.000€** para proyectos innovadores.
- **ENISA** (si se constituye SL): préstamo participativo de hasta **25.000€**.

Total de ayudas accesibles en el escenario conservador: **7.176€**, lo que cubre prácticamente todos los costes operativos del primer año.

## Síntesis final

| Dimensión | Resultado |
|-----------|-----------|
| Técnica | Python full-stack, sin JavaScript manual, MVC adaptado a Reflex |
| Datos | MongoDB NoSQL, embedding + referencing, 4 colecciones |
| Seguridad | bcrypt, RBAC por roles, RGPD cumplido, LSSI cumplido |
| Negocio | Punto equilibrio: 24 ventas/año, ROI +18% a +506% en Año 1 |
| Legal | Autónomo, IVA 21%, IRPF progresivo, MIT license |
| Viabilidad global | **89% — PROYECTO ALTAMENTE VIABLE** |

## Próximos pasos del proyecto

- Integración con **Stripe** para pagos online
- Sistema de **notificaciones** en tiempo real
- **Exámenes y certificados** automáticos
- **Analítica avanzada** con gráficos de progreso
- Recomendaciones personalizadas con **IA**
- **Deploy a producción**: Reflex Cloud o Docker + VPS

La reflexión final es esta: **Python es suficiente** para construir una aplicación web profesional, segura y económicamente viable. Un solo lenguaje, un solo stack, un proyecto real.

Muchas gracias. Quedo abierto a preguntas.

---

---

# APÉNDICE — RESPUESTAS A PREGUNTAS FRECUENTES

**¿Por qué autónomo y no Sociedad Limitada?**
Para el primer año, el autónomo es más ágil y barato. La tarifa plana reduce la SS a 80€/mes. Si los beneficios superan 40.000€, el cambio a SL es más eficiente fiscalmente.

**¿Qué pasa con el RGPD y los datos de los estudiantes?**
Los datos se almacenan en MongoDB Atlas con cifrado AES-256 en reposo y TLS en tránsito. La plataforma incluye política de privacidad, gestión de cookies y formularios con consentimiento explícito.

**¿No es más lento que usar React directamente?**
En producción, Reflex compila a React optimizado. La diferencia de rendimiento es mínima para este tipo de aplicación. La ganancia en velocidad de desarrollo es enorme.

**¿Se puede usar SQL en lugar de MongoDB?**
Sí. Reflex funciona con cualquier base de datos. MongoDB se eligió por la flexibilidad de esquema para cursos con estructura variable.

**¿Cómo se hace el deploy?**
Reflex Cloud o Docker + VPS. Coste estimado: 0-20€/mes en Reflex Cloud, 360€/año en VPS propio.

**¿Qué fue lo más difícil de desarrollar?**
El sistema de estados con herencia y el bug del doble `on_mount`. Entender cómo el estado reactivo se sincroniza con el frontend requiere cambiar la forma de pensar respecto al desarrollo web tradicional.

---

*Guion oral para presentación de 30 minutos — E-Learning JCB*
*~3.900 palabras · ~130 palabras/minuto · 30 minutos*
*Módulos: DAW · FOL · EMPRESA e Iniciativa Emprendedora*
