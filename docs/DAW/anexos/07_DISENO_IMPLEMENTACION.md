# 7. DOCUMENTACIÓN DEL DISEÑO E IMPLEMENTACIÓN

## 7.1. Prototipos de la Aplicación

### 7.1.1. Wireframes Iniciales

Los wireframes se diseñaron en **Figma** durante la Fase 1 del proyecto para establecer la estructura visual antes del desarrollo.

#### Wireframe 1: Página de Inicio (Home)

```
┌──────────────────────────────────────────────────────────────┐
│  [LOGO] E-Learning JCB      [Cursos] [Instructores] [Login] │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│          🎓 Aprende con los Mejores Cursos Online           │
│                                                              │
│        Plataforma educativa con información transparente     │
│                                                              │
│              [Explorar Cursos] [Comenzar Gratis]            │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  Cursos Destacados                                          │
│                                                              │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐           │
│  │ Curso  │  │ Curso  │  │ Curso  │  │ Curso  │           │
│  │   1    │  │   2    │  │   3    │  │   4    │           │
│  │ ⭐ 4.8 │  │ ⭐ 4.9 │  │ ⭐ 4.7 │  │ ⭐ 5.0 │           │
│  └────────┘  └────────┘  └────────┘  └────────┘           │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  Footer: Sobre Nosotros | Contacto | Política Privacidad    │
└──────────────────────────────────────────────────────────────┘
```

**Decisiones de diseño**:
- Hero section con CTA claro ("Explorar Cursos")
- Grid de cursos destacados (4 columnas en desktop)
- Valoraciones visibles desde home
- Navegación simple en header

---

#### Wireframe 2: Listado de Cursos

```
┌──────────────────────────────────────────────────────────────┐
│  [LOGO] E-Learning JCB      [Cursos] [Instructores] [Login] │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Catálogo de Cursos                                         │
│                                                              │
│  [Buscar............................]  [🔍]                 │
│                                                              │
│  Filtros:                                                    │
│  ☐ Principiante  ☐ Intermedio  ☐ Avanzado                  │
│  [Categoría ▼]  [Duración ▼]  [Valoración ▼]               │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐    │
│  │ [IMG] Python para Principiantes          ⭐ 4.8     │    │
│  │                                         (127 reseñas)│    │
│  │ Aprende Python desde cero...                        │    │
│  │                                                      │    │
│  │ 👤 Juan Pérez | ⏱️ 12 horas | 📚 Principiante      │    │
│  │ 💰 99€                              [Ver Detalles]  │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ [IMG] JavaScript Avanzado             ⭐ 4.9        │    │
│  │                                         (89 reseñas) │    │
│  │ Domina JavaScript moderno...                        │    │
│  │ [...]                                                │    │
│  └─────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

**Decisiones de diseño**:
- Barra de búsqueda prominente
- Filtros horizontales para fácil acceso
- Cards de curso con información clave visible
- Valoración y número de reseñas para confianza

---

#### Wireframe 3: Detalle de Curso

```
┌──────────────────────────────────────────────────────────────┐
│  [LOGO] E-Learning JCB      [Cursos] [Instructores] [Login] │
├──────────────────────────────────────────────────────────────┤
│  Home > Cursos > Python para Principiantes                   │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────┐  Python para Principiantes            │
│  │                 │                                         │
│  │   [IMAGEN]      │  ⭐⭐⭐⭐⭐ 4.8 (127 valoraciones)      │
│  │   DEL CURSO     │                                         │
│  │                 │  👤 Instructor: Juan Pérez              │
│  │                 │  ⏱️ Duración: 12 horas                  │
│  └─────────────────┘  📚 Nivel: Principiante                │
│                       💰 99€    [Inscribirse Ahora]         │
│                                                              │
│  Descripción                                                 │
│  ────────────────────────────────────────────────────────   │
│  Aprende Python desde cero con este curso completo...       │
│  [Texto completo de descripción]                            │
│                                                              │
│  ¿Qué aprenderás?                                           │
│  ────────────────────────────────────────────────────────   │
│  ✓ Variables y tipos de datos                               │
│  ✓ Estructuras de control                                   │
│  ✓ Funciones y módulos                                      │
│  [...]                                                       │
│                                                              │
│  Contenido del Curso (Secciones y Lecciones)                │
│  ────────────────────────────────────────────────────────   │
│  ▼ Sección 1: Introducción a Python (3 lecciones, 1.5h)    │
│     1. ¿Qué es Python? (15 min)                             │
│     2. Instalación de Python (30 min)                       │
│     3. Primer programa (45 min)                             │
│                                                              │
│  ▼ Sección 2: Variables y Tipos de Datos (5 lecciones, 2h) │
│     1. Variables en Python (20 min)                         │
│     2. Tipos de datos básicos (30 min)                      │
│     [...]                                                    │
│                                                              │
│  Reseñas de Estudiantes                                     │
│  ────────────────────────────────────────────────────────   │
│  ⭐⭐⭐⭐⭐ María López - "Excelente curso para empezar"     │
│  "Me encantó la claridad de las explicaciones..."           │
│                                                              │
│  ⭐⭐⭐⭐ Carlos Ruiz - "Muy bueno"                          │
│  "Buen contenido, aunque algo largo..."                     │
└──────────────────────────────────────────────────────────────┘
```

**Decisiones de diseño**:
- **Información clave arriba**: Valoración, instructor, duración visible sin scroll
- **Botón CTA prominente**: "Inscribirse Ahora" bien visible
- **Contenido desplegable**: Secciones y lecciones completamente visibles (diferenciador clave)
- **Reseñas verificadas**: Mostrar feedback real de estudiantes

---

### 7.1.2. Mockups de Alta Fidelidad

Los mockups finales incorporan el diseño de **Chakra UI** con colores y estilos definitivos:

#### Paleta de Colores

```
Colores Principales:
- Primary:   #3182CE (Azul)
- Secondary: #2D3748 (Gris oscuro)
- Success:   #38A169 (Verde)
- Warning:   #DD6B20 (Naranja)
- Error:     #E53E3E (Rojo)

Colores de Fondo:
- Background: #FFFFFF (Blanco)
- Gray.50:    #F7FAFC (Gris muy claro)
- Gray.100:   #EDF2F7 (Gris claro)
```

#### Tipografía

```
Familia: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif

Tamaños:
- Heading 1: 36px (2xl)
- Heading 2: 30px (xl)
- Heading 3: 24px (lg)
- Body:      16px (md)
- Small:     14px (sm)
```

---

## 7.2. Diseño de Interfaces

### 7.2.1. Componentes Principales

#### CourseCard (Tarjeta de Curso)

**Archivo**: `E_Learning_JCB_Reflex/components/course_card.py`

**Descripción**: Componente reutilizable para mostrar información resumida de un curso

**Propiedades**:
- `course`: Objeto con datos del curso (título, descripción, valoración, precio)
- `show_instructor`: Boolean para mostrar/ocultar instructor

**Estructura Visual**:
```
┌─────────────────────────────────┐
│ [Imagen del curso]              │
│                                 │
├─────────────────────────────────┤
│ Título del Curso                │
│ ⭐⭐⭐⭐ 4.5 (23 reseñas)       │
│                                 │
│ Descripción breve del curso     │
│ que se trunca a 2 líneas...     │
│                                 │
│ 👤 Instructor                   │
│ ⏱️ 10 horas | 📚 Intermedio    │
│                                 │
│ 💰 99€          [Ver Detalles] │
└─────────────────────────────────┘
```

**Implementación** (pseudocódigo):
```python
def course_card(course: Course, show_instructor: bool = True) -> rx.Component:
    return rx.box(
        rx.image(src=course.image_url),
        rx.vstack(
            rx.heading(course.title),
            rx.hstack(
                rx.icon("star"),
                rx.text(f"{course.rating} ({course.num_ratings} reseñas)")
            ),
            rx.text(course.short_description),
            rx.hstack(
                rx.text(f"⏱️ {course.duration_hours}h"),
                rx.badge(course.level)
            ),
            rx.hstack(
                rx.text(f"{course.price}€"),
                rx.button("Ver Detalles", on_click=...)
            )
        ),
        border_width="1px",
        border_radius="md",
        overflow="hidden"
    )
```

---

#### Navbar (Barra de Navegación)

**Archivo**: `E_Learning_JCB_Reflex/components/navbar.py`

**Descripción**: Navegación principal de la aplicación

**Estructura**:
```
┌────────────────────────────────────────────────────────────┐
│ [LOGO] E-Learning JCB   [Cursos] [Instructores]  [Login]  │
└────────────────────────────────────────────────────────────┘
```

**Estados**:
- **Usuario no autenticado**: Mostrar "Login" y "Registrarse"
- **Usuario autenticado**: Mostrar avatar + dropdown con "Perfil", "Dashboard", "Logout"

**Responsive**:
- Desktop (>768px): Navegación horizontal
- Mobile (<768px): Menú hamburguesa

---

### 7.2.2. Páginas Principales

#### Página de Login

**Ruta**: `/login`

**Componentes**:
- Formulario centrado con:
  - Campo email (validación de formato)
  - Campo contraseña (tipo password)
  - Checkbox "Recordarme"
  - Botón "Iniciar Sesión"
  - Link "¿Olvidaste tu contraseña?" (futuro)
  - Link "¿No tienes cuenta? Regístrate"

**Validaciones**:
- Email con formato válido (@, .)
- Contraseña no vacía
- Feedback de error si credenciales incorrectas

**Flujo**:
1. Usuario ingresa email y contraseña
2. Click en "Iniciar Sesión"
3. Validación client-side
4. Petición a `AuthState.handle_login()`
5. Si OK: Redirigir a dashboard según rol
6. Si error: Mostrar mensaje de error

---

#### Dashboard de Estudiante

**Ruta**: `/student/dashboard`

**Protección**: `@require_role(["student"])`

**Secciones**:
1. **Resumen**: Cursos inscritos, completados, en progreso
2. **Mis Cursos**: Grid de cursos con barra de progreso
3. **Recomendaciones**: Cursos sugeridos (basados en inscripciones)
4. **Actividad Reciente**: Últimas lecciones completadas

**Ejemplo Visual**:
```
┌─────────────────────────────────────────────────────────┐
│ Dashboard de Estudiante - Hola, María                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐                  │
│ │   3     │ │   1     │ │   2     │                  │
│ │ Inscritos│ │Completado│ │En Progreso│                │
│ └─────────┘ └─────────┘ └─────────┘                  │
│                                                         │
│ Mis Cursos                                             │
│ ┌────────────────────────────────┐                    │
│ │ Python para Principiantes      │                    │
│ │ ████████░░ 80% completado       │                    │
│ └────────────────────────────────┘                    │
│                                                         │
│ ┌────────────────────────────────┐                    │
│ │ JavaScript Avanzado             │                    │
│ │ ██████░░░░ 60% completado       │                    │
│ └────────────────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

---

## 7.3. Diseño Lógico - Diagramación UML

### 7.3.1. Diagrama de Casos de Uso

```
                        E-Learning JCB Platform
┌──────────────────────────────────────────────────────────┐
│                                                          │
│   Estudiante                   Instructor          Admin│
│      │                            │                  │   │
│      │  (Buscar cursos)           │                  │   │
│      ├────────────────┐           │                  │   │
│      │                │           │                  │   │
│      │  (Inscribirse) │    (Crear curso)             │   │
│      ├────────────────┼───────────────┐              │   │
│      │                │               │              │   │
│      │  (Ver progreso)│    (Editar curso)     (Gestionar)│
│      ├────────────────┤               │         (usuarios)│
│      │                │    (Ver estadísticas)        │   │
│      │  (Valorar      │               │              │   │
│      │   curso)       │               │              │   │
│      │                │               │              │   │
│      │  (Completar    │               │              │   │
│      │   lección)     │               │              │   │
│                                                          │
└──────────────────────────────────────────────────────────┘

Actores:
- Estudiante: Usuario que consume cursos
- Instructor: Usuario que crea y gestiona cursos
- Admin: Usuario con permisos completos
```

**Casos de Uso Principales**:

| Actor | Caso de Uso | Descripción |
|-------|-------------|-------------|
| **Estudiante** | Buscar cursos | Buscar cursos por título, categoría, nivel |
| | Inscribirse en curso | Matricularse en un curso específico |
| | Ver progreso | Consultar progreso en cursos inscritos |
| | Completar lección | Marcar lección como completada |
| | Valorar curso | Dejar valoración y reseña de curso |
| **Instructor** | Crear curso | Crear curso con secciones y lecciones |
| | Editar curso | Modificar información de curso existente |
| | Eliminar curso | Borrar curso propio |
| | Ver estadísticas | Consultar inscripciones, valoraciones |
| **Admin** | Gestionar usuarios | Ver, editar, eliminar usuarios |
| | Moderar contenido | Revisar y aprobar cursos |
| | Ver reportes | Estadísticas globales del sistema |

---

### 7.3.2. Diagrama de Clases

```
┌─────────────────────────────────────┐
│           User                      │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - name: str                         │
│ - email: str (unique)               │
│ - password: str (hashed)            │
│ - role: str (admin|instructor|student)│
│ - bio: str (optional)               │
│ - created_at: datetime              │
├─────────────────────────────────────┤
│ + is_admin() -> bool                │
│ + is_instructor() -> bool           │
│ + is_student() -> bool              │
│ + to_dict() -> dict                 │
│ + from_dict(data) -> User           │
└─────────────────────────────────────┘
           ▲
           │ 1
           │ instructs
           │
           │ *
┌─────────────────────────────────────┐
│           Course                    │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - title: str                        │
│ - description: str                  │
│ - instructor_id: ObjectId           │
│ - level: str (beginner|intermediate|advanced)│
│ - duration_hours: float             │
│ - price: float                      │
│ - image_url: str                    │
│ - sections: List[Section]           │
│ - created_at: datetime              │
├─────────────────────────────────────┤
│ + get_total_lessons() -> int        │
│ + get_average_rating() -> float     │
│ + to_dict() -> dict                 │
│ + from_dict(data) -> Course         │
└─────────────────────────────────────┘
           │ 1
           │ has
           │
           │ *
┌─────────────────────────────────────┐
│          Section                    │
├─────────────────────────────────────┤
│ - title: str                        │
│ - description: str                  │
│ - order: int                        │
│ - lessons: List[Lesson]             │
├─────────────────────────────────────┤
│ + get_duration() -> float           │
│ + to_dict() -> dict                 │
└─────────────────────────────────────┘
           │ 1
           │ contains
           │
           │ *
┌─────────────────────────────────────┐
│          Lesson                     │
├─────────────────────────────────────┤
│ - title: str                        │
│ - content: str                      │
│ - duration_minutes: int             │
│ - order: int                        │
│ - video_url: str (optional)         │
├─────────────────────────────────────┤
│ + to_dict() -> dict                 │
└─────────────────────────────────────┘


┌─────────────────────────────────────┐
│        Enrollment                   │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - user_id: ObjectId                 │
│ - course_id: ObjectId               │
│ - enrolled_at: datetime             │
│ - completed: bool                   │
├─────────────────────────────────────┤
│ + to_dict() -> dict                 │
│ + from_dict(data) -> Enrollment     │
└─────────────────────────────────────┘
        │                    │
        │ *                  │ *
        │                    │
   ┌────┴───┐         ┌─────┴────┐
   │  User  │         │  Course  │
   └────────┘         └──────────┘


┌─────────────────────────────────────┐
│         Progress                    │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - enrollment_id: ObjectId           │
│ - lesson_id: str                    │
│ - completed_at: datetime            │
├─────────────────────────────────────┤
│ + to_dict() -> dict                 │
└─────────────────────────────────────┘
        │ *
        │ tracks
        │ 1
┌───────┴─────────────────────────────┐
│        Enrollment                   │
└─────────────────────────────────────┘


┌─────────────────────────────────────┐
│          Rating                     │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - user_id: ObjectId                 │
│ - course_id: ObjectId               │
│ - rating: int (1-5)                 │
│ - review: str (optional)            │
│ - created_at: datetime              │
├─────────────────────────────────────┤
│ + to_dict() -> dict                 │
│ + from_dict(data) -> Rating         │
└─────────────────────────────────────┘
        │ *              │ *
        │                │
   ┌────┴───┐     ┌─────┴────┐
   │  User  │     │  Course  │
   └────────┘     └──────────┘
```

**Relaciones**:
- Un **User** puede ser instructor de muchos **Courses** (1:N)
- Un **Course** tiene muchas **Sections** (1:N, embebido)
- Una **Section** tiene muchas **Lessons** (1:N, embebido)
- Un **User** puede tener muchos **Enrollments** (1:N)
- Un **Course** puede tener muchos **Enrollments** (1:N)
- Un **Enrollment** tiene muchos **Progress** (1:N)
- Un **User** puede dejar muchos **Ratings** (1:N)
- Un **Course** puede tener muchos **Ratings** (1:N)

---

### 7.3.3. Diagrama de Secuencia: Inscripción a Curso

```
Usuario    CourseDetailPage   EnrollmentState   EnrollmentService   MongoDB
  │              │                  │                  │              │
  │  Click       │                  │                  │              │
  │ "Inscribirse"│                  │                  │              │
  ├─────────────>│                  │                  │              │
  │              │ handle_enroll()  │                  │              │
  │              ├─────────────────>│                  │              │
  │              │                  │ enroll_student() │              │
  │              │                  ├─────────────────>│              │
  │              │                  │                  │ Verificar    │
  │              │                  │                  │ duplicado    │
  │              │                  │                  ├─────────────>│
  │              │                  │                  │<─────────────┤
  │              │                  │                  │  No existe   │
  │              │                  │                  │              │
  │              │                  │                  │ INSERT       │
  │              │                  │                  │ enrollment   │
  │              │                  │                  ├─────────────>│
  │              │                  │                  │<─────────────┤
  │              │                  │                  │   OK         │
  │              │                  │<─────────────────┤              │
  │              │                  │     True         │              │
  │              │<─────────────────┤                  │              │
  │              │   Success        │                  │              │
  │<─────────────┤                  │                  │              │
  │ Mostrar      │                  │                  │              │
  │ "Inscrito"   │                  │                  │              │
  │ + Redirigir  │                  │                  │              │
  │              │                  │                  │              │
```

**Descripción del flujo**:
1. Usuario hace click en botón "Inscribirse" en página de detalle de curso
2. Evento se captura en `CourseDetailPage` y llama a `EnrollmentState.handle_enroll()`
3. Estado llama a `EnrollmentService.enroll_student(user_id, course_id)`
4. Servicio verifica en MongoDB si ya existe inscripción (evitar duplicados)
5. Si no existe, inserta nuevo documento en colección `enrollments`
6. MongoDB retorna confirmación
7. Servicio retorna `True` al estado
8. Estado actualiza UI mostrando "Inscrito exitosamente"
9. Usuario es redirigido a dashboard de estudiante

---

### 7.3.4. Diagrama de Actividades: Crear Curso Completo

```
      ┌─────────┐
      │ Inicio  │
      └────┬────┘
           │
           ▼
    ┌──────────────┐
    │ Login como   │
    │ Instructor   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐      No    ┌──────────┐
    │ ¿Autenticado?├────────────>│ Redirigir│
    │              │             │ a /login │
    └──────┬───────┘             └──────────┘
           │ Sí
           ▼
    ┌──────────────┐
    │ Ir a /instructor│
    │ /courses/new │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Completar    │
    │ formulario   │
    │ de curso     │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐      No    ┌──────────┐
    │ ¿Datos       ├────────────>│ Mostrar  │
    │ válidos?     │             │ errores  │
    └──────┬───────┘             └────┬─────┘
           │ Sí                       │
           ▼                          │
    ┌──────────────┐                 │
    │ Guardar curso│<────────────────┘
    │ en BD        │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Añadir       │
    │ Sección 1    │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Añadir       │
    │ Lección 1.1  │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐      Sí    ┌──────────┐
    │ ¿Más         ├────────────>│ Añadir   │
    │ lecciones?   │             │ lección  │
    └──────┬───────┘             └────┬─────┘
           │ No                       │
           ▼                          │
    ┌──────────────┐                 │
    │ ¿Más         │<────────────────┘
    │ secciones?   │
    └──────┬───────┘
           │ No
           ▼
    ┌──────────────┐
    │ Publicar     │
    │ curso        │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Curso visible│
    │ en catálogo  │
    └──────┬───────┘
           │
           ▼
      ┌─────────┐
      │   Fin   │
      └─────────┘
```

---

## 7.4. Descripción Modular del Software

### 7.4.1. Arquitectura en Capas

La aplicación sigue una **arquitectura en capas** con separación clara de responsabilidades:

```
┌─────────────────────────────────────────────────────────┐
│                 CAPA DE PRESENTACIÓN                    │
│         (Pages: index.py, courses.py, login.py...)      │
│              Renderizado de UI al usuario               │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              CAPA DE LÓGICA DE UI                       │
│    (States: CourseState, AuthState, EnrollmentState)    │
│       Gestión de estado reactivo y eventos de usuario   │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│            CAPA DE LÓGICA DE NEGOCIO                    │
│ (Services: CourseService, UserService, EnrollmentService)│
│          Operaciones CRUD y validaciones                │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              CAPA DE MODELOS                            │
│      (Models: User, Course, Enrollment, Progress)       │
│         Definición de entidades y validaciones          │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│            CAPA DE ACCESO A DATOS                       │
│         (Database: mongodb.py con Motor driver)         │
│           Conexión y operaciones en MongoDB             │
└─────────────────────────────────────────────────────────┘
```

**Ventajas de esta arquitectura**:
- ✅ Separación de responsabilidades (cada capa tiene una función clara)
- ✅ Testabilidad (cada capa puede probarse independientemente)
- ✅ Mantenibilidad (cambios en una capa no afectan a otras)
- ✅ Escalabilidad (fácil añadir nuevas funcionalidades)

---

### 7.4.2. Módulos Principales

#### Módulo: models/

**Responsabilidad**: Definición de entidades de datos

**Archivos**:
- `user.py`: Modelo de usuario con roles
- `course.py`: Modelo de curso con secciones y lecciones
- `enrollment.py`: Modelo de inscripción
- `progress.py`: Modelo de progreso de estudiante
- `rating.py`: Modelo de valoraciones

**Ejemplo** (`user.py`):
```python
class User:
    def __init__(self, name: str, email: str, password: str, role: str = "student"):
        self.name = name
        self.email = email
        self.password = password  # Hashed con bcrypt
        self.role = role  # admin | instructor | student
        self.bio = ""
        self.created_at = datetime.now()

    def is_admin(self) -> bool:
        return self.role == "admin"

    def is_instructor(self) -> bool:
        return self.role == "instructor"

    def is_student(self) -> bool:
        return self.role == "student"
```

---

#### Módulo: services/

**Responsabilidad**: Lógica de negocio y operaciones CRUD

**Archivos**:
- `user_service.py`: CRUD de usuarios, autenticación
- `course_service.py`: CRUD de cursos
- `enrollment_service.py`: Gestión de inscripciones
- `progress_service.py`: Seguimiento de progreso
- `rating_service.py`: Gestión de valoraciones

**Ejemplo** (`enrollment_service.py`):
```python
class EnrollmentService:
    async def enroll_student(self, user_id: str, course_id: str) -> bool:
        # Verificar si ya está inscrito
        existing = await db.enrollments.find_one({
            "user_id": ObjectId(user_id),
            "course_id": ObjectId(course_id)
        })

        if existing:
            return False  # Ya inscrito

        # Crear inscripción
        enrollment = {
            "user_id": ObjectId(user_id),
            "course_id": ObjectId(course_id),
            "enrolled_at": datetime.now(),
            "completed": False
        }

        result = await db.enrollments.insert_one(enrollment)
        return result.inserted_id is not None
```

---

#### Módulo: states/

**Responsabilidad**: Gestión de estado reactivo de Reflex

**Archivos**:
- `auth_state.py`: Estado de autenticación (login, registro)
- `course_state.py`: Estado de listado de cursos
- `course_detail_state.py`: Estado de detalle de curso
- `enrollment_state.py`: Estado de inscripciones
- `student_dashboard_state.py`: Estado de dashboard

**Ejemplo** (`auth_state.py`):
```python
class AuthState(rx.State):
    is_authenticated: bool = False
    current_user: dict = {}
    error: str = ""
    success: str = ""

    async def handle_login(self, form_data: dict):
        email = form_data["email"]
        password = form_data["password"]

        # Llamar a servicio
        user = await UserService().login(email, password)

        if user:
            self.is_authenticated = True
            self.current_user = user
            self.success = "Login exitoso"
            return rx.redirect("/dashboard")
        else:
            self.error = "Credenciales incorrectas"
```

---

#### Módulo: pages/

**Responsabilidad**: Renderizado de páginas completas

**Archivos**:
- `index.py`: Página de inicio
- `courses.py`: Listado de cursos
- `course_detail.py`: Detalle de curso
- `login.py`: Página de login
- `register.py`: Página de registro
- `student_dashboard.py`: Dashboard de estudiante
- `instructor_dashboard.py`: Dashboard de instructor
- `admin_dashboard.py`: Dashboard de administrador

---

#### Módulo: components/

**Responsabilidad**: Componentes reutilizables de UI

**Archivos**:
- `navbar.py`: Barra de navegación
- `course_card.py`: Tarjeta de curso
- `instructor_card.py`: Tarjeta de instructor
- `section_list.py`: Lista de secciones con lecciones
- `protected.py`: Componentes de protección de rutas (RBAC)

---

#### Módulo: utils/

**Responsabilidad**: Utilidades reutilizables

**Archivos**:
- `password.py`: Hash y verificación de contraseñas (bcrypt)
- `route_helpers.py`: Generación de URLs
- `formatters.py`: Formato de fechas, números, duración
- `validators.py`: Validación de inputs (email, contraseña)

---

## 7.5. Diseño de Base de Datos

### 7.5.1. Esquema Lógico de MongoDB

MongoDB es una base de datos **NoSQL orientada a documentos**. Cada colección almacena documentos JSON.

#### Colección: `users`

**Descripción**: Usuarios de la plataforma (estudiantes, instructores, admins)

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "password": "$2b$12$hashedpassword...",
  "role": "instructor",  // admin | instructor | student
  "bio": "Desarrollador Python con 10 años de experiencia",
  "created_at": ISODate("2025-11-01T10:00:00Z")
}
```

**Índices**:
- `email`: Único (asegurar emails únicos)
- `role`: Normal (consultas frecuentes por rol)

---

#### Colección: `courses`

**Descripción**: Cursos disponibles en la plataforma

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "title": "Python para Principiantes",
  "description": "Aprende Python desde cero...",
  "instructor_id": ObjectId("..."),  // Referencia a users
  "level": "beginner",  // beginner | intermediate | advanced
  "duration_hours": 12.5,
  "price": 99.0,
  "image_url": "https://example.com/images/python-course.jpg",
  "sections": [
    {
      "title": "Introducción a Python",
      "description": "Primeros pasos con Python",
      "order": 1,
      "lessons": [
        {
          "title": "¿Qué es Python?",
          "content": "Python es un lenguaje...",
          "duration_minutes": 15,
          "order": 1,
          "video_url": "https://example.com/videos/lesson1.mp4"
        },
        {
          "title": "Instalación de Python",
          "content": "Para instalar Python...",
          "duration_minutes": 30,
          "order": 2
        }
      ]
    },
    {
      "title": "Variables y Tipos de Datos",
      "description": "Fundamentos de variables",
      "order": 2,
      "lessons": [ /* ... */ ]
    }
  ],
  "created_at": ISODate("2025-11-05T14:30:00Z")
}
```

**Índices**:
- `instructor_id`: Normal (consultas de cursos por instructor)
- `title`: Texto (búsqueda full-text)
- `level`: Normal (filtrado por nivel)

**Nota**: Secciones y lecciones están **embebidas** (no en colecciones separadas) porque:
- Siempre se consultan juntas
- No se consultan independientemente
- Mejora el rendimiento (1 query vs múltiples)

---

#### Colección: `enrollments`

**Descripción**: Inscripciones de estudiantes a cursos

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "user_id": ObjectId("..."),  // Referencia a users
  "course_id": ObjectId("..."),  // Referencia a courses
  "enrolled_at": ISODate("2025-11-10T09:15:00Z"),
  "completed": false
}
```

**Índices**:
- `user_id, course_id`: Compuesto y único (prevenir inscripciones duplicadas)
- `user_id`: Normal (consultas de inscripciones por usuario)
- `course_id`: Normal (consultas de inscripciones por curso)

---

#### Colección: `progress`

**Descripción**: Progreso de estudiantes en lecciones

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "enrollment_id": ObjectId("..."),  // Referencia a enrollments
  "lesson_id": "section_0_lesson_1",  // Identificador de lección (string)
  "completed_at": ISODate("2025-11-11T16:45:00Z")
}
```

**Índices**:
- `enrollment_id`: Normal (consultas de progreso por inscripción)
- `enrollment_id, lesson_id`: Compuesto y único (prevenir duplicados)

**Nota**: `lesson_id` es un string (no ObjectId) porque las lecciones están embebidas en cursos

---

#### Colección: `ratings`

**Descripción**: Valoraciones y reseñas de cursos

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "user_id": ObjectId("..."),  // Referencia a users
  "course_id": ObjectId("..."),  // Referencia a courses
  "rating": 5,  // 1-5 estrellas
  "review": "Excelente curso, muy claro y didáctico",
  "created_at": ISODate("2025-11-12T12:00:00Z")
}
```

**Índices**:
- `course_id`: Normal (consultas de valoraciones por curso)
- `user_id, course_id`: Compuesto y único (un usuario solo puede valorar un curso una vez)

---

### 7.5.2. Diagrama Entidad-Relación (Adaptado a MongoDB)

```
┌─────────────┐          ┌──────────────┐          ┌─────────────┐
│    users    │          │   courses    │          │ enrollments │
├─────────────┤          ├──────────────┤          ├─────────────┤
│ _id (PK)    │1───────N │ instructor_id│          │ _id (PK)    │
│ name        │          │ (FK)         │          │ user_id (FK)│
│ email       │          │ title        │N───────1 │ course_id   │
│ password    │          │ description  │          │ (FK)        │
│ role        │          │ sections[]   │          │ enrolled_at │
│ bio         │          │   ├─lessons[]│          │ completed   │
│ created_at  │          │ level        │          └─────────────┘
└─────────────┘          │ duration_h   │                │
      │                  │ price        │                │1
      │                  │ image_url    │                │
      │1                 │ created_at   │                │
      │                  └──────────────┘                │N
      │                        │                  ┌──────────────┐
      │                        │1                 │   progress   │
      │                        │                  ├──────────────┤
      │                        │                  │ _id (PK)     │
      │                        │N                 │ enrollment_id│
      │                  ┌─────────────┐          │ (FK)         │
      │                  │   ratings   │          │ lesson_id    │
      │                  ├─────────────┤          │ completed_at │
      └────────────────N │ user_id (FK)│          └──────────────┘
                         │ course_id   │
                         │ (FK)        │
                         │ rating      │
                         │ review      │
                         │ created_at  │
                         └─────────────┘
```

**Relaciones**:
- Un **user** puede instruir muchos **courses** (1:N)
- Un **user** puede tener muchos **enrollments** (1:N)
- Un **course** puede tener muchos **enrollments** (1:N)
- Un **enrollment** puede tener muchos **progress** (1:N)
- Un **user** puede tener muchos **ratings** (1:N)
- Un **course** puede tener muchos **ratings** (1:N)

---

### 7.5.3. Consultas Más Frecuentes y Optimización

| Consulta | Frecuencia | Índice Utilizado | Tiempo Estimado |
|----------|------------|------------------|-----------------|
| **Listado de cursos** | Alta | `_id` (implícito) | <50ms |
| **Buscar cursos por texto** | Alta | `title` (texto) | <100ms |
| **Filtrar cursos por nivel** | Media | `level` | <50ms |
| **Cursos de un instructor** | Media | `instructor_id` | <50ms |
| **Verificar inscripción** | Alta | `user_id, course_id` (compuesto) | <30ms |
| **Progreso de estudiante** | Alta | `enrollment_id` | <50ms |
| **Valoraciones de curso** | Media | `course_id` | <50ms |
| **Calcular promedio de valoraciones** | Media | Agregación MongoDB | <100ms |

**Optimizaciones implementadas**:
1. ✅ Índices en campos de consulta frecuente
2. ✅ Índices compuestos para consultas complejas
3. ✅ Proyecciones para devolver solo campos necesarios
4. ✅ Agregaciones para cálculos complejos (promedio de rating)
5. ✅ Secciones y lecciones embebidas (evita JOINs)

---

## 7.6. Otras Estructuras de Datos Utilizadas

### 7.6.1. Estados de Reflex (Client-Side)

Reflex gestiona estados reactivos en el cliente que se sincronizan automáticamente con el servidor:

**Ejemplo**: `CourseState`
```python
class CourseState(rx.State):
    courses: list[dict] = []  # Lista de cursos
    loading: bool = False     # Estado de carga
    error: str = ""           # Mensaje de error
    search_query: str = ""    # Búsqueda actual
    filter_level: str = "all" # Filtro de nivel
```

**Ventajas**:
- Reactividad automática (cambios en estado actualizan UI)
- Sin necesidad de Redux/Context API
- Tipado fuerte con Python type hints

---

### 7.6.2. Caché de Sesión

Reflex almacena datos de sesión en **cookies** cifradas:

**Datos almacenados**:
- `is_authenticated`: Boolean
- `current_user`: Diccionario con datos de usuario
- `session_id`: Token único de sesión

**Ventajas**:
- Persistencia entre recargas de página
- Seguridad (cookies HTTP-only, cifradas)
- Fácil gestión (Reflex lo maneja automáticamente)

---

## 7.7. Estudio de Seguridad de la Aplicación

### 7.7.1. Medidas de Seguridad Implementadas

#### 1. Autenticación Segura

**Hash de Contraseñas con bcrypt**

```python
import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)  # 2^12 = 4,096 iteraciones
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )
```

**Características**:
- ✅ Salt único por contraseña (resistente a rainbow tables)
- ✅ 12 rounds (4,096 iteraciones, balance seguridad/rendimiento)
- ✅ Algoritmo bcrypt (diseñado para ser lento, resistente a brute force)

---

#### 2. Control de Acceso Basado en Roles (RBAC)

**Componentes de Protección** (`components/protected.py`):

```python
def require_auth(component):
    """Requiere autenticación"""
    def wrapper(state):
        if not state.is_authenticated:
            return rx.redirect("/login")
        return component(state)
    return wrapper

def require_role(allowed_roles: list[str]):
    """Requiere rol específico"""
    def decorator(component):
        def wrapper(state):
            if not state.is_authenticated:
                return rx.redirect("/login")
            if state.current_user.get("role") not in allowed_roles:
                return rx.text("Acceso denegado")
            return component(state)
        return wrapper
    return decorator

def admin_only(component):
    """Solo administradores"""
    return require_role(["admin"])(component)
```

**Uso**:
```python
@admin_only
def admin_dashboard():
    return rx.box(...)
```

---

#### 3. Validación de Inputs

**Client-Side** (Reflex States):
```python
def validate_email(email: str) -> bool:
    return "@" in email and "." in email

def validate_password(password: str) -> bool:
    return len(password) >= 6 and len(password) <= 128
```

**Server-Side** (Services):
```python
async def create_user(self, user_data: dict) -> bool:
    # Validar datos
    if not user_data.get("email") or not validate_email(user_data["email"]):
        return False

    # Verificar email único
    existing = await db.users.find_one({"email": user_data["email"]})
    if existing:
        return False

    # Hashear contraseña
    user_data["password"] = hash_password(user_data["password"])

    # Insertar
    result = await db.users.insert_one(user_data)
    return result.inserted_id is not None
```

---

#### 4. Protección contra Inyección NoSQL

MongoDB + Motor utiliza **queries parametrizadas** que previenen inyecciones:

**✅ Seguro** (recomendado):
```python
user = await db.users.find_one({"email": email})
```

**❌ Inseguro** (NUNCA usar):
```python
# NO HACER - vulnerable a inyección
query = f"db.users.find({{email: '{email}'}})"
```

**Motor sanitiza automáticamente** las queries, por lo que no es posible inyectar código malicioso.

---

#### 5. Cifrado de Comunicaciones

**TLS/SSL** (HTTPS):
- ✅ MongoDB Atlas usa TLS 1.2+ (cifrado en tránsito)
- ✅ Reflex Cloud proporciona HTTPS automático
- ✅ Certificados Let's Encrypt gratuitos

**Cifrado en Reposo**:
- ✅ MongoDB Atlas cifra datos en disco (AES-256)
- ✅ Backups automáticos cifrados

---

### 7.7.2. Matriz Completa de Seguridad

Referencia completa en [Anexo - Análisis de Seguridad Completo] (Sección 2.2 de documento previo generado por agente Explore).

**Resumen**:
- ✅ 11 fortalezas implementadas
- ⚠️ 3 parcialmente implementadas
- ❌ 6 no implementadas (planificadas para post-v1.0)

**Nivel de madurez de seguridad**: **INTERMEDIO** (adecuado para MVP)

---

### 7.7.3. Plan de Mejoras de Seguridad (Roadmap)

| Mejora | Prioridad | Esfuerzo | Versión Planificada |
|--------|-----------|----------|---------------------|
| **Rate limiting** en login | Alta | 8h | v1.1 (Q3 2026) |
| **Expiración de sesión** (24h inactividad) | Alta | 6h | v1.1 |
| **Recuperación de contraseña** por email | Media | 16h | v1.2 (Q4 2026) |
| **Two-Factor Authentication (2FA)** | Baja | 24h | v2.0 (2027) |
| **Auditoría de cambios** (logs) | Media | 12h | v1.2 |
| **Sanitización HTML explícita** | Baja | 4h | v1.1 |

---

**Conclusión Sección 7**: El diseño e implementación de E-Learning JCB Platform sigue principios sólidos de arquitectura de software (separación de capas, modularidad, reutilización). Los diagramas UML proporcionan una visión clara de la estructura y flujos del sistema. El diseño de base de datos MongoDB está optimizado para las consultas más frecuentes. Las medidas de seguridad implementadas son adecuadas para un MVP, con plan de mejoras para versiones futuras.

---

<div style="page-break-after: always;"></div>
