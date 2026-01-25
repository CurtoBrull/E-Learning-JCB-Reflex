# Seguridad y Autenticación - E-Learning JCB Reflex

## 🔐 Sistema de Autenticación

### Arquitectura de Seguridad

La plataforma implementa un sistema de autenticación robusto basado en:

```
┌─────────────────────────────────────────┐
│            FRONTEND (React)             │
│   - Formularios de login/registro       │
│   - Validación en tiempo real           │
│   - Gestión de estado de sesión         │
└─────────────────────────────────────────┘
                    ↓ HTTPS
┌─────────────────────────────────────────┐
│           BACKEND (FastAPI)             │
│   - Validación de credenciales          │
│   - Hash de contraseñas (bcrypt)        │
│   - Gestión de sesiones                 │
└─────────────────────────────────────────┘
                    ↓ TLS/SSL
┌─────────────────────────────────────────┐
│          BASE DE DATOS (MongoDB)        │
│   - Almacenamiento seguro               │
│   - Índices únicos (email)              │
│   - Encriptación en reposo              │
└─────────────────────────────────────────┘
```

---

## 🔑 Gestión de Contraseñas

### Hash con bcrypt

#### Implementación (`utils/password.py`)
```python
import bcrypt

def hash_password(password: str) -> str:
    """
    Hashear contraseña con bcrypt y salt único.
    
    Características:
    - Salt automático y único por contraseña
    - Factor de trabajo: 12 (2^12 = 4096 iteraciones)
    - Resistente a ataques de rainbow table
    - Resistente a ataques de fuerza bruta
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        str: Hash de la contraseña con salt incluido
        
    Ejemplo:
        >>> hashed = hash_password("mi_contraseña_segura")
        >>> print(hashed)
        $2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj/RK.s5uIoO
    """
    # Generar salt único
    salt = bcrypt.gensalt(rounds=12)
    
    # Hashear contraseña con salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """
    Verificar contraseña contra hash almacenado.
    
    Args:
        password: Contraseña en texto plano a verificar
        hashed: Hash almacenado en la base de datos
        
    Returns:
        bool: True si la contraseña es correcta
        
    Ejemplo:
        >>> is_valid = verify_password("mi_contraseña", stored_hash)
        >>> print(is_valid)  # True o False
    """
    try:
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            hashed.encode('utf-8')
        )
    except Exception as e:
        print(f"Error verifying password: {e}")
        return False
```

#### Características de Seguridad
- **Salt único**: Cada contraseña tiene su propio salt aleatorio
- **Factor de trabajo**: 12 rounds (4096 iteraciones)
- **Resistencia temporal**: Aumenta automáticamente la seguridad con el tiempo
- **Protección contra timing attacks**: bcrypt incluye protecciones integradas

### Políticas de Contraseñas

#### Requisitos Mínimos
```python
PASSWORD_REQUIREMENTS = {
    "min_length": 6,
    "max_length": 128,
    "require_uppercase": False,  # Futuro
    "require_lowercase": False,  # Futuro
    "require_numbers": False,    # Futuro
    "require_symbols": False,    # Futuro
    "prevent_common": False      # Futuro
}

def validate_password_strength(password: str) -> tuple[bool, str]:
    """
    Validar fortaleza de contraseña.
    
    Args:
        password: Contraseña a validar
        
    Returns:
        tuple[bool, str]: (es_válida, mensaje_error)
    """
    if len(password) < PASSWORD_REQUIREMENTS["min_length"]:
        return False, f"La contraseña debe tener al menos {PASSWORD_REQUIREMENTS['min_length']} caracteres"
    
    if len(password) > PASSWORD_REQUIREMENTS["max_length"]:
        return False, f"La contraseña no puede tener más de {PASSWORD_REQUIREMENTS['max_length']} caracteres"
    
    # Futuras validaciones adicionales
    # - Mayúsculas y minúsculas
    # - Números y símbolos
    # - Contraseñas comunes
    
    return True, ""
```

---

## 👤 Sistema de Roles

### Definición de Roles

#### Roles Disponibles
```python
class UserRole:
    STUDENT = "student"
    INSTRUCTOR = "instructor" 
    ADMIN = "admin"
    
    @classmethod
    def get_all_roles(cls) -> list[str]:
        return [cls.STUDENT, cls.INSTRUCTOR, cls.ADMIN]
    
    @classmethod
    def is_valid_role(cls, role: str) -> bool:
        return role in cls.get_all_roles()
```

#### Jerarquía de Permisos
```
Admin (Máximos permisos)
├── Gestión completa de usuarios
├── Gestión completa de cursos  
├── Acceso a estadísticas globales
├── Configuración del sistema
└── Todos los permisos de instructor y estudiante

Instructor (Permisos intermedios)
├── Crear y gestionar sus propios cursos
├── Ver estadísticas de sus cursos
├── Gestionar estudiantes de sus cursos
└── Todos los permisos de estudiante

Student (Permisos básicos)
├── Inscribirse en cursos
├── Ver contenido de cursos inscritos
├── Gestionar su propio perfil
└── Enviar mensajes de contacto
```

### Verificación de Roles

#### En Modelos
```python
class User:
    @property
    def is_student(self) -> bool:
        return self.role == UserRole.STUDENT
    
    @property
    def is_instructor(self) -> bool:
        return self.role == UserRole.INSTRUCTOR
    
    @property
    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN
    
    def has_role(self, required_role: str) -> bool:
        """Verificar si el usuario tiene un rol específico."""
        return self.role == required_role
    
    def has_any_role(self, roles: list[str]) -> bool:
        """Verificar si el usuario tiene alguno de los roles especificados."""
        return self.role in roles
```

#### En Estados
```python
class AuthState(rx.State):
    @rx.computed_var
    def user_role(self) -> str:
        if self.current_user:
            return self.current_user.get("role", "")
        return ""
    
    @rx.computed_var
    def is_user_admin(self) -> bool:
        return self.user_role == UserRole.ADMIN
    
    @rx.computed_var
    def is_user_instructor(self) -> bool:
        return self.user_role == UserRole.INSTRUCTOR
    
    @rx.computed_var
    def is_user_student(self) -> bool:
        return self.user_role == UserRole.STUDENT
```

---

## 🛡️ Protección de Rutas

### Componentes de Protección (`components/protected.py`)

#### Autenticación Básica
```python
def require_auth(component) -> rx.Component:
    """
    Requiere que el usuario esté autenticado.
    
    Args:
        component: Componente a proteger
        
    Returns:
        rx.Component: Componente protegido o página de login
    """
    return rx.cond(
        AuthState.is_authenticated,
        component,
        rx.redirect("/login")
    )
```

#### Protección por Rol
```python
def require_role(component, allowed_roles: list[str]) -> rx.Component:
    """
    Requiere que el usuario tenga uno de los roles especificados.
    
    Args:
        component: Componente a proteger
        allowed_roles: Lista de roles permitidos
        
    Returns:
        rx.Component: Componente protegido o mensaje de acceso denegado
    """
    return rx.cond(
        AuthState.is_authenticated,
        rx.cond(
            AuthState.user_role.is_in(allowed_roles),
            component,
            access_denied_message(allowed_roles)
        ),
        rx.redirect("/login")
    )

def admin_only(component) -> rx.Component:
    """Acceso exclusivo para administradores."""
    return require_role(component, [UserRole.ADMIN])

def instructor_only(component) -> rx.Component:
    """Acceso exclusivo para instructores."""
    return require_role(component, [UserRole.INSTRUCTOR])

def student_only(component) -> rx.Component:
    """Acceso exclusivo para estudiantes."""
    return require_role(component, [UserRole.STUDENT])

def instructor_or_admin(component) -> rx.Component:
    """Acceso para instructores y administradores."""
    return require_role(component, [UserRole.INSTRUCTOR, UserRole.ADMIN])
```

#### Protección Condicional
```python
def course_viewer_protection(component, course_id: str) -> rx.Component:
    """
    Protección específica para el visor de cursos.
    
    Requisitos:
    1. Usuario autenticado
    2. Usuario es estudiante
    3. Usuario inscrito en el curso
    
    Args:
        component: Componente del visor
        course_id: ID del curso
        
    Returns:
        rx.Component: Visor protegido o mensaje de error
    """
    return rx.cond(
        AuthState.is_authenticated,
        rx.cond(
            AuthState.is_user_student,
            rx.cond(
                CourseViewerState.is_enrolled,
                component,
                enrollment_required_message(course_id)
            ),
            student_role_required_message()
        ),
        rx.redirect("/login")
    )
```

### Mensajes de Acceso Denegado

#### Componentes de Error
```python
def access_denied_message(required_roles: list[str]) -> rx.Component:
    """
    Mensaje personalizado de acceso denegado.
    
    Args:
        required_roles: Roles requeridos para acceder
        
    Returns:
        rx.Component: Mensaje estilizado con opciones de navegación
    """
    roles_text = " o ".join(required_roles)
    
    return rx.center(
        rx.vstack(
            rx.icon("shield-x", size=64, color=rx.color("red", 9)),
            rx.heading("Acceso Denegado", size="7"),
            rx.text(
                f"Necesitas permisos de {roles_text} para acceder a esta página.",
                size="4",
                text_align="center"
            ),
            rx.hstack(
                rx.link(
                    rx.button("Volver al Inicio", variant="soft"),
                    href="/"
                ),
                rx.link(
                    rx.button("Mi Dashboard", variant="outline"),
                    href=AuthState.get_dashboard_url()
                ),
                spacing="3"
            ),
            spacing="4",
            align_items="center",
            max_width="400px"
        ),
        height="60vh"
    )

def enrollment_required_message(course_id: str) -> rx.Component:
    """Mensaje para cursos que requieren inscripción."""
    return rx.center(
        rx.vstack(
            rx.icon("book-x", size=64, color=rx.color("orange", 9)),
            rx.heading("Inscripción Requerida", size="7"),
            rx.text(
                "Debes inscribirte en este curso para acceder al contenido.",
                size="4",
                text_align="center"
            ),
            rx.link(
                rx.button("Ver Detalles del Curso", size="3"),
                href=f"/courses/{course_id}"
            ),
            spacing="4",
            align_items="center"
        ),
        height="60vh"
    )
```

---

## 🔒 Validaciones de Seguridad

### Validación de Entrada

#### Sanitización de Datos
```python
import html
import re

def sanitize_input(text: str) -> str:
    """
    Sanitizar entrada de usuario para prevenir XSS.
    
    Args:
        text: Texto a sanitizar
        
    Returns:
        str: Texto sanitizado
    """
    if not text:
        return ""
    
    # Escapar caracteres HTML
    sanitized = html.escape(text)
    
    # Remover caracteres de control
    sanitized = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', sanitized)
    
    return sanitized.strip()

def validate_email_format(email: str) -> bool:
    """
    Validar formato de email.
    
    Args:
        email: Email a validar
        
    Returns:
        bool: True si el formato es válido
    """
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None
```

#### Validación de Formularios
```python
class FormValidator:
    @staticmethod
    def validate_registration_form(data: dict) -> tuple[bool, list[str]]:
        """
        Validar formulario de registro.
        
        Args:
            data: Datos del formulario
            
        Returns:
            tuple[bool, list[str]]: (es_válido, lista_errores)
        """
        errors = []
        
        # Validar nombre
        if not data.get("first_name", "").strip():
            errors.append("El nombre es obligatorio")
        elif len(data["first_name"]) > 50:
            errors.append("El nombre no puede tener más de 50 caracteres")
        
        # Validar apellido
        if not data.get("last_name", "").strip():
            errors.append("El apellido es obligatorio")
        elif len(data["last_name"]) > 50:
            errors.append("El apellido no puede tener más de 50 caracteres")
        
        # Validar email
        email = data.get("email", "").strip().lower()
        if not email:
            errors.append("El email es obligatorio")
        elif not validate_email_format(email):
            errors.append("El formato del email no es válido")
        
        # Validar contraseña
        password = data.get("password", "")
        is_valid_password, password_error = validate_password_strength(password)
        if not is_valid_password:
            errors.append(password_error)
        
        # Validar confirmación de contraseña
        confirm_password = data.get("confirm_password", "")
        if password != confirm_password:
            errors.append("Las contraseñas no coinciden")
        
        # Validar rol
        role = data.get("role", "")
        if not UserRole.is_valid_role(role):
            errors.append("Rol no válido")
        
        return len(errors) == 0, errors
```

### Prevención de Ataques

#### Protección CSRF
```python
# Reflex maneja automáticamente la protección CSRF
# mediante tokens de estado únicos por sesión
```

#### Rate Limiting (Futuro)
```python
from collections import defaultdict
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self):
        self.attempts = defaultdict(list)
        self.max_attempts = 5
        self.window_minutes = 15
    
    def is_rate_limited(self, identifier: str) -> bool:
        """
        Verificar si un identificador está limitado por rate limiting.
        
        Args:
            identifier: IP o user ID
            
        Returns:
            bool: True si está limitado
        """
        now = datetime.now()
        window_start = now - timedelta(minutes=self.window_minutes)
        
        # Limpiar intentos antiguos
        self.attempts[identifier] = [
            attempt for attempt in self.attempts[identifier]
            if attempt > window_start
        ]
        
        # Verificar límite
        return len(self.attempts[identifier]) >= self.max_attempts
    
    def record_attempt(self, identifier: str):
        """Registrar un intento de login."""
        self.attempts[identifier].append(datetime.now())
```

#### Protección de Inyección
```python
# MongoDB con Motor previene automáticamente inyección NoSQL
# mediante el uso de consultas parametrizadas

# Ejemplo seguro:
async def get_user_by_email(email: str) -> User | None:
    # Esto es seguro - Motor maneja la sanitización
    user_data = await db.users.find_one({"email": email})
    return User.from_dict(user_data) if user_data else None

# Evitar (aunque Motor lo previene):
# query = f"{{email: '{email}'}}"  # Vulnerable a inyección
```

---

## 🔐 Gestión de Sesiones

### Estado de Sesión

#### Almacenamiento de Sesión
```python
class AuthState(rx.State):
    # Información de sesión
    current_user: dict | None = None
    session_id: str = ""
    login_time: datetime | None = None
    last_activity: datetime | None = None
    
    def establish_session(self, user: User):
        """
        Establecer sesión de usuario.
        
        Args:
            user: Usuario autenticado
        """
        self.current_user = user.to_dict()
        self.session_id = self.generate_session_id()
        self.login_time = datetime.now()
        self.last_activity = datetime.now()
    
    def update_activity(self):
        """Actualizar timestamp de última actividad."""
        self.last_activity = datetime.now()
    
    def clear_session(self):
        """Limpiar sesión de usuario."""
        self.current_user = None
        self.session_id = ""
        self.login_time = None
        self.last_activity = None
    
    @staticmethod
    def generate_session_id() -> str:
        """Generar ID único de sesión."""
        import secrets
        return secrets.token_urlsafe(32)
```

#### Expiración de Sesión (Futuro)
```python
SESSION_TIMEOUT_HOURS = 24

def is_session_expired(self) -> bool:
    """Verificar si la sesión ha expirado."""
    if not self.last_activity:
        return True
    
    expiry_time = self.last_activity + timedelta(hours=SESSION_TIMEOUT_HOURS)
    return datetime.now() > expiry_time
```

---

## 🚨 Logging y Auditoría

### Eventos de Seguridad

#### Logging de Autenticación
```python
import logging

security_logger = logging.getLogger("security")

class SecurityLogger:
    @staticmethod
    def log_login_attempt(email: str, success: bool, ip_address: str = None):
        """Registrar intento de login."""
        status = "SUCCESS" if success else "FAILED"
        security_logger.info(
            f"LOGIN_{status}: email={email}, ip={ip_address}"
        )
    
    @staticmethod
    def log_password_change(user_id: str, ip_address: str = None):
        """Registrar cambio de contraseña."""
        security_logger.info(
            f"PASSWORD_CHANGE: user_id={user_id}, ip={ip_address}"
        )
    
    @staticmethod
    def log_role_change(admin_id: str, target_user_id: str, 
                       old_role: str, new_role: str):
        """Registrar cambio de rol."""
        security_logger.warning(
            f"ROLE_CHANGE: admin={admin_id}, target={target_user_id}, "
            f"old_role={old_role}, new_role={new_role}"
        )
    
    @staticmethod
    def log_unauthorized_access(user_id: str, attempted_resource: str):
        """Registrar intento de acceso no autorizado."""
        security_logger.warning(
            f"UNAUTHORIZED_ACCESS: user_id={user_id}, "
            f"resource={attempted_resource}"
        )
```

### Auditoría de Cambios (Futuro)

#### Modelo de Auditoría
```python
@dataclass
class AuditLog:
    id: str
    user_id: str
    action: str  # CREATE, UPDATE, DELETE, LOGIN, LOGOUT
    resource_type: str  # USER, COURSE, ENROLLMENT
    resource_id: str
    old_values: dict
    new_values: dict
    ip_address: str
    user_agent: str
    timestamp: datetime
    
    def to_dict(self) -> dict:
        return {
            "_id": ObjectId(self.id) if self.id else None,
            "userId": self.user_id,
            "action": self.action,
            "resourceType": self.resource_type,
            "resourceId": self.resource_id,
            "oldValues": self.old_values,
            "newValues": self.new_values,
            "ipAddress": self.ip_address,
            "userAgent": self.user_agent,
            "timestamp": self.timestamp
        }
```

---

## 🔧 Configuración de Seguridad

### Variables de Entorno

#### Configuración Segura
```bash
# .env (desarrollo)
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/db
JWT_SECRET_KEY=your-super-secret-key-here
BCRYPT_ROUNDS=12
SESSION_TIMEOUT_HOURS=24
RATE_LIMIT_ATTEMPTS=5
RATE_LIMIT_WINDOW_MINUTES=15

# .env.production
MONGODB_URI=mongodb+srv://prod_user:complex_pass@prod_cluster.mongodb.net/prod_db
JWT_SECRET_KEY=production-secret-key-very-long-and-random
BCRYPT_ROUNDS=14
SESSION_TIMEOUT_HOURS=8
RATE_LIMIT_ATTEMPTS=3
RATE_LIMIT_WINDOW_MINUTES=30
```

### Configuración de Producción

#### Checklist de Seguridad
- [ ] **HTTPS obligatorio**: Certificado SSL/TLS válido
- [ ] **Variables de entorno**: Secretos no hardcodeados
- [ ] **Base de datos**: Conexión encriptada (TLS)
- [ ] **Contraseñas**: Factor de trabajo bcrypt ≥ 12
- [ ] **Rate limiting**: Implementado en endpoints críticos
- [ ] **Logging**: Eventos de seguridad registrados
- [ ] **Backups**: Encriptados y seguros
- [ ] **Actualizaciones**: Dependencias actualizadas regularmente

---

*Documentación de Seguridad y Autenticación*  
*Proyecto: E-Learning JCB Reflex*  
*Actualizado: 25 de enero de 2025*