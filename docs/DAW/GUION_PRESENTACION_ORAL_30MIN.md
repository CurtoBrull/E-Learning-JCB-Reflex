# E-Learning JCB — Guion de Presentación Oral (30 minutos)
> Texto completo para leer/adaptar · ~130 palabras/minuto
> **PARTE 1:** Exposición teórica ~15 min · ~1.950 palabras
> **PARTE 2:** Demostración práctica ~15 min · ~1.950 palabras
> Incluye módulos FOL (Formación y Orientación Laboral) y EMPRESA e Iniciativa Emprendedora

---

## ESTRUCTURA RÁPIDA

### PARTE 1 — Exposición Teórica (15 minutos)

| Bloque | Tema | Módulo | Tiempo |
|--------|------|--------|--------|
| 1 | Introducción y contexto del proyecto | DAW | 1 min |
| 2 | Mercado, oportunidad y modelo de negocio | EMPRESA | 2 min |
| 3 | Viabilidad: técnica, económica y legal | FOL + EMPRESA | 2 min |
| 4 | Arquitectura general del sistema | DAW | 1.5 min |
| 5 | La base de datos: MongoDB y modelos | DAW | 1.5 min |
| 6 | Autenticación y sistema de roles | DAW | 2 min |
| 7 | Los estados de Reflex: el backend | DAW | 2 min |
| 8 | Páginas, componentes y funcionalidades | DAW | 1 min |
| 9 | Conclusiones, ayudas y próximos pasos | FOL + DAW | 1 min |

### PARTE 2 — Demostración Práctica (15 minutos)

| Demo | Funcionalidad | Tiempo |
|------|--------------|--------|
| D1 | Página principal y navegación | 1 min |
| D2 | Registro e inicio de sesión | 2 min |
| D3 | Catálogo y búsqueda en tiempo real | 2 min |
| D4 | Visor de curso (experiencia estudiante) | 2 min |
| D5 | Dashboard instructor y CRUD de cursos | 3 min |
| D6 | Dashboard administrador | 2 min |
| D7 | Protección de rutas por rol | 1 min |
| D8 | Conexión código Python → UI | 2 min |

---

---

# PARTE 1 — EXPOSICIÓN TEÓRICA

---

# BLOQUE 1 — INTRODUCCIÓN Y CONTEXTO (pagina 1 del PDF)
**⏱ 1 minuto · ~130 palabras**

---

Buenos días a todos.

Voy a presentaros **E-Learning JCB**, una plataforma de formación online construida íntegramente en Python. No hay ni una sola línea de JavaScript escrita manualmente.

Esto es posible gracias a **Reflex**, un framework que compila código Python en React + FastAPI automáticamente. Escribes Python puro; Reflex genera el frontend y el backend por debajo.

Para tener la escala en mente: (pag 2 del PDF)

- **39 archivos Python**, **0 líneas de JavaScript manual**
- **30 páginas web**, **33 rutas registradas**
- **10 clases de estado** gestionando toda la lógica
- **~18.000 líneas de código**

---

---

# BLOQUE 2 — MERCADO, OPORTUNIDAD Y MODELO DE NEGOCIO (pagina 3 del PDF)
**⏱ 2 minutos · ~260 palabras · Módulo: EMPRESA**

---

El e-learning es uno de los sectores con mayor crecimiento sostenido de la última década: mercado global de **$315 mil millones** en 2023, proyección de **$457 mil millones** para 2026 a un CAGR del **13,7%**.

He identificado tres segmentos con potencial real:

**Formación técnica**: 120.000 profesionales IT en España. Ticket medio 49€-199€. Proyección conservadora Año 1: **13.860€** con 100 estudiantes.

**Corporativo B2B**: 2,9 millones de PYMEs. Con solo 5 empresas cliente: **12.000€** al año.

**Marketplace de instructores**: 20 instructores, 50 ventas/mes, comisión 25% → **14.850€** al año.

Los competidores directos —Udemy, Coursera, Domestika, Platzi— dejan desatendido el nicho de **formación técnica accesible y de calidad para el mercado español**. Ese es nuestro hueco.

El modelo de negocio tiene tres patas: (pag 4 del PDF)

1. **Freemium**: cursos básicos gratuitos, premium de 49€ a 99€.
2. **Comisiones**: 25-30% por venta de instructor.
3. **Suscripciones corporativas**: desde 200€/mes.

El **punto de equilibrio son solo 24 ventas al año** —2 cursos al mes—, un umbral altamente accesible.

---

---

# BLOQUE 3 — VIABILIDAD: TÉCNICA, ECONÓMICA Y LEGAL (pagina 5 del PDF)
**⏱ 2 minutos · ~260 palabras · Módulo: FOL + EMPRESA**

---

## Forma jurídica: autónomo

Se ha optado por **trabajador autónomo** por tres razones: coste de constitución cero, gestión simplificada y **tarifa plana de 80€/mes** los primeros doce meses —ahorro de 2.676€—. Si el negocio supera los 40.000€ de beneficio, el cambio a SL es más eficiente fiscalmente.

## Obligaciones fiscales

- **IVA 21%**: Modelo 303 trimestral + Modelo 390 anual.
- **IRPF**: Modelo 130 trimestral, estimación directa simplificada.
- **RETA**: 80€/mes Año 1; cuota por rendimientos netos a partir del Año 2.

## Marco legal

- **RGPD**: datos en MongoDB Atlas con cifrado AES-256 (reposo) y TLS (tránsito), política de privacidad y gestión de cookies.
- **LSSI**: precios visibles, contratación electrónica documentada.
- **Propiedad intelectual**: código bajo **licencia MIT**, dependencias bajo Apache 2.0/PSF.

## Resumen económico

| Concepto | Valor |
|----------|-------|
| Coste operativo anual | 4.376€ |
| Bolsa de ayudas accesibles | 7.176€ |
| Punto de equilibrio | 24 ventas/año |
| ROI Año 1 (sin coste desarrollo) | +18% a +506% |
| **Viabilidad global** | **89% — PROYECTO VIABLE** |

---

---

# BLOQUE 4 — ARQUITECTURA GENERAL DEL SISTEMA (pagina 6 del PDF)
**⏱ 1.5 minutos · ~195 palabras · Módulo: DAW**

---

La arquitectura sigue un patrón en capas adaptado al paradigma reactivo de Reflex. Hay **cinco capas**:

1. **Navegador**: ejecuta React generado automáticamente. HTML/CSS/JS que yo nunca escribí.
2. **Páginas y componentes**: 30 archivos Python definiendo la UI.
3. **Estados**: 10 clases Python que almacenan datos y sincronizan la UI vía WebSocket.
4. **Servicios**: 4 módulos Python que encapsulan todas las operaciones con MongoDB.
5. **MongoDB Atlas**: base de datos NoSQL en la nube, 4 colecciones.

Las rutas dinámicas como `/courses/[course_id]` extraen el parámetro de la URL e inyectan su valor en el estado automáticamente.

Stack completo: **Python 3.14 + Reflex + MongoDB Atlas + Motor async + bcrypt + Granian + Redis**.

---

---

# BLOQUE 5 — LA BASE DE DATOS: MONGODB Y LOS MODELOS (pagina 7 del PDF)
**⏱ 1.5 minutos · ~195 palabras · Módulo: DAW**

---

¿Por qué MongoDB? Porque los cursos tienen estructura variable. Con SQL necesitaría nuevas tablas y JOINs costosos para cada variación. Con MongoDB, un curso es un **documento JSON flexible**.

El proyecto usa cuatro colecciones: `users`, `courses`, `contacts`, `categories`.

La colección `courses` aplica el patrón **embedding vs referencing**:
- **Lecciones y reseñas** embebidas: siempre se leen junto al curso.
- **Referencias a estudiantes e instructores**: solo ObjectIDs, porque se consultan independientemente.

Un detalle crítico: MongoDB almacena IDs como tipo `ObjectId`, no como string. Sin convertir con `str()`, la comparación `"abc123" == ObjectId("abc123")` devuelve `False` —un bug silencioso en producción.

Los servicios usan `async`/`await` con Motor: mientras MongoDB responde, el servidor atiende otras peticiones sin bloqueos.

---

---

# BLOQUE 6 — AUTENTICACIÓN Y SISTEMA DE ROLES (pagina 8 del PDF)
**⏱ 2 minutos · ~260 palabras · Módulo: DAW**

---

Hay tres roles con capacidades distintas: **estudiante**, **instructor** y **administrador**.

El corazón es `AuthState`, con propiedades computadas mediante `@rx.var` que se recalculan automáticamente cuando el estado cambia:

```python
class AuthState(rx.State):
    is_authenticated: bool = False
    current_user: dict = {}

    @rx.var
    def is_user_admin(self) -> bool:
        return self.current_user.get("role", "") == "admin"
```

El **flujo de login** en cinco pasos:

1. Buscar usuario por email —error genérico para no revelar qué campo es incorrecto.
2. Verificar contraseña con **bcrypt** (hash irreversible con salt aleatorio → bloquea ataques rainbow table).
3. Guardar usuario en estado: `self.current_user`, `self.is_authenticated = True`.
4. Redirigir según rol: `/admin/dashboard`, `/instructor/dashboard` o `/student/dashboard`.
5. El estado se propaga: navbar, menús y rutas protegidas se actualizan solos.

La **protección de rutas** usa Higher Order Components con `rx.cond()`. La protección real del backend está en los servicios: si el estado no lo permite, las operaciones de MongoDB no se ejecutan.

---

---

# BLOQUE 7 — LOS ESTADOS DE REFLEX: EL BACKEND (pagina 9 del PDF)
**⏱ 2 minutos · ~260 palabras · Módulo: DAW**

---

El **State** es el concepto central de Reflex: una clase Python que almacena datos, define acciones y se sincroniza con el frontend vía WebSocket. Los diez estados forman una jerarquía con `AuthState` en la cima; los estados hijos heredan `current_user` sin duplicar código.

**Búsqueda en tiempo real** con `@rx.var`:

```python
@rx.var
def filtered_courses(self) -> list[dict]:
    query = self.search_query.lower()
    return [c for c in self.courses
            if query in c.get("title", "").lower()]
```

El usuario escribe → el var se recalcula → la lista se actualiza. Sin llamadas al servidor.

**Un bug real que resolví**: el *doble `on_mount`*. En desarrollo, el StrictMode de React ejecuta `on_mount` dos veces. El formulario se abría y se cerraba inmediatamente. La solución fue **idempotencia con un flag de estado**: la primera llamada abre el formulario y desactiva el flag; la segunda lo detecta y no hace nada.

Este tipo de bug —código correcto ejecutado dos veces— es el más difícil de diagnosticar.

---

---

# BLOQUE 8 — PÁGINAS, COMPONENTES Y FUNCIONALIDADES (pagina 10 del PDF)
**⏱ 1 minuto · ~130 palabras · Módulo: DAW**

---

Cinco funcionalidades clave que demuestran la amplitud del proyecto —y que veremos en vivo en la demostración:

1. **Visor de cursos**: sidebar con índice, progreso guardado por lección en MongoDB.
2. **Dashboards diferenciados**: admin, instructor y estudiante con datos reales de MongoDB.
3. **Búsqueda en tiempo real**: var computada sin llamadas al servidor.
4. **CRUD de cursos**: un formulario unificado para crear y editar, con `$addToSet` para evitar duplicados atómicamente.
5. **Diseño responsive**: `rx.breakpoints()` genera media queries en una sola línea de Python.

---

---

# BLOQUE 9 — CONCLUSIONES, AYUDAS Y PRÓXIMOS PASOS (paginas 11-12 del PDF)
**⏱ 1 minuto · ~130 palabras · Módulo: FOL + DAW**

---

Ayudas reales para el lanzamiento: tarifa plana SS (2.676€), Kit Digital (1.500€), Almería Emprende (3.000€). Total: **7.176€** —prácticamente todos los costes operativos del primer año cubiertos.

| Dimensión | Resultado |
|-----------|-----------|
| Técnica | Python full-stack, 0 JS manual |
| Datos | MongoDB, embedding + referencing |
| Seguridad | bcrypt, RBAC, RGPD, LSSI |
| Negocio | Equilibrio en 24 ventas/año |
| Viabilidad global | **89% — ALTAMENTE VIABLE** |

Próximos pasos: Stripe, notificaciones WebSocket, exámenes/certificados, analítica con IA, deploy en Reflex Cloud/Docker.

**Python es suficiente** para construir una plataforma web profesional, segura y comercialmente viable.

---
---

# PARTE 2 — DEMOSTRACIÓN PRÁCTICA

> **⏱ 15 minutos totales · Aplicación en ejecución**
> Abrir la aplicación en el navegador antes de empezar. Usuario admin y usuario estudiante preparados.

---

# DEMO D1 — PÁGINA PRINCIPAL Y NAVEGACIÓN
**⏱ 1 minuto**

---

*(Abrir la aplicación en el navegador, pantalla en la página de inicio `/`)*

Esto es lo que ve cualquier visitante al entrar. La página principal carga datos reales de MongoDB: número de cursos, instructores activos, estudiantes inscritos. No hay ningún número hardcodeado.

Fijaos en la **navbar**: sin sesión iniciada, solo muestra "Iniciar Sesión" y "Registrarse". En cuanto el usuario se autentique, el menú cambiará automáticamente sin recargar la página.

Podemos navegar al catálogo completo de cursos.

---

---

# DEMO D2 — REGISTRO E INICIO DE SESIÓN
**⏱ 2 minutos**

---

*(Navegar a `/register`)*

El formulario de registro tiene validación en Python. Si el email ya existe, el mensaje de error es genérico —"credenciales incorrectas"— nunca revela si el email está registrado o no. Eso es seguridad by design.

*(Registrar un nuevo usuario o usar uno existente)*

Ahora iniciamos sesión como **estudiante**.

*(Navegar a `/login`, iniciar sesión con cuenta de estudiante)*

Observad lo que pasa: la navbar cambia instantáneamente. Aparece el menú de usuario con el nombre. Esto es el **estado reactivo de Reflex**: `AuthState.is_authenticated` pasa a `True` y todos los componentes que dependen de ese valor se actualizan solos vía WebSocket.

El sistema nos redirige automáticamente al dashboard de estudiante, porque el rol detectado es `"student"`.

---

---

# DEMO D3 — CATÁLOGO Y BÚSQUEDA EN TIEMPO REAL
**⏱ 2 minutos**

---

*(Navegar a `/courses`)*

Esta es la página de catálogo. Los cursos se cargan desde MongoDB al montar la página.

Ahora voy a escribir en el buscador.

*(Escribir una palabra en el campo de búsqueda)*

Fijaos: los resultados se filtran **mientras escribo**, sin hacer ninguna petición al servidor. Esto es la var computada `filtered_courses` que vimos en el código: se recalcula en Python cada vez que cambia `search_query`, y Reflex sincroniza el resultado con la UI automáticamente.

Si borro el texto, vuelven todos los cursos. Cero latencia, cero llamadas al servidor.

También podemos filtrar por categoría. Las categorías se gestionan desde el panel de administrador y se cargan dinámicamente.

---

---

# DEMO D4 — VISOR DE CURSO (EXPERIENCIA ESTUDIANTE)
**⏱ 2 minutos**

---

*(Hacer clic en un curso)*

Esta es la página de detalle del curso. Si el estudiante no está inscrito, ve la información y el botón de inscripción.

*(Inscribirse en el curso o entrar a uno ya inscrito)*

Al estar inscrito, accedemos al **visor de curso**. La estructura es:

- **Sidebar izquierdo**: índice de lecciones. La lección actual está resaltada.
- **Panel central**: contenido de la lección activa.
- **Progreso**: cada lección visitada queda marcada como completada en MongoDB.

*(Navegar entre lecciones)*

Cambiar de lección actualiza el panel central instantáneamente. El progreso se guarda en la base de datos para que el estudiante pueda retomarlo desde cualquier dispositivo.

---

---

# DEMO D5 — DASHBOARD INSTRUCTOR Y CRUD DE CURSOS
**⏱ 3 minutos**

---

*(Cerrar sesión y volver a iniciar como instructor)*

Iniciamos sesión como **instructor**. El sistema nos redirige a `/instructor/dashboard` automáticamente —mismo código de login, distinta redirección según el rol.

*(Mostrar el dashboard de instructor)*

El dashboard muestra los cursos propios del instructor y sus KPIs: alumnos inscritos, ingresos, valoraciones.

Vamos a **crear un nuevo curso**.

*(Hacer clic en "Nuevo Curso")*

El formulario maneja tanto la creación como la edición. El flag `is_editing` distingue los dos modos —cuando es `False`, al guardar se crea un documento nuevo en MongoDB y se vincula al instructor con `$addToSet`, que garantiza no añadir duplicados de forma atómica.

*(Rellenar el formulario y guardar)*

El curso aparece en la lista inmediatamente. Ahora vamos a **editarlo**.

*(Hacer clic en editar)*

El mismo formulario se reutiliza. `is_editing` es `True`, así que al guardar se ejecuta `update_one` en lugar de `insert_one`.

Por último, el **dialog de confirmación** antes de eliminar: evita borrados accidentales. Es un componente de Reflex (`rx.alert_dialog`) sin JavaScript.

---

---

# DEMO D6 — DASHBOARD ADMINISTRADOR
**⏱ 2 minutos**

---

*(Cerrar sesión e iniciar como administrador)*

El administrador llega a `/admin/dashboard`. Las estadísticas globales se inyectan desde MongoDB en tiempo de carga: total de usuarios, cursos, inscripciones activas. Nada hardcodeado.

*(Mostrar secciones del panel)*

Desde aquí el administrador puede:

- **Gestionar usuarios**: ver todos los usuarios, cambiar roles, desactivar cuentas.
- **Gestionar cursos**: visibilidad global de todo el catálogo, poder editar o eliminar cualquier curso.
- **Gestionar categorías**: añadir, editar o eliminar las categorías que aparecen en el filtro del catálogo. Cualquier cambio aquí se refleja inmediatamente en la página pública.

Toda esta gestión está en Python puro, sin ningún panel de administración externo.

---

---

# DEMO D7 — PROTECCIÓN DE RUTAS POR ROL
**⏱ 1 minuto**

---

*(Con sesión de estudiante iniciada, intentar navegar manualmente a `/admin/dashboard`)*

Escribo directamente en la barra de direcciones `/admin/dashboard`.

El sistema muestra la **pantalla de acceso denegado** —no redirige, no crashea, simplemente renderiza el componente de error. Esto es `rx.cond(AuthState.is_user_admin, contenido_admin, pantalla_error)`.

*(Intentar `/instructor/dashboard` con cuenta de estudiante)*

Mismo resultado. La protección no es solo visual: los servicios de MongoDB tampoco ejecutan operaciones si el estado no tiene el rol correcto. Doble capa de seguridad.

---

---

# DEMO D8 — CONEXIÓN CÓDIGO PYTHON → UI
**⏱ 2 minutos**

---

*(Abrir el editor de código junto al navegador, o mostrar un fragmento de código en pantalla)*

Para cerrar, quiero mostrar directamente la conexión entre una línea de Python y lo que acabáis de ver.

Esta es la navbar:

```python
rx.cond(
    AuthState.is_authenticated,
    rx.menu.root(rx.menu.trigger(rx.text(AuthState.user_name)), ...),
    rx.hstack(rx.link("Iniciar Sesión"), rx.button("Registrarse"))
)
```

No hay HTML. No hay JavaScript. `rx.cond` en Python se compila a un componente React condicional. `AuthState.user_name` es una var reactiva que el framework sincroniza automáticamente.

Y este es el responsive design de la cuadrícula de cursos:

```python
rx.grid(
    columns=rx.breakpoints(initial="1", sm="2", md="3", lg="4"),
    gap="4",
)
```

Una línea genera los cuatro breakpoints de CSS. Lo que habría sido 20 líneas de media queries es una llamada a función en Python.

Eso resume el proyecto: **un lenguaje, una forma de pensar, una aplicación completa**.

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
*PARTE 1: ~1.950 palabras · ~15 minutos · Teórica*
*PARTE 2: ~1.950 palabras · ~15 minutos · Práctica (demo en vivo)*
*Módulos: DAW · FOL · EMPRESA e Iniciativa Emprendedora*
