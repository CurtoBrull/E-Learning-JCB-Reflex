# 5. PLANIFICACIÓN TEMPORAL DEL DESARROLLO

## 5.1. Cronograma General del Proyecto

### 5.1.1. Duración Total y Fases Principales

**Fecha de inicio**: Noviembre 2025
**Fecha de entrega**: Mayo 2026
**Duración total**: 26 semanas (6 meses)

El proyecto se estructura en **9 fases principales** con objetivos y entregables específicos:

```
Noviembre 2025          Diciembre 2025          Enero 2026              Febrero 2026
│                       │                       │                       │
├─ FASE 1: Config.      ├─ FASE 2: Cursos      ├─ FASE 3: Instructores├─ FASE 5: Autenticación
│  (Semanas 1-2)        │  (Semanas 3-5)        │  (Semanas 6-7)        │  (Semanas 9-12)
│                       │                       ├─ FASE 4: Refactor.   │
│                       │                       │  (Semana 8)           │

Marzo 2026              Abril 2026              Mayo 2026
│                       │                       │
├─ FASE 6: Inscripciones├─ FASE 7: Panel Instr.├─ FASE 8: Avanzadas
│  (Semanas 13-16)      │  (Semanas 17-20)      │  (Semanas 21-23)
│                       │                       ├─ FASE 9: Pruebas/Docs
│                       │                       │  (Semanas 24-26)
│                       │                       └─ DEFENSA (Última semana)
```

---

## 5.2. Detalle de Fases de Desarrollo

### FASE 1: Configuración Inicial y Análisis (Semanas 1-2)
**Fechas**: 3-16 Noviembre 2025
**Duración**: 2 semanas (40 horas)

#### Objetivos
- Configurar entorno de desarrollo completo
- Establecer conexión con MongoDB Atlas
- Definir estructura de proyecto
- Analizar requisitos en profundidad
- Crear diseño inicial de arquitectura

#### Tareas Detalladas

| Tarea | Descripción | Horas | Responsable |
|-------|-------------|-------|-------------|
| **1.1. Configuración de entorno** | | **8h** | |
| - Instalar Python 3.10+ | Configurar versión compatible | 1h | Desarrollador |
| - Crear entorno virtual | `python -m venv reflex-env` | 0.5h | Desarrollador |
| - Instalar Reflex | `pip install reflex==0.8.24` | 0.5h | Desarrollador |
| - Configurar VS Code | Extensions, Pylance, Black | 1h | Desarrollador |
| - Inicializar Git/GitHub | Repositorio, .gitignore, README | 1h | Desarrollador |
| - Configurar pre-commit hooks | Black, flake8, mypy | 2h | Desarrollador |
| - Documentar instalación | README con instrucciones | 2h | Desarrollador |
| **1.2. Configuración de MongoDB** | | **6h** | |
| - Crear cuenta MongoDB Atlas | Registro, verificación email | 0.5h | Desarrollador |
| - Crear cluster M0 gratuito | Configuración región EU-West | 1h | Desarrollador |
| - Configurar seguridad | IP whitelist, usuario BD | 1h | Desarrollador |
| - Instalar Motor driver | `pip install motor` | 0.5h | Desarrollador |
| - Crear conexión asíncrona | `database/mongodb.py` | 2h | Desarrollador |
| - Probar conexión | Script de test | 1h | Desarrollador |
| **1.3. Estructura del proyecto** | | **10h** | |
| - Definir arquitectura en capas | Carpetas: models, services, states, pages | 2h | Desarrollador |
| - Crear estructura de directorios | mkdir components, utils, etc. | 1h | Desarrollador |
| - Configurar rxconfig.py | Personalización Reflex | 2h | Desarrollador |
| - Definir convenciones de código | Docstrings, naming, imports | 2h | Desarrollador |
| - Crear archivos base | `__init__.py`, imports | 1h | Desarrollador |
| - Documentar estructura | Diagrama de carpetas | 2h | Desarrollador |
| **1.4. Análisis de requisitos** | | **12h** | |
| - Entrevistas con stakeholders | Estudiantes, instructores potenciales | 3h | Desarrollador |
| - Definir user stories | Formato "Como [rol], quiero [acción]" | 3h | Desarrollador |
| - Priorizar funcionalidades | MoSCoW (Must, Should, Could, Won't) | 2h | Desarrollador |
| - Diseñar wireframes | Figma: login, cursos, detalle | 3h | Desarrollador |
| - Documentar requisitos | Documento de especificaciones | 1h | Desarrollador |
| **1.5. Diseño de arquitectura** | | **4h** | |
| - Diagrama de arquitectura | Capas, flujo de datos | 2h | Desarrollador |
| - Definir modelos de datos | User, Course, Section, Lesson | 1h | Desarrollador |
| - Planificar API endpoints | REST-like con Reflex | 1h | Desarrollador |

#### Entregables
- ✅ Entorno de desarrollo funcional
- ✅ Conexión a MongoDB Atlas operativa
- ✅ Repositorio Git inicializado
- ✅ Documento de requisitos (10 user stories)
- ✅ Wireframes de 5 pantallas principales
- ✅ Diagrama de arquitectura

#### Criterios de Aceptación
- [ ] `reflex run` ejecuta sin errores
- [ ] Conexión a MongoDB Atlas exitosa (test script pasa)
- [ ] Git commits iniciales en GitHub
- [ ] Documento de requisitos aprobado por tutor

---

### FASE 2: Módulo de Cursos (Semanas 3-5)
**Fechas**: 17 Noviembre - 7 Diciembre 2025
**Duración**: 3 semanas (60 horas)

#### Objetivos
- Implementar modelos de datos para cursos
- Desarrollar servicios CRUD de cursos
- Crear interfaz de listado de cursos
- Implementar página de detalle de curso
- Sistema de secciones y lecciones

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **2.1. Modelos de datos** | | **10h** |
| - Modelo Course | Clase con validaciones | 3h |
| - Modelo Section | Estructura de secciones | 2h |
| - Modelo Lesson | Lecciones con duración | 2h |
| - Modelo Rating | Valoraciones de cursos | 2h |
| - Testing de modelos | Unit tests con pytest | 1h |
| **2.2. Servicios de cursos** | | **15h** |
| - CourseService.get_all_courses() | Listado con filtros | 3h |
| - CourseService.get_course_by_id() | Detalle con populate | 3h |
| - CourseService.create_course() | Inserción con validación | 3h |
| - CourseService.update_course() | Actualización parcial | 2h |
| - CourseService.delete_course() | Borrado lógico/físico | 2h |
| - Manejo de errores | Try-except, logging | 2h |
| **2.3. Estados de Reflex** | | **10h** |
| - CourseState (lista) | Estado para listado | 3h |
| - CourseDetailState | Estado para detalle | 3h |
| - Eventos de carga | handle_load_courses | 2h |
| - Variables computadas | Filtros, búsqueda | 2h |
| **2.4. Componentes UI** | | **12h** |
| - CourseCard | Card de curso reutilizable | 3h |
| - CourseList | Grid responsive de cards | 2h |
| - CourseDetail | Página de detalle completa | 4h |
| - SectionList | Acordeón de secciones | 2h |
| - LessonItem | Item de lección con duración | 1h |
| **2.5. Páginas** | | **8h** |
| - /courses (listado) | Página principal de cursos | 3h |
| - /course/[id] (detalle) | Enrutamiento dinámico | 3h |
| - Navegación (breadcrumbs) | Migas de pan | 2h |
| **2.6. Testing e integración** | | **5h** |
| - Unit tests servicios | Pytest async | 2h |
| - Integration tests | E2E con playwright (opcional) | 2h |
| - Corrección de bugs | Debugging | 1h |

#### Entregables
- ✅ 4 modelos de datos implementados
- ✅ 5 métodos de servicio CRUD
- ✅ 5 componentes UI reutilizables
- ✅ 2 páginas funcionales
- ✅ 15+ unit tests

#### Criterios de Aceptación
- [ ] Listado de cursos carga desde MongoDB
- [ ] Detalle de curso muestra secciones y lecciones
- [ ] Diseño responsive en móvil y desktop
- [ ] Tests pasan sin errores

---

### FASE 3: Módulo de Instructores (Semanas 6-7)
**Fechas**: 8-21 Diciembre 2025
**Duración**: 2 semanas (40 horas)

#### Objetivos
- Implementar modelo User con rol instructor
- Crear servicios de gestión de usuarios
- Desarrollar perfiles de instructores
- Listado de instructores con estadísticas

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **3.1. Modelo User** | | **8h** |
| - Diseño del modelo | Campos: name, email, role, bio | 2h |
| - Roles (enum) | admin, instructor, student | 1h |
| - Propiedades computadas | is_admin, is_instructor, is_student | 2h |
| - Validaciones | Email único, formato válido | 2h |
| - Testing | Unit tests | 1h |
| **3.2. UserService** | | **12h** |
| - get_user_by_id() | Recuperar usuario | 2h |
| - get_user_by_email() | Login lookup | 2h |
| - create_user() | Registro | 3h |
| - update_user() | Edición de perfil | 2h |
| - get_instructors() | Solo instructores | 2h |
| - get_instructor_stats() | Cursos, inscripciones | 1h |
| **3.3. Estados** | | **6h** |
| - InstructorState (listado) | Lista de instructores | 2h |
| - InstructorDetailState | Perfil + cursos | 3h |
| - Eventos de carga | Asíncronos | 1h |
| **3.4. Componentes** | | **8h** |
| - InstructorCard | Card con foto, bio, stats | 3h |
| - InstructorProfile | Perfil completo | 3h |
| - InstructorCoursesList | Cursos del instructor | 2h |
| **3.5. Páginas** | | **4h** |
| - /instructors (listado) | Grid de instructores | 2h |
| - /instructor/[id] (detalle) | Perfil completo | 2h |
| **3.6. Testing** | | **2h** |
| - Unit tests | Servicios y modelos | 2h |

#### Entregables
- ✅ Modelo User con 3 roles
- ✅ 6 métodos UserService
- ✅ 3 componentes de instructor
- ✅ 2 páginas funcionales
- ✅ 10+ unit tests

#### Criterios de Aceptación
- [ ] Listado de instructores muestra estadísticas
- [ ] Perfil de instructor muestra cursos
- [ ] Roles correctamente definidos

---

### FASE 4: Refactorización y Optimización (Semana 8)
**Fechas**: 22-28 Diciembre 2025
**Duración**: 1 semana (20 horas)

#### Objetivos
- Limpieza de código duplicado
- Creación de utilidades reutilizables
- Optimización de rendimiento
- Corrección de deprecaciones
- Documentación técnica

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **4.1. Refactorización** | | **8h** |
| - Extraer helpers comunes | utils/helpers.py | 2h |
| - Consolidar estilos | Chakra UI theming | 2h |
| - Optimizar consultas BD | Índices, proyecciones | 2h |
| - Eliminar código muerto | Imports no usados, etc. | 2h |
| **4.2. Utilidades** | | **6h** |
| - route_helpers.py | Generación de URLs | 2h |
| - formatters.py | Formato de fechas, números | 2h |
| - validators.py | Validación de inputs | 2h |
| **4.3. Documentación** | | **4h** |
| - Docstrings en funciones | Google style | 2h |
| - README actualizado | Instrucciones claras | 1h |
| - Comentarios en código complejo | Explicaciones | 1h |
| **4.4. Performance** | | **2h** |
| - Lazy loading de imágenes | Optimización | 1h |
| - Memoización de componentes | React.memo equivalente | 1h |

#### Entregables
- ✅ Código refactorizado
- ✅ 3 archivos de utilidades
- ✅ Documentación completa
- ✅ Mejoras de rendimiento (15% más rápido)

---

### FASE 5: Sistema de Autenticación y Roles (Semanas 9-12)
**Fechas**: 29 Diciembre 2025 - 25 Enero 2026
**Duración**: 4 semanas (80 horas)

#### Objetivos
- Implementar hash de contraseñas con bcrypt
- Sistema de login y registro
- Gestión de sesiones
- Control de acceso basado en roles (RBAC)
- Protección de rutas

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **5.1. Seguridad de contraseñas** | | **8h** |
| - Instalar bcrypt | `pip install bcrypt` | 0.5h |
| - Crear password.py | hash_password(), verify_password() | 3h |
| - Testing de hash | Verificar salt único | 2h |
| - Documentar seguridad | Buenas prácticas | 2.5h |
| **5.2. AuthState** | | **20h** |
| - Registro de usuarios | Validación, hash, insert | 6h |
| - Login | Verificación, sesión | 6h |
| - Logout | Limpieza de sesión | 2h |
| - Gestión de sesión | is_authenticated, current_user | 3h |
| - Manejo de errores | Mensajes claros | 3h |
| **5.3. RBAC (Control de acceso)** | | **16h** |
| - Componentes protegidos | protected.py | 4h |
| - require_auth() | HOC de autenticación | 3h |
| - require_role() | HOC de autorización | 3h |
| - admin_only(), instructor_only() | Shortcuts | 2h |
| - Redirecciones | A login si no auth | 2h |
| - Testing de permisos | Unit tests | 2h |
| **5.4. Páginas de auth** | | **16h** |
| - /login (Login) | Formulario + validación | 5h |
| - /register (Registro) | Form completo | 5h |
| - /profile (Perfil) | Edición de datos | 4h |
| - Feedback visual | Success, error messages | 2h |
| **5.5. Protección de rutas** | | **12h** |
| - /admin/* protegido | Solo admins | 3h |
| - /instructor/* protegido | Solo instructores | 3h |
| - /student/* protegido | Solo estudiantes | 3h |
| - Testing de protección | Intentos no autorizados | 3h |
| **5.6. Cambio de contraseña** | | **8h** |
| - Formulario de cambio | Actual + nueva + confirmar | 3h |
| - Verificación de actual | Seguridad | 2h |
| - Actualización en BD | Hash de nueva | 2h |
| - Notificación email (futuro) | Placeholder | 1h |

#### Entregables
- ✅ Sistema de hash bcrypt
- ✅ Login y registro funcionales
- ✅ RBAC con 6 funciones de protección
- ✅ 3 páginas de autenticación
- ✅ Rutas protegidas
- ✅ 20+ tests de seguridad

#### Criterios de Aceptación
- [ ] Usuario puede registrarse y hacer login
- [ ] Contraseñas hasheadas con bcrypt (12 rounds)
- [ ] Roles funcionan correctamente
- [ ] Intentos de acceso no autorizados redirigen a login

---

### FASE 6: Inscripciones y Seguimiento de Progreso (Semanas 13-16)
**Fechas**: 26 Enero - 22 Febrero 2026
**Duración**: 4 semanas (80 horas)

#### Objetivos
- Sistema de inscripción a cursos
- Seguimiento de lecciones completadas
- Dashboard de estudiante
- Progreso por curso

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **6.1. Modelo Enrollment** | | **8h** |
| - Diseño del modelo | user_id, course_id, enrolled_at | 3h |
| - Índices | Compuesto (user_id, course_id) | 2h |
| - Validaciones | Unicidad, existencia | 2h |
| - Testing | Unit tests | 1h |
| **6.2. EnrollmentService** | | **16h** |
| - enroll_student() | Inserción con validaciones | 4h |
| - unenroll_student() | Desins cripción | 2h |
| - get_user_enrollments() | Cursos del usuario | 3h |
| - get_course_enrollments() | Estudiantes del curso | 3h |
| - is_enrolled() | Verificación booleana | 2h |
| - Testing | Unit e integration tests | 2h |
| **6.3. Modelo Progress** | | **8h** |
| - Diseño | enrollment_id, lesson_id, completed_at | 3h |
| - Cálculo de porcentaje | Método computado | 3h |
| - Testing | Validaciones | 2h |
| **6.4. ProgressService** | | **16h** |
| - mark_lesson_complete() | Marcar completada | 4h |
| - get_course_progress() | Progreso de curso | 4h |
| - get_user_progress() | Progreso global | 4h |
| - get_completion_percentage() | Cálculo % | 2h |
| - Testing | Unit tests | 2h |
| **6.5. Dashboard de estudiante** | | **20h** |
| - Diseño UI | Wireframe en Figma | 3h |
| - StudentDashboardState | Estado con datos | 5h |
| - Tarjetas de cursos | Mis cursos con progreso | 5h |
| - Gráficos de progreso | Progress bars | 3h |
| - Estadísticas | Cursos completados, en progreso | 2h |
| - Testing UI | Manual, screenshots | 2h |
| **6.6. Botón de inscripción** | | **8h** |
| - Componente EnrollButton | Lógica de inscripción | 3h |
| - Estados (inscrito, no inscrito) | Condicional | 2h |
| - Feedback | Success/error messages | 2h |
| - Testing | Casos de uso | 1h |
| **6.7. Página de curso (actualizada)** | | **4h** |
| - Botón de inscripción | Integración | 2h |
| - Progreso si inscrito | Barra de progreso | 2h |

#### Entregables
- ✅ 2 modelos (Enrollment, Progress)
- ✅ 2 servicios completos
- ✅ Dashboard de estudiante
- ✅ Sistema de inscripción funcional
- ✅ Seguimiento de progreso
- ✅ 25+ tests

#### Criterios de Aceptación
- [ ] Estudiante puede inscribirse en cursos
- [ ] No se permiten inscripciones duplicadas
- [ ] Dashboard muestra cursos inscritos
- [ ] Progreso se calcula correctamente

---

### FASE 7: Panel de Instructor (Semanas 17-20)
**Fechas**: 23 Febrero - 22 Marzo 2026
**Duración**: 4 semanas (80 horas)

#### Objetivos
- Panel de gestión de cursos (CRUD)
- Creación de cursos con secciones y lecciones
- Estadísticas de instructor
- Dashboard de instructor

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **7.1. CRUD de cursos (instructor)** | | **24h** |
| - Formulario de creación | Título, descripción, nivel, etc. | 6h |
| - Formulario de edición | Actualización de datos | 5h |
| - Confirmación de borrado | Modal de confirmación | 2h |
| - Validaciones | Client-side y server-side | 4h |
| - InstructorCourseState | Estado de gestión | 5h |
| - Testing | E2E del flujo | 2h |
| **7.2. Gestión de secciones** | | **16h** |
| - Formulario de sección | Añadir/editar secciones | 5h |
| - Ordenación | Drag & drop o up/down | 4h |
| - Eliminación | Con confirmación | 2h |
| - SectionManagerState | Estado | 3h |
| - Testing | Unit tests | 2h |
| **7.3. Gestión de lecciones** | | **16h** |
| - Formulario de lección | Título, contenido, duración | 6h |
| - Editor de contenido | Textarea con preview | 4h |
| - Ordenación | Dentro de sección | 2h |
| - Eliminación | Con confirmación | 2h |
| - Testing | Unit tests | 2h |
| **7.4. Dashboard de instructor** | | **16h** |
| - Diseño UI | Wireframe | 3h |
| - InstructorDashboardState | Datos agregados | 5h |
| - Estadísticas | Cursos, inscripciones, ratings | 4h |
| - Gráficos | Charts de tendencias | 3h |
| - Testing | Manual | 1h |
| **7.5. Listado de cursos (instructor)** | | **6h** |
| - Tabla de cursos | Mis cursos con acciones | 3h |
| - Filtros | Por estado, fecha, etc. | 2h |
| - Acciones rápidas | Editar, eliminar, ver | 1h |
| **7.6. Rutas protegidas** | | **2h** |
| - /instructor/dashboard | Solo instructores | 0.5h |
| - /instructor/courses/new | Creación | 0.5h |
| - /instructor/courses/[id]/edit | Edición | 0.5h |
| - Testing | Intentos no autorizados | 0.5h |

#### Entregables
- ✅ CRUD completo de cursos
- ✅ Gestión de secciones y lecciones
- ✅ Dashboard de instructor
- ✅ Estadísticas y gráficos
- ✅ Rutas protegidas
- ✅ 20+ tests

#### Criterios de Aceptación
- [ ] Instructor puede crear curso completo
- [ ] Secciones y lecciones se ordenan correctamente
- [ ] Dashboard muestra estadísticas reales
- [ ] Solo instructores acceden a su panel

---

### FASE 8: Funcionalidades Avanzadas (Semanas 21-23)
**Fechas**: 23 Marzo - 12 Abril 2026
**Duración**: 3 semanas (60 horas)

#### Objetivos
- Motor de búsqueda de cursos
- Sistema de filtros avanzados
- Recomendaciones básicas
- Listas de favoritos

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **8.1. Búsqueda de cursos** | | **16h** |
| - Índice de texto en MongoDB | title, description | 2h |
| - Endpoint de búsqueda | search_courses(query) | 4h |
| - SearchState | Estado reactivo | 4h |
| - UI de búsqueda | Barra con autocompletado | 4h |
| - Highlighting | Resaltar términos | 2h |
| **8.2. Sistema de filtros** | | **16h** |
| - Filtro por categoría | Dropdown | 3h |
| - Filtro por nivel | Principiante, Intermedio, Avanzado | 3h |
| - Filtro por duración | Rango de horas | 3h |
| - Filtro por valoración | >= 4 estrellas, etc. | 3h |
| - Combinación de filtros | AND lógico | 3h |
| - Testing | Casos complejos | 1h |
| **8.3. Sistema de recomendaciones** | | **12h** |
| - Algoritmo básico | Cursos similares por categoría | 4h |
| - Basado en inscripciones | "Usuarios que tomaron X también tomaron Y" | 4h |
| - UI de recomendaciones | Sección en detalle de curso | 3h |
| - Testing | Validación de lógica | 1h |
| **8.4. Listas de favoritos** | | **12h** |
| - Modelo Favorite | user_id, course_id | 2h |
| - FavoriteService | add, remove, get_favorites | 4h |
| - Botón de favorito | Corazón togglable | 3h |
| - Página de favoritos | /student/favorites | 2h |
| - Testing | Unit tests | 1h |
| **8.5. Mejoras de UX** | | **4h** |
| - Loading skeletons | Placeholders | 2h |
| - Animaciones | Transiciones suaves | 1h |
| - Tooltips | Ayudas contextuales | 1h |

#### Entregables
- ✅ Motor de búsqueda funcional
- ✅ 4 tipos de filtros
- ✅ Sistema de recomendaciones
- ✅ Listas de favoritos
- ✅ Mejoras de UX
- ✅ 15+ tests

#### Criterios de Aceptación
- [ ] Búsqueda retorna resultados relevantes
- [ ] Filtros se combinan correctamente
- [ ] Recomendaciones son pertinentes
- [ ] Favoritos persisten en BD

---

### FASE 9: Pruebas, Documentación y Despliegue (Semanas 24-26)
**Fechas**: 13 Abril - 3 Mayo 2026
**Duración**: 3 semanas (60 horas)

#### Objetivos
- Testing exhaustivo
- Documentación técnica completa
- Manuales de usuario
- Despliegue en producción
- Preparación de defensa

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **9.1. Testing** | | **16h** |
| - Unit tests (cobertura 80%) | Pytest | 6h |
| - Integration tests | Flujos E2E | 4h |
| - Manual testing | Casos de uso reales | 3h |
| - Corrección de bugs | Debugging | 3h |
| **9.2. Documentación técnica** | | **16h** |
| - Arquitectura y tecnologías | Diagrama, stack | 3h |
| - Modelos y servicios | Descripción detallada | 3h |
| - Estados y componentes | Reflex specifics | 3h |
| - Base de datos | Esquemas, colecciones | 2h |
| - Seguridad | Medidas implementadas | 2h |
| - Scripts y utilidades | Helpers, scripts | 2h |
| - Conclusiones | Métricas, aprendizajes | 1h |
| **9.3. Manual de usuario** | | **12h** |
| - Guía para estudiantes | Con capturas | 4h |
| - Guía para instructores | CRUD de cursos | 4h |
| - Guía para administradores | Gestión | 2h |
| - FAQ | Preguntas frecuentes | 2h |
| **9.4. Manual de configuración** | | **6h** |
| - Requisitos del sistema | Especificaciones | 1h |
| - Instalación paso a paso | Comandos detallados | 2h |
| - Variables de entorno | .env.example | 1h |
| - Troubleshooting | Problemas comunes | 2h |
| **9.5. Memoria del proyecto** | | **20h** |
| - Sección 1: Introducción | Descripción, objetivos | 2h |
| - Sección 2: Análisis del entorno | Oportunidades, ayudas | 3h |
| - Sección 3: Sistema actual | Contexto, necesidades | 2h |
| - Sección 4: Solución propuesta | Tecnologías, presupuesto | 3h |
| - Sección 5: Planificación | Este documento | 2h |
| - Sección 6: Viabilidad | Técnica, económica, legal | 3h |
| - Sección 7: Diseño e implementación | UML, BD, interfaces | 3h |
| - Secciones finales | Bibliografía, anexos | 2h |
| **9.6. Despliegue** | | **6h** |
| - Configurar Reflex Cloud | Cuenta, proyecto | 1h |
| - Deploy a producción | reflex deploy | 2h |
| - Configurar dominio | DNS, SSL | 1h |
| - Pruebas en producción | Smoke tests | 1h |
| - Monitoreo | Logs, errores | 1h |
| **9.7. Preparación de defensa** | | **4h** |
| - Presentación PowerPoint | 20 slides | 2h |
| - Ensayo de defensa | 30 minutos | 1h |
| - Video demostración | 5-10 minutos | 1h |

#### Entregables
- ✅ Cobertura de tests >80%
- ✅ Documentación técnica completa (9 documentos)
- ✅ Manual de usuario (40+ páginas)
- ✅ Memoria del proyecto (40+ páginas)
- ✅ Aplicación desplegada en producción
- ✅ Presentación para defensa
- ✅ Video demostración

#### Criterios de Aceptación
- [ ] Tests pasan sin errores
- [ ] Documentación revisada por tutor
- [ ] Aplicación accesible públicamente
- [ ] Defensa aprobada por tribunal

---

## 5.3. Diagrama de Gantt

```
Fase / Semana            1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
──────────────────────────────────────────────────────────────────────────────────────────────────────
1. Configuración Inicial ██ ██
2. Módulo de Cursos         ██ ██ ██
3. Módulo de Instructores            ██ ██
4. Refactorización                      ██
5. Autenticación                        ██ ██ ██ ██
6. Inscripciones/Progreso                           ██ ██ ██ ██
7. Panel de Instructor                                         ██ ██ ██ ██
8. Funcionalidades Avanzadas                                               ██ ██ ██
9. Pruebas/Documentación                                                        ██ ██ ██
──────────────────────────────────────────────────────────────────────────────────────────────────────
Entrega a Tutor                                                                                   ⚠️
Defensa del Proyecto                                                                              ✅
```

---

## 5.4. Hitos Principales (Milestones)

| Hito | Fecha | Entregable | Criterio de Éxito |
|------|-------|------------|-------------------|
| **M1: Entorno Configurado** | 16/11/2025 | Repositorio + MongoDB | ✅ `reflex run` funciona |
| **M2: MVP de Cursos** | 7/12/2025 | Listado + Detalle | ✅ Cursos visibles desde BD |
| **M3: Instructores Implementados** | 21/12/2025 | Perfiles + Stats | ✅ Listado de instructores funcional |
| **M4: Autenticación Completa** | 25/01/2026 | Login + Registro + RBAC | ✅ Usuarios pueden registrarse y acceder |
| **M5: Sistema de Inscripciones** | 22/02/2026 | Enrollment + Progress | ✅ Estudiantes se inscriben y ven progreso |
| **M6: Panel de Instructor** | 22/03/2026 | CRUD Cursos | ✅ Instructor crea curso completo |
| **M7: Funcionalidades Avanzadas** | 12/04/2026 | Búsqueda + Filtros | ✅ Búsqueda retorna resultados |
| **M8: Aplicación Desplegada** | 26/04/2026 | Producción online | ✅ URL pública accesible |
| **M9: Entrega Final** | 3/05/2026 | Memoria + Manuales | ✅ Documentación completa |
| **M10: Defensa Exitosa** | 10/05/2026 | Presentación | ✅ Proyecto aprobado |

---

## 5.5. Entregas Periódicas al Tutor

Según el guión del proyecto, se requieren **entregas cada 3 semanas** mínimo:

| Entrega | Fecha | Semanas Cubiertas | Contenido |
|---------|-------|-------------------|-----------|
| **E1** | 30/11/2025 | 1-4 | - Entorno configurado<br>- Módulo de Cursos (avance 50%)<br>- Wireframes<br>- Documento de requisitos |
| **E2** | 21/12/2025 | 5-8 | - Módulo de Cursos (100%)<br>- Módulo de Instructores (100%)<br>- Refactorización completa<br>- Primeros tests |
| **E3** | 11/01/2026 | 9-11 | - Autenticación (avance 60%)<br>- Login y registro funcionales<br>- Primeras rutas protegidas |
| **E4** | 1/02/2026 | 12-14 | - Autenticación (100%)<br>- Inscripciones (avance 50%)<br>- RBAC completo |
| **E5** | 22/02/2026 | 15-17 | - Inscripciones (100%)<br>- Dashboard de estudiante<br>- Panel de instructor (avance 30%) |
| **E6** | 15/03/2026 | 18-20 | - Panel de instructor (100%)<br>- CRUD completo de cursos |
| **E7** | 5/04/2026 | 21-23 | - Funcionalidades avanzadas (100%)<br>- Búsqueda y filtros operativos |
| **E8** | 26/04/2026 | 24-25 | - Testing completo<br>- Documentación técnica<br>- Despliegue en producción |
| **E9** | 3/05/2026 | 26 | - Memoria completa<br>- Manuales de usuario<br>- Presentación defensa |

**Nota**: El tutor debe dar **visto bueno** a cada entrega para poder continuar.

---

## 5.6. Plan de Mantenimiento (Post-Proyecto)

Una vez finalizado el proyecto académico, se plantea el siguiente plan de mantenimiento:

### Mantenimiento Correctivo

**Frecuencia**: Según necesidad (on-demand)

| Actividad | Descripción | Tiempo Estimado |
|-----------|-------------|-----------------|
| **Corrección de bugs** | Resolución de errores reportados | 2-4h/bug |
| **Actualizaciones de seguridad** | Parches de dependencias | 1h/mes |
| **Respaldo de base de datos** | Verificación de backups automáticos | 0.5h/semana |
| **Monitoreo de uptime** | Revisión de logs, errores | 1h/semana |

**Coste estimado**: 10-15h/mes = 250-375€/mes

---

### Mantenimiento Evolutivo

**Frecuencia**: Trimestral

| Actividad | Descripción | Tiempo Estimado |
|-----------|-------------|-----------------|
| **Actualización de Reflex** | Upgrade a versión minor | 4h/trimestre |
| **Actualización de dependencias** | pip-upgrade, testing | 3h/trimestre |
| **Optimización de BD** | Índices, queries lentas | 4h/trimestre |
| **Mejoras de UI** | Feedback de usuarios | 8h/trimestre |
| **Nuevas funcionalidades menores** | Features pequeños | 12h/trimestre |

**Coste estimado**: 31h/trimestre = 775€/trimestre = **260€/mes promedio**

---

### Mantenimiento Preventivo

**Frecuencia**: Mensual

| Actividad | Descripción | Tiempo Estimado |
|-----------|-------------|-----------------|
| **Revisión de rendimiento** | Tiempos de carga, optimización | 2h/mes |
| **Análisis de seguridad** | Escaneo de vulnerabilidades | 2h/mes |
| **Revisión de métricas** | Analytics, uso de recursos | 1h/mes |
| **Backup manual** | Verificación adicional | 0.5h/mes |

**Coste estimado**: 5.5h/mes = 137.5€/mes

---

### Resumen de Costes de Mantenimiento

| Tipo | Horas/Mes | Coste/Mes (25€/h) | Coste/Año |
|------|-----------|-------------------|-----------|
| Correctivo | 10-15h | 250-375€ | 3,000-4,500€ |
| Evolutivo | ~10h | 260€ | 3,120€ |
| Preventivo | 5.5h | 137.5€ | 1,650€ |
| **TOTAL** | **25-31h** | **647-772€** | **7,770-9,270€** |

**Nota**: Si se contrata desarrollador junior part-time (20h/mes), el coste se reduce a **2,000€/mes** (salario de 24,000€/año prorrateado).

---

## 5.7. Modificaciones y Ampliaciones Futuras

### Funcionalidades Planificadas Post v1.0

#### Prioridad Alta (Q3 2026)

| Funcionalidad | Descripción | Esfuerzo Estimado | Valor de Negocio |
|---------------|-------------|-------------------|------------------|
| **Sistema de pagos** | Integración con Stripe | 40h (1 mes) | ⭐⭐⭐⭐⭐ |
| **Certificados digitales** | Generación automática de PDFs | 24h (3 semanas) | ⭐⭐⭐⭐ |
| **Notificaciones email** | SendGrid para avisos | 16h (2 semanas) | ⭐⭐⭐⭐ |

**Total Q3**: 80h (2 meses) - **Inversión**: 2,000€

---

#### Prioridad Media (Q4 2026)

| Funcionalidad | Descripción | Esfuerzo Estimado | Valor de Negocio |
|---------------|-------------|-------------------|------------------|
| **Videoconferencias** | Integración Jitsi/Zoom | 60h (1.5 meses) | ⭐⭐⭐⭐ |
| **Chat en tiempo real** | WebSockets con Reflex | 40h (1 mes) | ⭐⭐⭐ |
| **Foros de discusión** | Por curso, threading | 48h (1.5 meses) | ⭐⭐⭐ |

**Total Q4**: 148h (3.5 meses) - **Inversión**: 3,700€

---

#### Prioridad Baja (2027)

| Funcionalidad | Descripción | Esfuerzo Estimado | Valor de Negocio |
|---------------|-------------|-------------------|------------------|
| **App móvil nativa** | React Native | 200h (5 meses) | ⭐⭐⭐⭐⭐ |
| **Gamificación** | Puntos, badges, rankings | 80h (2 meses) | ⭐⭐⭐ |
| **IA de recomendaciones** | Machine Learning | 120h (3 meses) | ⭐⭐⭐⭐ |

**Total 2027**: 400h (10 meses) - **Inversión**: 10,000€

---

## 5.8. Riesgos y Contingencias

### Identificación de Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| **Retrasos en desarrollo** | Media (40%) | Alto | - Buffer de 20h por fase<br>- Entregas periódicas para detectar retrasos |
| **Bugs críticos pre-defensa** | Baja (20%) | Alto | - Testing exhaustivo en Fase 9<br>- Manual testing 1 semana antes |
| **MongoDB Atlas caído** | Muy Baja (5%) | Medio | - Backups automáticos diarios<br>- SLA 99.9% de Atlas |
| **Cambios de requisitos** | Media (30%) | Medio | - Alcance bien definido<br>- Cambios solo post v1.0 |
| **Falta de tiempo para documentación** | Baja (15%) | Alto | - Documentar durante desarrollo<br>- Fase 9 dedicada exclusivamente |
| **Enfermedad/ausencia** | Baja (10%) | Alto | - Buffer de 2 semanas en planificación<br>- Entregas adelantadas |

---

### Plan de Contingencia

**Escenario 1: Retraso de 1-2 semanas**
- **Acción**: Reducir scope de Fase 8 (funcionalidades avanzadas)
- **Features a posponer**: Recomendaciones, favoritos
- **Impacto**: Mínimo, no son funcionalidades core

**Escenario 2: Bug crítico encontrado en Semana 25**
- **Acción**: Postergar documentación 1 semana, priorizar corrección
- **Recurso adicional**: Solicitar extensión de 1 semana al tutor
- **Impacto**: Entrega ajustada pero dentro de plazo ampliado

**Escenario 3: MongoDB Atlas no disponible**
- **Acción**: Migración temporal a MongoDB local con Docker
- **Tiempo de recuperación**: 4 horas
- **Impacto**: Mínimo, datos se restauran desde backup

---

## 5.9. Conclusiones de la Planificación

### Resumen Ejecutivo

- **Duración total**: 26 semanas (6 meses)
- **Horas totales**: 520 horas
- **Fases**: 9 fases bien definidas
- **Entregas periódicas**: 9 entregas cada 3 semanas
- **Hitos**: 10 milestones principales
- **Buffer**: 40 horas para imprevistos (7.7% del total)

### Viabilidad Temporal

| Aspecto | Evaluación | Justificación |
|---------|------------|---------------|
| **Realismo** | ✅ Alto | 20h/semana es sostenible para estudiante DAW |
| **Flexibilidad** | ✅ Alta | Buffer de 40h + posibilidad de reducir scope |
| **Riesgos** | ⚠️ Medios | Identificados y mitigados |
| **Cumplimiento** | ✅ Probable | Planificación detallada y entregas frecuentes |

### Próximos Pasos

1. **Aprobación del tutor**: Revisión de esta planificación
2. **Inicio Fase 1**: 3 de Noviembre 2025
3. **Primera entrega**: 30 de Noviembre 2025
4. **Seguimiento semanal**: Actualización de progreso

---

<div style="page-break-after: always;"></div>
