# E-Learning JCB Reflex

[![Website e-learning-jcb-reflex](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://github.com/CurtoBrull) [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/CurtoBrull)

## Proyecto de Desarrollo de Aplicaciones Web

## E-Learning JCB

### Desarrollo de una Plataforma de E-learning con Reflex

## Tabla de Contenidos

- [E-Learning JCB Reflex](#e-learning-jcb-reflex)
  - [Proyecto de Desarrollo de Aplicaciones Web](#proyecto-de-desarrollo-de-aplicaciones-web)
  - [E-Learning JCB](#e-learning-jcb)
    - [Desarrollo de una Plataforma de E-learning con Reflex](#desarrollo-de-una-plataforma-de-e-learning-con-reflex)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción del Proyecto](#descripción-del-proyecto)
  - [Arquitectura del Proyecto](#arquitectura-del-proyecto)
    - [Estructura del Proyecto y Buenas Prácticas](#estructura-del-proyecto-y-buenas-prácticas)
  - [Requisitos Previos](#requisitos-previos)
  - [Instalación](#instalación)
  - [Configuración de Variables de Entorno](#configuración-de-variables-de-entorno)
  - [Autenticación y Usuarios](#autenticación-y-usuarios)
  - [Modelado de la Base de Datos](#modelado-de-la-base-de-datos)
    - [Relaciones entre las Colecciones](#relaciones-entre-las-colecciones)
    - [Colecciones](#colecciones)
      - [User (colección)](#user-colección)
      - [Course (colección)](#course-colección)
      - [Lesson (colección)](#lesson-colección)
      - [Enrollment (colección)](#enrollment-colección)
      - [Review (colección)](#review-colección)
      - [Category (colección)](#category-colección)
  - [Comandos para Ejecutar el Proyecto](#comandos-para-ejecutar-el-proyecto)
  - [Git Flow](#git-flow)
    - [Nomenclatura de los commits](#nomenclatura-de-los-commits)
  - [Documentación del Proyecto](#documentación-del-proyecto)
  - [Introducción](#introducción)
  - [Análisis del Entorno y Público Objetivo](#análisis-del-entorno-y-público-objetivo)
  - [Solución Propuesta](#solución-propuesta)
  - [Planificación Temporal del Desarrollo](#planificación-temporal-del-desarrollo)
  - [Viabilidad del Proyecto](#viabilidad-del-proyecto)
  - [Mejoras a implementar en un futuro](#mejoras-a-implementar-en-un-futuro)
  - [Conclusión](#conclusión)

## Descripción del Proyecto

Plataforma de aprendizaje en línea similar a Udemy o Platzi. Proporciona a los estudiantes la posibilidad de inscribirse en cursos y a los instructores la capacidad de crear y gestionar sus cursos.

Este proyecto es una aplicación web de E-Learning desarrollada con **Reflex**, **MongoDB** y **Python**. Los estudiantes pueden inscribirse en cursos, acceder al material y dejar valoraciones, mientras que los instructores pueden crear y gestionar cursos.

## Arquitectura del Proyecto

- **Framework**: ![Reflex](https://img.shields.io/badge/Reflex-5646ED?style=for-the-badge&logo=reflex&logoColor=white) - Framework Python para aplicaciones web full-stack
- **Backend**: ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
- **Frontend**: ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) (generado automáticamente por Reflex)
- **Base de Datos**: ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) con Motor (driver asíncrono)
- **Estilo**: Chakra UI (integrado en Reflex)

### Estructura del Proyecto y Buenas Prácticas

La estructura del proyecto sigue las mejores prácticas para aplicaciones Reflex:

```text
E-Learning-JCB-Reflex/
├── E_Learning_JCB_Reflex/
│   ├── E_Learning_JCB_Reflex.py    # Aplicación principal
│   ├── __init__.py
│   ├── models/                      # Modelos de datos (Pydantic)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── lesson.py
│   │   ├── enrollment.py
│   │   ├── review.py
│   │   └── category.py
│   ├── database/                    # Configuración de base de datos
│   │   ├── __init__.py
│   │   └── mongodb.py
│   ├── components/                  # Componentes reutilizables
│   │   └── __init__.py
│   ├── pages/                       # Páginas de la aplicación
│   │   └── __init__.py
│   └── services/                    # Lógica de negocio
│       └── __init__.py
├── assets/                          # Recursos estáticos
├── .web/                           # Frontend generado (no versionar)
├── reflex-env/                     # Entorno virtual (no versionar)
├── .env                            # Variables de entorno (no versionar)
├── .env.example                    # Ejemplo de variables de entorno
├── .gitignore
├── requirements.txt
├── rxconfig.py                     # Configuración de Reflex
└── README.md
```

**Buenas prácticas implementadas:**

- Separación clara de modelos, servicios y componentes
- Uso de tipado estricto con Python type hints
- Gestión de variables de entorno con python-dotenv
- Base de datos no relacional con MongoDB
- Arquitectura modular y escalable
- Documentación detallada

## Requisitos Previos

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) >= 3.10 (recomendado 3.14)
- ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) - Base de datos (MongoDB Atlas recomendado para tier gratuito)
- ![Node.js](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) >= 20.19.0 (para el frontend de Reflex)

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/CurtoBrull/E-Learning-JCB-Reflex
   cd E-Learning-JCB-Reflex
   ```

2. Crear y activar un entorno virtual con Python 3.14:

   ```bash
   python3.14 -m venv reflex-env
   source reflex-env/bin/activate  # En Windows: reflex-env\Scripts\activate
   ```

3. Instalar las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

4. [Configurar Variables de Entorno](#configuración-de-variables-de-entorno)

5. Iniciar el proyecto:

   ```bash
   reflex run
   ```

6. Acceder a la aplicación:

   ```text
   Frontend: http://localhost:3000/
   Backend API: http://localhost:8000/
   ```

7. (Opcional) Crear usuarios de ejemplo para testing:

   ```bash
   python scripts/create_sample_users.py
   ```

8. En el caso de ya tener el proyecto instalado, podemos arrancarlo con:

   ```bash
   source reflex-env/bin/activate && reflex run
   ```

   Ver [Usuarios de Ejemplo](docs/USUARIOS_EJEMPLO.md) para credenciales de acceso.

## Configuración de Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto basándote en `.env.example`:

```bash
# MongoDB Configuration
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/database?retryWrites=true&w=majority&appName=cluster-name

# JWT Secret for authentication (generate a random string)
JWT_SECRET=your-secret-key-here

# API Configuration
API_URL=http://localhost:8000
```

**Nota**: Nunca subas el archivo `.env` al repositorio. Usa `.env.example` como plantilla.

## Autenticación y Usuarios

La plataforma cuenta con un sistema de autenticación completo con bcrypt para hash de contraseñas.

### Características de Seguridad

- 🔐 **Hash de contraseñas**: Bcrypt con salt automático
- 🔑 **Validación de email**: Formato correcto y unicidad
- 🛡️ **Gestión de sesiones**: Estado persistente de autenticación
- 👥 **Sistema de roles**: Student, Instructor, Admin

### Usuarios de Ejemplo

Para facilitar el testing y desarrollo, se han creado usuarios de ejemplo:

| Rol | Email | Contraseña | Nombre |
|-----|-------|-----------|--------|
| 👨‍🎓 Student | maria.garcia@elearningjcb.com | student123 | María García |
| 👨‍🏫 Instructor | carlos.rodriguez@elearningjcb.com | instructor123 | Carlos Rodríguez |
| 👨‍💼 Admin | ana.martinez@elearningjcb.com | admin123 | Ana Martínez |

📖 **Documentación completa**: Ver [docs/USUARIOS_EJEMPLO.md](docs/USUARIOS_EJEMPLO.md)

### Páginas de Autenticación

- **Login**: `/login` - Inicio de sesión con email y contraseña
- **Registro**: `/register` - Creación de cuenta con selección de rol
- **Logout**: Disponible desde cualquier página cuando estés autenticado

### Crear Usuarios Adicionales

```bash
# Ejecutar script de creación de usuarios
python scripts/create_sample_users.py

# O crear manualmente desde la interfaz web
# Navegar a http://localhost:3000/register
```

## Modelado de la Base de Datos

La base de datos está modelada con las siguientes colecciones en MongoDB:

- **User**: Información de los usuarios (estudiantes e instructores)
- **Course**: Cursos ofrecidos en la plataforma
- **Lesson**: Lecciones individuales que pertenecen a un curso
- **Enrollment**: Relación entre estudiantes y cursos inscritos
- **Review**: Valoraciones de estudiantes sobre cursos
- **Category**: Categorías para clasificar cursos

### Relaciones entre las Colecciones

MongoDB es una base de datos no relacional, lo que permite flexibilidad en el diseño:

- **User ↔ Course**:
  - Los instructores crean cursos (referencia `instructor_id` en Course)
  - Los estudiantes se inscriben mediante Enrollment

- **Course ↔ Lesson**:
  - Cada curso contiene múltiples lecciones
  - Las lecciones referencian al curso mediante `course_id`

- **Enrollment**:
  - Tabla de unión entre User (estudiante) y Course
  - Campos: `student_id`, `course_id`, `enrolled_at`, `progress`

- **Review**:
  - Relaciona estudiantes con cursos valorados
  - Campos: `student_id`, `course_id`, `rating`, `comment`

- **Category**:
  - Los cursos pueden tener múltiples categorías
  - Array de `category_ids` en Course

### Colecciones

#### User (colección)

```python
{
  "_id": ObjectId,
  "firstName": str,
  "lastName": str,
  "email": str (único),
  "password": str (hasheado con bcrypt),
  "role": str ("student" | "instructor" | "admin"),
  "instructorProfile": dict (opcional),
  "enrollments": [ObjectId] (opcional),
  "coursesCreated": [ObjectId] (opcional),
  "createdAt": datetime
}
```

**Roles disponibles:**
- **student**: Usuario que aprende cursos
- **instructor**: Usuario que crea y gestiona cursos
- **admin**: Usuario con acceso completo a la plataforma

#### Course (colección)

```python
{
  "_id": ObjectId,
  "title": str,
  "description": str,
  "instructor_id": ObjectId (ref User),
  "category_ids": [ObjectId] (ref Category),
  "price": float,
  "thumbnail": str (opcional),
  "level": str ("beginner" | "intermediate" | "advanced"),
  "duration": int (minutos),
  "created_at": datetime,
  "updated_at": datetime
}
```

#### Lesson (colección)

```python
{
  "_id": ObjectId,
  "title": str,
  "content": str,
  "course_id": ObjectId (ref Course),
  "order": int,
  "video_url": str (opcional),
  "duration": int (minutos),
  "created_at": datetime,
  "updated_at": datetime
}
```

#### Enrollment (colección)

```python
{
  "_id": ObjectId,
  "student_id": ObjectId (ref User),
  "course_id": ObjectId (ref Course),
  "enrolled_at": datetime,
  "progress": float (0-100),
  "completed": bool,
  "completed_at": datetime (opcional)
}
```

#### Review (colección)

```python
{
  "_id": ObjectId,
  "course_id": ObjectId (ref Course),
  "student_id": ObjectId (ref User),
  "rating": int (1-5),
  "comment": str,
  "created_at": datetime,
  "updated_at": datetime
}
```

#### Category (colección)

```python
{
  "_id": ObjectId,
  "name": str (único),
  "description": str,
  "icon": str (opcional),
  "created_at": datetime
}
```

## Comandos para Ejecutar el Proyecto

- **Desarrollo**: `reflex run`
- **Modo debug**: `reflex run --loglevel debug`
- **Producción**: `reflex export && reflex run --env prod`
- **Limpiar archivos compilados**: `reflex clean`
- **Inicializar base de datos**: `reflex db init`

### Detener Servicios

Para detener los servicios de Reflex corriendo en los puertos 3000 y 8000:

```bash
# Detener servicios en puertos específicos
lsof -ti:3000,8000 | xargs kill -9

# Verificar que los puertos estén liberados
lsof -i:3000,8000
```

### Despliegue en Reflex Cloud

Para desplegar la aplicación en Reflex Cloud:

```bash
reflex deploy --project 80b9f062-22e7-44e5-ab3c-4a5485a994bb --envfile .env
```

**Notas:**

- El ID del proyecto (`80b9f062-22e7-44e5-ab3c-4a5485a994bb`) es único para esta aplicación
- El flag `--envfile .env` carga las variables de entorno desde el archivo `.env`
- Asegúrate de tener configuradas las credenciales de Reflex con `reflex login`

## Git Flow

- Nombre de la **rama principal**: `main`

- Nombre de la **rama de desarrollo**: `develop`

  Se realizarán pruebas en ramas feature antes de merge a main.

- Nombre de la **rama de feature**: `feature/feature-name`

- Nombre de la **rama de hotfix**: `hotfix/hotfix-name` (commits directos a `main`)

- Nombre de la **rama de workflows**: `workflow/workflow-name` (commits directos a `main`)

- Nombre de la **rama de documentación**: `documentation/documentation-name` (commits directos a `main`)

- Nombre de la **rama para linting**: `linting/linting-name`

### Nomenclatura de los commits

Se utiliza la siguiente nomenclatura sin numeración automática:

- **CDP**: `[CDP] descripción` - Código general, configuraciones iniciales
- **CDPF**: `[CDPF] descripción` - Desarrollo frontend (componentes Reflex)
- **CDPB**: `[CDPB] descripción` - Desarrollo backend (API, servicios)
- **CDPDB**: `[CDPDB] descripción` - Base de datos (modelos, migraciones)
- **CDPR**: `[CDPR] descripción` - Refactorizaciones y mejoras
- **WF**: `[WF] descripción` - Workflows de GitHub
- **HF**: `[HF] descripción` - Hotfixes urgentes
- **DOC**: `[DOC] descripción` - Documentación
- **TEST**: `[TEST] descripción` - Tests y pruebas

**Ejemplos:**

```text
[CDP] Configuración inicial del proyecto Reflex
[CDPF] Creación de componente de tarjeta de curso
[CDPB] Implementación de API de autenticación
[CDPDB] Modelo de usuario y validaciones
```

## Documentación del Proyecto

## Introducción

El objetivo de esta plataforma es hacer que la educación online sea más accesible y fácil para todos. Se ofrecen cursos interactivos en diferentes formatos, como videos y evaluaciones, accesibles desde cualquier lugar y dispositivo. Los instructores podrán crear y gestionar sus cursos, mientras que los estudiantes tendrán un espacio bien organizado para aprender y seguir su progreso de manera sencilla.

## Análisis del Entorno y Público Objetivo

La formación online está creciendo cada vez más debido a la flexibilidad que ofrece, representando una gran oportunidad para el desarrollo de plataformas educativas. El proyecto identifica oportunidades para que expertos moneticen sus conocimientos. Se garantiza el cumplimiento de normativas fiscales y de protección de datos (GDPR) para asegurar la información personal de los usuarios.

**Público objetivo:**

- Estudiantes que buscan aprendizaje flexible
- Instructores que desean compartir conocimiento
- Empresas de formación que necesitan plataformas efectivas

## Solución Propuesta

La plataforma se desarrolla con las siguientes tecnologías:

- **Framework Full-Stack**: Reflex (Python) - Desarrollo unificado frontend/backend
- **Backend**: FastAPI (integrado en Reflex) - API RESTful robusta
- **Frontend**: React (generado por Reflex) - Interfaz reactiva y moderna
- **Base de Datos**: MongoDB Atlas - Base de datos NoSQL escalable
- **Estilos**: Chakra UI - Sistema de diseño integrado en Reflex
- **Infraestructura**: Servicios en la nube (a definir para deployment)

**Ventajas de usar Reflex:**

- Desarrollo unificado en Python (frontend + backend)
- Menos código, mayor productividad
- Type-safety completo
- Hot reload automático
- SEO-friendly con server-side rendering

## Planificación Temporal del Desarrollo

El desarrollo está planificado para aproximadamente 12 semanas:

- **Semanas 1-2**: Análisis de requerimientos y diseño de arquitectura
- **Semana 3**: Diseño de base de datos MongoDB y configuración inicial
- **Semanas 4-5**: Configuración de Reflex y módulo de autenticación
- **Semanas 6-7**: Desarrollo de gestión de cursos y lecciones
- **Semana 8**: Módulo de inscripciones y seguimiento de progreso
- **Semana 9**: Sistema de valoraciones y reviews
- **Semana 10**: Testing y corrección de bugs
- **Semanas 11-12**: Documentación, optimización y deployment

## Viabilidad del Proyecto

- **Viabilidad Técnica**: Reflex permite desarrollo rápido con Python puro. Las tecnologías elegidas (MongoDB, FastAPI, React) son estables y bien documentadas.

- **Viabilidad Económica**:
  - MongoDB Atlas: Tier gratuito (512 MB)
  - Reflex: Framework open-source gratuito
  - Deployment: Opciones gratuitas disponibles (Railway, Fly.io)
  - Modelo de negocio: Suscripciones y comisiones por curso

- **Viabilidad Operativa**: Sistema diseñado para ser intuitivo tanto para instructores como estudiantes. Funcionalidades clave: inscripciones, progreso, evaluaciones.

- **Viabilidad Legal**:
  - Cumplimiento GDPR para protección de datos
  - Normativas fiscales para gestión de pagos
  - Términos de servicio y privacidad

## Mejoras a implementar en un futuro

La plataforma está en fase de desarrollo. Mejoras futuras:

- [ ] Sistema de pagos integrado (Stripe/PayPal)
- [ ] Certificados de finalización de cursos
- [ ] Chat en vivo entre estudiantes e instructores
- [ ] Gamificación (badges, puntos, rankings)
- [ ] Recomendaciones personalizadas con ML
- [ ] Aplicación móvil nativa
- [ ] Streaming de video en vivo para clases
- [ ] Foros de discusión por curso
- [ ] API pública para integraciones
- [ ] Modo offline para contenido descargado

## Conclusión

El proyecto es viable técnica, económica y operativamente. Reflex permite desarrollo ágil manteniendo Python como lenguaje único. MongoDB proporciona flexibilidad para escalar. El mercado de E-learning presenta una oportunidad significativa para ofrecer una plataforma educativa de calidad, accesible y escalable.
