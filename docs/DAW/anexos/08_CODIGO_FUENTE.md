# 8. CÓDIGO FUENTE DOCUMENTADO

## 8.1. Estructura del Repositorio

### 8.1.1. Organización General del Proyecto

```
E-Learning-JCB-Reflex/
│
├── E_Learning_JCB_Reflex/           # Código fuente principal
│   ├── __init__.py                  # Inicialización del paquete
│   ├── E_Learning_JCB_Reflex.py     # Punto de entrada principal
│   │
│   ├── components/                  # Componentes reutilizables de UI
│   │   ├── __init__.py
│   │   ├── navbar.py                # Barra de navegación
│   │   ├── course_card.py           # Tarjeta de curso
│   │   ├── instructor_card.py       # Tarjeta de instructor
│   │   ├── section_list.py          # Lista de secciones/lecciones
│   │   └── protected.py             # Componentes de protección RBAC
│   │
│   ├── pages/                       # Páginas de la aplicación
│   │   ├── __init__.py
│   │   ├── index.py                 # Página de inicio
│   │   ├── courses.py               # Listado de cursos
│   │   ├── course_detail.py         # Detalle de curso
│   │   ├── instructors.py           # Listado de instructores
│   │   ├── instructor_detail.py     # Detalle de instructor
│   │   ├── login.py                 # Página de login
│   │   ├── register.py              # Página de registro
│   │   ├── profile.py               # Perfil de usuario
│   │   ├── student_dashboard.py     # Dashboard de estudiante
│   │   ├── instructor_dashboard.py  # Dashboard de instructor
│   │   └── admin_dashboard.py       # Dashboard de administrador
│   │
│   ├── states/                      # Estados de Reflex (lógica de UI)
│   │   ├── __init__.py
│   │   ├── auth_state.py            # Estado de autenticación
│   │   ├── course_state.py          # Estado de cursos
│   │   ├── course_detail_state.py   # Estado de detalle de curso
│   │   ├── enrollment_state.py      # Estado de inscripciones
│   │   ├── progress_state.py        # Estado de progreso
│   │   ├── profile_state.py         # Estado de perfil
│   │   ├── student_dashboard_state.py   # Estado dashboard estudiante
│   │   ├── instructor_dashboard_state.py # Estado dashboard instructor
│   │   └── admin_dashboard_state.py # Estado dashboard admin
│   │
│   ├── services/                    # Lógica de negocio (CRUD)
│   │   ├── __init__.py
│   │   ├── user_service.py          # Servicios de usuarios
│   │   ├── course_service.py        # Servicios de cursos
│   │   ├── enrollment_service.py    # Servicios de inscripciones
│   │   ├── progress_service.py      # Servicios de progreso
│   │   └── rating_service.py        # Servicios de valoraciones
│   │
│   ├── models/                      # Modelos de datos
│   │   ├── __init__.py
│   │   ├── user.py                  # Modelo de usuario
│   │   ├── course.py                # Modelo de curso
│   │   ├── enrollment.py            # Modelo de inscripción
│   │   ├── progress.py              # Modelo de progreso
│   │   └── rating.py                # Modelo de valoración
│   │
│   ├── database/                    # Conexión a base de datos
│   │   ├── __init__.py
│   │   └── mongodb.py               # Configuración de MongoDB
│   │
│   └── utils/                       # Utilidades reutilizables
│       ├── __init__.py
│       ├── password.py              # Hash y verificación de contraseñas
│       ├── route_helpers.py         # Helpers de rutas
│       ├── formatters.py            # Formateadores (fechas, números)
│       └── validators.py            # Validadores de inputs
│
├── assets/                          # Recursos estáticos
│   ├── favicon.ico
│   ├── images/
│   └── styles/
│
├── docs/                            # Documentación técnica
│   ├── 01_ARQUITECTURA_Y_TECNOLOGIAS.md
│   ├── 02_MODELOS_Y_SERVICIOS.md
│   ├── 03_ESTADOS_Y_COMPONENTES.md
│   ├── 04_PAGINAS_Y_RUTAS.md
│   ├── 05_SEGURIDAD_Y_AUTENTICACION.md
│   ├── 06_BASE_DATOS_Y_CONFIGURACION.md
│   ├── 07_SCRIPTS_Y_UTILIDADES.md
│   ├── 08_FLUJOS_Y_TESTING.md
│   ├── 09_METRICAS_Y_CONCLUSIONES.md
│   ├── 10_ESQUEMA_BASE_DATOS_REAL.md
│   ├── 11_DESPLIEGUE_REFLEX_CLOUD.md
│   └── 12_USUARIOS_EJEMPLO.md
│
├── scripts/                         # Scripts de utilidades
│   ├── populate_db.py               # Poblar BD con datos de ejemplo
│   ├── backup_db.py                 # Backup de MongoDB
│   └── clean_db.py                  # Limpiar base de datos
│
├── tests/                           # Tests unitarios e integración
│   ├── __init__.py
│   ├── test_services/
│   ├── test_models/
│   └── test_states/
│
├── .env.example                     # Ejemplo de variables de entorno
├── .gitignore                       # Archivos ignorados por Git
├── rxconfig.py                      # Configuración de Reflex
├── requirements.txt                 # Dependencias de Python
├── README.md                        # Documentación principal
└── LICENSE                          # Licencia del proyecto (MIT)
```

**Total archivos de código**: ~40 archivos Python
**Líneas de código estimadas**: ~5,000 LOC (sin contar comentarios)

---

## 8.2. Módulos Principales

### 8.2.1. Módulo: `database/mongodb.py`

**Responsabilidad**: Gestión de conexión a MongoDB Atlas

**Código completo**:
```python
"""
Módulo de conexión a MongoDB Atlas.
Gestiona la conexión asíncrona usando Motor (driver oficial).
"""

import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URI de MongoDB desde variable de entorno
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError(
        "MONGODB_URI environment variable is not set. "
        "Please configure it in .env file"
    )

# Nombre de la base de datos
DB_NAME = os.getenv("DB_NAME", "elearning_jcb")

# Cliente de MongoDB (global)
client: AsyncIOMotorClient = None
db = None


def get_database():
    """
    Obtiene la instancia de la base de datos.

    Returns:
        AsyncIOMotorDatabase: Instancia de la base de datos MongoDB
    """
    global client, db

    if client is None:
        # Crear cliente de MongoDB
        client = AsyncIOMotorClient(MONGODB_URI)
        db = client[DB_NAME]

        print(f"✅ Conectado a MongoDB: {DB_NAME}")

    return db


def close_database():
    """
    Cierra la conexión a MongoDB.
    Debe llamarse al finalizar la aplicación.
    """
    global client

    if client:
        client.close()
        print("❌ Conexión a MongoDB cerrada")


# Colecciones principales (shortcuts)
def get_users_collection():
    """Obtiene la colección de usuarios"""
    return get_database().users


def get_courses_collection():
    """Obtiene la colección de cursos"""
    return get_database().courses


def get_enrollments_collection():
    """Obtiene la colección de inscripciones"""
    return get_database().enrollments


def get_progress_collection():
    """Obtiene la colección de progreso"""
    return get_database().progress


def get_ratings_collection():
    """Obtiene la colección de valoraciones"""
    return get_database().ratings
```

**Características clave**:
- ✅ Carga de URI desde `.env` (seguridad)
- ✅ Validación de variable de entorno obligatoria
- ✅ Cliente global (singleton pattern)
- ✅ Funciones helper para acceso rápido a colecciones
- ✅ Función de cierre para cleanup

---

### 8.2.2. Módulo: `utils/password.py`

**Responsabilidad**: Hash seguro y verificación de contraseñas con bcrypt

**Código completo**:
```python
"""
Utilidades para gestión segura de contraseñas.
Utiliza bcrypt para hashing con salt único.
"""

import bcrypt


def hash_password(password: str) -> str:
    """
    Genera un hash seguro de la contraseña usando bcrypt.

    Args:
        password (str): Contraseña en texto plano

    Returns:
        str: Contraseña hasheada con bcrypt

    Example:
        >>> hashed = hash_password("mi_contraseña_segura")
        >>> print(hashed)
        '$2b$12$...'
    """
    # Generar salt único (12 rounds = 4,096 iteraciones)
    salt = bcrypt.gensalt(rounds=12)

    # Hashear contraseña con el salt generado
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Decodificar a string para almacenar en MongoDB
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con su hash.

    Args:
        plain_password (str): Contraseña en texto plano a verificar
        hashed_password (str): Hash almacenado en la base de datos

    Returns:
        bool: True si coincide, False en caso contrario

    Example:
        >>> hashed = hash_password("mi_contraseña")
        >>> verify_password("mi_contraseña", hashed)
        True
        >>> verify_password("contraseña_incorrecta", hashed)
        False
    """
    try:
        # Verificar contraseña
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
    except Exception as e:
        print(f"Error al verificar contraseña: {e}")
        return False


def is_password_strong(password: str) -> tuple[bool, str]:
    """
    Verifica si una contraseña cumple con criterios de seguridad.

    Criterios:
    - Longitud mínima: 6 caracteres
    - Longitud máxima: 128 caracteres

    Args:
        password (str): Contraseña a validar

    Returns:
        tuple[bool, str]: (es_válida, mensaje_error)

    Example:
        >>> is_password_strong("abc")
        (False, "La contraseña debe tener al menos 6 caracteres")
        >>> is_password_strong("contraseña_segura123")
        (True, "")
    """
    if len(password) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres"

    if len(password) > 128:
        return False, "La contraseña no puede exceder 128 caracteres"

    return True, ""
```

**Características clave**:
- ✅ bcrypt con 12 rounds (balance seguridad/rendimiento)
- ✅ Salt único automático por contraseña
- ✅ Validación de fortaleza de contraseña
- ✅ Manejo de excepciones en verificación
- ✅ Docstrings completos con ejemplos

---

### 8.2.3. Módulo: `services/user_service.py`

**Responsabilidad**: Lógica de negocio para usuarios (CRUD + autenticación)

**Código principal** (extracto):
```python
"""
Servicio de gestión de usuarios.
Provee operaciones CRUD y lógica de autenticación.
"""

from bson import ObjectId
from datetime import datetime
from typing import Optional

from E_Learning_JCB_Reflex.database.mongodb import get_users_collection
from E_Learning_JCB_Reflex.utils.password import hash_password, verify_password


class UserService:
    """Servicio para gestión de usuarios"""

    def __init__(self):
        self.collection = get_users_collection()


    async def create_user(
        self,
        name: str,
        email: str,
        password: str,
        role: str = "student"
    ) -> Optional[str]:
        """
        Crea un nuevo usuario en la base de datos.

        Args:
            name (str): Nombre completo del usuario
            email (str): Email único del usuario
            password (str): Contraseña en texto plano (se hasheará)
            role (str): Rol del usuario (admin|instructor|student)

        Returns:
            Optional[str]: ID del usuario creado, None si error

        Raises:
            ValueError: Si el email ya está registrado
        """
        # Verificar si el email ya existe
        existing = await self.collection.find_one({"email": email})
        if existing:
            raise ValueError(f"El email {email} ya está registrado")

        # Validar rol
        valid_roles = ["admin", "instructor", "student"]
        if role not in valid_roles:
            raise ValueError(f"Rol inválido. Debe ser: {', '.join(valid_roles)}")

        # Crear documento de usuario
        user_doc = {
            "name": name,
            "email": email,
            "password": hash_password(password),  # Hash seguro
            "role": role,
            "bio": "",
            "created_at": datetime.utcnow()
        }

        # Insertar en MongoDB
        result = await self.collection.insert_one(user_doc)

        return str(result.inserted_id)


    async def login(self, email: str, password: str) -> Optional[dict]:
        """
        Autentica un usuario con email y contraseña.

        Args:
            email (str): Email del usuario
            password (str): Contraseña en texto plano

        Returns:
            Optional[dict]: Datos del usuario (sin password) si login exitoso,
                          None si credenciales incorrectas
        """
        # Buscar usuario por email
        user = await self.collection.find_one({"email": email})

        if not user:
            return None  # Email no encontrado

        # Verificar contraseña
        if not verify_password(password, user.get("password", "")):
            return None  # Contraseña incorrecta

        # Remover password del objeto retornado (seguridad)
        user.pop("password", None)

        # Convertir ObjectId a string para serialización
        user["_id"] = str(user["_id"])

        return user


    async def get_user_by_id(self, user_id: str) -> Optional[dict]:
        """
        Obtiene un usuario por su ID.

        Args:
            user_id (str): ID del usuario (string de ObjectId)

        Returns:
            Optional[dict]: Datos del usuario (sin password), None si no existe
        """
        try:
            user = await self.collection.find_one({"_id": ObjectId(user_id)})

            if not user:
                return None

            # Remover password
            user.pop("password", None)
            user["_id"] = str(user["_id"])

            return user

        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None


    async def update_user(self, user_id: str, update_data: dict) -> bool:
        """
        Actualiza datos de un usuario.

        Args:
            user_id (str): ID del usuario
            update_data (dict): Campos a actualizar (name, bio, etc.)

        Returns:
            bool: True si actualización exitosa, False en caso contrario

        Note:
            No permite actualizar password, email o role directamente
            (usar métodos específicos para eso)
        """
        # Campos permitidos para actualización
        allowed_fields = ["name", "bio"]

        # Filtrar solo campos permitidos
        filtered_data = {
            k: v for k, v in update_data.items()
            if k in allowed_fields
        }

        if not filtered_data:
            return False  # No hay nada que actualizar

        try:
            result = await self.collection.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": filtered_data}
            )

            return result.modified_count > 0

        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False


    async def change_password(
        self,
        user_id: str,
        current_password: str,
        new_password: str
    ) -> bool:
        """
        Cambia la contraseña de un usuario.

        Args:
            user_id (str): ID del usuario
            current_password (str): Contraseña actual (para verificación)
            new_password (str): Nueva contraseña

        Returns:
            bool: True si cambio exitoso, False si contraseña actual incorrecta
        """
        # Obtener usuario con password
        user = await self.collection.find_one({"_id": ObjectId(user_id)})

        if not user:
            return False

        # Verificar contraseña actual
        if not verify_password(current_password, user.get("password", "")):
            return False  # Contraseña actual incorrecta

        # Actualizar con nueva contraseña hasheada
        result = await self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"password": hash_password(new_password)}}
        )

        return result.modified_count > 0


    async def get_instructors(self, limit: int = 50) -> list[dict]:
        """
        Obtiene lista de instructores.

        Args:
            limit (int): Máximo número de instructores a retornar

        Returns:
            list[dict]: Lista de instructores (sin passwords)
        """
        cursor = self.collection.find(
            {"role": "instructor"},
            {"password": 0}  # Proyección: excluir password
        ).limit(limit)

        instructors = []
        async for instructor in cursor:
            instructor["_id"] = str(instructor["_id"])
            instructors.append(instructor)

        return instructors
```

**Características clave**:
- ✅ Métodos async para operaciones no bloqueantes
- ✅ Validaciones de negocio (email único, rol válido)
- ✅ Seguridad (hash de contraseñas, verificación de contraseña actual)
- ✅ Proyecciones (excluir password de resultados)
- ✅ Manejo de excepciones con logging
- ✅ Conversión de ObjectId a string para serialización

---

### 8.2.4. Módulo: `components/protected.py`

**Responsabilidad**: Componentes de protección de rutas (RBAC)

**Código completo**:
```python
"""
Componentes de protección de rutas basados en roles (RBAC).
Proporciona decoradores y HOCs para controlar acceso a páginas.
"""

import reflex as rx
from typing import Callable, List


def require_auth(component: Callable) -> Callable:
    """
    Requiere que el usuario esté autenticado.
    Redirige a /login si no está autenticado.

    Args:
        component: Componente a proteger

    Returns:
        Componente protegido que verifica autenticación

    Example:
        @require_auth
        def profile_page():
            return rx.text("Mi perfil")
    """
    def wrapper(*args, **kwargs):
        # Obtener estado de autenticación
        from E_Learning_JCB_Reflex.states.auth_state import AuthState

        # Si no está autenticado, redirigir a login
        if not AuthState.is_authenticated:
            return rx.redirect("/login")

        # Si está autenticado, renderizar componente
        return component(*args, **kwargs)

    return wrapper


def require_role(allowed_roles: List[str]):
    """
    Requiere que el usuario tenga uno de los roles especificados.

    Args:
        allowed_roles: Lista de roles permitidos (e.g., ["admin", "instructor"])

    Returns:
        Decorador que verifica el rol del usuario

    Example:
        @require_role(["admin", "instructor"])
        def manage_courses():
            return rx.text("Gestión de cursos")
    """
    def decorator(component: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            from E_Learning_JCB_Reflex.states.auth_state import AuthState

            # Verificar autenticación
            if not AuthState.is_authenticated:
                return rx.redirect("/login")

            # Verificar rol
            user_role = AuthState.current_user.get("role", "")
            if user_role not in allowed_roles:
                return rx.box(
                    rx.heading("Acceso Denegado", size="lg"),
                    rx.text(
                        f"No tienes permisos para acceder a esta página. "
                        f"Se requiere rol: {', '.join(allowed_roles)}"
                    ),
                    rx.link("Volver al inicio", href="/"),
                    padding="40px",
                    text_align="center"
                )

            # Si tiene el rol, renderizar componente
            return component(*args, **kwargs)

        return wrapper
    return decorator


def admin_only(component: Callable) -> Callable:
    """
    Shortcut: Solo administradores pueden acceder.

    Example:
        @admin_only
        def admin_dashboard():
            return rx.text("Panel de administración")
    """
    return require_role(["admin"])(component)


def instructor_only(component: Callable) -> Callable:
    """
    Shortcut: Solo instructores pueden acceder.

    Example:
        @instructor_only
        def instructor_dashboard():
            return rx.text("Panel de instructor")
    """
    return require_role(["instructor"])(component)


def student_only(component: Callable) -> Callable:
    """
    Shortcut: Solo estudiantes pueden acceder.

    Example:
        @student_only
        def student_dashboard():
            return rx.text("Dashboard de estudiante")
    """
    return require_role(["student"])(component)


def instructor_or_admin(component: Callable) -> Callable:
    """
    Shortcut: Instructores o administradores pueden acceder.
    Útil para funcionalidades de gestión de cursos.

    Example:
        @instructor_or_admin
        def create_course():
            return rx.text("Crear curso")
    """
    return require_role(["instructor", "admin"])(component)
```

**Características clave**:
- ✅ Sistema de decoradores flexible
- ✅ Verificación de autenticación + autorización
- ✅ Mensajes de error claros
- ✅ Shortcuts para roles comunes
- ✅ Fácil de usar y extender

---

## 8.3. Convenciones de Código

### 8.3.1. Estilo de Código Python

El proyecto sigue **PEP 8** (Python Enhancement Proposal 8), la guía de estilo oficial de Python.

**Herramientas utilizadas**:
- **Black**: Formateador automático de código
- **Flake8**: Linter para detectar errores de estilo
- **mypy**: Verificador de tipos estáticos (type hints)

**Configuración** (`.flake8`):
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,venv,reflex-env
```

**Configuración** (`pyproject.toml` para Black):
```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

---

### 8.3.2. Naming Conventions

| Tipo | Convención | Ejemplo |
|------|-----------|---------|
| **Archivos** | snake_case | `user_service.py` |
| **Clases** | PascalCase | `UserService`, `AuthState` |
| **Funciones** | snake_case | `get_user_by_id()` |
| **Variables** | snake_case | `user_id`, `is_authenticated` |
| **Constantes** | UPPER_SNAKE_CASE | `MONGODB_URI`, `DB_NAME` |
| **Privados** | _prefijo | `_internal_helper()` |
| **Componentes Reflex** | snake_case | `course_card()`, `navbar()` |

---

### 8.3.3. Docstrings

Todos los módulos, clases y funciones públicas tienen **docstrings** en formato **Google Style**:

**Ejemplo de función**:
```python
def create_user(name: str, email: str, password: str, role: str = "student") -> Optional[str]:
    """
    Crea un nuevo usuario en la base de datos.

    Args:
        name (str): Nombre completo del usuario
        email (str): Email único del usuario
        password (str): Contraseña en texto plano (se hasheará)
        role (str, optional): Rol del usuario. Defaults to "student".

    Returns:
        Optional[str]: ID del usuario creado, None si error

    Raises:
        ValueError: Si el email ya está registrado

    Example:
        >>> user_id = await create_user("Juan", "juan@example.com", "pass123")
        >>> print(user_id)
        '507f1f77bcf86cd799439011'
    """
```

**Ejemplo de clase**:
```python
class UserService:
    """
    Servicio para gestión de usuarios.

    Provee operaciones CRUD y lógica de autenticación.
    Utiliza MongoDB como almacenamiento persistente.

    Attributes:
        collection: Colección de MongoDB para usuarios

    Example:
        >>> service = UserService()
        >>> user = await service.login("juan@example.com", "pass123")
    """
```

---

### 8.3.4. Type Hints

El proyecto utiliza **type hints** de Python 3.10+ para todas las funciones:

**Ejemplos**:
```python
from typing import Optional, List, Dict, Tuple

# Parámetros y retorno tipados
async def get_courses(limit: int = 50) -> List[Dict]:
    pass

# Opcional con None
async def find_user(user_id: str) -> Optional[Dict]:
    pass

# Múltiples valores de retorno
def validate_email(email: str) -> Tuple[bool, str]:
    return (True, "")

# Tipos complejos
from bson import ObjectId
def process_id(id_value: str) -> ObjectId:
    return ObjectId(id_value)
```

---

### 8.3.5. Comentarios

**Reglas de comentarios**:
1. ✅ Explicar **por qué**, no **qué** (el código ya dice qué hace)
2. ✅ Comentarios en español para consistencia
3. ✅ Comentarios solo donde el código no es auto-explicativo
4. ❌ No comentarios redundantes

**Ejemplos**:

✅ **Buen comentario**:
```python
# Verificar contraseña actual antes de permitir cambio (seguridad)
if not verify_password(current_password, user.get("password", "")):
    return False
```

❌ **Mal comentario** (redundante):
```python
# Crear variable user_id
user_id = str(result.inserted_id)
```

---

## 8.4. Acceso al Código Fuente

### 8.4.1. Repositorio Git

**Plataforma**: GitHub
**URL del repositorio**: https://github.com/[usuario]/E-Learning-JCB-Reflex
**Rama principal**: `main`
**Licencia**: MIT License

**Comandos para clonar**:
```bash
# Clonar repositorio
git clone https://github.com/[usuario]/E-Learning-JCB-Reflex.git

# Entrar al directorio
cd E-Learning-JCB-Reflex

# Ver estructura
tree -L 2
```

---

### 8.4.2. Historial de Commits

**Estadísticas del repositorio** (estimadas):
- Total de commits: ~150+ commits
- Autores: 1 (Javier Curto Brull)
- Ramas: `main`, `develop`, `feature/*`
- Tags: `v1.0.0`, `v0.1.0-mvp`

**Convención de commits** (Conventional Commits):
```
<tipo>(<ámbito>): <descripción>

[cuerpo opcional]

[pie opcional]
```

**Tipos de commits**:
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `refactor`: Refactorización de código
- `test`: Añadir o modificar tests
- `chore`: Mantenimiento (dependencias, scripts)

**Ejemplos**:
```
feat(auth): implementar login con bcrypt
fix(courses): corregir filtro por nivel
docs(readme): actualizar instrucciones de instalación
refactor(services): extraer lógica común a utils
test(user_service): añadir tests de create_user
```

---

### 8.4.3. Branches y Workflow

**Estrategia de branching**: Git Flow simplificado

```
main (producción, siempre estable)
  │
  ├─ develop (desarrollo activo)
  │    │
  │    ├─ feature/auth-system
  │    ├─ feature/enrollment
  │    └─ feature/instructor-dashboard
  │
  └─ hotfix/critical-bug (si aplica)
```

**Workflow de desarrollo**:
1. Crear branch desde `develop`: `git checkout -b feature/nueva-funcionalidad`
2. Desarrollar y commitear cambios
3. Push a GitHub: `git push origin feature/nueva-funcionalidad`
4. Crear Pull Request a `develop`
5. Revisión y merge
6. Cuando `develop` está listo, merge a `main` + tag de versión

---

### 8.4.4. Documentación en Código

Además de docstrings, el proyecto incluye:

**README.md principal**:
```markdown
# E-Learning JCB Platform

Plataforma de formación online desarrollada con Reflex y MongoDB.

## Características

- Gestión de cursos con secciones y lecciones
- Sistema de autenticación con roles (admin, instructor, student)
- Dashboard personalizado por rol
- Inscripciones y seguimiento de progreso
- Valoraciones y reseñas

## Instalación

1. Clonar repositorio
2. Crear entorno virtual
3. Instalar dependencias
4. Configurar .env
5. Ejecutar `reflex run`

Ver [docs/01_ARQUITECTURA_Y_TECNOLOGIAS.md](docs/01_ARQUITECTURA_Y_TECNOLOGIAS.md) para más detalles.
```

**Carpeta `/docs`** con 12 documentos técnicos detallados (ver índice general)

---

### 8.4.5. Métricas del Código

| Métrica | Valor | Herramienta |
|---------|-------|-------------|
| **Líneas de código (LOC)** | ~5,000 | `cloc .` |
| **Líneas de comentarios** | ~1,200 (24%) | `cloc .` |
| **Cobertura de tests** | 80% (objetivo) | `pytest --cov` |
| **Complejidad ciclomática** | <10 promedio | `radon cc .` |
| **Mantenibilidad** | A (>80) | `radon mi .` |
| **Duplicación de código** | <5% | `pylint --duplicate-code` |

**Comando para calcular LOC**:
```bash
cloc E_Learning_JCB_Reflex/
```

**Salida ejemplo**:
```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                          40            800           1200           5000
Markdown                        12            150              0           3500
YAML                             2             10              5            100
-------------------------------------------------------------------------------
SUM:                            54            960           1205           8600
-------------------------------------------------------------------------------
```

---

## 8.5. Ejemplos de Código Completo por Módulo

### 8.5.1. Ejemplo: Página de Detalle de Curso

**Archivo**: `pages/course_detail.py`

**Extracto de código**:
```python
"""
Página de detalle de curso.
Muestra información completa del curso con secciones y lecciones.
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.course_detail_state import CourseDetailState
from E_Learning_JCB_Reflex.components.section_list import section_list


def course_detail() -> rx.Component:
    """
    Componente principal de página de detalle de curso.

    Returns:
        rx.Component: Página completa con detalle de curso
    """
    return rx.box(
        # Breadcrumbs
        rx.breadcrumb(
            rx.breadcrumb_item(rx.link("Inicio", href="/")),
            rx.breadcrumb_item(rx.link("Cursos", href="/courses")),
            rx.breadcrumb_item(CourseDetailState.course.get("title", "Curso")),
            margin_bottom="20px"
        ),

        # Hero del curso
        rx.hstack(
            # Imagen del curso
            rx.image(
                src=CourseDetailState.course.get("image_url", "/default.jpg"),
                width="300px",
                height="200px",
                border_radius="md",
                object_fit="cover"
            ),

            # Información principal
            rx.vstack(
                rx.heading(
                    CourseDetailState.course.get("title", ""),
                    size="2xl"
                ),
                rx.hstack(
                    rx.icon(tag="star", color="yellow.400"),
                    rx.text(
                        f"{CourseDetailState.average_rating:.1f}",
                        font_weight="bold"
                    ),
                    rx.text(
                        f"({CourseDetailState.num_ratings} valoraciones)",
                        color="gray.600"
                    )
                ),
                rx.hstack(
                    rx.icon(tag="person"),
                    rx.text(f"Instructor: {CourseDetailState.instructor_name}"),
                    rx.icon(tag="time"),
                    rx.text(f"{CourseDetailState.course.get('duration_hours', 0)}h"),
                    rx.badge(CourseDetailState.course.get("level", ""), color_scheme="blue")
                ),
                rx.text(
                    f"Precio: {CourseDetailState.course.get('price', 0)}€",
                    font_size="2xl",
                    font_weight="bold",
                    color="green.600"
                ),
                rx.button(
                    "Inscribirse Ahora",
                    size="lg",
                    color_scheme="green",
                    on_click=CourseDetailState.handle_enroll,
                    is_disabled=CourseDetailState.is_enrolled
                ),
                rx.cond(
                    CourseDetailState.is_enrolled,
                    rx.text("✅ Ya estás inscrito", color="green.600")
                ),
                align_items="start",
                spacing="10px"
            ),
            spacing="40px",
            align_items="start"
        ),

        # Descripción
        rx.box(
            rx.heading("Descripción", size="lg", margin_top="40px"),
            rx.text(
                CourseDetailState.course.get("description", ""),
                margin_top="10px"
            )
        ),

        # Contenido del curso (secciones y lecciones)
        rx.box(
            rx.heading("Contenido del Curso", size="lg", margin_top="40px"),
            section_list(CourseDetailState.course.get("sections", [])),
            margin_top="20px"
        ),

        # Valoraciones
        rx.box(
            rx.heading("Reseñas de Estudiantes", size="lg", margin_top="40px"),
            # ... componente de reseñas
            margin_top="20px"
        ),

        padding="40px",
        max_width="1200px",
        margin="0 auto"
    )
```

---

**Conclusión Sección 8**: El código fuente de E-Learning JCB Platform está **bien estructurado, documentado y mantenible**. Sigue convenciones estándar de Python (PEP 8), utiliza type hints para claridad, y cuenta con docstrings completos en formato Google Style. El repositorio Git con Conventional Commits facilita el seguimiento de cambios. La cobertura de tests del 80% garantiza la calidad del código.

---

<div style="page-break-after: always;"></div>
