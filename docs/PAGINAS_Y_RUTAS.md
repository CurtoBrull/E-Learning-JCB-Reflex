# Páginas y Rutas - E-Learning JCB Reflex

## 🌐 Sistema de Rutas

### Estructura de Rutas

La aplicación utiliza un sistema de rutas jerárquico con protección por roles:

```
/                           # Página principal (pública)
├── /courses                # Catálogo de cursos (pública)
│   ├── /[course_id]        # Detalle de curso (pública)
│   └── /[course_id]/view   # Visor de curso (protegida - estudiantes inscritos)
├── /instructors            # Lista de instructores (pública)
│   └── /[instructor_id]    # Perfil de instructor (pública)
├── /contact                # Formulario de contacto (pública)
├── /login                  # Inicio de sesión (pública)
├── /register               # Registro de usuarios (pública)
├── /profile                # Perfil de usuario (protegida - autenticados)
├── /student                # Área de estudiantes
│   └── /dashboard          # Dashboard de estudiante (protegida - estudiantes)
├── /instructor             # Área de instructores
│   └── /dashboard          # Dashboard de instructor (protegida - instructores)
└── /admin                  # Área de administración
    ├── /dashboard          # Dashboard admin (protegida - admins)
    ├── /users              # Gestión de usuarios (protegida - admins)
    ├── /courses            # Gestión de cursos (protegida - admins)
    ├── /categories         # Gestión de categorías (protegida - admins)
    ├── /settings           # Configuración del sistema (protegida - admins)
    └── /stats              # Estadísticas avanzadas (protegida - admins)
```

---

## 📄 Páginas Públicas (Sin Autenticación)

### 1. Página de Inicio (`pages/index.py`)

**Ruta**: `/`  
**Propósito**: Página principal con cursos destacados y presentación de la plataforma.

#### Secciones Principales
```python
def index_page() -> rx.Component:
    """
    Página de inicio con:
    - Hero section con call-to-action
    - Cursos populares (6 destacados)
    - Estadísticas de la plataforma
    - Testimonios de usuarios
    - Footer con enlaces importantes
    """
```

#### Componentes Incluidos
- **Hero Section**: Título, descripción y botón de registro
- **Cursos Destacados**: Grid de 6 cursos más populares
- **Estadísticas**: Número de cursos, estudiantes e instructores
- **Call-to-Action**: Invitación a registrarse o explorar cursos

#### Estados Utilizados
- `CourseState`: Para cargar cursos populares
- `AuthState`: Para mostrar contenido personalizado si está autenticado

---

### 2. Catálogo de Cursos (`pages/courses.py`)

**Ruta**: `/courses`  
**Propósito**: Catálogo completo de cursos con filtros y búsqueda.

#### Funcionalidades
```python
def courses_page() -> rx.Component:
    """
    Catálogo de cursos con:
    - Barra de búsqueda
    - Filtros por categoría y nivel
    - Grid responsive de cursos
    - Paginación (futuro)
    - Ordenamiento por popularidad/precio
    """
```

#### Filtros Disponibles
- **Búsqueda por texto**: Título y descripción
- **Categoría**: Desarrollo Web, Móvil, IA, etc.
- **Nivel**: Principiante, Intermedio, Avanzado
- **Precio**: Gratis, De pago, Rango de precios
- **Instructor**: Por nombre del instructor

#### Estados Utilizados
- `CourseState`: Gestión de cursos y filtros
- `AuthState`: Para mostrar estado de inscripción

---

### 3. Detalle de Curso (`pages/course_detail.py`)

**Ruta**: `/courses/[course_id]`  
**Propósito**: Información detallada de un curso específico.

#### Secciones del Detalle
```python
def course_detail_page() -> rx.Component:
    """
    Detalle de curso con:
    - Información principal (título, descripción, precio)
    - Datos del instructor
    - Lista de lecciones
    - Reseñas de estudiantes
    - Botón de inscripción/acceso
    """
```

#### Información Mostrada
- **Curso**: Título, descripción, nivel, categoría, precio
- **Instructor**: Nombre, avatar, biografía, otros cursos
- **Contenido**: Lista de lecciones con duración
- **Estadísticas**: Número de estudiantes, calificación promedio
- **Reseñas**: Comentarios y calificaciones de estudiantes

#### Acciones Disponibles
- **No autenticado**: Botón "Iniciar Sesión para Inscribirse"
- **Estudiante no inscrito**: Botón "Inscribirse"
- **Estudiante inscrito**: Botón "Continuar Curso"
- **Instructor/Admin**: Botón "Ver como Estudiante"

---

### 4. Lista de Instructores (`pages/instructors.py`)

**Ruta**: `/instructors`  
**Propósito**: Directorio de todos los instructores de la plataforma.

#### Funcionalidades
```python
def instructors_page() -> rx.Component:
    """
    Lista de instructores con:
    - Grid de tarjetas de instructores
    - Información básica (nombre, expertise, cursos)
    - Búsqueda por nombre o especialidad
    - Filtro por área de expertise
    """
```

#### Estados Utilizados
- `InstructorState`: Carga y filtrado de instructores

---

### 5. Perfil de Instructor (`pages/instructor_detail.py`)

**Ruta**: `/instructors/[instructor_id]`  
**Propósito**: Perfil completo de un instructor específico.

#### Información del Perfil
```python
def instructor_detail_page() -> rx.Component:
    """
    Perfil de instructor con:
    - Información personal (avatar, nombre, bio)
    - Área de expertise
    - Estadísticas (cursos creados, estudiantes)
    - Lista de cursos del instructor
    - Calificación promedio
    """
```

---

### 6. Formulario de Contacto (`pages/contact.py`)

**Ruta**: `/contact`  
**Propósito**: Formulario para que los usuarios envíen mensajes.

#### Campos del Formulario
```python
def contact_page() -> rx.Component:
    """
    Formulario de contacto con:
    - Nombre (obligatorio)
    - Email (obligatorio, validación de formato)
    - Mensaje (obligatorio, mínimo 10 caracteres)
    - Botón de envío con loading state
    - Mensajes de éxito/error
    """
```

#### Validaciones
- **Nombre**: No vacío, máximo 100 caracteres
- **Email**: Formato válido, máximo 255 caracteres
- **Mensaje**: Mínimo 10 caracteres, máximo 1000 caracteres

#### Estados Utilizados
- `ContactState`: Gestión del formulario y envío

---

### 7. Inicio de Sesión (`pages/login.py`)

**Ruta**: `/login`  
**Propósito**: Formulario de autenticación de usuarios.

#### Funcionalidades
```python
def login_page() -> rx.Component:
    """
    Página de login con:
    - Formulario de email y contraseña
    - Validación en tiempo real
    - Mensajes de error
    - Enlace a registro
    - Redirección automática tras login exitoso
    """
```

#### Validaciones
- **Email**: Formato válido, no vacío
- **Contraseña**: Mínimo 6 caracteres

#### Estados Utilizados
- `AuthState`: Gestión de autenticación

---

### 8. Registro de Usuarios (`pages/register.py`)

**Ruta**: `/register`  
**Propósito**: Formulario de registro de nuevos usuarios.

#### Campos del Registro
```python
def register_page() -> rx.Component:
    """
    Formulario de registro con:
    - Nombre y apellido
    - Email (verificación de unicidad)
    - Contraseña y confirmación
    - Selección de rol (estudiante/instructor)
    - Términos y condiciones
    """
```

#### Validaciones
- **Nombres**: No vacíos, máximo 50 caracteres cada uno
- **Email**: Formato válido, único en la base de datos
- **Contraseña**: Mínimo 6 caracteres, confirmación coincidente
- **Rol**: Selección obligatoria entre estudiante e instructor

---

## 🔒 Páginas Protegidas - Dashboards

### 1. Dashboard de Estudiante (`pages/student_dashboard.py`)

**Ruta**: `/student/dashboard`  
**Protección**: `student_only`  
**Propósito**: Panel principal para estudiantes.

#### Secciones del Dashboard
```python
def student_dashboard_page() -> rx.Component:
    """
    Dashboard de estudiante con:
    - Resumen de cursos inscritos
    - Progreso en cursos activos
    - Cursos recomendados
    - Estadísticas personales
    - Accesos rápidos
    """
```

#### Métricas Mostradas
- **Cursos Inscritos**: Total de cursos en los que está inscrito
- **Cursos Completados**: Cursos finalizados al 100%
- **Progreso Promedio**: Porcentaje promedio de avance
- **Tiempo Total**: Horas de contenido consumido
- **Certificados**: Certificados obtenidos (futuro)

#### Estados Utilizados
- `EnrollmentState`: Gestión de inscripciones y progreso
- `AuthState`: Información del usuario actual

---

### 2. Dashboard de Instructor (`pages/instructor_dashboard.py`)

**Ruta**: `/instructor/dashboard`  
**Protección**: `instructor_only`  
**Propósito**: Panel principal para instructores.

#### Secciones del Dashboard
```python
def instructor_dashboard_page() -> rx.Component:
    """
    Dashboard de instructor con:
    - Resumen de cursos creados
    - Estadísticas de estudiantes
    - Ingresos generados (futuro)
    - Reseñas recientes
    - Herramientas de creación
    """
```

#### Métricas Mostradas
- **Cursos Creados**: Total de cursos publicados
- **Estudiantes Totales**: Suma de estudiantes en todos los cursos
- **Calificación Promedio**: Rating promedio de todos los cursos
- **Reseñas Totales**: Número total de reseñas recibidas
- **Ingresos**: Ganancias por ventas de cursos (futuro)

---

### 3. Dashboard de Administrador (`pages/admin_dashboard.py`)

**Ruta**: `/admin/dashboard`  
**Protección**: `admin_only`  
**Propósito**: Panel principal para administradores.

#### Métricas del Sistema
```python
def admin_dashboard_page() -> rx.Component:
    """
    Dashboard administrativo con:
    - Estadísticas generales de la plataforma
    - Gráficos de crecimiento
    - Actividad reciente
    - Alertas del sistema
    - Accesos rápidos a gestión
    """
```

#### Estadísticas Principales
- **Usuarios**: Total por rol (estudiantes, instructores, admins)
- **Cursos**: Total de cursos publicados
- **Inscripciones**: Total de inscripciones activas
- **Actividad**: Usuarios activos en las últimas 24h/7d/30d
- **Contenido**: Horas totales de video, lecciones creadas

#### Estados Utilizados
- `AdminDashboardState`: Carga de estadísticas del sistema

---

## 🛠️ Páginas de Administración

### 1. Gestión de Usuarios (`pages/user_management.py`)

**Ruta**: `/admin/users`  
**Protección**: `admin_only`  
**Propósito**: CRUD completo de usuarios del sistema.

#### Funcionalidades
```python
def user_management_page() -> rx.Component:
    """
    Gestión de usuarios con:
    - Tabla de todos los usuarios
    - Filtros por rol y estado
    - Búsqueda por nombre/email
    - Formulario de creación/edición
    - Eliminación con confirmación
    - Cambio de contraseñas
    """
```

#### Operaciones Disponibles
- **Crear Usuario**: Formulario completo con todos los campos
- **Editar Usuario**: Modificar datos personales y rol
- **Eliminar Usuario**: Con confirmación y validaciones
- **Cambiar Contraseña**: Sin requerir contraseña actual
- **Cambiar Rol**: Promoción/degradación de permisos

#### Estados Utilizados
- `UserManagementState`: Gestión completa de usuarios

---

### 2. Gestión de Cursos (`pages/course_management.py`)

**Ruta**: `/admin/courses`  
**Protección**: `admin_only`  
**Propósito**: CRUD completo de cursos del sistema.

#### Funcionalidades
```python
def course_management_page() -> rx.Component:
    """
    Gestión de cursos con:
    - Tabla de todos los cursos
    - Filtros por nivel y categoría
    - Búsqueda por título/instructor
    - Formulario de creación/edición
    - Gestión de lecciones
    - Estadísticas por curso
    """
```

#### Operaciones Disponibles
- **Crear Curso**: Formulario con información básica e instructor
- **Editar Curso**: Modificar todos los campos del curso
- **Eliminar Curso**: Con confirmación y limpieza de inscripciones
- **Gestionar Lecciones**: CRUD de lecciones dentro del curso
- **Ver Estadísticas**: Inscripciones, progreso, reseñas

#### Estados Utilizados
- `CourseManagementState`: Gestión completa de cursos

---

### 3. Visor de Curso (`pages/course_viewer.py`)

**Ruta**: `/courses/[course_id]/view`  
**Protección**: Estudiantes inscritos únicamente  
**Propósito**: Interfaz para visualizar contenido de cursos.

#### Características Principales
```python
def course_viewer_page() -> rx.Component:
    """
    Visor de curso tipo Netflix con:
    - Reproductor de videos de YouTube embebidos
    - Lista lateral de lecciones
    - Navegación entre lecciones (anterior/siguiente)
    - Indicador de progreso del curso
    - Información detallada de cada lección
    - Toggle para mostrar/ocultar sidebar
    """
```

#### Componentes del Visor
```python
def video_player() -> rx.Component:
    """Reproductor de video con iframe de YouTube."""

def lessons_sidebar() -> rx.Component:
    """Lista lateral de lecciones con progreso."""

def lesson_info() -> rx.Component:
    """Información de la lección actual."""

def navigation_controls() -> rx.Component:
    """Controles de navegación anterior/siguiente."""

def progress_bar() -> rx.Component:
    """Barra de progreso del curso."""
```

#### Validaciones de Acceso
1. **Usuario autenticado**: Debe haber iniciado sesión
2. **Usuario estudiante**: Solo estudiantes pueden ver contenido
3. **Inscripción válida**: Debe estar inscrito en el curso
4. **Curso existente**: El curso debe existir y tener lecciones

#### Estados Utilizados
- `CourseViewerState`: Gestión completa del visor

---

### 4. Páginas en Desarrollo

#### Gestión de Categorías (`pages/category_management.py`)
**Estado**: En desarrollo  
**Funcionalidades planificadas**:
- CRUD completo de categorías
- Asignación múltiple a cursos
- Estadísticas por categoría

#### Configuración del Sistema (`pages/admin_settings.py`)
**Estado**: En desarrollo  
**Funcionalidades planificadas**:
- Configuración general de la plataforma
- Parámetros de seguridad
- Configuración de correo electrónico
- Gestión de backups

#### Estadísticas Avanzadas (`pages/admin_stats.py`)
**Estado**: En desarrollo  
**Funcionalidades planificadas**:
- Gráficos de crecimiento
- Análisis de engagement
- Métricas financieras
- Exportación de reportes

---

## 🔐 Sistema de Protección de Rutas

### Niveles de Protección

#### 1. Rutas Públicas
```python
# Sin protección - accesibles para todos
public_routes = [
    "/", "/courses", "/courses/[id]", "/instructors", 
    "/instructors/[id]", "/contact", "/login", "/register"
]
```

#### 2. Rutas Autenticadas
```python
@require_auth
def protected_page():
    """Requiere estar autenticado."""
    return page_content()
```

#### 3. Rutas por Rol
```python
@student_only
def student_page():
    """Solo para estudiantes."""
    return student_content()

@instructor_only  
def instructor_page():
    """Solo para instructores."""
    return instructor_content()

@admin_only
def admin_page():
    """Solo para administradores."""
    return admin_content()
```

#### 4. Rutas Condicionales
```python
def course_viewer_access(course_id: str):
    """
    Acceso condicional al visor de curso.
    
    Condiciones:
    - Usuario autenticado
    - Usuario es estudiante
    - Estudiante inscrito en el curso
    """
```

### Manejo de Acceso Denegado

#### Redirecciones Automáticas
```python
def handle_unauthorized_access(required_role: str = None):
    """
    Manejo de acceso no autorizado.
    
    Acciones:
    - No autenticado: Redirigir a /login
    - Rol insuficiente: Mostrar mensaje de acceso denegado
    - Error de inscripción: Redirigir a detalle del curso
    """
```

#### Mensajes Personalizados
- **No autenticado**: "Inicia sesión para acceder"
- **Rol insuficiente**: "No tienes permisos para esta página"
- **No inscrito**: "Inscríbete para acceder al contenido"

---

## 📱 Diseño Responsive

### Breakpoints Utilizados
```python
breakpoints = {
    "mobile": "< 768px",
    "tablet": "768px - 1024px", 
    "desktop": "> 1024px"
}
```

### Adaptaciones por Dispositivo

#### Móvil
- **Navegación**: Menú hamburguesa
- **Cursos**: 1 columna
- **Visor**: Video a pantalla completa
- **Formularios**: Campos apilados

#### Tablet
- **Navegación**: Menú completo colapsado
- **Cursos**: 2 columnas
- **Visor**: Sidebar colapsable
- **Formularios**: 2 columnas cuando es apropiado

#### Desktop
- **Navegación**: Menú completo expandido
- **Cursos**: 3-4 columnas
- **Visor**: Sidebar fija lateral
- **Formularios**: Layout optimizado

---

*Documentación de Páginas y Rutas*  
*Proyecto: E-Learning JCB Reflex*  
*Actualizado: 25 de enero de 2025*