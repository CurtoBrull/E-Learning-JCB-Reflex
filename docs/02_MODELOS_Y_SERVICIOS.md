# Modelos y Servicios - E-Learning JCB Reflex

## 🗂️ Modelos de Datos

### 1. User (`models/user.py`)

**Propósito**: Representa todos los usuarios del sistema (estudiantes, instructores, administradores).

#### Estructura del Modelo
```python
@dataclass
class User:
    id: str                          # ID único (ObjectId de MongoDB)
    first_name: str                  # Nombre del usuario
    last_name: str                   # Apellido del usuario
    email: str                       # Email único para autenticación
    password: str                    # Contraseña hasheada con bcrypt
    role: str                        # "student" | "instructor" | "admin"
    instructor_profile: dict         # Perfil adicional para instructores
    enrollments: list               # Inscripciones a cursos (estudiantes)
    courses_created: list           # Cursos creados (instructores)
    created_at: datetime            # Fecha de creación
    updated_at: datetime            # Fecha de última actualización
```

#### Propiedades del Modelo
```python
@property
def is_student(self) -> bool:
    """Verificar si el usuario es estudiante."""
    return self.role == "student"

@property
def is_instructor(self) -> bool:
    """Verificar si el usuario es instructor."""
    return self.role == "instructor"

@property
def is_admin(self) -> bool:
    """Verificar si el usuario es administrador."""
    return self.role == "admin"

def get_full_name(self) -> str:
    """Obtener nombre completo del usuario."""
    return f"{self.first_name} {self.last_name}"
```

#### Métodos de Conversión
```python
def to_dict(self) -> dict:
    """Convertir a formato MongoDB (camelCase)."""
    return {
        "_id": ObjectId(self.id) if self.id else None,
        "firstName": self.first_name,
        "lastName": self.last_name,
        "email": self.email,
        "password": self.password,
        "role": self.role,
        "instructorProfile": self.instructor_profile,
        "enrollments": self.enrollments,
        "coursesCreated": self.courses_created,
        "createdAt": self.created_at,
        "updatedAt": self.updated_at
    }

@classmethod
def from_dict(cls, data: dict) -> "User":
    """Crear instancia desde MongoDB (camelCase → snake_case)."""
    return cls(
        id=str(data.get("_id", "")),
        first_name=data.get("firstName", ""),
        last_name=data.get("lastName", ""),
        email=data.get("email", ""),
        password=data.get("password", ""),
        role=data.get("role", "student"),
        instructor_profile=data.get("instructorProfile", {}),
        enrollments=data.get("enrollments", []),
        courses_created=data.get("coursesCreated", []),
        created_at=data.get("createdAt"),
        updated_at=data.get("updatedAt")
    )
```

#### Validaciones Implementadas
- **Email único**: Verificación en base de datos
- **Formato de email**: Contiene "@" y "."
- **Contraseña**: Mínimo 6 caracteres
- **Rol válido**: Solo "student", "instructor", "admin"
- **Nombres**: No vacíos, máximo 50 caracteres

---

### 2. Course (`models/course.py`)

**Propósito**: Representa un curso completo con instructor, lecciones y reseñas.

#### Clases Anidadas

##### Instructor Embebido
```python
@dataclass
class Instructor:
    user_id: str                     # ID del usuario instructor
    name: str                        # Nombre completo del instructor
    email: str                       # Email del instructor
    avatar: str                      # URL del avatar
    bio: str                         # Biografía del instructor
    expertise: str                   # Área de especialización
```

##### Lección del Curso
```python
@dataclass
class Lesson:
    id: str                          # ID único de la lección
    title: str                       # Título de la lección
    content: str                     # Descripción/contenido
    video_url: str                   # URL del video de YouTube
    duration: int                    # Duración en minutos
    order: int                       # Orden en el curso
    created_at: datetime             # Fecha de creación
```

##### Reseña del Curso
```python
@dataclass
class Review:
    id: str                          # ID único de la reseña
    student_id: str                  # ID del estudiante
    student_name: str                # Nombre del estudiante
    rating: int                      # Calificación (1-5)
    comment: str                     # Comentario de la reseña
    created_at: datetime             # Fecha de creación
```

#### Estructura Principal del Curso
```python
@dataclass
class Course:
    id: str                          # ID único del curso
    title: str                       # Título del curso
    description: str                 # Descripción detallada
    instructor: Instructor           # Objeto instructor embebido
    price: float                     # Precio del curso
    thumbnail: str                   # URL de imagen del curso
    level: str                       # "beginner" | "intermediate" | "advanced"
    category: str                    # Categoría principal
    categories: List[str]            # Lista de categorías
    students: List[str]              # IDs de estudiantes inscritos
    lessons: List[Lesson]            # Lecciones del curso
    reviews: List[Review]            # Reseñas del curso
    average_rating: int              # Calificación promedio
    total_reviews: int               # Total de reseñas
    created_at: datetime             # Fecha de creación
    updated_at: datetime             # Fecha de actualización
```

#### Métodos del Curso
```python
def add_student(self, student_id: str) -> None:
    """Añadir estudiante al curso."""
    if student_id not in self.students:
        self.students.append(student_id)

def remove_student(self, student_id: str) -> None:
    """Remover estudiante del curso."""
    if student_id in self.students:
        self.students.remove(student_id)

def add_lesson(self, lesson: Lesson) -> None:
    """Añadir lección al curso."""
    self.lessons.append(lesson)
    self.lessons.sort(key=lambda x: x.order)

def calculate_average_rating(self) -> float:
    """Calcular calificación promedio."""
    if not self.reviews:
        return 0.0
    return sum(review.rating for review in self.reviews) / len(self.reviews)
```

---

### 3. Contact (`models/contact.py`)

**Propósito**: Mensajes de contacto enviados por usuarios.

#### Estructura del Modelo
```python
@dataclass
class Contact:
    id: str                          # ID único del mensaje
    name: str                        # Nombre del remitente
    email: str                       # Email del remitente
    message: str                     # Contenido del mensaje
    created_at: datetime             # Fecha de creación
    updated_at: datetime             # Fecha de actualización
    status: str                      # "pending" | "read" | "replied"
    admin_notes: str                 # Notas internas del admin
```

#### Métodos del Contacto
```python
def mark_as_read(self) -> None:
    """Marcar mensaje como leído."""
    self.status = "read"
    self.updated_at = datetime.now()

def mark_as_replied(self, notes: str = "") -> None:
    """Marcar mensaje como respondido."""
    self.status = "replied"
    self.admin_notes = notes
    self.updated_at = datetime.now()
```

---

## ⚙️ Servicios de Lógica de Negocio

### 1. UserService (`services/user_service.py`)

**Propósito**: Gestión completa de usuarios en la base de datos.

#### Operaciones de Consulta
```python
class UserService:
    async def get_user_by_id(self, user_id: str) -> User | None:
        """
        Obtener usuario por ID.
        
        Args:
            user_id: ID del usuario (ObjectId como string)
            
        Returns:
            User | None: Usuario encontrado o None
        """
        
    async def get_user_by_email(self, email: str) -> User | None:
        """
        Obtener usuario por email.
        
        Args:
            email: Email del usuario
            
        Returns:
            User | None: Usuario encontrado o None
        """
        
    async def get_users_by_ids(self, user_ids: List[str]) -> Dict[str, User]:
        """
        Obtener múltiples usuarios por IDs.
        
        Args:
            user_ids: Lista de IDs de usuarios
            
        Returns:
            Dict[str, User]: Diccionario ID -> Usuario
        """
```

#### Operaciones por Rol
```python
    async def get_all_students(self) -> List[User]:
        """Obtener todos los estudiantes."""
        
    async def get_all_instructors(self) -> List[User]:
        """Obtener todos los instructores."""
        
    async def get_all_admins(self) -> List[User]:
        """Obtener todos los administradores."""
```

#### Operaciones CRUD
```python
    async def create_user(self, first_name: str, last_name: str, 
                         email: str, password: str, role: str) -> bool:
        """
        Crear nuevo usuario.
        
        Args:
            first_name: Nombre del usuario
            last_name: Apellido del usuario
            email: Email único
            password: Contraseña en texto plano (se hasheará)
            role: Rol del usuario
            
        Returns:
            bool: True si se creó exitosamente
        """
        
    async def update_user(self, user_id: str, update_data: dict) -> bool:
        """
        Actualizar usuario existente.
        
        Args:
            user_id: ID del usuario
            update_data: Datos a actualizar (formato camelCase)
            
        Returns:
            bool: True si se actualizó exitosamente
        """
        
    async def delete_user(self, user_id: str) -> bool:
        """
        Eliminar usuario.
        
        Args:
            user_id: ID del usuario
            
        Returns:
            bool: True si se eliminó exitosamente
        """
```

#### Gestión de Contraseñas
```python
    async def change_password(self, user_id: str, current_password: str, 
                             new_password: str) -> bool:
        """
        Cambiar contraseña validando la actual.
        
        Args:
            user_id: ID del usuario
            current_password: Contraseña actual
            new_password: Nueva contraseña
            
        Returns:
            bool: True si se cambió exitosamente
        """
        
    async def admin_change_password(self, user_id: str, new_password: str) -> bool:
        """
        Cambiar contraseña sin validación (solo admins).
        
        Args:
            user_id: ID del usuario
            new_password: Nueva contraseña
            
        Returns:
            bool: True si se cambió exitosamente
        """
```

#### Características de Seguridad
- **Hash de contraseñas**: Todas las contraseñas se hashean con bcrypt
- **Salt único**: Cada contraseña tiene su propio salt
- **Verificación previa**: Validación de contraseña actual antes de cambios
- **Función especial admin**: Cambio sin verificación para administradores

---

### 2. CourseService (`services/course_service.py`)

**Propósito**: Gestión de cursos y contenido educativo.

#### Operaciones de Consulta
```python
class CourseService:
    async def get_popular_courses(self, limit: int = 6) -> List[Course]:
        """
        Obtener cursos más populares.
        
        Args:
            limit: Número máximo de cursos a retornar
            
        Returns:
            List[Course]: Lista de cursos ordenados por popularidad
        """
        
    async def get_all_courses(self) -> List[Course]:
        """Obtener todos los cursos del sistema."""
        
    async def get_course_by_id(self, course_id: str) -> Course | None:
        """
        Obtener curso por ID.
        
        Args:
            course_id: ID del curso
            
        Returns:
            Course | None: Curso encontrado o None
        """
        
    async def get_courses_by_instructor(self, instructor_id: str) -> List[Course]:
        """
        Obtener cursos de un instructor específico.
        
        Args:
            instructor_id: ID del instructor
            
        Returns:
            List[Course]: Lista de cursos del instructor
        """
```

#### Operaciones CRUD
```python
    async def create_course(self, course_data: dict) -> bool:
        """
        Crear nuevo curso.
        
        Args:
            course_data: Datos del curso
            
        Returns:
            bool: True si se creó exitosamente
        """
        
    async def update_course(self, course_id: str, update_data: dict) -> bool:
        """
        Actualizar curso existente.
        
        Args:
            course_id: ID del curso
            update_data: Datos a actualizar
            
        Returns:
            bool: True si se actualizó exitosamente
        """
        
    async def delete_course(self, course_id: str) -> bool:
        """
        Eliminar curso.
        
        Args:
            course_id: ID del curso
            
        Returns:
            bool: True si se eliminó exitosamente
        """
```

#### Gestión de Lecciones
```python
    async def add_lesson_to_course(self, course_id: str, lesson_data: dict) -> bool:
        """Añadir lección a un curso."""
        
    async def update_lesson(self, course_id: str, lesson_id: str, 
                           lesson_data: dict) -> bool:
        """Actualizar lección específica."""
        
    async def delete_lesson(self, course_id: str, lesson_id: str) -> bool:
        """Eliminar lección de un curso."""
        
    async def reorder_lessons(self, course_id: str, lesson_orders: List[dict]) -> bool:
        """Reordenar lecciones de un curso."""
```

---

### 3. EnrollmentService (`services/enrollment_service.py`)

**Propósito**: Gestión de inscripciones de estudiantes a cursos.

#### Operaciones Principales
```python
class EnrollmentService:
    async def enroll_student(self, student_id: str, course_id: str) -> bool:
        """
        Inscribir estudiante en un curso.
        
        Validaciones:
        - Usuario debe ser estudiante
        - Curso debe existir
        - No debe estar ya inscrito
        
        Args:
            student_id: ID del estudiante
            course_id: ID del curso
            
        Returns:
            bool: True si se inscribió exitosamente
        """
        
    async def unenroll_student(self, student_id: str, course_id: str) -> bool:
        """
        Desinscribir estudiante de un curso.
        
        Args:
            student_id: ID del estudiante
            course_id: ID del curso
            
        Returns:
            bool: True si se desinscribió exitosamente
        """
        
    async def is_enrolled(self, student_id: str, course_id: str) -> bool:
        """
        Verificar si un estudiante está inscrito en un curso.
        
        Args:
            student_id: ID del estudiante
            course_id: ID del curso
            
        Returns:
            bool: True si está inscrito
        """
```

#### Consultas de Inscripciones
```python
    async def get_student_enrollments(self, student_id: str) -> List[dict]:
        """
        Obtener todas las inscripciones de un estudiante.
        
        Args:
            student_id: ID del estudiante
            
        Returns:
            List[dict]: Lista de cursos inscritos con metadatos
        """
        
    async def get_course_enrollments(self, course_id: str) -> List[dict]:
        """
        Obtener todos los estudiantes inscritos en un curso.
        
        Args:
            course_id: ID del curso
            
        Returns:
            List[dict]: Lista de estudiantes inscritos
        """
        
    async def count_total_enrollments(self) -> int:
        """Contar total de inscripciones en el sistema."""
```

#### Validaciones Implementadas
- **Usuario estudiante**: Solo estudiantes pueden inscribirse
- **Curso existente**: Verificación de existencia del curso
- **Prevención duplicados**: No permite inscripciones duplicadas
- **Actualización contadores**: Mantiene contadores sincronizados

---

### 4. ContactService (`services/contact_service.py`)

**Propósito**: Gestión de mensajes de contacto.

#### Operaciones Principales
```python
class ContactService:
    async def create_contact(self, name: str, email: str, message: str) -> bool:
        """
        Crear nuevo mensaje de contacto.
        
        Args:
            name: Nombre del remitente
            email: Email del remitente
            message: Contenido del mensaje
            
        Returns:
            bool: True si se creó exitosamente
        """
        
    async def get_all_contacts(self) -> List[Contact]:
        """Obtener todos los mensajes de contacto."""
        
    async def get_contact_by_email(self, email: str) -> List[Contact]:
        """
        Obtener mensajes de un email específico.
        
        Args:
            email: Email del remitente
            
        Returns:
            List[Contact]: Lista de mensajes del email
        """
        
    async def mark_contact_as_read(self, contact_id: str) -> bool:
        """Marcar mensaje como leído."""
        
    async def mark_contact_as_replied(self, contact_id: str, notes: str) -> bool:
        """Marcar mensaje como respondido con notas."""
```

---

## 🔄 Patrones de Diseño en Servicios

### Repository Pattern
Los servicios actúan como repositorios que abstraen el acceso a datos:

```python
# Interfaz consistente independiente de la implementación
async def get_by_id(self, id: str) -> Model | None
async def create(self, data: dict) -> bool
async def update(self, id: str, data: dict) -> bool
async def delete(self, id: str) -> bool
```

### Unit of Work Pattern
Las operaciones complejas se manejan como transacciones:

```python
async def enroll_student(self, student_id: str, course_id: str) -> bool:
    # 1. Validar estudiante
    # 2. Validar curso
    # 3. Verificar no duplicado
    # 4. Actualizar usuario
    # 5. Actualizar curso
    # 6. Confirmar transacción
```

### Factory Pattern
Los modelos se crean desde diferentes fuentes:

```python
# Desde MongoDB
user = User.from_dict(mongo_data)

# Desde formulario
user = User.from_form_data(form_data)

# Nuevo usuario
user = User.create_new(name, email, password, role)
```

---

## 🛡️ Validaciones y Seguridad

### Validaciones de Entrada
- **Sanitización**: Limpieza de datos de entrada
- **Formato**: Validación de formatos (email, URLs)
- **Longitud**: Límites de caracteres
- **Tipos**: Verificación de tipos de datos

### Validaciones de Negocio
- **Unicidad**: Emails únicos, no duplicados
- **Relaciones**: Integridad referencial
- **Estados**: Transiciones válidas de estado
- **Permisos**: Autorización por rol

### Manejo de Errores
```python
try:
    result = await service_operation()
    return result
except ValidationError as e:
    logger.error(f"Validation error: {e}")
    return None
except DatabaseError as e:
    logger.error(f"Database error: {e}")
    return None
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    return None
```

---

*Documentación de Modelos y Servicios*  
*Proyecto: E-Learning JCB Reflex*  
*Actualizado: 25 de enero de 2025*