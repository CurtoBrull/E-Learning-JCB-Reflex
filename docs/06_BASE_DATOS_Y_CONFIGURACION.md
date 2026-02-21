# Base de Datos y Configuración - E-Learning JCB Reflex

## 💾 Arquitectura de Base de Datos

### MongoDB Atlas - Configuración

La aplicación utiliza **MongoDB Atlas** como base de datos principal, aprovechando sus características de escalabilidad y disponibilidad global.

#### Configuración de Conexión (`database/mongodb.py`)
```python
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

class MongoDB:
    """
    Gestor de conexión asíncrona a MongoDB Atlas.
    
    Características:
    - Singleton pattern para una sola instancia
    - Conexión asíncrona con Motor
    - Pool de conexiones automático
    - Manejo de errores de conexión
    """
    
    _client: AsyncIOMotorClient = None
    _db = None
    
    @classmethod
    async def connect(cls):
        """
        Establecer conexión con MongoDB Atlas.
        
        Configuración:
        - URI desde variable de entorno
        - Pool de conexiones: 10-100 conexiones
        - Timeout de conexión: 10 segundos
        - Timeout de operación: 30 segundos
        """
        if cls._client is None:
            try:
                mongodb_uri = os.getenv("MONGODB_URI")
                if not mongodb_uri:
                    raise ValueError("MONGODB_URI not found in environment variables")
                
                cls._client = AsyncIOMotorClient(
                    mongodb_uri,
                    maxPoolSize=100,
                    minPoolSize=10,
                    connectTimeoutMS=10000,
                    serverSelectionTimeoutMS=10000,
                    socketTimeoutMS=30000
                )
                
                # Verificar conexión
                await cls._client.admin.command('ping')
                cls._db = cls._client.get_default_database()
                
                print("✅ Connected to MongoDB Atlas successfully")
                
            except Exception as e:
                print(f"❌ Failed to connect to MongoDB: {e}")
                raise
    
    @classmethod
    def get_db(cls):
        """
        Obtener instancia de la base de datos.
        
        Returns:
            AsyncIOMotorDatabase: Instancia de la base de datos
        """
        if cls._db is None:
            raise RuntimeError("Database not connected. Call connect() first.")
        return cls._db
    
    @classmethod
    async def close(cls):
        """Cerrar conexión a MongoDB."""
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._db = None
            print("🔌 MongoDB connection closed")
```

---

## 🗄️ Esquema de Datos

### Colecciones Principales

La base de datos contiene **5 colecciones principales**:

| Colección | Documentos | Diseño | Propósito |
|-----------|------------|--------|-----------|
| `users` | ~1K-10K | Embebido | Usuarios del sistema |
| `courses` | ~100-1K | Embebido | Cursos de la plataforma |
| `contacts` | ~100-1K | Simple | Mensajes de contacto |
| `lessons` | ~1K-10K | Simple | Lecciones standalone |
| `logentries` | ~10K+ | Embebido | Logs del sistema |

### Diseño de Documentos

#### 1. Colección `users`
```javascript
{
  "_id": ObjectId("..."),
  "firstName": "María",
  "lastName": "García", 
  "email": "maria.garcia@email.com",
  "password": "$2b$12$...", // Hash bcrypt
  "role": "student", // "student" | "instructor" | "admin"
  "instructorProfile": {
    "avatarUrl": "https://...",
    "bio": "Desarrolladora Full Stack...",
    "expertise": "Desarrollo Web",
    "socialLinks": {
      "linkedin": "https://linkedin.com/in/...",
      "github": "https://github.com/..."
    }
  },
  "enrollments": [
    {
      "courseId": ObjectId("..."),
      "enrolledAt": ISODate("2025-01-15T10:00:00Z"),
      "progress": 45.5,
      "completed": false,
      "lastAccessedAt": ISODate("2025-01-20T15:30:00Z")
    }
  ],
  "coursesCreated": [ObjectId("..."), ObjectId("...")],
  "createdAt": ISODate("2025-01-01T00:00:00Z"),
  "updatedAt": ISODate("2025-01-20T12:00:00Z")
}
```
#### 2. Colección `courses`
```javascript
{
  "_id": ObjectId("..."),
  "title": "Desarrollo Web Full Stack con React y Node.js",
  "description": "Aprende a crear aplicaciones web completas...",
  "instructor": {
    "userId": ObjectId("..."),
    "name": "Carlos Rodríguez",
    "email": "carlos@email.com",
    "avatar": "https://...",
    "bio": "Instructor con 10 años de experiencia..."
  },
  "price": 99.99,
  "thumbnail": "https://images.example.com/course-thumbnail.jpg",
  "level": "intermediate", // "beginner" | "intermediate" | "advanced"
  "category": "Desarrollo Web",
  "categories": ["Desarrollo Web", "JavaScript", "React", "Node.js"],
  "students": [ObjectId("..."), ObjectId("...")], // IDs de estudiantes inscritos
  "lessons": [
    {
      "id": "lesson_001",
      "title": "Introducción a React",
      "content": "En esta lección aprenderemos los conceptos básicos...",
      "videoUrl": "https://www.youtube.com/watch?v=...",
      "duration": 25, // minutos
      "order": 1,
      "createdAt": ISODate("2025-01-01T00:00:00Z")
    },
    {
      "id": "lesson_002", 
      "title": "Componentes y Props",
      "content": "Los componentes son la base de React...",
      "videoUrl": "https://www.youtube.com/watch?v=...",
      "duration": 30,
      "order": 2,
      "createdAt": ISODate("2025-01-02T00:00:00Z")
    }
  ],
  "reviews": [
    {
      "id": "review_001",
      "studentId": ObjectId("..."),
      "studentName": "Ana Martínez",
      "rating": 5, // 1-5 estrellas
      "comment": "Excelente curso, muy bien explicado",
      "createdAt": ISODate("2025-01-15T00:00:00Z")
    }
  ],
  "averageRating": 4.8,
  "totalReviews": 25,
  "createdAt": ISODate("2025-01-01T00:00:00Z"),
  "updatedAt": ISODate("2025-01-20T00:00:00Z")
}
```

#### 3. Colección `contacts`
```javascript
{
  "_id": ObjectId("..."),
  "name": "Juan Pérez",
  "email": "juan.perez@email.com",
  "message": "Tengo una pregunta sobre los cursos de JavaScript...",
  "status": "pending", // "pending" | "read" | "replied"
  "adminNotes": "Respondido por email el 20/01/2025",
  "createdAt": ISODate("2025-01-18T10:30:00Z"),
  "updatedAt": ISODate("2025-01-20T14:15:00Z")
}
```

#### 4. Colección `lessons` (Diseño Híbrido)
```javascript
{
  "_id": ObjectId("..."),
  "courseId": ObjectId("..."),
  "title": "Introducción a React Hooks",
  "content": "Los hooks son una característica introducida en React 16.8...",
  "videoUrl": "https://www.youtube.com/watch?v=...",
  "duration": 35,
  "order": 5,
  "resources": [
    {
      "type": "pdf",
      "title": "Guía de React Hooks",
      "url": "https://resources.example.com/react-hooks.pdf"
    },
    {
      "type": "code",
      "title": "Ejemplos de código",
      "url": "https://github.com/example/react-hooks-examples"
    }
  ],
  "createdAt": ISODate("2025-01-05T00:00:00Z"),
  "updatedAt": ISODate("2025-01-10T00:00:00Z")
}
```

#### 5. Colección `logentries` (Auditoría)
```javascript
{
  "_id": ObjectId("..."),
  "userId": ObjectId("..."),
  "action": "LOGIN", // "LOGIN" | "LOGOUT" | "CREATE_COURSE" | "ENROLL" | etc.
  "resourceType": "USER", // "USER" | "COURSE" | "ENROLLMENT"
  "resourceId": ObjectId("..."),
  "metadata": {
    "ipAddress": "192.168.1.100",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "sessionId": "abc123...",
    "oldValues": {...}, // Para operaciones UPDATE
    "newValues": {...}  // Para operaciones UPDATE
  },
  "timestamp": ISODate("2025-01-20T15:45:30Z")
}
```

---

## 📊 Diseño Embebido vs Normalizado

### Ventajas del Diseño Actual

#### ✅ Beneficios del Diseño Embebido
- **Menos consultas**: Todo en un documento reduce round-trips
- **Mejor rendimiento**: Lectura de cursos completos en una consulta
- **Consistencia atómica**: Operaciones ACID a nivel de documento
- **Simplicidad**: Menos joins complejos
- **Escalabilidad de lectura**: Optimizado para consultas frecuentes

#### ⚠️ Consideraciones del Diseño
- **Tamaño de documentos**: Límite de 16MB por documento en MongoDB
- **Duplicación de datos**: Información del instructor repetida
- **Actualizaciones complejas**: Cambios en instructor requieren múltiples updates
- **Crecimiento**: Documentos grandes con muchas lecciones/reviews

### Estrategias de Optimización

#### 1. Proyecciones Selectivas
```javascript
// Solo campos necesarios para listado
db.courses.find(
  {},
  {
    title: 1,
    thumbnail: 1,
    price: 1,
    level: 1,
    "instructor.name": 1,
    averageRating: 1,
    students: 1
  }
)

// Excluir lecciones para vista general
db.courses.find(
  {},
  { lessons: 0, reviews: 0 }
)
```

#### 2. Agregaciones Eficientes
```javascript
// Estadísticas de cursos por instructor
db.courses.aggregate([
  {
    $group: {
      _id: "$instructor.userId",
      instructorName: { $first: "$instructor.name" },
      totalCourses: { $sum: 1 },
      totalStudents: { $sum: { $size: "$students" } },
      avgRating: { $avg: "$averageRating" }
    }
  }
])

// Cursos más populares
db.courses.aggregate([
  {
    $addFields: {
      studentsCount: { $size: "$students" }
    }
  },
  {
    $sort: { studentsCount: -1 }
  },
  {
    $limit: 10
  }
])
```

---

## 🔍 Índices de Base de Datos

### Índices Implementados

#### Colección `users`
```javascript
// Índice único para email (autenticación)
db.users.createIndex({ "email": 1 }, { unique: true })

// Índice para búsqueda por rol
db.users.createIndex({ "role": 1 })

// Índice compuesto para instructores activos
db.users.createIndex({ "role": 1, "createdAt": -1 })

// Índice para inscripciones de estudiante
db.users.createIndex({ "enrollments.courseId": 1 })
```

#### Colección `courses`
```javascript
// Índice para búsqueda por categoría
db.courses.createIndex({ "category": 1 })

// Índice para cursos por instructor
db.courses.createIndex({ "instructor.userId": 1 })

// Índice para estudiantes inscritos
db.courses.createIndex({ "students": 1 })

// Índice de texto completo para búsqueda
db.courses.createIndex({ 
  "title": "text", 
  "description": "text",
  "categories": "text"
})

// Índice compuesto para filtros comunes
db.courses.createIndex({ 
  "level": 1, 
  "category": 1, 
  "averageRating": -1 
})

// Índice para ordenamiento por popularidad
db.courses.createIndex({ "students": 1, "averageRating": -1 })
```

#### Colección `contacts`
```javascript
// Índice para búsqueda por email
db.contacts.createIndex({ "email": 1 })

// Índice para filtrado por estado
db.contacts.createIndex({ "status": 1, "createdAt": -1 })
```

#### Colección `lessons`
```javascript
// Índice para lecciones por curso
db.lessons.createIndex({ "courseId": 1, "order": 1 })

// Índice para búsqueda de contenido
db.lessons.createIndex({ "title": "text", "content": "text" })
```

#### Colección `logentries`
```javascript
// Índice para logs por usuario
db.logentries.createIndex({ "userId": 1, "timestamp": -1 })

// Índice para logs por acción
db.logentries.createIndex({ "action": 1, "timestamp": -1 })

// Índice TTL para limpieza automática (90 días)
db.logentries.createIndex({ "timestamp": 1 }, { expireAfterSeconds: 7776000 })
```

### Estrategias de Indexación

#### 1. Índices Compuestos
```javascript
// Para consultas con múltiples filtros
db.courses.createIndex({ 
  "level": 1,           // Filtro más selectivo primero
  "category": 1,        // Segundo filtro
  "averageRating": -1   // Ordenamiento al final
})
```

#### 2. Índices Parciales
```javascript
// Solo para cursos publicados
db.courses.createIndex(
  { "instructor.userId": 1 },
  { partialFilterExpression: { "status": "published" } }
)

// Solo para usuarios activos
db.users.createIndex(
  { "email": 1 },
  { partialFilterExpression: { "active": true } }
)
```

#### 3. Índices Sparse
```javascript
// Solo documentos con campo no nulo
db.users.createIndex(
  { "instructorProfile.expertise": 1 },
  { sparse: true }
)
```

---

## ⚙️ Configuración del Sistema

### Variables de Entorno

#### Archivo `.env.example`
```bash
# ==============================================
# CONFIGURACIÓN DE BASE DE DATOS
# ==============================================

# MongoDB Atlas URI
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority

# Configuración de conexión
MONGODB_MAX_POOL_SIZE=100
MONGODB_MIN_POOL_SIZE=10
MONGODB_CONNECT_TIMEOUT_MS=10000
MONGODB_SERVER_SELECTION_TIMEOUT_MS=10000

# ==============================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ==============================================

# Puertos de la aplicación
BACKEND_PORT=8000
FRONTEND_PORT=3000

# URL de la API
API_URL=http://localhost:8000

# Configuración CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# ==============================================
# CONFIGURACIÓN DE SEGURIDAD
# ==============================================

# Clave secreta para JWT (generar una aleatoria)
JWT_SECRET_KEY=your-super-secret-jwt-key-here-make-it-long-and-random

# Configuración de bcrypt
BCRYPT_ROUNDS=12

# Configuración de sesiones
SESSION_TIMEOUT_HOURS=24

# ==============================================
# CONFIGURACIÓN DE DESARROLLO
# ==============================================

# Nivel de logging
LOG_LEVEL=INFO

# Modo de desarrollo
DEBUG=true

# Configuración del navegador (WSL/Linux)
BROWSER=/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe

# ==============================================
# CONFIGURACIÓN DE PRODUCCIÓN
# ==============================================

# Dominio de producción
PRODUCTION_DOMAIN=https://elearning-jcb.com

# Configuración de email (futuro)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=noreply@elearning-jcb.com
SMTP_PASSWORD=your-email-password

# Configuración de almacenamiento (futuro)
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=elearning-jcb-assets
```

#### Configuración por Ambiente

##### Desarrollo (`.env`)
```bash
MONGODB_URI=mongodb+srv://dev_user:dev_pass@dev-cluster.mongodb.net/elearning_dev
API_URL=http://localhost:8000
DEBUG=true
LOG_LEVEL=DEBUG
BCRYPT_ROUNDS=10  # Menor para desarrollo más rápido
```

##### Testing (`.env.test`)
```bash
MONGODB_URI=mongodb+srv://test_user:test_pass@test-cluster.mongodb.net/elearning_test
API_URL=http://localhost:8001
DEBUG=true
LOG_LEVEL=DEBUG
BCRYPT_ROUNDS=4   # Mínimo para tests rápidos
```

##### Producción (`.env.production`)
```bash
MONGODB_URI=mongodb+srv://prod_user:complex_secure_password@prod-cluster.mongodb.net/elearning_prod
API_URL=https://api.elearning-jcb.com
DEBUG=false
LOG_LEVEL=WARNING
BCRYPT_ROUNDS=14  # Mayor seguridad en producción
SESSION_TIMEOUT_HOURS=8  # Sesiones más cortas
```

---

## 🚀 Configuración de Reflex

### Archivo `rxconfig.py`
```python
import os
import reflex as rx
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Determinar si estamos en producción
is_production = os.getenv("DEBUG", "true").lower() == "false"

class Config:
    """Configuración centralizada de la aplicación."""
    
    # Información básica
    APP_NAME = "E_Learning_JCB_Reflex"
    VERSION = "1.0.0"
    
    # Puertos
    BACKEND_PORT = int(os.getenv("BACKEND_PORT", "8000"))
    FRONTEND_PORT = int(os.getenv("FRONTEND_PORT", "3000"))
    
    # URLs
    API_URL = os.getenv("API_URL", f"http://localhost:{BACKEND_PORT}")
    
    # CORS
    if is_production:
        CORS_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
    else:
        CORS_ORIGINS = ["*"]  # Permitir todo en desarrollo
    
    # Base de datos
    MONGODB_URI = os.getenv("MONGODB_URI")
    
    # Seguridad
    JWT_SECRET = os.getenv("JWT_SECRET_KEY", "dev-secret-key")
    BCRYPT_ROUNDS = int(os.getenv("BCRYPT_ROUNDS", "12"))

# Configuración de Reflex
config = rx.Config(
    app_name=Config.APP_NAME,
    
    # Puertos
    backend_port=Config.BACKEND_PORT,
    frontend_port=Config.FRONTEND_PORT,
    
    # API
    api_url=Config.API_URL,
    
    # CORS
    cors_allowed_origins=Config.CORS_ORIGINS,
    
    # Host (0.0.0.0 para permitir conexiones externas)
    backend_host="0.0.0.0",
    
    # Plugins
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    
    # Configuración de compilación
    compile_timeout=300,  # 5 minutos
    
    # Configuración de desarrollo
    hot_reload=not is_production,
    
    # Configuración de producción
    production_mode=is_production,
)
```

### Configuración Avanzada

#### 1. Configuración de Logging
```python
import logging
from datetime import datetime

def setup_logging():
    """Configurar sistema de logging."""
    
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    
    # Formato de logs
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configuración básica
    logging.basicConfig(
        level=getattr(logging, log_level),
        format=log_format,
        handlers=[
            logging.StreamHandler(),  # Consola
            logging.FileHandler(f"logs/app_{datetime.now().strftime('%Y%m%d')}.log")
        ]
    )
    
    # Logger específico para seguridad
    security_logger = logging.getLogger("security")
    security_handler = logging.FileHandler("logs/security.log")
    security_handler.setFormatter(logging.Formatter(log_format))
    security_logger.addHandler(security_handler)
    security_logger.setLevel(logging.INFO)

# Inicializar logging
setup_logging()
```

#### 2. Configuración de Middleware
```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import time

def setup_middleware(app: FastAPI):
    """Configurar middleware de la aplicación."""
    
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=Config.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
    
    # Trusted hosts (solo en producción)
    if is_production:
        allowed_hosts = os.getenv("ALLOWED_HOSTS", "").split(",")
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=allowed_hosts
        )
    
    # Middleware de timing
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
```

---

## 📦 Comandos de Desarrollo y Despliegue

### Comandos Básicos

#### Desarrollo Local
```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# Ejecutar en modo desarrollo
reflex run

# Ejecutar con logging detallado
reflex run --loglevel debug

# Ejecutar en puerto específico
reflex run --backend-port 8001 --frontend-port 3001
```

#### Testing
```bash
# Ejecutar tests
pytest

# Tests con cobertura
pytest --cov=E_Learning_JCB_Reflex

# Tests específicos
pytest tests/test_auth.py

# Tests de integración
pytest tests/integration/
```

#### Producción
```bash
# Compilar para producción
reflex export

# Ejecutar en modo producción
reflex run --env prod

# Con configuración específica
reflex run --env prod --backend-host 0.0.0.0 --backend-port 8000
```

### Scripts de Utilidad

#### Gestión de Base de Datos
```bash
# Verificar conexión
python scripts/test_connection.py

# Crear usuarios de ejemplo
python scripts/create_sample_users.py

# Añadir videos a lecciones
python scripts/add_video_urls_to_lessons.py

# Backup de base de datos
python scripts/backup_database.py

# Restaurar base de datos
python scripts/restore_database.py --file backup_20250125.json
```

#### Mantenimiento
```bash
# Limpiar archivos compilados
reflex clean

# Actualizar dependencias
pip install --upgrade -r requirements.txt

# Verificar seguridad
pip audit

# Formatear código
black E_Learning_JCB_Reflex/

# Linting
flake8 E_Learning_JCB_Reflex/
```

---

## 🌐 Despliegue en Reflex Cloud

### Configuración de Despliegue

#### 1. Preparación
```bash
# Instalar Reflex CLI
pip install reflex

# Login en Reflex Cloud
reflex login

# Inicializar proyecto
reflex init --template blank
```

#### 2. Configuración del Proyecto
```bash
# Crear proyecto en Reflex Cloud
reflex deploy --create

# Configurar variables de entorno
reflex env set MONGODB_URI "mongodb+srv://..."
reflex env set JWT_SECRET_KEY "production-secret-key"
reflex env set BCRYPT_ROUNDS "14"

# Desplegar aplicación
reflex deploy
```

#### 3. Configuración de Dominio
```bash
# Configurar dominio personalizado
reflex domain add elearning-jcb.com

# Configurar SSL automático
reflex ssl enable
```

### Configuración de Producción

#### Variables de Entorno en Reflex Cloud
```bash
# Base de datos
reflex env set MONGODB_URI "mongodb+srv://prod_user:secure_pass@prod-cluster.mongodb.net/elearning_prod"

# Seguridad
reflex env set JWT_SECRET_KEY "super-secure-production-key-very-long-and-random"
reflex env set BCRYPT_ROUNDS "14"
reflex env set SESSION_TIMEOUT_HOURS "8"

# Configuración de aplicación
reflex env set DEBUG "false"
reflex env set LOG_LEVEL "WARNING"
reflex env set API_URL "https://api.elearning-jcb.com"

# CORS para producción
reflex env set CORS_ALLOWED_ORIGINS "https://elearning-jcb.com,https://www.elearning-jcb.com"
```

---

## 🔧 Optimización y Monitoreo

### Métricas de Base de Datos

#### 1. Monitoreo de Rendimiento
```javascript
// Estadísticas de colecciones
db.stats()

// Estadísticas específicas por colección
db.users.stats()
db.courses.stats()

// Operaciones lentas
db.setProfilingLevel(2, { slowms: 100 })
db.system.profile.find().sort({ ts: -1 }).limit(5)
```

#### 2. Análisis de Índices
```javascript
// Uso de índices
db.courses.explain("executionStats").find({ category: "Desarrollo Web" })

// Índices no utilizados
db.courses.aggregate([{ $indexStats: {} }])

// Tamaño de índices
db.courses.totalIndexSize()
```

### Optimización de Consultas

#### 1. Consultas Eficientes
```python
# Proyección selectiva
async def get_courses_summary():
    """Obtener resumen de cursos sin lecciones."""
    cursor = db.courses.find(
        {},
        {
            "title": 1,
            "thumbnail": 1, 
            "price": 1,
            "level": 1,
            "instructor.name": 1,
            "averageRating": 1,
            "students": 1
        }
    )
    return await cursor.to_list(length=None)

# Agregación optimizada
async def get_instructor_stats():
    """Estadísticas de instructores con agregación."""
    pipeline = [
        {
            "$group": {
                "_id": "$instructor.userId",
                "name": {"$first": "$instructor.name"},
                "totalCourses": {"$sum": 1},
                "totalStudents": {"$sum": {"$size": "$students"}},
                "avgRating": {"$avg": "$averageRating"}
            }
        },
        {"$sort": {"totalStudents": -1}}
    ]
    return await db.courses.aggregate(pipeline).to_list(length=None)
```

#### 2. Cache de Consultas (Futuro)
```python
import redis
import json
from datetime import timedelta

class QueryCache:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            decode_responses=True
        )
    
    async def get_cached_courses(self, cache_key: str):
        """Obtener cursos desde cache."""
        cached_data = self.redis_client.get(cache_key)
        if cached_data:
            return json.loads(cached_data)
        return None
    
    async def cache_courses(self, cache_key: str, courses: list, ttl: int = 300):
        """Cachear cursos por 5 minutos."""
        self.redis_client.setex(
            cache_key,
            ttl,
            json.dumps(courses, default=str)
        )
```

---

*Documentación de Base de Datos y Configuración*  
*Proyecto: E-Learning JCB Reflex*  
*Actualizado: 25 de enero de 2025*