# Esquema de Base de Datos MongoDB - E-Learning JCB

Este documento describe el esquema REAL de la base de datos MongoDB utilizada en la plataforma E-Learning JCB, obtenido directamente de MongoDB Atlas.

## Información General

- **Base de Datos**: MongoDB Atlas
- **Nombre BD**: `elearning-jcb-db-cluster`
- **Driver**: Motor (async) + PyMongo
- **Nota**: Este esquema refleja la estructura actual en producción

---

## Colecciones

Esta base de datos contiene **5 colecciones**: `courses`, `users`, `contacts`, `lessons`, y `logentries`.

### Resumen de Colecciones

| Colección | Propósito | Diseño | Relaciones |
|-----------|-----------|---------|------------|
| **courses** | Cursos de la plataforma | Embebido (lessons, reviews) | Referencia a users (instructor, students) |
| **users** | Usuarios (estudiantes, instructors, admins) | Embebido (instructorProfile, enrollments) | Referencia a courses |
| **contacts** | Mensajes de contacto | Simple | Ninguna |
| **lessons** | Lecciones standalone | Simple | Referencia a courses |
| **logentries** | Logs del sistema | Embebido (metadata) | Referencias opcionales a users/courses |

---

### 1. courses

Contiene todos los cursos disponibles en la plataforma. **NOTA IMPORTANTE**: Las lecciones y reviews están embebidas en el documento del curso, no en colecciones separadas.

```javascript
{
  _id: ObjectId,                    // ID único del curso (requerido)
  __v: Number,                      // Versión del documento - Mongoose (requerido)
  title: String,                    // Título del curso (requerido)
  description: String,              // Descripción detallada del curso (requerido)
  image: String,                    // URL de imagen del curso (requerido)
  price: Number (double),           // Precio del curso (requerido)
  category: String,                 // Categoría principal (requerido)
  categories: [String],             // Array de categorías múltiples (requerido)
  instructor: {                     // Objeto con información del instructor (requerido)
    userId: ObjectId,               // ID del usuario instructor (requerido)
    name: String,                   // Nombre del instructor (requerido)
    email: String,                  // Email del instructor (requerido)
    avatarUrl: String               // URL del avatar del instructor (requerido)
  },
  students: [ObjectId | String],   // Array de IDs de estudiantes inscritos (requerido)
  lessons: [                        // Array de lecciones embebidas (requerido)
    {
      _id: String,                  // ID de la lección (requerido)
      title: String,                // Título de la lección (requerido)
      content: String,              // Contenido de la lección (requerido)
      createdAt: String             // Fecha de creación ISO string (requerido)
    }
  ],
  reviews: [                        // Array de reviews embebidas (opcional)
    {
      _id: String,                  // ID de la review (requerido en reviews)
      student: String,              // Nombre del estudiante (requerido en reviews)
      rating: Number (int),         // Calificación 1-5 (requerido en reviews)
      comment: String,              // Comentario (requerido en reviews)
      createdAt: String             // Fecha de creación ISO string (requerido en reviews)
    }
  ],
  averageRating: Number (int),      // Calificación promedio calculada (opcional)
  totalReviews: Number (int),       // Total de reviews (opcional)
  createdAt: Date                   // Fecha de creación del curso (requerido)
}
```

**Índices recomendados:**

- `category`
- `categories`
- `instructor.userId`
- `title` (texto)
- `students`

**Ejemplo real:**

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439012"),
  __v: 0,
  title: "Introducción a React para Principiantes",
  description: "Aprende los fundamentos de React desde cero con proyectos prácticos",
  image: "/courses/Course_React_Beginners.webp",
  price: 49.99,
  category: "Desarrollo Web",
  categories: ["Desarrollo Web", "Frontend", "JavaScript", "React"],
  instructor: {
    userId: ObjectId("507f1f77bcf86cd799439011"),
    name: "María Gómez",
    email: "maria.gomez@example.com",
    avatarUrl: "/instructors/Inst_Maria_Gomez.webp"
  },
  students: [
    ObjectId("507f1f77bcf86cd799439015"),
    "507f1f77bcf86cd799439016",
    ObjectId("507f1f77bcf86cd799439017")
  ],
  lessons: [
    {
      _id: "lesson-react-001",
      title: "¿Qué es React?",
      content: "React es una biblioteca de JavaScript para construir interfaces de usuario...",
      createdAt: "2024-01-21T10:00:00.000Z"
    },
    {
      _id: "lesson-react-002",
      title: "Componentes en React",
      content: "Los componentes son la base de React y permiten dividir la UI en piezas reutilizables...",
      createdAt: "2024-01-22T10:00:00.000Z"
    },
    {
      _id: "lesson-react-003",
      title: "Props y State",
      content: "Props y State son conceptos fundamentales para manejar datos en React...",
      createdAt: "2024-01-23T10:00:00.000Z"
    }
  ],
  reviews: [
    {
      _id: "review-001",
      student: "Carlos Ruiz",
      rating: 5,
      comment: "Excelente curso, muy bien explicado y con ejemplos prácticos",
      createdAt: "2024-03-01T14:20:00.000Z"
    },
    {
      _id: "review-002",
      student: "Ana López",
      rating: 4,
      comment: "Buen curso para empezar, me hubiera gustado más contenido avanzado",
      createdAt: "2024-03-05T16:45:00.000Z"
    }
  ],
  averageRating: 4,
  totalReviews: 2,
  createdAt: ISODate("2024-01-20T10:00:00.000Z")
}
```

---

### 2. users

Contiene todos los usuarios de la plataforma (estudiantes, instructores y administradores). **NOTA IMPORTANTE**: El perfil de instructor está embebido en el documento de usuario cuando el rol es "instructor".

```javascript
{
  _id: ObjectId,                    // ID único del usuario (requerido)
  __v: Number (int),                // Versión del documento - Mongoose (opcional)
  email: String,                    // Email del usuario (requerido, único)
  firstName: String,                // Nombre del usuario (requerido)
  lastName: String,                 // Apellido del usuario (requerido)
  password: String,                 // Contraseña hasheada (requerido)
  role: String,                     // Rol: "student" | "instructor" | "admin" (requerido)
  createdAt: Date,                  // Fecha de creación de la cuenta (requerido)
  avatarUrl: String,                // URL del avatar del usuario (opcional)
  bio: String,                      // Biografía del usuario (opcional)
  coursesCreated: [String],         // Array de IDs de cursos creados (opcional, solo instructores)
  enrollments: [                    // Array de inscripciones a cursos (opcional, estudiantes)
    {
      course: String,               // ID del curso (requerido en enrollments)
      enrolledAt: String            // Fecha de inscripción ISO string (requerido en enrollments)
    }
  ],
  instructorProfile: {              // Perfil extendido de instructor (opcional, solo instructores)
    avatarUrl: String,              // URL del avatar del instructor (requerido en instructorProfile)
    bio: String,                    // Biografía del instructor (requerido en instructorProfile)
    socialLinks: {                  // Redes sociales (requerido en instructorProfile)
      linkedin: String,             // URL de LinkedIn (requerido en socialLinks)
      twitter: String,              // URL de Twitter (requerido en socialLinks)
      website: String               // URL del sitio web (requerido en socialLinks)
    }
  },
  ratings: {                        // Calificaciones del instructor (opcional, solo instructores)
    averageRating: Number (double|int), // Calificación promedio (requerido en ratings)
    totalReviews: Number (int)      // Total de reviews recibidas (requerido en ratings)
  },
  socialLinks: {                    // Redes sociales del usuario (opcional)
    linkedin: String,               // URL de LinkedIn (requerido en socialLinks)
    twitter: String,                // URL de Twitter (requerido en socialLinks)
    website: String                 // URL del sitio web (requerido en socialLinks)
  }
}
```

**Índices recomendados:**

- `email` (único)
- `role`
- `coursesCreated`
- `"enrollments.course"`
- `createdAt`

**Ejemplo real - Estudiante:**

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439015"),
  __v: 0,
  email: "carlos.ruiz@example.com",
  firstName: "Carlos",
  lastName: "Ruiz",
  password: "$2b$10$...",  // Hash de bcrypt
  role: "student",
  createdAt: ISODate("2024-02-15T10:00:00.000Z"),
  avatarUrl: "/avatars/carlos_ruiz.webp",
  bio: "Desarrollador web en formación, apasionado por el frontend",
  enrollments: [
    {
      course: "507f1f77bcf86cd799439012",
      enrolledAt: "2024-03-01T09:00:00.000Z"
    },
    {
      course: "507f1f77bcf86cd799439013",
      enrolledAt: "2024-03-15T14:30:00.000Z"
    }
  ],
  socialLinks: {
    linkedin: "https://linkedin.com/in/carlos-ruiz",
    twitter: "https://twitter.com/carlosruiz",
    website: "https://carlosruiz.dev"
  }
}
```

**Ejemplo real - Instructor:**

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  __v: 0,
  email: "maria.gomez@example.com",
  firstName: "María",
  lastName: "Gómez",
  password: "$2b$10$...",  // Hash de bcrypt
  role: "instructor",
  createdAt: ISODate("2024-01-10T10:00:00.000Z"),
  avatarUrl: "/instructors/Inst_Maria_Gomez.webp",
  bio: "Desarrolladora Full Stack con 10 años de experiencia",
  coursesCreated: [
    "507f1f77bcf86cd799439012",
    "507f1f77bcf86cd799439013",
    "507f1f77bcf86cd799439014"
  ],
  instructorProfile: {
    avatarUrl: "/instructors/Inst_Maria_Gomez.webp",
    bio: "Experta en React, Node.js y MongoDB. Apasionada por enseñar y compartir conocimiento.",
    socialLinks: {
      linkedin: "https://linkedin.com/in/maria-gomez-dev",
      twitter: "https://twitter.com/mariagomezdev",
      website: "https://mariagomez.dev"
    }
  },
  ratings: {
    averageRating: 4.8,
    totalReviews: 156
  },
  socialLinks: {
    linkedin: "https://linkedin.com/in/maria-gomez-dev",
    twitter: "https://twitter.com/mariagomezdev",
    website: "https://mariagomez.dev"
  }
}
```

---

### 3. contacts

Almacena los mensajes de contacto enviados por los usuarios a través del formulario de contacto de la plataforma.

```javascript
{
  _id: ObjectId,                    // ID único del mensaje (requerido)
  __v: Number (int),                // Versión del documento - Mongoose (requerido)
  name: String,                     // Nombre del remitente (requerido)
  email: String,                    // Email del remitente (requerido)
  message: String,                  // Contenido del mensaje (requerido)
  createdAt: Date,                  // Fecha de creación del mensaje (requerido)
  updatedAt: Date                   // Fecha de última actualización (requerido)
}
```

**Índices recomendados:**

- `email`
- `createdAt` (descendente)
- `updatedAt`

**Ejemplo real:**

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439020"),
  __v: 0,
  name: "Pedro Sánchez",
  email: "pedro.sanchez@example.com",
  message: "Hola, estoy interesado en conocer más sobre sus cursos de Python avanzado. ¿Tienen algún curso disponible para este tema?",
  createdAt: ISODate("2024-03-10T15:30:00.000Z"),
  updatedAt: ISODate("2024-03-10T15:30:00.000Z")
}
```

---

### 4. lessons

Contiene lecciones como documentos independientes. **NOTA**: Esta colección coexiste con las lecciones embebidas en `courses`. Puede indicar una migración en curso o un esquema híbrido.

```javascript
{
  _id: ObjectId,                    // ID único de la lección (requerido)
  __v: Number (int),                // Versión del documento - Mongoose (requerido)
  title: String,                    // Título de la lección (requerido)
  content: String,                  // Contenido de la lección (requerido)
  course: ObjectId,                 // ID del curso al que pertenece (requerido)
  createdAt: Date                   // Fecha de creación de la lección (requerido)
}
```

**Índices recomendados:**

- `course` (para obtener todas las lecciones de un curso)
- `createdAt`
- Índice compuesto: `{ course: 1, createdAt: 1 }` para lecciones ordenadas por curso

**Ejemplo real:**

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439030"),
  __v: 0,
  title: "Introducción a Hooks en React",
  content: "Los Hooks son una nueva característica de React 16.8 que te permiten usar estado y otras características de React sin escribir una clase. En esta lección aprenderemos sobre useState y useEffect...",
  course: ObjectId("507f1f77bcf86cd799439012"),
  createdAt: ISODate("2024-01-24T10:00:00.000Z")
}
```

---

### 5. logentries

Registra eventos y logs del sistema para auditoría, debugging y monitoreo.

```javascript
{
  _id: ObjectId,                    // ID único del log (requerido)
  __v: Number (int),                // Versión del documento - Mongoose (requerido)
  level: String,                    // Nivel del log: "info" | "warn" | "error" (requerido)
  message: String,                  // Mensaje descriptivo del evento (requerido)
  timestamp: Date,                  // Timestamp del evento (requerido)
  metadata: {                       // Datos adicionales del evento (requerido)
    timestamp: String,              // Timestamp en formato ISO string (requerido)
    userId: String,                 // ID del usuario relacionado (opcional)
    userRole: String,               // Rol del usuario (opcional)
    courseId: String,               // ID del curso relacionado (opcional)
    action: String,                 // Acción realizada (opcional)
    error: String,                  // Mensaje de error (opcional)
    stack: String                   // Stack trace del error (opcional)
  },
  createdAt: Date,                  // Fecha de creación del log (requerido)
  updatedAt: Date                   // Fecha de última actualización (requerido)
}
```

**Índices recomendados:**

- `level`
- `timestamp` (descendente, para logs recientes)
- `"metadata.userId"`
- `"metadata.courseId"`
- `createdAt` (descendente)
- Índice compuesto: `{ level: 1, timestamp: -1 }` para filtrar por nivel y ordenar por fecha

**Ejemplo real - Info:**

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439040"),
  __v: 0,
  level: "info",
  message: "Usuario inscrito en curso exitosamente",
  timestamp: ISODate("2024-03-15T10:30:00.000Z"),
  metadata: {
    timestamp: "2024-03-15T10:30:00.000Z",
    userId: "507f1f77bcf86cd799439015",
    userRole: "student",
    courseId: "507f1f77bcf86cd799439012",
    action: "enrollment_created"
  },
  createdAt: ISODate("2024-03-15T10:30:00.000Z"),
  updatedAt: ISODate("2024-03-15T10:30:00.000Z")
}
```

**Ejemplo real - Error:**

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439041"),
  __v: 0,
  level: "error",
  message: "Error al procesar pago del curso",
  timestamp: ISODate("2024-03-15T14:45:00.000Z"),
  metadata: {
    timestamp: "2024-03-15T14:45:00.000Z",
    userId: "507f1f77bcf86cd799439016",
    userRole: "student",
    courseId: "507f1f77bcf86cd799439013",
    action: "payment_processing",
    error: "Payment gateway timeout",
    stack: "Error: Payment gateway timeout\n    at PaymentService.processPayment (payment.js:45:11)\n    at async CourseService.enrollUser (course.js:123:5)"
  },
  createdAt: ISODate("2024-03-15T14:45:00.000Z"),
  updatedAt: ISODate("2024-03-15T14:45:00.000Z")
}
```

---

## Notas Importantes sobre el Esquema Real

### Relaciones entre Colecciones

```text
┌──────────────┐
│   courses    │ ◄──┐
├──────────────┤    │
│ instructor ──┼──┐ │ (referencia)
│ students[] ──┼─┐│ │
│ lessons[] ───┤ ││ │ (embebido)
│ reviews[] ───┤ ││ │ (embebido)
└──────────────┘ ││ │
                 ││ │
┌──────────────┐ ││ │
│    users     │ ◄┘│ │
├──────────────┤   │ │
│ enrollments[]├───┘ │ (referencia a courses)
│ coursesCreated[] ──┘ (referencia a courses)
│ instructorProfile ─┤ (embebido, solo instructors)
└──────────────┘

┌──────────────┐
│   lessons    │ (standalone, diseño híbrido)
├──────────────┤
│ course ──────┼───► courses (referencia)
└──────────────┘

┌──────────────┐
│  contacts    │ (independiente)
└──────────────┘

┌──────────────┐
│ logentries   │ (independiente, referencias opcionales)
├──────────────┤
│ metadata.userId     ───► users (opcional)
│ metadata.courseId   ───► courses (opcional)
└──────────────┘
```

### Diferencias con el Esquema Planeado

El esquema actual de MongoDB difiere del esquema normalizado planificado originalmente:

#### 1. **Diseño Embebido vs Normalizado**

**Actual (Embebido)**:

- `lessons` están embebidas dentro de `courses`
- `reviews` están embebidas dentro de `courses`
- `instructor` es un objeto embebido (no solo un ID de referencia)

**Ventajas del diseño actual (courses)**:

- ✅ Menos consultas a la BD (todo en un documento)
- ✅ Mejor rendimiento para lectura de cursos
- ✅ Consistencia atómica (todo o nada)

**Desventajas del diseño actual (courses)**:

- ❌ Documentos grandes si hay muchas lecciones/reviews
- ❌ Duplicación de datos del instructor
- ❌ Límite de 16MB por documento en MongoDB
- ❌ Dificulta queries complejas sobre lecciones específicas

**Notas sobre users**:

- El campo `instructorProfile` solo existe para usuarios con `role: "instructor"`
- Los campos `enrollments` y `coursesCreated` mantienen referencias a cursos por ID
- La información del instructor en la colección `courses` está duplicada (desnormalizada)
- Esto permite obtener cursos con info del instructor sin hacer JOIN
- Considerar actualizar `courses.instructor` cuando se modifique el perfil del instructor

**Notas sobre lessons**:

- ⚠️ **DISEÑO HÍBRIDO**: Las lecciones existen tanto embebidas en `courses.lessons` como en la colección separada `lessons`
- Esto puede indicar una migración en progreso o diferentes casos de uso
- **Recomendación**: Decidir una estrategia única:
  - **Opción A**: Solo lecciones embebidas (mejor para lectura de cursos completos)
  - **Opción B**: Solo colección separada (mejor para gestión y queries de lecciones)
  - **Opción C**: Mantener híbrido pero sincronizar datos entre ambas ubicaciones

**Notas sobre contacts y logentries**:

- Colecciones de soporte para funcionalidad de la plataforma
- No tienen relaciones directas con courses/users
- `logentries` debe tener retención limitada (considerar TTL index para auto-eliminación de logs antiguos)

#### 2. **Campos Calculados**

- `averageRating` y `totalReviews` se calculan y almacenan
- Deben actualizarse cada vez que se agrega/modifica una review

#### 3. **Campo `__v`**

- Campo de versión de Mongoose
- Se incrementa con cada actualización del documento
- Útil para control de concurrencia optimista

#### 4. **Tipos de Datos Mixtos**

- `students` puede contener tanto ObjectId como String
- Esto puede causar inconsistencias - se recomienda estandarizar

---

## Modelos de Datos Actualizados para Reflex

Dado el esquema real, necesitamos modelos `Course` y `User` en Python:

### Modelo Course

```python
# E_Learning_JCB_Reflex/models/course.py

from datetime import datetime
from typing import Optional, List

class Instructor:
    """Información del instructor embebida en el curso."""

    def __init__(self, user_id: str, name: str, email: str, avatar_url: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.avatar_url = avatar_url

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=str(data.get("userId", "")),
            name=data.get("name", ""),
            email=data.get("email", ""),
            avatar_url=data.get("avatarUrl", "")
        )


class Lesson:
    """Lección embebida en el curso."""

    def __init__(self, _id: str, title: str, content: str, created_at: str):
        self.id = _id
        self.title = title
        self.content = content
        self.created_at = created_at

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            _id=data.get("_id", ""),
            title=data.get("title", ""),
            content=data.get("content", ""),
            created_at=data.get("createdAt", "")
        )


class Review:
    """Review embebida en el curso."""

    def __init__(self, _id: str, student: str, rating: int, comment: str, created_at: str):
        self.id = _id
        self.student = student
        self.rating = rating
        self.comment = comment
        self.created_at = created_at

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            _id=data.get("_id", ""),
            student=data.get("student", ""),
            rating=data.get("rating", 0),
            comment=data.get("comment", ""),
            created_at=data.get("createdAt", "")
        )


class Course:
    """Modelo de curso según esquema real de MongoDB."""

    def __init__(
        self,
        _id: Optional[str],
        title: str,
        description: str,
        image: str,
        price: float,
        category: str,
        categories: List[str],
        instructor: Instructor,
        students: List[str],
        lessons: List[Lesson],
        reviews: Optional[List[Review]] = None,
        average_rating: Optional[int] = None,
        total_reviews: Optional[int] = None,
        created_at: Optional[datetime] = None,
        __v: int = 0
    ):
        self.id = str(_id) if _id else None
        self.title = title
        self.description = description
        self.image = image
        self.price = price
        self.category = category
        self.categories = categories
        self.instructor = instructor
        self.students = students
        self.lessons = lessons
        self.reviews = reviews or []
        self.average_rating = average_rating
        self.total_reviews = total_reviews
        self.created_at = created_at
        self.__v = __v

    @classmethod
    def from_dict(cls, data: dict) -> "Course":
        """Crear instancia de Course desde documento de MongoDB."""
        instructor_data = data.get("instructor", {})
        instructor = Instructor.from_dict(instructor_data)

        lessons_data = data.get("lessons", [])
        lessons = [Lesson.from_dict(lesson) for lesson in lessons_data]

        reviews_data = data.get("reviews", [])
        reviews = [Review.from_dict(review) for review in reviews_data]

        return cls(
            _id=data.get("_id"),
            title=data.get("title", ""),
            description=data.get("description", ""),
            image=data.get("image", ""),
            price=data.get("price", 0.0),
            category=data.get("category", ""),
            categories=data.get("categories", []),
            instructor=instructor,
            students=[str(s) for s in data.get("students", [])],
            lessons=lessons,
            reviews=reviews,
            average_rating=data.get("averageRating"),
            total_reviews=data.get("totalReviews"),
            created_at=data.get("createdAt"),
            __v=data.get("__v", 0)
        )
```

### Modelo User

```python
# E_Learning_JCB_Reflex/models/user.py

from datetime import datetime
from typing import Optional, List

class SocialLinks:
    """Enlaces de redes sociales del usuario."""

    def __init__(self, linkedin: str = "", twitter: str = "", website: str = ""):
        self.linkedin = linkedin
        self.twitter = twitter
        self.website = website

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            linkedin=data.get("linkedin", ""),
            twitter=data.get("twitter", ""),
            website=data.get("website", "")
        )


class InstructorProfile:
    """Perfil extendido de instructor."""

    def __init__(self, avatar_url: str, bio: str, social_links: SocialLinks):
        self.avatar_url = avatar_url
        self.bio = bio
        self.social_links = social_links

    @classmethod
    def from_dict(cls, data: dict):
        social_links_data = data.get("socialLinks", {})
        return cls(
            avatar_url=data.get("avatarUrl", ""),
            bio=data.get("bio", ""),
            social_links=SocialLinks.from_dict(social_links_data)
        )


class Ratings:
    """Calificaciones del instructor."""

    def __init__(self, average_rating: float, total_reviews: int):
        self.average_rating = average_rating
        self.total_reviews = total_reviews

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            average_rating=data.get("averageRating", 0.0),
            total_reviews=data.get("totalReviews", 0)
        )


class Enrollment:
    """Inscripción a un curso."""

    def __init__(self, course: str, enrolled_at: str):
        self.course = course
        self.enrolled_at = enrolled_at

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            course=data.get("course", ""),
            enrolled_at=data.get("enrolledAt", "")
        )


class User:
    """Modelo de usuario según esquema real de MongoDB."""

    def __init__(
        self,
        _id: Optional[str],
        email: str,
        first_name: str,
        last_name: str,
        password: str,
        role: str,
        created_at: datetime,
        avatar_url: Optional[str] = None,
        bio: Optional[str] = None,
        courses_created: Optional[List[str]] = None,
        enrollments: Optional[List[Enrollment]] = None,
        instructor_profile: Optional[InstructorProfile] = None,
        ratings: Optional[Ratings] = None,
        social_links: Optional[SocialLinks] = None,
        __v: int = 0
    ):
        self.id = str(_id) if _id else None
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role = role
        self.created_at = created_at
        self.avatar_url = avatar_url
        self.bio = bio
        self.courses_created = courses_created or []
        self.enrollments = enrollments or []
        self.instructor_profile = instructor_profile
        self.ratings = ratings
        self.social_links = social_links
        self.__v = __v

    @property
    def full_name(self) -> str:
        """Nombre completo del usuario."""
        return f"{self.first_name} {self.last_name}"

    @property
    def is_instructor(self) -> bool:
        """Verifica si el usuario es instructor."""
        return self.role == "instructor"

    @property
    def is_student(self) -> bool:
        """Verifica si el usuario es estudiante."""
        return self.role == "student"

    @property
    def is_admin(self) -> bool:
        """Verifica si el usuario es administrador."""
        return self.role == "admin"

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Crear instancia de User desde documento de MongoDB."""
        enrollments_data = data.get("enrollments", [])
        enrollments = [Enrollment.from_dict(e) for e in enrollments_data]

        instructor_profile = None
        if "instructorProfile" in data:
            instructor_profile = InstructorProfile.from_dict(data["instructorProfile"])

        ratings = None
        if "ratings" in data:
            ratings = Ratings.from_dict(data["ratings"])

        social_links = None
        if "socialLinks" in data:
            social_links = SocialLinks.from_dict(data["socialLinks"])

        return cls(
            _id=data.get("_id"),
            email=data.get("email", ""),
            first_name=data.get("firstName", ""),
            last_name=data.get("lastName", ""),
            password=data.get("password", ""),
            role=data.get("role", "student"),
            created_at=data.get("createdAt"),
            avatar_url=data.get("avatarUrl"),
            bio=data.get("bio"),
            courses_created=data.get("coursesCreated", []),
            enrollments=enrollments,
            instructor_profile=instructor_profile,
            ratings=ratings,
            social_links=social_links,
            __v=data.get("__v", 0)
        )

    def to_dict(self) -> dict:
        """Convertir el usuario a diccionario para MongoDB."""
        user_dict = {
            "email": self.email,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "password": self.password,
            "role": self.role,
            "createdAt": self.created_at
        }

        if self.id:
            user_dict["_id"] = self.id

        if self.avatar_url:
            user_dict["avatarUrl"] = self.avatar_url

        if self.bio:
            user_dict["bio"] = self.bio

        if self.courses_created:
            user_dict["coursesCreated"] = self.courses_created

        if self.enrollments:
            user_dict["enrollments"] = [
                {"course": e.course, "enrolledAt": e.enrolled_at}
                for e in self.enrollments
            ]

        if self.instructor_profile:
            user_dict["instructorProfile"] = {
                "avatarUrl": self.instructor_profile.avatar_url,
                "bio": self.instructor_profile.bio,
                "socialLinks": {
                    "linkedin": self.instructor_profile.social_links.linkedin,
                    "twitter": self.instructor_profile.social_links.twitter,
                    "website": self.instructor_profile.social_links.website
                }
            }

        if self.ratings:
            user_dict["ratings"] = {
                "averageRating": self.ratings.average_rating,
                "totalReviews": self.ratings.total_reviews
            }

        if self.social_links:
            user_dict["socialLinks"] = {
                "linkedin": self.social_links.linkedin,
                "twitter": self.social_links.twitter,
                "website": self.social_links.website
            }

        user_dict["__v"] = self.__v

        return user_dict
```

### Modelo Contact

```python
# E_Learning_JCB_Reflex/models/contact.py

from datetime import datetime
from typing import Optional

class Contact:
    """Modelo de mensaje de contacto según esquema real de MongoDB."""

    def __init__(
        self,
        _id: Optional[str],
        name: str,
        email: str,
        message: str,
        created_at: datetime,
        updated_at: datetime,
        __v: int = 0
    ):
        self.id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.message = message
        self.created_at = created_at
        self.updated_at = updated_at
        self.__v = __v

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
        """Crear instancia de Contact desde documento de MongoDB."""
        return cls(
            _id=data.get("_id"),
            name=data.get("name", ""),
            email=data.get("email", ""),
            message=data.get("message", ""),
            created_at=data.get("createdAt"),
            updated_at=data.get("updatedAt"),
            __v=data.get("__v", 0)
        )

    def to_dict(self) -> dict:
        """Convertir el contacto a diccionario para MongoDB."""
        contact_dict = {
            "name": self.name,
            "email": self.email,
            "message": self.message,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "__v": self.__v
        }

        if self.id:
            contact_dict["_id"] = self.id

        return contact_dict
```

### Modelo Lesson (standalone)

```python
# E_Learning_JCB_Reflex/models/lesson.py

from datetime import datetime
from typing import Optional

class LessonStandalone:
    """Modelo de lección standalone según esquema real de MongoDB.

    NOTA: Este modelo es para la colección 'lessons' separada.
    Para lecciones embebidas en courses, ver Course.Lesson en course.py
    """

    def __init__(
        self,
        _id: Optional[str],
        title: str,
        content: str,
        course: str,
        created_at: datetime,
        __v: int = 0
    ):
        self.id = str(_id) if _id else None
        self.title = title
        self.content = content
        self.course = course  # ObjectId como string
        self.created_at = created_at
        self.__v = __v

    @classmethod
    def from_dict(cls, data: dict) -> "LessonStandalone":
        """Crear instancia de LessonStandalone desde documento de MongoDB."""
        return cls(
            _id=data.get("_id"),
            title=data.get("title", ""),
            content=data.get("content", ""),
            course=str(data.get("course", "")),
            created_at=data.get("createdAt"),
            __v=data.get("__v", 0)
        )

    def to_dict(self) -> dict:
        """Convertir la lección a diccionario para MongoDB."""
        lesson_dict = {
            "title": self.title,
            "content": self.content,
            "course": self.course,
            "createdAt": self.created_at,
            "__v": self.__v
        }

        if self.id:
            lesson_dict["_id"] = self.id

        return lesson_dict
```

### Modelo LogEntry

```python
# E_Learning_JCB_Reflex/models/log_entry.py

from datetime import datetime
from typing import Optional

class LogMetadata:
    """Metadata del log entry."""

    def __init__(
        self,
        timestamp: str,
        user_id: Optional[str] = None,
        user_role: Optional[str] = None,
        course_id: Optional[str] = None,
        action: Optional[str] = None,
        error: Optional[str] = None,
        stack: Optional[str] = None
    ):
        self.timestamp = timestamp
        self.user_id = user_id
        self.user_role = user_role
        self.course_id = course_id
        self.action = action
        self.error = error
        self.stack = stack

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            timestamp=data.get("timestamp", ""),
            user_id=data.get("userId"),
            user_role=data.get("userRole"),
            course_id=data.get("courseId"),
            action=data.get("action"),
            error=data.get("error"),
            stack=data.get("stack")
        )

    def to_dict(self) -> dict:
        """Convertir metadata a diccionario."""
        metadata = {"timestamp": self.timestamp}

        if self.user_id:
            metadata["userId"] = self.user_id
        if self.user_role:
            metadata["userRole"] = self.user_role
        if self.course_id:
            metadata["courseId"] = self.course_id
        if self.action:
            metadata["action"] = self.action
        if self.error:
            metadata["error"] = self.error
        if self.stack:
            metadata["stack"] = self.stack

        return metadata


class LogEntry:
    """Modelo de log entry según esquema real de MongoDB."""

    # Niveles de log válidos
    LEVEL_INFO = "info"
    LEVEL_WARN = "warn"
    LEVEL_ERROR = "error"

    def __init__(
        self,
        _id: Optional[str],
        level: str,
        message: str,
        timestamp: datetime,
        metadata: LogMetadata,
        created_at: datetime,
        updated_at: datetime,
        __v: int = 0
    ):
        self.id = str(_id) if _id else None
        self.level = level
        self.message = message
        self.timestamp = timestamp
        self.metadata = metadata
        self.created_at = created_at
        self.updated_at = updated_at
        self.__v = __v

    @property
    def is_error(self) -> bool:
        """Verifica si el log es un error."""
        return self.level == self.LEVEL_ERROR

    @property
    def is_warning(self) -> bool:
        """Verifica si el log es un warning."""
        return self.level == self.LEVEL_WARN

    @property
    def is_info(self) -> bool:
        """Verifica si el log es informativo."""
        return self.level == self.LEVEL_INFO

    @classmethod
    def from_dict(cls, data: dict) -> "LogEntry":
        """Crear instancia de LogEntry desde documento de MongoDB."""
        metadata_data = data.get("metadata", {})
        metadata = LogMetadata.from_dict(metadata_data)

        return cls(
            _id=data.get("_id"),
            level=data.get("level", "info"),
            message=data.get("message", ""),
            timestamp=data.get("timestamp"),
            metadata=metadata,
            created_at=data.get("createdAt"),
            updated_at=data.get("updatedAt"),
            __v=data.get("__v", 0)
        )

    def to_dict(self) -> dict:
        """Convertir el log entry a diccionario para MongoDB."""
        log_dict = {
            "level": self.level,
            "message": self.message,
            "timestamp": self.timestamp,
            "metadata": self.metadata.to_dict(),
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "__v": self.__v
        }

        if self.id:
            log_dict["_id"] = self.id

        return log_dict
```

---

## Consultas Comunes Actualizadas

### Consultas para Courses

### 1. Obtener todos los cursos con información básica

```javascript
db.courses.find({}, {
  title: 1,
  description: 1,
  image: 1,
  price: 1,
  category: 1,
  "instructor.name": 1,
  "instructor.avatarUrl": 1,
  averageRating: 1,
  totalReviews: 1,
  students: 1
})
```

### 2. Obtener cursos de una categoría específica

```javascript
db.courses.find({
  categories: "Desarrollo Web"
})
```

### 3. Obtener cursos de un instructor

```javascript
db.courses.find({
  "instructor.userId": ObjectId("...")
})
```

### 4. Buscar cursos por texto

```javascript
db.courses.find({
  $text: { $search: "React JavaScript" }
})
```

### 5. Obtener cursos con número de estudiantes

```javascript
db.courses.aggregate([
  {
    $project: {
      title: 1,
      studentCount: { $size: "$students" },
      price: 1,
      category: 1
    }
  },
  { $sort: { studentCount: -1 } }
])
```

### 6. Obtener lecciones de un curso específico

```javascript
db.courses.findOne(
  { _id: ObjectId("...") },
  { lessons: 1, title: 1 }
)
```

### 7. Agregar una review a un curso

```javascript
db.courses.updateOne(
  { _id: ObjectId("...") },
  {
    $push: {
      reviews: {
        _id: "review-003",
        student: "Pedro Martínez",
        rating: 5,
        comment: "Increíble curso",
        createdAt: new Date().toISOString()
      }
    },
    $inc: { totalReviews: 1 }
  }
)

// Luego recalcular averageRating
```

### Consultas para Users

#### 1. Obtener usuario por email (login)

```javascript
db.users.findOne({
  email: "maria.gomez@example.com"
})
```

#### 2. Obtener todos los instructores

```javascript
db.users.find({
  role: "instructor"
}, {
  firstName: 1,
  lastName: 1,
  email: 1,
  "instructorProfile.avatarUrl": 1,
  "instructorProfile.bio": 1,
  "ratings.averageRating": 1,
  "ratings.totalReviews": 1
})
```

#### 3. Obtener cursos en los que está inscrito un estudiante

```javascript
db.users.findOne(
  { _id: ObjectId("...") },
  { enrollments: 1 }
)
```

#### 4. Obtener estudiantes inscritos en un curso específico

```javascript
db.users.find({
  "enrollments.course": "507f1f77bcf86cd799439012"
}, {
  firstName: 1,
  lastName: 1,
  email: 1,
  avatarUrl: 1
})
```

#### 5. Obtener cursos creados por un instructor

```javascript
db.users.findOne(
  { _id: ObjectId("..."), role: "instructor" },
  { coursesCreated: 1 }
)
```

#### 6. Buscar instructores por calificación

```javascript
db.users.find({
  role: "instructor",
  "ratings.averageRating": { $gte: 4.5 }
}).sort({ "ratings.averageRating": -1 })
```

#### 7. Inscribir estudiante en un curso

```javascript
db.users.updateOne(
  { _id: ObjectId("...") },
  {
    $push: {
      enrollments: {
        course: "507f1f77bcf86cd799439012",
        enrolledAt: new Date().toISOString()
      }
    }
  }
)
```

#### 8. Agregar curso creado por instructor

```javascript
db.users.updateOne(
  { _id: ObjectId("..."), role: "instructor" },
  {
    $push: { coursesCreated: "507f1f77bcf86cd799439012" }
  }
)
```

#### 9. Actualizar perfil de instructor

```javascript
db.users.updateOne(
  { _id: ObjectId("..."), role: "instructor" },
  {
    $set: {
      "instructorProfile.bio": "Nueva biografía",
      "instructorProfile.socialLinks.linkedin": "https://linkedin.com/in/new-profile"
    }
  }
)
```

#### 10. Obtener estadísticas de usuarios

```javascript
db.users.aggregate([
  {
    $group: {
      _id: "$role",
      count: { $sum: 1 }
    }
  }
])
```

### Consultas para Contacts

#### 1. Obtener mensajes de contacto recientes

```javascript
db.contacts.find()
  .sort({ createdAt: -1 })
  .limit(20)
```

#### 2. Buscar mensajes por email

```javascript
db.contacts.find({
  email: "pedro.sanchez@example.com"
}).sort({ createdAt: -1 })
```

#### 3. Obtener mensajes de un período de tiempo

```javascript
db.contacts.find({
  createdAt: {
    $gte: ISODate("2024-03-01T00:00:00.000Z"),
    $lt: ISODate("2024-04-01T00:00:00.000Z")
  }
}).sort({ createdAt: -1 })
```

#### 4. Buscar mensajes por contenido (texto)

```javascript
db.contacts.find({
  $or: [
    { message: { $regex: "Python", $options: "i" } },
    { name: { $regex: "Pedro", $options: "i" } }
  ]
})
```

#### 5. Contar total de mensajes de contacto

```javascript
db.contacts.countDocuments()
```

### Consultas para Lessons (standalone)

#### 1. Obtener todas las lecciones de un curso

```javascript
db.lessons.find({
  course: ObjectId("507f1f77bcf86cd799439012")
}).sort({ createdAt: 1 })
```

#### 2. Obtener lección específica por ID

```javascript
db.lessons.findOne({
  _id: ObjectId("507f1f77bcf86cd799439030")
})
```

#### 3. Contar lecciones por curso

```javascript
db.lessons.countDocuments({
  course: ObjectId("507f1f77bcf86cd799439012")
})
```

#### 4. Buscar lecciones por título o contenido

```javascript
db.lessons.find({
  $or: [
    { title: { $regex: "Hooks", $options: "i" } },
    { content: { $regex: "useState", $options: "i" } }
  ]
})
```

#### 5. Agregar nueva lección a un curso

```javascript
db.lessons.insertOne({
  title: "Props avanzadas en React",
  content: "En esta lección exploraremos el uso avanzado de props...",
  course: ObjectId("507f1f77bcf86cd799439012"),
  createdAt: new Date(),
  __v: 0
})
```

#### 6. Actualizar contenido de una lección

```javascript
db.lessons.updateOne(
  { _id: ObjectId("507f1f77bcf86cd799439030") },
  {
    $set: {
      content: "Contenido actualizado de la lección...",
      updatedAt: new Date()
    }
  }
)
```

#### 7. Eliminar lecciones de un curso

```javascript
db.lessons.deleteMany({
  course: ObjectId("507f1f77bcf86cd799439012")
})
```

### Consultas para LogEntries

#### 1. Obtener logs recientes

```javascript
db.logentries.find()
  .sort({ timestamp: -1 })
  .limit(100)
```

#### 2. Obtener solo errores

```javascript
db.logentries.find({
  level: "error"
}).sort({ timestamp: -1 })
```

#### 3. Obtener logs de un usuario específico

```javascript
db.logentries.find({
  "metadata.userId": "507f1f77bcf86cd799439015"
}).sort({ timestamp: -1 })
```

#### 4. Obtener logs de un curso específico

```javascript
db.logentries.find({
  "metadata.courseId": "507f1f77bcf86cd799439012"
}).sort({ timestamp: -1 })
```

#### 5. Buscar errores por mensaje

```javascript
db.logentries.find({
  level: "error",
  message: { $regex: "payment", $options: "i" }
}).sort({ timestamp: -1 })
```

#### 6. Obtener logs por acción específica

```javascript
db.logentries.find({
  "metadata.action": "enrollment_created"
}).sort({ timestamp: -1 })
```

#### 7. Contar errores por día

```javascript
db.logentries.aggregate([
  {
    $match: { level: "error" }
  },
  {
    $group: {
      _id: {
        $dateToString: { format: "%Y-%m-%d", date: "$timestamp" }
      },
      count: { $sum: 1 }
    }
  },
  { $sort: { _id: -1 } }
])
```

#### 8. Obtener logs de las últimas 24 horas

```javascript
const yesterday = new Date(Date.now() - 24 * 60 * 60 * 1000);

db.logentries.find({
  timestamp: { $gte: yesterday }
}).sort({ timestamp: -1 })
```

#### 9. Insertar nuevo log entry

```javascript
db.logentries.insertOne({
  level: "info",
  message: "Nueva acción del usuario",
  timestamp: new Date(),
  metadata: {
    timestamp: new Date().toISOString(),
    userId: "507f1f77bcf86cd799439015",
    userRole: "student",
    action: "course_viewed"
  },
  createdAt: new Date(),
  updatedAt: new Date(),
  __v: 0
})
```

#### 10. Eliminar logs antiguos (más de 90 días)

```javascript
const ninetyDaysAgo = new Date(Date.now() - 90 * 24 * 60 * 60 * 1000);

db.logentries.deleteMany({
  timestamp: { $lt: ninetyDaysAgo }
})
```

---

## Recomendaciones para Desarrollo

### 1. Decisión sobre Diseño Híbrido de Lessons

**IMPORTANTE**: Actualmente existe un diseño híbrido donde las lecciones están:

- ✅ Embebidas en `courses.lessons[]`
- ✅ En colección separada `lessons`

**Recomendaciones:**

**Opción A - Solo Lecciones Embebidas** (Recomendado para lectura):

- Eliminar colección `lessons`
- Mantener solo `courses.lessons[]`
- ✅ Mejor rendimiento al obtener cursos completos
- ✅ Consistencia atómica
- ❌ Dificulta gestión individual de lecciones

**Opción B - Solo Colección Separada**:

- Eliminar `courses.lessons[]`
- Mantener solo colección `lessons`
- ✅ Mejor para gestión CRUD de lecciones
- ✅ Evita documentos grandes en courses
- ❌ Requiere múltiples queries para obtener curso completo

**Opción C - Mantener Híbrido** (Solo si hay justificación):

- Si se usa, sincronizar ambas ubicaciones
- Implementar triggers o middleware para mantener consistencia
- Definir cuál es la "fuente de verdad"

### 2. Migración Futura (Opcional)

Si el número de reviews crece mucho, considerar migrar a colección separada:

```javascript
// Nueva estructura para reviews
reviews: { _id, course_id, student_id, rating, comment, created_at, ... }
```

### 3. Validación en Aplicación

Implementar validaciones estrictas:

**Para courses:**

- Convertir todos los `students` a ObjectId
- Validar formato de email en instructor
- Validar rating entre 1-5
- Limitar tamaño de arrays (lessons, reviews)

**Para users:**

- Validar formato de email único
- Hash de contraseñas con bcrypt (nunca almacenar en texto plano)
- Validar que `instructorProfile` solo existe si `role` es "instructor"
- Validar que `enrollments` solo existe si `role` es "student"
- Validar URLs en `avatarUrl` y `socialLinks`
- Sincronizar datos del instructor entre `users` y `courses` cuando se actualice

**Para contacts:**

- Validar formato de email
- Sanitizar contenido del mensaje (prevenir XSS)
- Limitar longitud del mensaje

**Para lessons:**

- Si se mantiene diseño híbrido, validar sincronización
- Validar que el curso existe antes de crear lección

**Para logentries:**

- Validar niveles de log (info, warn, error)
- Implementar TTL para logs antiguos
- Considerar sampling para logs de alto volumen

### 4. Índices a Crear

```javascript
// Índices para courses
// Texto completo
db.courses.createIndex({ title: "text", description: "text" })

// Consultas frecuentes
db.courses.createIndex({ category: 1 })
db.courses.createIndex({ "instructor.userId": 1 })
db.courses.createIndex({ students: 1 })
db.courses.createIndex({ averageRating: -1 })
db.courses.createIndex({ createdAt: -1 })

// Índices para users
// Email único para login
db.users.createIndex({ email: 1 }, { unique: true })

// Consultas frecuentes
db.users.createIndex({ role: 1 })
db.users.createIndex({ "enrollments.course": 1 })
db.users.createIndex({ coursesCreated: 1 })
db.users.createIndex({ "ratings.averageRating": -1 })
db.users.createIndex({ createdAt: -1 })

// Índice compuesto para instructores con buenas calificaciones
db.users.createIndex({ role: 1, "ratings.averageRating": -1 })

// Índices para contacts
db.contacts.createIndex({ email: 1 })
db.contacts.createIndex({ createdAt: -1 })
db.contacts.createIndex({ updatedAt: -1 })

// Índices para lessons (standalone)
db.lessons.createIndex({ course: 1 })
db.lessons.createIndex({ createdAt: 1 })
// Índice compuesto para lecciones ordenadas por curso y fecha
db.lessons.createIndex({ course: 1, createdAt: 1 })
// Texto completo para búsqueda en lecciones
db.lessons.createIndex({ title: "text", content: "text" })

// Índices para logentries
db.logentries.createIndex({ level: 1 })
db.logentries.createIndex({ timestamp: -1 })
db.logentries.createIndex({ "metadata.userId": 1 })
db.logentries.createIndex({ "metadata.courseId": 1 })
db.logentries.createIndex({ "metadata.action": 1 })
db.logentries.createIndex({ createdAt: -1 })
// Índice compuesto para filtrar por nivel y ordenar por timestamp
db.logentries.createIndex({ level: 1, timestamp: -1 })

// TTL Index para auto-eliminación de logs antiguos (opcional, después de 90 días)
db.logentries.createIndex(
  { timestamp: 1 },
  { expireAfterSeconds: 7776000 }  // 90 días = 90 * 24 * 60 * 60
)
```

---

**Última actualización**: 2025-11-12
**Versión del esquema**: 4.0 (esquema completo con 5 colecciones: courses, users, contacts, lessons, logentries)
