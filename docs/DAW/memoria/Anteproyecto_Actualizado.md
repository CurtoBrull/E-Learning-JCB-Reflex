# E-Learning JCB

**Anteproyecto Desarrollo de Aplicaciones Web**
**Alumno:** Javier Curto Brull
**Fecha:** 2025-2026
**Centro:** I.E.S. Al-Ándalus

---

## 1. Introducción

El objetivo de esta plataforma es hacer que la educación online sea más accesible y fácil para todos. La plataforma ofrece cursos interactivos con información detallada sobre instructores, lecciones organizadas por secciones, y un sistema de valoraciones que permite a los estudiantes evaluar la calidad del contenido.

Los **instructores** pueden gestionar sus perfiles y asociarse con cursos, mientras que los **estudiantes** tienen acceso a un catálogo completo de cursos con información detallada, incluyendo:

- Descripción completa del curso
- Contenido organizado por secciones y lecciones
- Duración estimada de cada lección
- Valoraciones y reseñas de otros estudiantes
- Información del instructor responsable

La plataforma está diseñada para ser intuitiva, rápida y accesible desde cualquier dispositivo.

---

## 2. Análisis del Entorno y Público Objetivo

La formación online está creciendo cada vez más debido a la flexibilidad que ofrece, y esto es una gran oportunidad para el desarrollo de este proyecto. La plataforma aprovecha esta tendencia ofreciendo una experiencia moderna y profesional.

### Público Objetivo

- **Estudiantes:** Personas que buscan formación flexible y accesible desde cualquier lugar
- **Instructores:** Profesionales que quieren compartir sus conocimientos y gestionar cursos
- **Empresas de formación:** Organizaciones que necesitan una plataforma efectiva para cursos corporativos

### Normativa y Seguridad

El proyecto cumple con:

- **GDPR** - Protección de datos personales
- **Normativas fiscales** aplicables a plataformas educativas
- **Seguridad de datos** con MongoDB Atlas (cifrado en tránsito y en reposo)

---

## 3. Solución Propuesta

### Stack Tecnológico

#### **Backend y Frontend: Reflex 0.8.19**

- Framework full-stack en Python que genera aplicaciones web completas
- Genera automáticamente el frontend en React desde código Python
- Gestión de estado reactiva integrada
- Enrutamiento dinámico nativo
- Componentes reutilizables y tipado fuerte

#### **Base de Datos: MongoDB Atlas**

- Base de datos NoSQL en la nube
- Motor asíncrono con Python Motor (driver oficial)
- Escalabilidad automática
- Respaldos automáticos y alta disponibilidad

#### **Infraestructura**

- Desarrollo local con servidor de desarrollo integrado
- Opción de despliegue en Reflex Cloud
- Posibilidad de containerización con Docker

### Arquitectura de la Aplicación

```text
E_Learning_JCB_Reflex/
├── components/           # Componentes reutilizables de UI
│   ├── navbar.py
│   ├── course_card.py
│   └── instructor_card.py
├── pages/               # Páginas de la aplicación
│   ├── index.py         # Página de inicio
│   ├── courses.py       # Listado de cursos
│   ├── course_detail.py # Detalle de curso
│   ├── instructors.py   # Listado de instructores
│   └── instructor_detail.py # Detalle de instructor
├── states/              # Gestión de estado
│   ├── course_state.py
│   └── instructor_state.py
├── services/            # Lógica de negocio
│   ├── course_service.py
│   └── user_service.py
├── models/              # Modelos de datos
│   ├── course.py
│   └── user.py
├── database/            # Conexión a MongoDB
│   └── mongodb.py
└── utils/               # Utilidades reutilizables
    └── route_helpers.py
```

---

## 4. Planificación Temporal del Desarrollo

**Duración total:** ~26 semanas (6 meses hasta entrega en Mayo)

### Fase 1: Configuración Inicial (Semanas 1-2)

- Análisis exhaustivo de requisitos y casos de uso
- Diseño de la arquitectura del sistema
- Configuración del entorno de desarrollo
- Establecimiento de conexión con base de datos
- Definición de estructura de proyecto y convenciones

### Fase 2: Módulo de Cursos (Semanas 3-5)

- Diseño e implementación de modelos de datos para cursos
- Desarrollo de capa de servicios para gestión de cursos
- Creación de interfaz de listado de cursos
- Implementación de páginas de detalle con enrutamiento
- Desarrollo de componentes visuales reutilizables
- Sistema de valoraciones y reseñas
- Integración entre módulos

### Fase 3: Módulo de Instructores (Semanas 6-7)

- Diseño e implementación de modelos de usuarios
- Desarrollo de servicios para gestión de perfiles
- Creación de listado de instructores
- Implementación de perfiles detallados
- Componentes de visualización de información
- Sistema de relación entre instructores y cursos

### Fase 4: Optimización y Refactorización (Semana 8)

- Organización de utilidades comunes
- Refactorización de código duplicado
- Mejoras de rendimiento y carga
- Documentación técnica del código
- Corrección de deprecaciones y warnings
- Estandarización de estilos y componentes

### Fase 5: Sistema de Autenticación (Semanas 9-12)

- Implementación de registro de usuarios
- Sistema de inicio y cierre de sesión
- Gestión segura de sesiones y tokens
- Desarrollo de perfiles editables
- Protección y autorización de rutas
- Recuperación de contraseña por email

### Fase 6: Sistema de Inscripciones y Progreso (Semanas 13-16)

- Funcionalidad de inscripción a cursos
- Seguimiento de progreso por lección
- Dashboard personalizado del estudiante
- Sistema de generación de certificados
- Historial académico del usuario
- Sistema de notificaciones de progreso

### Fase 7: Panel de Instructor (Semanas 17-20)

- Panel de gestión de cursos (crear, editar, eliminar)
- Herramientas para gestión de contenido
- Dashboard con análisis y estadísticas
- Sistema de gestión de reseñas
- Herramientas de comunicación con estudiantes
- Reportes y métricas de rendimiento

### Fase 8: Funcionalidades Avanzadas (Semanas 21-23)

- Motor de búsqueda avanzado
- Sistema de filtrado y categorización
- Algoritmo de recomendaciones personalizadas
- Funcionalidad de listas de favoritos
- Exportación de datos y reportes
- Mejoras de experiencia de usuario

### Fase 9: Pruebas y Documentación Final (Semanas 24-26)

- Desarrollo y ejecución de pruebas unitarias
- Pruebas de integración end-to-end
- Pruebas de carga y estrés del sistema
- Elaboración de manual de usuario
- Documentación técnica completa
- Creación de video demostración
- Preparación de defensa del proyecto

---

## 5. Viabilidad del Proyecto

### Viabilidad Técnica

**Fortalezas:**

- Reflex simplifica el desarrollo full-stack con Python
- Un solo lenguaje para frontend y backend
- MongoDB Atlas ofrece escalabilidad sin configuración compleja
- Stack moderno con documentación completa
- Arquitectura modular que facilita el mantenimiento

**Tecnologías probadas:**

- Reflex es un framework activo con comunidad creciente
- MongoDB es una tecnología madura y ampliamente utilizada
- Python Motor proporciona acceso asíncrono eficiente a MongoDB
- Despliegue simplificado con Reflex Cloud

### Viabilidad Económica

**Costos de Desarrollo:**

- MongoDB Atlas Free Tier (0€/mes) - suficiente para desarrollo
- Hosting local durante desarrollo (0€)
- Sin costos de infraestructura en fase de desarrollo

**Costos de Producción:**

- MongoDB Atlas Shared Cluster: ~9€/mes
- Reflex Cloud o servidor VPS: ~10-20€/mes
- Dominio personalizado: ~12€/año
- **Total estimado:** 20-30€/mes

**Modelo de Negocio:**

- **Suscripciones mensuales** para estudiantes (acceso ilimitado)
- **Modelo marketplace:** Comisión del 20-30% por curso vendido
- **Planes empresariales** para formación corporativa
- **Cursos gratuitos con certificados de pago**

**Retorno de inversión esperado:** 6-12 meses

### Viabilidad Operativa

**Desarrollo:**

- Arquitectura modular que facilita el desarrollo en equipo
- Código documentado siguiendo buenas prácticas de Python
- Sistema de utilidades reutilizables implementado
- Control de versiones con Git y convenciones claras

**Usabilidad:**

- Interfaz intuitiva con navegación clara
- Diseño responsive para móvil, tablet y desktop
- Carga rápida con renderizado optimizado de Reflex
- Accesibilidad considerada en el diseño de componentes

**Mantenimiento:**

- Separación clara entre lógica de negocio (services) y presentación (pages)
- Componentes reutilizables que reducen duplicación
- Dependencias documentadas para facilitar actualizaciones
- Estructura escalable para futuras funcionalidades

### Viabilidad Legal

**Cumplimiento Normativo:**

- **GDPR:** MongoDB Atlas cifra datos en tránsito (TLS) y en reposo (AES-256)
- **Cookies:** Sistema de consentimiento pendiente de implementar
- **Propiedad intelectual:** Sistema de derechos por curso establecido
- **Protección de datos:** Políticas de privacidad y términos de uso definidos
- **Fiscalidad:** Gestión de facturación e impuestos según normativa española

---

## 6. Conclusión

El proyecto E-Learning JCB se presenta como una plataforma educativa moderna que aprovechará tecnologías actuales y escalables. La combinación de **Reflex** y **MongoDB Atlas** proporcionará una base sólida para el desarrollo ágil de funcionalidades manteniendo la calidad del código.

### Objetivos Técnicos

El proyecto busca alcanzar los siguientes objetivos técnicos:

- **Stack tecnológico eficiente:** Utilización de Reflex + MongoDB Atlas
- **Arquitectura limpia:** Separación clara de responsabilidades y módulos
- **Código mantenible:** Documentación exhaustiva y convenciones claras
- **Funcionalidades esenciales:** Sistema completo de cursos e instructores
- **Escalabilidad:** Diseño preparado para crecimiento futuro

### Diferenciación

La plataforma se diferenciará por:

- **Desarrollo ágil** con Reflex (Python full-stack)
- **Experiencia de usuario** moderna y responsive
- **Información detallada** de cursos con lecciones estructuradas
- **Perfiles completos** de instructores con estadísticas
- **Sistema de valoraciones** transparente y útil

### Perspectivas de Crecimiento

El mercado de E-learning está en expansión continua, y E-Learning JCB estará posicionado para:

- **Captar estudiantes** que buscan formación flexible y accesible
- **Atraer instructores** que quieren monetizar su conocimiento
- **Servir empresas** con necesidades de formación corporativa
- **Escalar globalmente** con infraestructura cloud

Con una arquitectura sólida y un plan de desarrollo bien estructurado, el proyecto tiene el potencial de convertirse en una plataforma educativa completa y competitiva en el mercado actual del E-learning.

---

**Fecha de documento:** Noviembre 2024
**Versión:** 1.0
**Estado:** Anteproyecto
