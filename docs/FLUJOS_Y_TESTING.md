# Flujos y Testing - E-Learning JCB Reflex

## 🔄 Flujos de Usuario por Rol

### Flujo de Usuario No Autenticado

#### Navegación Pública
```
Página Principal (/)
├── Ver cursos destacados
├── Explorar estadísticas de la plataforma
├── Acceder a registro/login
└── Navegar a páginas públicas
    ├── Catálogo de Cursos (/courses)
    │   ├── Filtrar por categoría/nivel
    │   ├── Buscar cursos
    │   └── Ver detalles de curso
    ├── Lista de Instructores (/instructors)
    │   ├── Ver perfiles de instructores
    │   └── Ver cursos por instructor
    └── Formulario de Contacto (/contact)
        └── Enviar mensaje
```

#### Flujo de Registro
```
1. Acceder a /register
2. Completar formulario:
   - Nombre y apellido
   - Email (validación de unicidad)
   - Contraseña (mínimo 6 caracteres)
   - Confirmación de contraseña
   - Selección de rol (estudiante/instructor)
3. Validaciones en tiempo real
4. Envío del formulario
5. Creación de usuario con contraseña hasheada
6. Redirección automática a login
7. Mensaje de éxito
```

#### Flujo de Inicio de Sesión
```
1. Acceder a /login
2. Introducir credenciales:
   - Email
   - Contraseña
3. Validación de credenciales
4. Verificación con bcrypt
5. Establecimiento de sesión
6. Redirección según rol:
   - Estudiante → /student/dashboard
   - Instructor → /instructor/dashboard
   - Admin → /admin/dashboard
```

---

### Flujo de Estudiante

#### Dashboard de Estudiante (/student/dashboard)
```
Acceso al Dashboard
├── Ver resumen de cursos inscritos
├── Revisar progreso en cursos activos
├── Explorar cursos recomendados
├── Ver estadísticas personales
│   ├── Total de cursos inscritos
│   ├── Cursos completados
│   ├── Progreso promedio
│   └── Tiempo total de estudio
└── Accesos rápidos
    ├── Continuar último curso
    ├── Explorar nuevos cursos
    └── Ver perfil
```

#### Flujo de Inscripción a Curso
```
1. Navegar al catálogo (/courses)
2. Seleccionar curso de interés
3. Ver detalles del curso (/courses/[id])
   - Información del instructor
   - Lista de lecciones
   - Reseñas de otros estudiantes
   - Precio y nivel
4. Hacer clic en "Inscribirse"
5. Validaciones:
   - Usuario autenticado ✓
   - Usuario es estudiante ✓
   - No inscrito previamente ✓
6. Proceso de inscripción:
   - Añadir a lista de estudiantes del curso
   - Añadir curso a inscripciones del usuario
   - Actualizar contadores
7. Redirección a visor de curso (/courses/[id]/view)
```

#### Flujo de Visualización de Curso
```
Acceso al Visor (/courses/[id]/view)
├── Validaciones de acceso:
│   ├── Usuario autenticado ✓
│   ├── Usuario es estudiante ✓
│   └── Usuario inscrito en el curso ✓
├── Interfaz del visor:
│   ├── Reproductor de video (YouTube embed)
│   ├── Lista lateral de lecciones
│   ├── Información de la lección actual
│   ├── Controles de navegación
│   └── Barra de progreso del curso
└── Funcionalidades:
    ├── Reproducir video de la lección
    ├── Navegar entre lecciones (anterior/siguiente)
    ├── Seleccionar lección específica
    ├── Ver progreso del curso
    └── Alternar visibilidad de sidebar
```

#### Flujo de Gestión de Perfil
```
1. Acceder a /profile
2. Ver información actual:
   - Datos personales
   - Cursos inscritos
   - Estadísticas de progreso
3. Editar información:
   - Cambiar nombre/apellido
   - Actualizar email (validación de unicidad)
   - Cambiar contraseña (validación de contraseña actual)
4. Guardar cambios
5. Confirmación de actualización
```

---

### Flujo de Instructor

#### Dashboard de Instructor (/instructor/dashboard)
```
Acceso al Dashboard
├── Ver resumen de cursos creados
├── Revisar estadísticas de estudiantes
├── Analizar reseñas recientes
├── Ver métricas de rendimiento:
│   ├── Total de cursos publicados
│   ├── Estudiantes totales inscritos
│   ├── Calificación promedio
│   └── Total de reseñas recibidas
└── Herramientas de gestión:
    ├── Crear nuevo curso
    ├── Editar cursos existentes
    └── Ver estadísticas detalladas
```

#### Flujo de Creación de Curso (Futuro)
```
1. Acceder a herramientas de instructor
2. Hacer clic en "Crear Nuevo Curso"
3. Completar información básica:
   - Título del curso
   - Descripción detallada
   - Categoría y nivel
   - Precio
   - Imagen thumbnail
4. Añadir lecciones:
   - Título de la lección
   - Contenido/descripción
   - URL del video
   - Duración estimada
   - Orden en el curso
5. Configurar opciones avanzadas:
   - Requisitos previos
   - Certificado de finalización
   - Recursos adicionales
6. Previsualizar curso
7. Publicar curso
8. Notificación a estudiantes potenciales
```

---

### Flujo de Administrador

#### Dashboard Administrativo (/admin/dashboard)
```
Acceso al Dashboard
├── Ver estadísticas generales:
│   ├── Total de usuarios por rol
│   ├── Total de cursos publicados
│   ├── Total de inscripciones activas
│   ├── Usuarios activos (24h/7d/30d)
│   └── Horas totales de contenido
├── Monitorear actividad reciente:
│   ├── Nuevos registros
│   ├── Inscripciones recientes
│   ├── Cursos creados
│   └── Mensajes de contacto
├── Alertas del sistema:
│   ├── Errores críticos
│   ├── Rendimiento de la base de datos
│   └── Uso de recursos
└── Accesos rápidos:
    ├── Gestión de usuarios
    ├── Gestión de cursos
    ├── Ver mensajes de contacto
    └── Configuración del sistema
```

#### Flujo de Gestión de Usuarios (/admin/users)
```
1. Acceder a gestión de usuarios
2. Ver tabla de todos los usuarios:
   - Filtros por rol (estudiante/instructor/admin)
   - Búsqueda por nombre/email
   - Ordenamiento por fecha de registro
3. Operaciones disponibles:
   ├── Crear Usuario:
   │   ├── Completar formulario completo
   │   ├── Asignar rol
   │   ├── Generar contraseña temporal
   │   └── Enviar credenciales por email (futuro)
   ├── Editar Usuario:
   │   ├── Modificar datos personales
   │   ├── Cambiar rol (con confirmación)
   │   ├── Actualizar estado (activo/inactivo)
   │   └── Resetear contraseña
   ├── Eliminar Usuario:
   │   ├── Confirmación de eliminación
   │   ├── Verificar dependencias (cursos, inscripciones)
   │   ├── Limpieza de datos relacionados
   │   └── Log de auditoría
   └── Operaciones masivas:
       ├── Exportar lista de usuarios
       ├── Importar usuarios desde CSV (futuro)
       └── Envío masivo de notificaciones (futuro)
```

#### Flujo de Gestión de Cursos (/admin/courses)
```
1. Acceder a gestión de cursos
2. Ver tabla de todos los cursos:
   - Filtros por nivel/categoría
   - Búsqueda por título/instructor
   - Ordenamiento por popularidad/fecha
3. Operaciones disponibles:
   ├── Crear Curso:
   │   ├── Información básica del curso
   │   ├── Asignar instructor
   │   ├── Configurar precio y categoría
   │   └── Añadir lecciones iniciales
   ├── Editar Curso:
   │   ├── Modificar información general
   │   ├── Gestionar lecciones (CRUD)
   │   ├── Actualizar instructor asignado
   │   └── Cambiar estado (publicado/borrador)
   ├── Eliminar Curso:
   │   ├── Verificar inscripciones activas
   │   ├── Notificar a estudiantes inscritos
   │   ├── Procesar reembolsos (futuro)
   │   └── Limpieza de datos relacionados
   └── Estadísticas del curso:
       ├── Número de inscripciones
       ├── Progreso promedio de estudiantes
       ├── Calificaciones y reseñas
       └── Ingresos generados (futuro)
```

---

## 🧪 Estrategias de Testing

### Testing Manual

#### Checklist de Funcionalidades Básicas

##### Autenticación y Autorización
- [ ] **Registro de usuario**
  - [ ] Validación de campos obligatorios
  - [ ] Verificación de email único
  - [ ] Hash correcto de contraseña
  - [ ] Creación exitosa en base de datos
  - [ ] Redirección a login tras registro

- [ ] **Inicio de sesión**
  - [ ] Validación de credenciales correctas
  - [ ] Rechazo de credenciales incorrectas
  - [ ] Establecimiento de sesión
  - [ ] Redirección según rol del usuario

- [ ] **Protección de rutas**
  - [ ] Acceso denegado sin autenticación
  - [ ] Acceso denegado con rol insuficiente
  - [ ] Redirección correcta a login
  - [ ] Mensajes de error apropiados

##### Gestión de Cursos
- [ ] **Catálogo público**
  - [ ] Listado de todos los cursos
  - [ ] Filtros por categoría y nivel
  - [ ] Búsqueda por texto
  - [ ] Paginación (futuro)

- [ ] **Detalle de curso**
  - [ ] Información completa del curso
  - [ ] Datos del instructor
  - [ ] Lista de lecciones
  - [ ] Botón de inscripción/acceso según estado

- [ ] **Visor de curso**
  - [ ] Acceso solo para estudiantes inscritos
  - [ ] Reproducción de videos de YouTube
  - [ ] Navegación entre lecciones
  - [ ] Indicador de progreso

##### Dashboards por Rol
- [ ] **Dashboard de estudiante**
  - [ ] Cursos inscritos
  - [ ] Progreso en cursos
  - [ ] Estadísticas personales
  - [ ] Accesos rápidos

- [ ] **Dashboard de instructor**
  - [ ] Cursos creados
  - [ ] Estadísticas de estudiantes
  - [ ] Reseñas recibidas
  - [ ] Herramientas de gestión

- [ ] **Dashboard de administrador**
  - [ ] Estadísticas globales
  - [ ] Actividad reciente
  - [ ] Alertas del sistema
  - [ ] Accesos a gestión

##### Administración
- [ ] **Gestión de usuarios**
  - [ ] CRUD completo de usuarios
  - [ ] Filtros y búsqueda
  - [ ] Cambio de roles
  - [ ] Eliminación con validaciones

- [ ] **Gestión de cursos**
  - [ ] CRUD completo de cursos
  - [ ] Gestión de lecciones
  - [ ] Asignación de instructores
  - [ ] Estadísticas por curso

### Testing Automatizado (Futuro)

#### Unit Tests
```python
# tests/test_models.py
import pytest
from E_Learning_JCB_Reflex.models.user import User
from E_Learning_JCB_Reflex.models.course import Course

class TestUserModel:
    def test_user_creation(self):
        """Test creación básica de usuario."""
        user = User(
            id="",
            first_name="Juan",
            last_name="Pérez",
            email="juan@test.com",
            password="hashed_password",
            role="student"
        )
        
        assert user.get_full_name() == "Juan Pérez"
        assert user.is_student == True
        assert user.is_instructor == False
        assert user.is_admin == False
    
    def test_user_to_dict(self):
        """Test conversión a diccionario."""
        user = User(
            id="507f1f77bcf86cd799439011",
            first_name="María",
            last_name="García",
            email="maria@test.com",
            password="hashed_password",
            role="instructor"
        )
        
        user_dict = user.to_dict()
        
        assert user_dict["firstName"] == "María"
        assert user_dict["lastName"] == "García"
        assert user_dict["email"] == "maria@test.com"
        assert user_dict["role"] == "instructor"
    
    def test_user_from_dict(self):
        """Test creación desde diccionario."""
        data = {
            "_id": "507f1f77bcf86cd799439011",
            "firstName": "Admin",
            "lastName": "Principal",
            "email": "admin@test.com",
            "password": "hashed_password",
            "role": "admin"
        }
        
        user = User.from_dict(data)
        
        assert user.first_name == "Admin"
        assert user.last_name == "Principal"
        assert user.is_admin == True

class TestCourseModel:
    def test_course_creation(self):
        """Test creación básica de curso."""
        course = Course(
            id="",
            title="Test Course",
            description="Test Description",
            price=99.99,
            level="beginner",
            category="Test"
        )
        
        assert course.title == "Test Course"
        assert course.price == 99.99
        assert course.level == "beginner"
    
    def test_add_student_to_course(self):
        """Test añadir estudiante al curso."""
        course = Course(
            id="",
            title="Test Course",
            students=[]
        )
        
        course.add_student("student_id_1")
        course.add_student("student_id_2")
        
        assert len(course.students) == 2
        assert "student_id_1" in course.students
        
        # No debe añadir duplicados
        course.add_student("student_id_1")
        assert len(course.students) == 2
```

#### Integration Tests
```python
# tests/test_services.py
import pytest
import asyncio
from E_Learning_JCB_Reflex.services.user_service import UserService
from E_Learning_JCB_Reflex.services.course_service import CourseService
from E_Learning_JCB_Reflex.services.enrollment_service import EnrollmentService

class TestUserService:
    @pytest.mark.asyncio
    async def test_create_user(self):
        """Test creación de usuario."""
        user_service = UserService()
        
        result = await user_service.create_user(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="test123",
            role="student"
        )
        
        assert result == True
        
        # Verificar que el usuario existe
        user = await user_service.get_user_by_email("test@example.com")
        assert user is not None
        assert user.first_name == "Test"
        assert user.role == "student"
    
    @pytest.mark.asyncio
    async def test_duplicate_email(self):
        """Test prevención de emails duplicados."""
        user_service = UserService()
        
        # Crear primer usuario
        result1 = await user_service.create_user(
            first_name="User1",
            last_name="Test",
            email="duplicate@example.com",
            password="test123",
            role="student"
        )
        assert result1 == True
        
        # Intentar crear segundo usuario con mismo email
        result2 = await user_service.create_user(
            first_name="User2",
            last_name="Test",
            email="duplicate@example.com",
            password="test456",
            role="instructor"
        )
        assert result2 == False

class TestEnrollmentService:
    @pytest.mark.asyncio
    async def test_enroll_student(self):
        """Test inscripción de estudiante."""
        enrollment_service = EnrollmentService()
        
        # Crear usuario y curso de prueba
        student_id = "test_student_id"
        course_id = "test_course_id"
        
        result = await enrollment_service.enroll_student(student_id, course_id)
        assert result == True
        
        # Verificar inscripción
        is_enrolled = await enrollment_service.is_enrolled(student_id, course_id)
        assert is_enrolled == True
    
    @pytest.mark.asyncio
    async def test_prevent_duplicate_enrollment(self):
        """Test prevención de inscripciones duplicadas."""
        enrollment_service = EnrollmentService()
        
        student_id = "test_student_id"
        course_id = "test_course_id"
        
        # Primera inscripción
        result1 = await enrollment_service.enroll_student(student_id, course_id)
        assert result1 == True
        
        # Segunda inscripción (debe fallar)
        result2 = await enrollment_service.enroll_student(student_id, course_id)
        assert result2 == False
```

#### End-to-End Tests (Futuro)
```python
# tests/test_e2e.py
import pytest
from playwright.async_api import async_playwright

class TestE2EFlows:
    @pytest.mark.asyncio
    async def test_student_registration_and_enrollment(self):
        """Test flujo completo de registro e inscripción."""
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            # 1. Ir a página de registro
            await page.goto("http://localhost:3000/register")
            
            # 2. Completar formulario de registro
            await page.fill('input[name="firstName"]', "Test")
            await page.fill('input[name="lastName"]', "Student")
            await page.fill('input[name="email"]', "teststudent@example.com")
            await page.fill('input[name="password"]', "test123")
            await page.fill('input[name="confirmPassword"]', "test123")
            await page.select_option('select[name="role"]', "student")
            
            # 3. Enviar formulario
            await page.click('button[type="submit"]')
            
            # 4. Verificar redirección a login
            await page.wait_for_url("**/login")
            
            # 5. Hacer login
            await page.fill('input[name="email"]', "teststudent@example.com")
            await page.fill('input[name="password"]', "test123")
            await page.click('button[type="submit"]')
            
            # 6. Verificar redirección a dashboard de estudiante
            await page.wait_for_url("**/student/dashboard")
            
            # 7. Ir a catálogo de cursos
            await page.click('a[href="/courses"]')
            
            # 8. Seleccionar un curso
            await page.click('.course-card:first-child')
            
            # 9. Inscribirse en el curso
            await page.click('button:has-text("Inscribirse")')
            
            # 10. Verificar acceso al visor
            await page.wait_for_url("**/courses/*/view")
            
            # 11. Verificar elementos del visor
            await page.wait_for_selector('iframe[src*="youtube.com/embed"]')
            await page.wait_for_selector('.lessons-sidebar')
            await page.wait_for_selector('.progress-bar')
            
            await browser.close()
    
    @pytest.mark.asyncio
    async def test_admin_user_management(self):
        """Test flujo de gestión de usuarios por admin."""
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            # 1. Login como admin
            await page.goto("http://localhost:3000/login")
            await page.fill('input[name="email"]', "admin@elearning.com")
            await page.fill('input[name="password"]', "admin123")
            await page.click('button[type="submit"]')
            
            # 2. Ir a gestión de usuarios
            await page.click('a[href="/admin/users"]')
            
            # 3. Crear nuevo usuario
            await page.click('button:has-text("Crear Usuario")')
            await page.fill('input[name="firstName"]', "New")
            await page.fill('input[name="lastName"]', "User")
            await page.fill('input[name="email"]', "newuser@example.com")
            await page.fill('input[name="password"]', "newpass123")
            await page.select_option('select[name="role"]', "instructor")
            await page.click('button:has-text("Guardar")')
            
            # 4. Verificar que el usuario aparece en la tabla
            await page.wait_for_selector('text=newuser@example.com')
            
            # 5. Editar usuario
            await page.click('button[data-user-email="newuser@example.com"][data-action="edit"]')
            await page.fill('input[name="firstName"]', "Updated")
            await page.click('button:has-text("Guardar")')
            
            # 6. Verificar actualización
            await page.wait_for_selector('text=Updated User')
            
            await browser.close()
```

### Performance Testing (Futuro)

#### Load Testing
```python
# tests/test_performance.py
import asyncio
import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor

class TestPerformance:
    async def test_concurrent_logins(self):
        """Test múltiples logins concurrentes."""
        async def login_user(session, user_id):
            async with session.post(
                "http://localhost:8000/api/login",
                json={
                    "email": f"user{user_id}@test.com",
                    "password": "test123"
                }
            ) as response:
                return response.status
        
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            
            # 100 logins concurrentes
            tasks = [login_user(session, i) for i in range(100)]
            results = await asyncio.gather(*tasks)
            
            end_time = time.time()
            duration = end_time - start_time
            
            # Verificar que todos los logins fueron exitosos
            assert all(status == 200 for status in results)
            
            # Verificar que el tiempo total es razonable (< 5 segundos)
            assert duration < 5.0
            
            print(f"100 logins concurrentes completados en {duration:.2f} segundos")
    
    async def test_course_loading_performance(self):
        """Test rendimiento de carga de cursos."""
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            
            async with session.get("http://localhost:8000/api/courses") as response:
                courses = await response.json()
                
            end_time = time.time()
            duration = end_time - start_time
            
            # Verificar respuesta exitosa
            assert response.status == 200
            assert len(courses) > 0
            
            # Verificar tiempo de respuesta (< 1 segundo)
            assert duration < 1.0
            
            print(f"Carga de {len(courses)} cursos completada en {duration:.3f} segundos")
```

---

## 📊 Datos de Prueba

### Usuarios de Ejemplo

Los usuarios de ejemplo se crean mediante el script `scripts/create_sample_users.py`:

#### Administradores
```python
{
    "email": "admin@elearning.com",
    "password": "admin123",
    "role": "admin",
    "firstName": "Admin",
    "lastName": "Principal"
}
```

#### Instructores
```python
[
    {
        "email": "carlos.rodriguez@elearning.com",
        "password": "instructor123",
        "role": "instructor",
        "firstName": "Carlos",
        "lastName": "Rodríguez",
        "instructorProfile": {
            "expertise": "Desarrollo Web Full Stack",
            "bio": "Desarrollador Full Stack con más de 10 años de experiencia...",
            "yearsExperience": 10
        }
    },
    {
        "email": "maria.garcia@elearning.com",
        "password": "instructor123",
        "role": "instructor",
        "firstName": "María",
        "lastName": "García",
        "instructorProfile": {
            "expertise": "Inteligencia Artificial",
            "bio": "Experta en IA y Machine Learning...",
            "yearsExperience": 8
        }
    }
]
```

#### Estudiantes
```python
[
    {
        "email": "juan.perez@email.com",
        "password": "student123",
        "role": "student",
        "firstName": "Juan",
        "lastName": "Pérez"
    },
    {
        "email": "laura.martinez@email.com",
        "password": "student123",
        "role": "student",
        "firstName": "Laura",
        "lastName": "Martínez"
    }
]
```

### Cursos de Ejemplo

Los cursos se pueden crear manualmente o mediante scripts de población de datos:

#### Curso de Desarrollo Web
```python
{
    "title": "Desarrollo Web Full Stack con React y Node.js",
    "description": "Aprende a crear aplicaciones web completas desde cero...",
    "instructor": {
        "userId": "instructor_id",
        "name": "Carlos Rodríguez",
        "email": "carlos.rodriguez@elearning.com"
    },
    "price": 99.99,
    "level": "intermediate",
    "category": "Desarrollo Web",
    "lessons": [
        {
            "title": "Introducción a React",
            "content": "Conceptos básicos de React...",
            "videoUrl": "https://www.youtube.com/embed/w7ejDZ8SWv8",
            "duration": 25,
            "order": 1
        }
    ]
}
```

### Escenarios de Testing

#### Escenario 1: Registro e Inscripción Completa
```
1. Usuario visita la página principal
2. Hace clic en "Registrarse"
3. Completa el formulario de registro como estudiante
4. Confirma el email (futuro)
5. Inicia sesión con las credenciales
6. Explora el catálogo de cursos
7. Selecciona un curso de interés
8. Se inscribe en el curso
9. Accede al visor de curso
10. Reproduce la primera lección
11. Navega entre lecciones
12. Verifica el progreso del curso
```

#### Escenario 2: Gestión Administrativa
```
1. Admin inicia sesión
2. Accede al dashboard administrativo
3. Revisa estadísticas generales
4. Va a gestión de usuarios
5. Crea un nuevo instructor
6. Asigna permisos apropiados
7. Va a gestión de cursos
8. Crea un nuevo curso
9. Asigna el curso al instructor creado
10. Publica el curso
11. Verifica que aparece en el catálogo público
```

#### Escenario 3: Flujo de Instructor
```
1. Instructor inicia sesión
2. Accede a su dashboard
3. Revisa estadísticas de sus cursos
4. Ve las reseñas recientes
5. Accede a la gestión de un curso específico
6. Añade una nueva lección
7. Actualiza el contenido de una lección existente
8. Reordena las lecciones
9. Publica los cambios
10. Verifica los cambios en el visor público
```

---

## 🔍 Validaciones Implementadas

### Validaciones de Frontend (Reflex States)

#### Formulario de Registro
```python
def validate_registration_form(self):
    """Validaciones en tiempo real del formulario de registro."""
    errors = []
    
    # Validar nombre
    if not self.first_name.strip():
        errors.append("El nombre es obligatorio")
    elif len(self.first_name) > 50:
        errors.append("El nombre no puede tener más de 50 caracteres")
    
    # Validar email
    if not self.email.strip():
        errors.append("El email es obligatorio")
    elif not self.is_valid_email(self.email):
        errors.append("El formato del email no es válido")
    
    # Validar contraseña
    if len(self.password) < 6:
        errors.append("La contraseña debe tener al menos 6 caracteres")
    
    # Validar confirmación
    if self.password != self.confirm_password:
        errors.append("Las contraseñas no coinciden")
    
    self.form_errors = errors
    return len(errors) == 0
```

#### Formulario de Curso
```python
def validate_course_form(self):
    """Validaciones del formulario de curso."""
    errors = []
    
    # Validar título
    if not self.course_title.strip():
        errors.append("El título del curso es obligatorio")
    elif len(self.course_title) > 200:
        errors.append("El título no puede tener más de 200 caracteres")
    
    # Validar precio
    try:
        price = float(self.course_price)
        if price < 0:
            errors.append("El precio no puede ser negativo")
    except ValueError:
        errors.append("El precio debe ser un número válido")
    
    # Validar instructor
    if not self.course_instructor_email.strip():
        errors.append("El email del instructor es obligatorio")
    
    self.form_errors = errors
    return len(errors) == 0
```

### Validaciones de Backend (Servicios)

#### Validaciones de Usuario
```python
async def validate_user_creation(self, user_data: dict) -> tuple[bool, list[str]]:
    """Validaciones completas para creación de usuario."""
    errors = []
    
    # Validar email único
    existing_user = await self.get_user_by_email(user_data["email"])
    if existing_user:
        errors.append("Ya existe un usuario con este email")
    
    # Validar formato de email
    if not self.is_valid_email_format(user_data["email"]):
        errors.append("El formato del email no es válido")
    
    # Validar rol
    if user_data["role"] not in ["student", "instructor", "admin"]:
        errors.append("Rol no válido")
    
    # Validar contraseña
    if len(user_data["password"]) < 6:
        errors.append("La contraseña debe tener al menos 6 caracteres")
    
    return len(errors) == 0, errors
```

#### Validaciones de Inscripción
```python
async def validate_enrollment(self, student_id: str, course_id: str) -> tuple[bool, str]:
    """Validaciones para inscripción de estudiante."""
    
    # Validar que el usuario existe y es estudiante
    user = await self.user_service.get_user_by_id(student_id)
    if not user:
        return False, "Usuario no encontrado"
    
    if not user.is_student:
        return False, "Solo los estudiantes pueden inscribirse en cursos"
    
    # Validar que el curso existe
    course = await self.course_service.get_course_by_id(course_id)
    if not course:
        return False, "Curso no encontrado"
    
    # Validar que no esté ya inscrito
    is_enrolled = await self.is_enrolled(student_id, course_id)
    if is_enrolled:
        return False, "Ya estás inscrito en este curso"
    
    return True, ""
```

### Validaciones de Seguridad

#### Validación de Acceso a Rutas
```python
def validate_course_viewer_access(self, user: User, course_id: str) -> tuple[bool, str]:
    """Validar acceso al visor de curso."""
    
    # Usuario debe estar autenticado
    if not user:
        return False, "Debes iniciar sesión para acceder"
    
    # Usuario debe ser estudiante
    if not user.is_student:
        return False, "Solo los estudiantes pueden ver el contenido de los cursos"
    
    # Usuario debe estar inscrito en el curso
    is_enrolled = any(
        enrollment["courseId"] == course_id 
        for enrollment in user.enrollments
    )
    
    if not is_enrolled:
        return False, "Debes inscribirte en este curso para acceder al contenido"
    
    return True, ""
```

#### Validación de Permisos Administrativos
```python
def validate_admin_operation(self, user: User, operation: str, target_id: str = None) -> tuple[bool, str]:
    """Validar operaciones administrativas."""
    
    # Usuario debe ser admin
    if not user or not user.is_admin:
        return False, "No tienes permisos de administrador"
    
    # Validaciones específicas por operación
    if operation == "delete_user":
        if target_id == user.id:
            return False, "No puedes eliminarte a ti mismo"
    
    elif operation == "change_role":
        if target_id == user.id:
            return False, "No puedes cambiar tu propio rol"
    
    elif operation == "delete_course":
        # Verificar si el curso tiene estudiantes inscritos
        course = self.course_service.get_course_by_id(target_id)
        if course and len(course.students) > 0:
            return False, "No puedes eliminar un curso con estudiantes inscritos"
    
    return True, ""
```

---

*Documentación de Flujos y Testing*  
*Proyecto: E-Learning JCB Reflex*  
*Actualizado: 25 de enero de 2025*