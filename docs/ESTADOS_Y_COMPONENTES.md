# Estados y Componentes - E-Learning JCB Reflex

## 🎛️ Estados de la Aplicación (Reflex States)

Los estados en Reflex manejan la lógica de UI y la interacción con los servicios de backend.

### 1. AuthState (`states/auth_state.py`)

**Propósito**: Gestión de autenticación y sesión de usuario.

#### Variables de Estado
```python
class AuthState(rx.State):
    # Usuario actual
    current_user: User | None = None
    
    # Formulario de login
    login_email: str = ""
    login_password: str = ""
    
    # Estados de UI
    error: str = ""
    success: str = ""
    loading: bool = False
```

#### Propiedades Computadas
```python
@rx.computed_var
def is_authenticated(self) -> bool:
    """Verificar si hay un usuario autenticado."""
    return self.current_user is not None

@rx.computed_var
def user_name(self) -> str:
    """Obtener nombre del usuario actual."""
    if self.current_user:
        return self.current_user.get_full_name()
    return ""

@rx.computed_var
def user_role(self) -> str:
    """Obtener rol del usuario actual."""
    if self.current_user:
        return self.current_user.role
    return ""

@rx.computed_var
def is_user_admin(self) -> bool:
    """Verificar si el usuario es administrador."""
    return self.user_role == "admin"

@rx.computed_var
def is_user_instructor(self) -> bool:
    """Verificar si el usuario es instructor."""
    return self.user_role == "instructor"

@rx.computed_var
def is_user_student(self) -> bool:
    """Verificar si el usuario es estudiante."""
    return self.user_role == "student"
```

#### Métodos Principales
```python
async def handle_login(self):
    """
    Procesar inicio de sesión.
    
    Flujo:
    1. Validar campos obligatorios
    2. Buscar usuario por email
    3. Verificar contraseña con bcrypt
    4. Establecer sesión
    5. Redirigir según rol
    """

async def handle_logout(self):
    """
    Cerrar sesión del usuario.
    
    Flujo:
    1. Limpiar current_user
    2. Limpiar formularios
    3. Redirigir a página principal
    """

def redirect_to_dashboard(self):
    """
    Redirigir al dashboard según el rol del usuario.
    
    Rutas:
    - Admin: /admin/dashboard
    - Instructor: /instructor/dashboard  
    - Student: /student/dashboard
    """
```

---

### 2. CourseState (`states/course_state.py`)

**Propósito**: Gestión de cursos en la interfaz de usuario.

#### Variables de Estado
```python
class CourseState(rx.State):
    # Lista de cursos
    courses: List[Course] = []
    popular_courses: List[Course] = []
    
    # Curso actual
    current_course: Course | None = None
    
    # Filtros y búsqueda
    search_query: str = ""
    category_filter: str = "all"
    level_filter: str = "all"
    
    # Estados de UI
    loading: bool = False
    error: str = ""
```

#### Métodos Principales
```python
async def load_popular_courses(self):
    """Cargar cursos destacados para la página principal."""

async def load_courses(self):
    """Cargar catálogo completo de cursos."""

async def load_course_by_id(self, course_id: str):
    """Cargar curso específico por ID."""

async def load_course_from_url(self):
    """Extraer ID de URL dinámica y cargar curso."""

def apply_filters(self):
    """Aplicar filtros de búsqueda, categoría y nivel."""
```

---

### 3. CourseViewerState (`states/course_viewer_state.py`)

**Propósito**: Gestión del visor de cursos para estudiantes inscritos.

#### Variables de Estado
```python
class CourseViewerState(AuthState):
    # Información del curso
    current_course_id: str = ""
    course_title: str = ""
    course_thumbnail: str = ""
    
    # Lecciones
    lessons: list[dict] = []
    current_lesson_index: int = 0
    
    # Estados de UI
    loading: bool = False
    error: str = ""
    is_enrolled: bool = False
    sidebar_visible: bool = True
```

#### Propiedades Computadas
```python
@rx.var
def current_lesson(self) -> dict:
    """Obtener la lección actualmente seleccionada."""
    if 0 <= self.current_lesson_index < len(self.lessons):
        return self.lessons[self.current_lesson_index]
    return {}

@rx.var
def current_video_url(self) -> str:
    """
    Convertir URL de YouTube a formato embed.
    
    Soporta:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    
    Returns:
        str: URL en formato embed
    """

@rx.var
def has_previous_lesson(self) -> bool:
    """Verificar si existe una lección anterior."""
    return self.current_lesson_index > 0

@rx.var
def has_next_lesson(self) -> bool:
    """Verificar si existe una lección siguiente."""
    return self.current_lesson_index < len(self.lessons) - 1

@rx.var
def progress_percentage(self) -> float:
    """Calcular porcentaje de progreso en el curso."""
    if len(self.lessons) == 0:
        return 0.0
    return ((self.current_lesson_index + 1) / len(self.lessons)) * 100
```

#### Métodos de Navegación
```python
async def load_course_viewer_from_url(self):
    """
    Cargar curso desde URL y verificar inscripción.
    
    Validaciones:
    - Usuario autenticado
    - Usuario es estudiante
    - Usuario inscrito en el curso
    - Curso existe y tiene lecciones
    """

def select_lesson(self, index: int):
    """Seleccionar lección específica por índice."""

def go_to_previous_lesson(self):
    """Navegar a la lección anterior."""

def go_to_next_lesson(self):
    """Navegar a la lección siguiente."""

def toggle_sidebar(self):
    """Alternar visibilidad de la sidebar."""
```

---

### 4. CourseManagementState (`states/course_management_state.py`)

**Propósito**: Gestión completa de cursos (CRUD) para administradores.

#### Variables de Estado
```python
class CourseManagementState(AuthState):
    # Listas de cursos
    courses: list[dict] = []
    filtered_courses: list[dict] = []
    
    # Búsqueda y filtros
    search_query: str = ""
    level_filter: str = "all"
    
    # Formulario de curso
    show_course_dialog: bool = False
    dialog_mode: str = "create"  # "create" o "edit"
    selected_course_id: str = ""
    
    # Campos del formulario
    course_title: str = ""
    course_description: str = ""
    course_price: str = ""
    course_level: str = "beginner"
    course_category: str = ""
    course_image: str = ""
    course_instructor_name: str = ""
    course_instructor_email: str = ""
    
    # Diálogo de eliminación
    show_delete_dialog: bool = False
    course_to_delete_id: str = ""
    course_to_delete_title: str = ""
```

#### Métodos CRUD
```python
async def load_courses(self):
    """Cargar todos los cursos del sistema."""

async def save_course(self):
    """
    Guardar curso (crear nuevo o actualizar existente).
    
    Validaciones:
    - Título y descripción obligatorios
    - Datos del instructor obligatorios
    - Precio válido y no negativo
    """

async def confirm_delete_course(self):
    """Confirmar eliminación de curso."""

def open_create_course_dialog(self):
    """Abrir diálogo para crear curso nuevo."""

def open_edit_course_dialog(self, course_data):
    """Abrir diálogo para editar curso existente."""
```

---

### 5. EnrollmentState (`states/enrollment_state.py`)

**Propósito**: Gestión de inscripciones en la UI.

#### Variables de Estado
```python
class EnrollmentState(rx.State):
    # Inscripciones del usuario
    enrolled_courses: List[dict] = []
    available_courses: List[Course] = []
    
    # Estados de inscripción
    enrollment_status: str = ""
    show_enrollment_dialog: bool = False
    
    # Estadísticas
    total_enrolled: int = 0
    completed_courses: int = 0
```

#### Propiedades Computadas
```python
@rx.computed_var
def total_enrolled_courses(self) -> int:
    """Número total de cursos inscritos."""
    return len(self.enrolled_courses)

@rx.computed_var
def completed_courses(self) -> int:
    """Número de cursos completados."""
    return len([c for c in self.enrolled_courses if c.get("completed", False)])

@rx.computed_var
def average_progress(self) -> float:
    """Progreso promedio en todos los cursos."""
    if not self.enrolled_courses:
        return 0.0
    total_progress = sum(c.get("progress", 0) for c in self.enrolled_courses)
    return total_progress / len(self.enrolled_courses)
```

---

### 6. UserManagementState (`states/user_management_state.py`)

**Propósito**: Administración de usuarios (solo admins).

#### Variables de Estado
```python
class UserManagementState(rx.State):
    # Lista de usuarios
    users: List[User] = []
    filtered_users: List[User] = []
    
    # Usuario seleccionado
    selected_user: User | None = None
    
    # Filtros
    search_query: str = ""
    role_filter: str = "all"
    
    # Formulario de usuario
    show_user_dialog: bool = False
    dialog_mode: str = "create"
```

#### Métodos de Gestión
```python
async def load_users(self):
    """Cargar todos los usuarios del sistema."""

async def save_user(self):
    """Crear o actualizar usuario."""

async def confirm_delete_user(self):
    """Eliminar usuario con confirmación."""

def apply_filters(self):
    """Aplicar filtros de búsqueda y rol."""
```

---

### 7. Estados Adicionales

#### AdminDashboardState
- **Propósito**: Estadísticas del dashboard administrativo
- **Funciones**: Cargar métricas de usuarios, cursos e inscripciones

#### ContactState  
- **Propósito**: Gestión del formulario de contacto
- **Funciones**: Validación y envío de mensajes

#### InstructorState
- **Propósito**: Información de instructores
- **Funciones**: Listado y perfiles detallados de instructores

#### ProfileState
- **Propósito**: Gestión del perfil del usuario
- **Funciones**: Edición de datos personales y cambio de contraseña

---

## 🧩 Componentes de UI

### 1. Navbar (`components/navbar.py`)

**Propósito**: Barra de navegación responsive con menús dinámicos.

#### Características
- **Responsive**: Versiones desktop y móvil
- **Dinámico**: Menú cambia según rol del usuario
- **Theming**: Botón de cambio de tema (dark/light)
- **Navegación**: Logo y título clicables

#### Funciones Principales
```python
def navbar_link(text: str, url: str) -> rx.Component:
    """
    Crear enlace de navegación.
    
    Args:
        text: Texto del enlace
        url: URL de destino
        
    Returns:
        rx.Component: Enlace estilizado
    """

def user_menu() -> rx.Component:
    """
    Menú de usuario con opciones según rol.
    
    Opciones comunes:
    - Perfil
    - Cerrar sesión
    
    Opciones por rol:
    - Admin: Gestión de usuarios, cursos, estadísticas
    - Instructor: Dashboard de instructor
    - Student: Dashboard de estudiante, mis cursos
    """

def navbar() -> rx.Component:
    """
    Componente principal de navegación.
    
    Estructura:
    - Logo y título (izquierda)
    - Enlaces principales (centro)
    - Menú de usuario (derecha)
    - Botón de tema (derecha)
    """
```

#### Navegación por Rol
```python
# Enlaces para usuarios no autenticados
public_links = [
    ("Inicio", "/"),
    ("Cursos", "/courses"),
    ("Instructores", "/instructors"),
    ("Contacto", "/contact")
]

# Enlaces adicionales para estudiantes
student_links = [
    ("Mi Dashboard", "/student/dashboard"),
    ("Mis Cursos", "/student/courses")
]

# Enlaces adicionales para instructores
instructor_links = [
    ("Mi Dashboard", "/instructor/dashboard"),
    ("Mis Cursos", "/instructor/courses")
]

# Enlaces adicionales para administradores
admin_links = [
    ("Dashboard Admin", "/admin/dashboard"),
    ("Usuarios", "/admin/users"),
    ("Cursos", "/admin/courses"),
    ("Estadísticas", "/admin/stats")
]
```

---

### 2. CourseCard (`components/course_card.py`)

**Propósito**: Tarjeta visual para mostrar información de cursos.

#### Elementos Incluidos
```python
def course_card(course: dict) -> rx.Component:
    """
    Tarjeta de curso con información completa.
    
    Elementos:
    - Imagen thumbnail (16:9 ratio)
    - Badge de nivel (beginner/intermediate/advanced)
    - Título del curso (máximo 2 líneas)
    - Descripción (máximo 3 líneas)
    - Precio formateado
    - Información del instructor
    - Número de estudiantes
    - Calificación promedio
    - Botón de acción (Ver/Inscribirse)
    
    Args:
        course: Diccionario con datos del curso
        
    Returns:
        rx.Component: Tarjeta estilizada del curso
    """
```

#### Estilos y Efectos
```python
# Efectos hover
card_hover_effects = {
    "transform": "translateY(-4px)",
    "box_shadow": "0 8px 25px rgba(0,0,0,0.15)",
    "transition": "all 0.3s ease"
}

# Colores por nivel
level_colors = {
    "beginner": "green",
    "intermediate": "blue", 
    "advanced": "red"
}

# Formato de precio
def format_price(price: float) -> str:
    if price == 0:
        return "Gratis"
    return f"€{price:.2f}"
```

---

### 3. InstructorCard (`components/instructor_card.py`)

**Propósito**: Tarjeta visual para mostrar información de instructores.

#### Elementos Incluidos
```python
def instructor_card(instructor: dict) -> rx.Component:
    """
    Tarjeta de instructor con información completa.
    
    Elementos:
    - Avatar circular con fallback
    - Nombre del instructor
    - Badge de área de expertise
    - Biografía (máximo 3 líneas)
    - Estadísticas (cursos, estudiantes)
    - Calificación promedio
    - Botón "Ver Perfil"
    
    Args:
        instructor: Diccionario con datos del instructor
        
    Returns:
        rx.Component: Tarjeta estilizada del instructor
    """
```

#### Avatar y Fallback
```python
def instructor_avatar(instructor: dict) -> rx.Component:
    """
    Avatar del instructor con fallback.
    
    Fallback: Iniciales del nombre en círculo colorido
    """
    avatar_url = instructor.get("avatar", "")
    name = instructor.get("name", "")
    
    if avatar_url:
        return rx.image(
            src=avatar_url,
            width="80px",
            height="80px",
            border_radius="50%"
        )
    else:
        # Generar iniciales
        initials = "".join([n[0] for n in name.split()[:2]]).upper()
        return rx.box(
            rx.text(initials, color="white", weight="bold"),
            width="80px",
            height="80px",
            border_radius="50%",
            bg=f"linear-gradient(45deg, {get_color_for_name(name)})",
            display="flex",
            align_items="center",
            justify_content="center"
        )
```

---

### 4. Protected (`components/protected.py`)

**Propósito**: Componentes de protección de rutas por rol.

#### Componentes Disponibles
```python
def require_auth(component) -> rx.Component:
    """
    Requiere autenticación para acceder al componente.
    
    Args:
        component: Componente a proteger
        
    Returns:
        rx.Component: Componente protegido o mensaje de acceso denegado
    """

def require_role(component, allowed_roles: List[str]) -> rx.Component:
    """
    Requiere rol específico para acceder al componente.
    
    Args:
        component: Componente a proteger
        allowed_roles: Lista de roles permitidos
        
    Returns:
        rx.Component: Componente protegido o mensaje de acceso denegado
    """

def admin_only(component) -> rx.Component:
    """Acceso solo para administradores."""
    return require_role(component, ["admin"])

def instructor_only(component) -> rx.Component:
    """Acceso solo para instructores."""
    return require_role(component, ["instructor"])

def student_only(component) -> rx.Component:
    """Acceso solo para estudiantes."""
    return require_role(component, ["student"])

def instructor_or_admin(component) -> rx.Component:
    """Acceso para instructores y administradores."""
    return require_role(component, ["instructor", "admin"])
```

#### Mensajes de Acceso Denegado
```python
def access_denied_message(required_role: str = None) -> rx.Component:
    """
    Mensaje de acceso denegado personalizado.
    
    Args:
        required_role: Rol requerido (opcional)
        
    Returns:
        rx.Component: Mensaje estilizado de acceso denegado
    """
    return rx.center(
        rx.vstack(
            rx.icon("shield-x", size=64, color="red"),
            rx.heading("Acceso Denegado", size="6"),
            rx.text(
                f"Necesitas permisos de {required_role} para acceder a esta página."
                if required_role else
                "No tienes permisos para acceder a esta página."
            ),
            rx.link(
                rx.button("Volver al Inicio", variant="soft"),
                href="/"
            ),
            spacing="4",
            align_items="center"
        ),
        height="50vh"
    )
```

---

## 🔄 Patrones de Estado en Reflex

### Computed Variables
```python
@rx.computed_var
def computed_property(self) -> str:
    """
    Propiedades que se recalculan automáticamente
    cuando cambian las dependencias.
    """
    return f"Computed value based on {self.some_state}"
```

### Event Handlers
```python
def handle_event(self, value: str):
    """
    Manejadores de eventos que actualizan el estado.
    Se ejecutan en el backend y actualizan la UI.
    """
    self.some_state = value
    # La UI se actualiza automáticamente
```

### Async Operations
```python
async def async_operation(self):
    """
    Operaciones asíncronas para llamadas a servicios.
    """
    self.loading = True
    try:
        result = await some_service.operation()
        self.data = result
    except Exception as e:
        self.error = str(e)
    finally:
        self.loading = False
```

### State Inheritance
```python
class ChildState(ParentState):
    """
    Herencia de estados para compartir funcionalidad común.
    """
    # Hereda todas las propiedades y métodos del padre
    additional_property: str = ""
```

---

## 🎨 Theming y Estilos

### Sistema de Colores
```python
# Colores principales
primary_colors = {
    "blue": rx.color("blue", 9),
    "green": rx.color("green", 9),
    "red": rx.color("red", 9),
    "gray": rx.color("gray", 9)
}

# Colores por nivel de curso
level_colors = {
    "beginner": "green",
    "intermediate": "blue",
    "advanced": "red"
}

# Colores por rol
role_colors = {
    "student": "blue",
    "instructor": "purple", 
    "admin": "red"
}
```

### Responsive Design
```python
# Breakpoints
breakpoints = {
    "sm": "640px",
    "md": "768px", 
    "lg": "1024px",
    "xl": "1280px"
}

# Responsive props
responsive_props = {
    "padding_x": ["4", "6", "8"],  # sm, md, lg
    "columns": ["1", "2", "3"],    # 1 col móvil, 2 tablet, 3 desktop
}
```

---

*Documentación de Estados y Componentes*  
*Proyecto: E-Learning JCB Reflex*  
*Actualizado: 25 de enero de 2025*