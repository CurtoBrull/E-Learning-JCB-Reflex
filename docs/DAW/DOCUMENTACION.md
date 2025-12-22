# Documentación del Proyecto E-Learning JCB Reflex

## 📋 Resumen General

E-Learning JCB Reflex es una plataforma completa de aprendizaje en línea construida con **Reflex** (framework full-stack de Python) y **MongoDB** como base de datos. El sistema implementa un modelo de roles (estudiantes, instructores y administradores) con funcionalidades específicas para cada uno.

---

## 🏗️ Arquitectura del Proyecto

### Estructura de Directorios

```
E_Learning_JCB_Reflex/
├── models/              # Modelos de datos (User, Course, Contact)
├── services/            # Servicios de base de datos (CRUD operations)
├── states/              # Estados de Reflex (gestión de UI y lógica)
├── components/          # Componentes reutilizables de UI
├── pages/               # Páginas de la aplicación
├── utils/               # Utilidades (password hashing, route helpers)
├── database/            # Configuración de MongoDB
└── E_Learning_JCB_Reflex.py  # Archivo principal y registro de rutas
```

---

## 📊 Modelos de Datos

### 1. User (models/user.py)
**Propósito**: Representa a todos los usuarios del sistema (estudiantes, instructores, admins)

**Atributos principales**:
- `id`: Identificador único (ObjectId de MongoDB)
- `first_name`, `last_name`: Nombre completo
- `email`: Email único para autenticación
- `password`: Contraseña hasheada con bcrypt
- `role`: Rol del usuario ("student", "instructor", "admin")
- `enrolled_courses`: Lista de cursos inscritos (solo estudiantes)
- `created_at`, `updated_at`: Timestamps automáticos

**Métodos**:
- `get_full_name()`: Retorna nombre completo concatenado
- `to_dict()`: Serializa a formato MongoDB (camelCase)
- `from_dict()`: Deserializa desde MongoDB (snake_case)

---

### 2. Course (models/course.py)
**Propósito**: Representa un curso completo con instructor, lecciones y reseñas

**Clases anidadas**:
- **Instructor**: Información del instructor (nombre, email, avatar, bio)
- **Lesson**: Lecciones del curso (título, contenido, orden, duración)
- **Review**: Reseñas de estudiantes (calificación, comentario, fecha)

**Atributos principales**:
- `title`, `description`: Información básica
- `thumbnail`: URL de imagen del curso
- `price`: Precio del curso
- `level`: Nivel (beginner/intermediate/advanced)
- `category`, `categories`: Categorización
- `instructor`: Objeto Instructor anidado
- `lessons`: Lista de lecciones (Lesson[])
- `reviews`: Lista de reseñas (Review[])
- `students`: IDs de estudiantes inscritos
- `average_rating`, `total_reviews`: Estadísticas calculadas

---

### 3. Contact (models/contact.py)
**Propósito**: Mensajes de contacto enviados por usuarios a través del formulario

**Atributos**:
- `name`, `email`: Datos del remitente
- `message`: Contenido del mensaje
- `created_at`, `updated_at`: Timestamps automáticos

---

## 🔧 Servicios (Capa de Datos)

### user_service.py
**Operaciones CRUD para usuarios**:
- `create_user()`: Crear nuevo usuario con contraseña hasheada
- `authenticate_user()`: Autenticar usuario (email + password con bcrypt)
- `get_user_by_id()`, `get_user_by_email()`: Búsqueda de usuarios
- `get_all_students()`, `get_all_instructors()`, `get_all_admins()`: Listados por rol
- `update_user()`: Actualizar información del usuario
- `delete_user()`: Eliminar usuario permanentemente
- `change_password()`: Cambiar contraseña validando la actual
- `admin_change_password()`: Cambiar contraseña sin validación (solo admins)
- `get_users_by_ids()`: Obtener múltiples usuarios por lista de IDs

**Seguridad**: Todas las contraseñas se hashean con bcrypt antes de almacenar

---

### course_service.py
**Operaciones CRUD para cursos**:
- `get_popular_courses(limit=6)`: Cursos destacados para homepage
- `get_all_courses()`: Catálogo completo de cursos
- `get_course_by_id()`: Detalle completo de un curso
- `create_course()`: Crear nuevo curso con timestamps automáticos
- `update_course()`: Actualizar campos específicos del curso
- `delete_course()`: Eliminar curso (IRREVERSIBLE)

**Nota**: El contador `studentsEnrolled` se inicializa en 0 al crear un curso

---

### enrollment_service.py
**Gestión de inscripciones de estudiantes**:
- `enroll_student()`: Inscribir estudiante en un curso
  - Valida que el usuario sea estudiante
  - Verifica que el curso exista
  - Previene inscripciones duplicadas
  - Incrementa contador de estudiantes del curso
- `unenroll_student()`: Desinscribir estudiante de un curso
  - Decrementa contador de estudiantes
- `is_enrolled()`: Verificar si un estudiante está inscrito
- `get_student_enrollments()`: Obtener cursos inscritos con información completa
- `count_total_enrollments()`: Contar inscripciones totales del sistema

**Estructura de inscripción**:
```python
{
    "courseId": ObjectId,
    "enrolledAt": datetime,
    "progress": 0-100,
    "completedLessons": [],
    "status": "active"
}
```

---

### contact_service.py
**Gestión de mensajes de contacto**:
- `create_contact()`: Guardar mensaje de contacto con timestamps automáticos
- `get_all_contacts()`: Obtener todos los mensajes (más recientes primero)
- `get_contact_by_email()`: Buscar mensajes de un email específico

---

## 🔐 Utilidades de Seguridad

### password.py
**Funciones de hashing de contraseñas con bcrypt**:
- `hash_password(password)`: Hashea contraseña con salt único automático
- `verify_password(password, hashed)`: Verifica contraseña contra hash

**Características de seguridad**:
- Cada contraseña genera un salt único (protección contra rainbow tables)
- Algoritmo bcrypt diseñado para ser lento (resistente a brute force)
- Salt embebido en el hash resultante (no se almacena por separado)

---

## 🎨 Estados de Reflex (UI y Lógica)

### AuthState (states/auth_state.py)
**Estado base de autenticación**:
- Gestiona login, logout y sesión del usuario
- Propiedades computadas:
  - `is_authenticated`: Verifica si hay usuario autenticado
  - `user_name`: Nombre completo del usuario actual
  - `user_role`: Rol del usuario ("student", "instructor", "admin")
  - `is_user_admin`, `is_user_instructor`, `is_user_student`: Validadores de rol
- Redireccionamiento automático al dashboard según rol

**Flujo de login**:
1. Validar email y contraseña no vacíos
2. Buscar usuario en base de datos por email
3. Verificar contraseña con bcrypt
4. Establecer sesión y redirigir a dashboard

---

### CourseState (states/course_state.py)
**Gestión de cursos en la UI**:
- `load_popular_courses()`: Cargar cursos para homepage (límite 6)
- `load_courses()`: Cargar catálogo completo
- `load_course_by_id()`: Cargar detalles completos de un curso
- `load_course_from_url()`: Extraer ID de URL dinámica y cargar curso

**Variables de estado**:
- Información del curso (title, description, thumbnail, price, level, etc.)
- Información del instructor (name, email, avatar, bio)
- Estadísticas (students_count, average_rating, total_reviews)
- Listas (categories, lessons, reviews)

---

### EnrollmentState (states/enrollment_state.py)
**Gestión de inscripciones**:
- `load_available_courses()`: Cargar cursos disponibles para inscripción
- `load_enrolled_courses()`: Cargar cursos del estudiante actual
- `enroll_in_course()`: Inscribir estudiante en un curso
- `confirm_unenroll()`: Desinscribir con confirmación previa
- `check_enrollment_status()`: Verificar si está inscrito en un curso

**Propiedades computadas**:
- `total_enrolled_courses`: Número de cursos inscritos
- `completed_courses`: Cursos con progreso 100%
- `average_progress`: Progreso promedio en todos los cursos

**Diálogos de confirmación**:
- Diálogo de confirmación para desinscripción
- Diálogo de resultado de inscripción (éxito/error)

---

### ProfileState (states/profile_state.py)
**Edición de perfil de usuario**:
- `update_profile()`: Actualizar nombre, apellido, email
- `change_password()`: Cambiar contraseña validando la actual
- `load_profile_data()`: Cargar datos del usuario en el formulario
- `toggle_password_section()`: Mostrar/ocultar sección de cambio de contraseña

**Validaciones**:
- Nombre y apellido obligatorios
- Email válido (debe contener "@")
- Nueva contraseña mínimo 6 caracteres
- Confirmación de contraseña debe coincidir

---

### UserManagementState (states/user_management_state.py)
**Administración de usuarios (solo admins)**:
- `load_users()`: Cargar todos los usuarios (estudiantes, instructors, admins)
- `save_user()`: Crear o actualizar usuario
- `confirm_delete_user()`: Eliminar usuario con confirmación
- `apply_filters()`: Filtrar por rol y búsqueda (nombre/email)

**Funcionalidades de filtrado**:
- Búsqueda por nombre o email
- Filtro por rol (all/student/instructor/admin)
- Actualización en tiempo real de `filtered_users`

**Protecciones**:
- Solo accesible para usuarios con rol "admin"
- No permite eliminar la propia cuenta del administrador
- Contraseña obligatoria al crear, opcional al editar

---

### InstructorState (states/instructor_state.py)
**Gestión de instructores en la UI**:
- `load_instructors()`: Cargar todos los instructores de la plataforma
- `load_instructor_by_id()`: Cargar perfil completo de un instructor específico
- `load_instructor_from_url()`: Extraer ID de URL y cargar instructor

**Variables de estado**:
- Información del instructor (name, email, avatar, bio, expertise)
- Estadísticas (total_courses, total_students únicos)
- Lista de cursos creados por el instructor

**Cálculos especiales**:
- Estudiantes únicos: Se usa un set para evitar contar duplicados (un estudiante puede estar en múltiples cursos del mismo instructor)

---

### ContactState (states/contact_state.py)
**Gestión del formulario de contacto**:
- `submit_contact()`: Validar y enviar mensaje a la base de datos
- `reset_form()`: Limpiar todos los campos del formulario
- Setters para cada campo (name, email, message)

**Validaciones**:
- Todos los campos son obligatorios
- Email debe contener "@" y "."
- Mensaje mínimo de 10 caracteres

**Comportamiento**:
- Si el envío es exitoso, resetea automáticamente el formulario
- Muestra mensajes de error en `error` o éxito en `success`

---

### AdminDashboardState (states/admin_dashboard_state.py)
**Dashboard administrativo con estadísticas**:
- `load_statistics()`: Cargar todas las estadísticas de la plataforma

**Estadísticas mostradas**:
- **Usuarios**: total_users, total_students, total_instructors, total_admins
- **Cursos**: total_courses
- **Inscripciones**: total_enrollments

**Precondiciones**:
- Usuario debe estar autenticado
- Usuario debe tener rol "admin"
- Si no cumple, la función retorna sin cargar datos

---

### CourseManagementState (states/course_management_state.py)
**Administración de cursos (solo admins)**:
- `load_courses()`: Cargar todos los cursos del sistema
- `save_course()`: Crear o actualizar curso con validaciones
- `confirm_delete_course()`: Eliminar curso con confirmación
- `apply_filters()`: Filtrar por búsqueda (título/descripción/categoría) y nivel

**Modos de operación**:
- **Modo "create"**: Crea nuevo curso con create_course()
- **Modo "edit"**: Actualiza curso existente con update_course()

**Validaciones**:
- Título y descripción obligatorios
- Datos del instructor (nombre y email) obligatorios
- Precio debe ser número válido y no negativo

**Funcionalidades de filtrado**:
- Búsqueda en título, descripción y categoría
- Filtro por nivel (all/beginner/intermediate/advanced)
- Actualización en tiempo real de `filtered_courses`

---

## 📄 Páginas de la Aplicación

### Páginas Públicas (sin autenticación)

#### index.py - Página Principal
- **Ruta**: `/`
- **Funcionalidad**: Homepage con mensaje de bienvenida y cursos populares destacados
- **Estado**: CourseState
- **Características**: Grid responsive con máximo 6 cursos, carga automática al montar

#### login.py - Inicio de Sesión
- **Ruta**: `/login`
- **Funcionalidad**: Formulario de autenticación con email y contraseña
- **Estado**: AuthState
- **Redirección**: Al dashboard según rol (student/instructor/admin)

#### register.py - Registro
- **Ruta**: `/register`
- **Funcionalidad**: Formulario de registro de nuevos usuarios
- **Estado**: RegisterState
- **Validaciones**: Email único, contraseña mínima, confirmación de contraseña

#### courses.py - Catálogo de Cursos
- **Ruta**: `/courses`
- **Funcionalidad**: Listado completo de todos los cursos disponibles
- **Estado**: CourseState
- **Características**: Grid responsive, carga todos los cursos

#### course_detail.py - Detalle de Curso
- **Ruta**: `/courses/[course_id]`
- **Funcionalidad**: Información completa del curso (lecciones, instructor, reseñas)
- **Estados**: CourseState, EnrollmentState
- **Características**: Botón de inscripción, detalles del instructor, lista de lecciones

#### instructors.py - Listado de Instructores
- **Ruta**: `/instructors`
- **Funcionalidad**: Todos los instructores de la plataforma
- **Estado**: InstructorState
- **Características**: Grid con tarjetas de instructores

#### instructor_detail.py - Perfil de Instructor
- **Ruta**: `/instructors/[instructor_id]`
- **Funcionalidad**: Perfil completo con cursos creados y estadísticas
- **Estado**: InstructorState
- **Características**: Bio, expertise, cursos, total de estudiantes

#### contact.py - Formulario de Contacto
- **Ruta**: `/contact`
- **Funcionalidad**: Envío de mensajes a la plataforma
- **Estado**: ContactState
- **Validaciones**: Campos obligatorios, email válido, mensaje mínimo 10 caracteres

---

### Páginas Protegidas (requieren autenticación)

#### profile.py - Perfil de Usuario
- **Ruta**: `/profile`
- **Protección**: `require_auth`
- **Funcionalidad**: Edición de datos personales y cambio de contraseña
- **Estado**: ProfileState

#### student_dashboard.py - Dashboard Estudiante
- **Ruta**: `/student/dashboard`
- **Protección**: `student_only`
- **Funcionalidad**: Cursos inscritos, progreso, estadísticas personales
- **Estado**: EnrollmentState

#### instructor_dashboard.py - Dashboard Instructor
- **Ruta**: `/instructor/dashboard`
- **Protección**: `instructor_only`
- **Funcionalidad**: Cursos creados, estadísticas de estudiantes
- **Estado**: InstructorState

#### admin_dashboard.py - Dashboard Administrativo
- **Ruta**: `/admin/dashboard`
- **Protección**: `admin_only`
- **Funcionalidad**: Estadísticas generales de la plataforma
- **Estado**: AdminDashboardState
- **Estadísticas**: Total usuarios por rol, cursos, inscripciones

#### user_management.py - Gestión de Usuarios
- **Ruta**: `/admin/users`
- **Protección**: `admin_only`
- **Funcionalidad**: CRUD completo de usuarios
- **Estado**: UserManagementState
- **Características**: Búsqueda, filtros por rol, crear/editar/eliminar usuarios

#### course_management.py - Gestión de Cursos
- **Ruta**: `/admin/courses`
- **Protección**: `admin_only`
- **Funcionalidad**: CRUD completo de cursos
- **Estado**: CourseManagementState
- **Características**: Búsqueda, filtros por nivel, crear/editar/eliminar cursos

---

## 🧩 Componentes Reutilizables

### protected.py
**Componentes de protección de rutas**:
- `require_auth(component)`: Requiere autenticación
- `require_role(component, allowed_roles)`: Requiere rol específico
- `admin_only(component)`: Solo administradores
- `instructor_only(component)`: Solo instructores
- `student_only(component)`: Solo estudiantes
- `instructor_or_admin(component)`: Instructores o admins

**Comportamiento**:
- Muestra componente si cumple requisitos
- Muestra mensaje de "Acceso Restringido" si no está autenticado
- Muestra mensaje de "Acceso Denegado" si no tiene el rol correcto

---

### navbar.py
**Barra de navegación responsive**:
- `navbar_link()`: Enlaces estilizados de navegación
- `user_menu()`: Menú desplegable para usuarios autenticados
- `navbar()`: Componente principal con versiones desktop y móvil

**Características**:
- Responsive (rx.desktop_only / rx.mobile_and_tablet)
- Menú dinámico según rol del usuario
- Botón de cambio de tema (dark/light mode)
- Logo y título clicables a homepage

---

### course_card.py
**Tarjeta visual de curso**:
- Imagen thumbnail con bordes redondeados
- Título y descripción (limitada a 3 líneas)
- Badge de nivel (beginner/intermediate/advanced)
- Precio formateado
- Nombre del instructor
- Efectos hover (elevación y sombra)
- Enlace a página de detalle del curso

---

### instructor_card.py
**Tarjeta visual de instructor**:
- Avatar circular con fallback
- Nombre del instructor
- Badge de área de expertise (opcional)
- Biografía (limitada a 3 líneas)
- Estadísticas (número de cursos)
- Efectos hover (elevación y sombra)
- Enlace a perfil del instructor

---

## 🗄️ Base de Datos

### MongoDB (database/mongodb.py)
**Gestor de conexión asíncrona**:
- Utiliza Motor (motor.motor_asyncio.AsyncIOMotorClient)
- Conexión singleton compartida en toda la aplicación
- Métodos:
  - `MongoDB.connect()`: Establecer conexión
  - `MongoDB.get_db()`: Obtener instancia de la base de datos
  - `MongoDB.close()`: Cerrar conexión

**Colecciones principales**:
- `users`: Usuarios del sistema
- `courses`: Cursos disponibles
- `contacts`: Mensajes de contacto

**Formato de datos**:
- MongoDB usa camelCase (firstName, createdAt)
- Python usa snake_case (first_name, created_at)
- Los modelos manejan la conversión automáticamente (to_dict/from_dict)

---

## 🛣️ Rutas de la Aplicación

### Rutas Públicas (sin autenticación)
- `/`: Página de inicio
- `/courses`: Catálogo de cursos
- `/courses/[course_id]`: Detalle de un curso
- `/instructors`: Listado de instructores
- `/instructors/[instructor_id]`: Detalle de un instructor
- `/contact`: Formulario de contacto
- `/login`: Inicio de sesión
- `/register`: Registro de nuevos usuarios

### Rutas Protegidas - Dashboards
- `/student/dashboard`: Dashboard para estudiantes (requiere rol student)
- `/instructor/dashboard`: Dashboard para instructores (requiere rol instructor)
- `/admin/dashboard`: Dashboard para administradores (requiere rol admin)

### Rutas Protegidas - Perfil
- `/profile`: Perfil de usuario (requiere autenticación)

### Rutas Protegidas - Administración
- `/admin/users`: Gestión de usuarios (solo admin)
- `/admin/courses`: Gestión de cursos (solo admin)

**Protección implementada en las páginas usando componentes de protected.py**

---

## 🔑 Sistema de Roles

### Estudiante (student)
**Permisos**:
- Ver catálogo de cursos e instructores
- Inscribirse en cursos
- Ver progreso de cursos inscritos
- Editar su propio perfil
- Enviar mensajes de contacto

**Dashboard**:
- Lista de cursos inscritos con progreso
- Estadísticas personales (cursos completados, promedio de progreso)
- Opción de desinscripción de cursos

---

### Instructor (instructor)
**Permisos**:
- Todo lo que puede hacer un estudiante
- Ver estadísticas de sus cursos
- Gestionar contenido de sus cursos (futuro)

**Dashboard**:
- Cursos creados
- Estadísticas de estudiantes inscritos
- Panel de gestión de cursos

---

### Administrador (admin)
**Permisos**:
- Acceso completo al sistema
- CRUD de usuarios (crear, editar, eliminar cualquier usuario)
- CRUD de cursos (gestión completa del catálogo)
- Ver mensajes de contacto
- Cambiar contraseñas de usuarios sin validación
- Ver estadísticas globales del sistema

**Dashboard**:
- Estadísticas generales (total usuarios, cursos, inscripciones)
- Acceso rápido a gestión de usuarios y cursos
- Panel de control administrativo

---

## 🔒 Seguridad Implementada

### Autenticación
- Contraseñas hasheadas con bcrypt (nunca se almacenan en texto plano)
- Salt único por contraseña (protección contra rainbow tables)
- Validación de email único en registro
- Verificación de contraseña en cambio de contraseña

### Autorización
- Sistema de roles (student/instructor/admin)
- Componentes de protección de rutas (require_auth, require_role)
- Validación de permisos en el backend (servicios)
- Restricciones específicas por rol en cada operación

### Validaciones
- Email válido en registro y edición
- Contraseña mínimo 6 caracteres
- Campos obligatorios en formularios
- Prevención de inscripciones duplicadas
- No permitir eliminar propia cuenta de admin

---

## 📦 Tecnologías Utilizadas

- **Reflex**: Framework full-stack de Python para desarrollo web
- **MongoDB**: Base de datos NoSQL
- **Motor**: Driver asíncrono de MongoDB para Python
- **bcrypt**: Hashing de contraseñas
- **Python 3.x**: Lenguaje de programación principal

---

## 📝 Convenciones de Código

### Nomenclatura
- **Python (snake_case)**: `first_name`, `created_at`, `get_full_name()`
- **MongoDB (camelCase)**: `firstName`, `createdAt`, `studentsEnrolled`
- **Conversión automática**: Los modelos manejan la traducción con `to_dict()` y `from_dict()`

### Docstrings
- Formato Google/NumPy
- Secciones: Args, Returns, Ejemplo, Nota
- Todas las funciones y clases documentadas en español

### Async/Await
- Todas las operaciones de base de datos son asíncronas
- Servicios usan `async def` y `await`
- Estados de Reflex pueden tener métodos async

---

## 🚀 Flujos Principales

### Flujo de Registro
1. Usuario completa formulario en `/register`
2. `RegisterState.handle_register()` valida campos
3. Verifica que el email no exista
4. Hashea la contraseña con bcrypt
5. `user_service.create_user()` guarda en MongoDB
6. Redirige a `/login`

### Flujo de Login
1. Usuario ingresa email y contraseña en `/login`
2. `AuthState.handle_login()` valida credenciales
3. `user_service.authenticate_user()` busca usuario
4. Verifica contraseña con bcrypt
5. Establece sesión en `AuthState.current_user`
6. Redirige a dashboard según rol

### Flujo de Inscripción
1. Estudiante autenticado ve curso en `/courses/[id]`
2. Click en botón "Inscribirse"
3. `EnrollmentState.enroll_in_course()` valida:
   - Usuario autenticado
   - Curso existe
   - No está ya inscrito
4. `enrollment_service.enroll_student()` crea inscripción
5. Incrementa contador `studentsEnrolled` del curso
6. Muestra diálogo de éxito
7. Actualiza lista de cursos inscritos

---

## 📊 Modelo de Datos de Inscripción

```python
# En el documento del usuario (colección users)
{
    "_id": ObjectId("..."),
    "firstName": "Juan",
    "lastName": "Pérez",
    "email": "juan@email.com",
    "role": "student",
    "enrolledCourses": [
        {
            "courseId": ObjectId("..."),
            "enrolledAt": ISODate("2024-01-15T10:00:00Z"),
            "progress": 45,  # 0-100
            "completedLessons": ["lesson1_id", "lesson2_id"],
            "status": "active"
        }
    ]
}

# En el documento del curso (colección courses)
{
    "_id": ObjectId("..."),
    "title": "Python Básico",
    "studentsEnrolled": 150,  # Se incrementa automáticamente
    "students": [ObjectId("user1"), ObjectId("user2"), ...]
}
```

---

## 🎯 Próximas Mejoras Sugeridas

1. **Paginación**: Implementar paginación en listados de cursos y usuarios
2. **Búsqueda avanzada**: Filtros por categoría, precio, nivel en cursos
3. **Sistema de lecciones**: Permitir completar lecciones y actualizar progreso
4. **Gestión de instructores**: CRUD de cursos para instructores
5. **Reseñas y calificaciones**: Permitir a estudiantes dejar reseñas
6. **Notificaciones**: Sistema de notificaciones para eventos importantes
7. **Analytics**: Dashboard con gráficas de estadísticas avanzadas
8. **Pagos**: Integración de pasarela de pagos para cursos premium

---

## 📚 Documentación de Referencia

- **Reflex Docs**: https://reflex.dev/docs
- **MongoDB Motor**: https://motor.readthedocs.io/
- **bcrypt**: https://pypi.org/project/bcrypt/

---

**Última actualización**: 2025-12-21
**Documentado por**: Claude Sonnet 4.5
**Estado del proyecto**: En desarrollo activo
