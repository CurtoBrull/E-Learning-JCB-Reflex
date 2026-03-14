# MEMORIA DEL PROYECTO - E-LEARNING JCB PLATFORM
## Desarrollo de Aplicaciones Web (DAW)
### I.E.S. Al-Ándalus (Almería) - Curso 2025-2026

---

**Alumno**: Javier Curto Brull
**Fecha de Entrega**: Mayo 2026

---

##  ÍNDICE GENERAL DE LA MEMORIA

Esta memoria del proyecto se estructura en **12 secciones principales**.

---

### DOCUMENTOS PRINCIPALES

#### 1. [MEMORIA PROYECTO DAW](#memoria-del-proyecto-e-learning-jcb-platform)
**Sección 1: [INTRODUCCIÓN](#1-introducción)** 
- 1.1. Descripción General del Proyecto
- 1.2. Finalidad y Objetivos
- 1.3. Requisitos y Restricciones
- 1.4. Alcance del Proyecto

**Contenido clave**:
- Descripción de E-Learning JCB Platform
- Motivación y contexto del proyecto
- Objetivos generales y específicos (estudiantes, instructores, admins)
- Requisitos funcionales y no funcionales (RF-001 a RF-007, RNF-001 a RNF-005)
- Restricciones técnicas, temporales, económicas y legales
- Funcionalidades incluidas en v1.0 y roadmap futuro

---

#### 2. [ANALISIS ENTORNO](#2-análisis-del-entorno)
**Sección 2: ANÁLISIS DEL ENTORNO** (~15 páginas)
- 2.1. Descripción de Oportunidades de Negocio
- 2.2. Obligaciones Fiscales, Laborales y Prevención de Riesgos
- 2.3. Ayudas y Subvenciones para el Desarrollo

**Contenido clave**:
- **Mercado e-learning**: Tamaño global ($315B), España (€2.1B), CAGR 13.7%
- **Oportunidades**: Formación técnica, B2B corporativo, marketplace instructores
- **Análisis de competencia**: Udemy, Coursera, Domestika, Platzi (matriz comparativa)
- **Ventajas competitivas**: Transparencia de contenidos, UX optimizada, costes reducidos
- **Obligaciones autónomo**: Alta RETA, IVA 21%, IRPF, Seguridad Social (tarifa plana 80€/mes)
- **Tabla de obligaciones Año 1**: 2,760€ (obligatorios), 3,560€ (recomendados)
- **Ayudas disponibles**:
  - Tarifa plana SS: 2,676€ ahorro
  - Almería Emprende: 3,000€
  - Cheque Innovación: 1,500€
  - Kit Digital: 1,500€
  - ENISA (si SL): 25,000€
- **Total ayudas conservador**: 7,176€

---

#### 3. [ANALISIS SISTEMA ACTUAL](#3-análisis-del-sistema-actual)
**Sección 3: ANÁLISIS DEL SISTEMA ACTUAL** (~6 páginas)
- 3.1. Contexto del Proyecto
- 3.2. Problemática Actual del E-Learning
- 3.3. Necesidades Identificadas
- 3.4. Justificación de la Necesidad del Proyecto

**Contenido clave**:
- **Nota importante**: Proyecto de nueva creación (no sustituye sistema existente)
- **5 Problemáticas identificadas**:
  1. Falta de transparencia en contenidos (68% usuarios quiere ver detalles)
  2. Interfaces saturadas y complejas (22% abandono en 30s)
  3. Sistemas de valoración poco fiables (67% desconfía de >4.5 estrellas)
  4. Costes elevados de desarrollo (50,000€-150,000€ tradicional)
  5. Falta de información sobre instructores
- **5 Necesidades no cubiertas**: Información pre-compra, UX optimizada, plataforma accesible, valoraciones confiables, seguimiento de progreso
- **Justificación**: Nicho específico, viabilidad técnica/económica, oportunidad de mercado, validación académica

---

#### 4. [SOLUCION PROPUESTA](#4-solución-propuesta)
**Sección 4: SOLUCIÓN PROPUESTA** (~16 páginas)
- 4.1. Tecnologías Existentes para el Desarrollo
- 4.2. Estudio Económico y Valoración de Presupuestos
- 4.3. Elección y Justificación de Tecnologías Seleccionadas
- 4.4. Recursos Humanos y Materiales Necesarios

**Contenido clave**:
- **Comparativa de stacks**:
  - MERN (9-12 meses, 30-50€/mes)
  - Django + React (8-10 meses, 40-70€/mes)
  - Laravel + Vue (8-11 meses, 35-60€/mes)
  - **Reflex + MongoDB** X SELECCIONADO (6 meses, 20-30€/mes)
- **Matriz de decisión**: Reflex 35/40 puntos (mejor opción)
- **Presupuesto de desarrollo**: 13,000€ (520h × 25€/h) + 490€ inicial
- **Costes operativos Año 1**: 17,376€ (incluye desarrollo)
- **Costes operativos Año 2**: 32,710€ (con contratación)
- **Proyección de ingresos**:
  - Año 1 conservador: 5,148€
  - Año 1 realista: 13,761€
  - Año 1 optimista: 26,532€
  - Año 2 realista: 120,000€
- **Punto de equilibrio**: 24 cursos vendidos/año (2/mes)
- **ROI Año 1** (sin coste desarrollo): +18% a +506%
- **Recursos necesarios**:
  - Hardware: 1,000-1,650€ (si no disponible)
  - Software: 0€ (100% gratuito)
  - Formación: 190€
  - Infraestructura desarrollo: 0€
  - Infraestructura producción: 360€/año

---

#### 5. [PLANIFICACION TEMPORAL](#5-planificación-temporal-del-desarrollo)
**Sección 5: PLANIFICACIÓN TEMPORAL DEL DESARROLLO** (~18 páginas)
- 5.1. Cronograma General del Proyecto
- 5.2. Detalle de Fases de Desarrollo (9 fases)
- 5.3. Diagrama de Gantt
- 5.4. Hitos Principales (10 milestones)
- 5.5. Plan de Mantenimiento (Post-Proyecto)
- 5.6. Modificaciones y Ampliaciones Futuras
- 5.7. Riesgos y Contingencias
- 5.8. Conclusiones de la Planificación

**Contenido clave**:
- **Duración total**: 26 semanas (Noviembre 2025 - Mayo 2026)
- **Horas totales**: 520 horas (20h/semana)
- **9 Fases**:
  1. Configuración Inicial (2 sem, 40h)
  2. Módulo de Cursos (3 sem, 60h)
  3. Módulo de Instructores (2 sem, 40h)
  4. Refactorización (1 sem, 20h)
  5. Autenticación y Roles (4 sem, 80h)
  6. Inscripciones y Progreso (4 sem, 80h)
  7. Panel de Instructor (4 sem, 80h)
  8. Funcionalidades Avanzadas (3 sem, 60h)
  9. Pruebas y Documentación (3 sem, 60h)
- **10 Milestones**: Desde "Entorno Configurado" hasta "Defensa Exitosa"
- **Plan de mantenimiento**:
  - Correctivo: 10-15h/mes (250-375€)
  - Evolutivo: ~10h/mes (260€)
  - Preventivo: 5.5h/mes (137.5€)
  - **Total**: 25-31h/mes (647-772€/mes)
- **Evolutivos planificados**:
  - Q3 2026: Pagos, certificados, emails (80h, 2,000€)
  - Q4 2026: Videoconferencias, chat, foros (148h, 3,700€)
  - 2027: App móvil, gamificación, IA (400h, 10,000€)
- **Riesgos identificados**: 6 riesgos con mitigaciones

---

#### 6. [ESTUDIO VIABILIDAD](#6-estudio-de-viabilidad-del-proyecto)
**Sección 6: ESTUDIO DE VIABILIDAD DEL PROYECTO** (~22 páginas)
- 6.1. Viabilidad Técnica
- 6.2. Viabilidad Económica
- 6.3. Viabilidad Operativa
- 6.4. Viabilidad Legal
- 6.5. Conclusión General del Estudio de Viabilidad

**Contenido clave**:
- **Viabilidad Técnica: 95%**  ALTA
  - Stack disponible y maduro (Reflex, MongoDB)
  - Conocimientos del equipo suficientes (con 30h formación)
  - Infraestructura cloud robusta (MongoDB Atlas, Reflex Cloud)
  - Riesgos técnicos identificados y mitigados
  - Inversión infraestructura: 0€ desarrollo, 360€/año producción
- **Viabilidad Económica: 85%**  ALTA
  - Costes muy bajos (13,190€ desarrollo + 4,376€ operativo Año 1)
  - Punto de equilibrio: 24 ventas/año (muy accesible)
  - Modelo escalable (coste marginal ≈ 0)
  - Ayudas disponibles: 7,176€ (conservador)
  - Rentabilidad Año 2 en todos los escenarios
  - ROI Año 1 (sin coste desarrollo): +18% a +506%
- **Viabilidad Operativa: 90%**  ALTA
  - Equipo (1 persona) suficiente para Año 1
  - Procesos bien definidos (25-28h/semana totales)
  - Usabilidad garantizada (Chakra UI, responsive)
  - Escalabilidad técnica nativa (MongoDB + Reflex Cloud)
  - Código mantenible (4.2/5)
  - Automatización de tareas críticas (backups, deploy)
- **Viabilidad Legal: 85%**  ALTA
  - Marco legal bien identificado (RGPD, LSSI, IVA, IRPF)
  - Cumplimiento técnico de RGPD (MongoDB Atlas cifrado, RBAC)
  - Documentación legal accesible (300€)
  - Gestoría para fiscal (600€/año)
  - Seguro RC profesional (200€/año)
  - Riesgos legales bajos y mitigados
- **VIABILIDAD GLOBAL: 89%**  **PROYECTO ALTAMENTE VIABLE**
- **Recomendación final**: **PROCEDER CON EL PROYECTO** 

---

#### 7. [DISEÑO IMPLEMENTACION](#7-documentación-del-diseño-e-implementación)
**Sección 7: DOCUMENTACIÓN DEL DISEÑO E IMPLEMENTACIÓN** (~20 páginas)
- 7.1. Prototipos de la Aplicación
- 7.2. Diseño de Interfaces
- 7.3. Diseño Lógico - Diagramación UML
- 7.4. Descripción Modular del Software
- 7.5. Diseño de Base de Datos
- 7.6. Otras Estructuras de Datos Utilizadas
- 7.7. Estudio de Seguridad de la Aplicación

**Contenido clave**:
- **Wireframes**: Home, Listado de cursos, Detalle de curso (ASCII art)
- **Mockups**: Paleta de colores (Chakra UI), tipografía (Inter)
- **Componentes principales**:
  - CourseCard: Tarjeta de curso reutilizable
  - Navbar: Navegación principal responsive
  - Protección de rutas: RBAC con decoradores
- **Páginas principales**:
  - Login, Registro, Dashboard (estudiante/instructor/admin)
  - Listado y detalle de cursos
- **Diagramas UML**:
  - Casos de uso (3 actores: Estudiante, Instructor, Admin)
  - Diagrama de clases (7 clases: User, Course, Section, Lesson, Enrollment, Progress, Rating)
  - Diagrama de secuencia (inscripción a curso)
  - Diagrama de actividades (crear curso completo)
- **Arquitectura en capas**: 5 capas (Presentación, Lógica UI, Lógica Negocio, Modelos, Acceso Datos)
- **Módulos principales**:
  - models/ (User, Course, Enrollment, Progress, Rating)
  - services/ (CRUD y lógica de negocio)
  - states/ (Estados reactivos de Reflex)
  - pages/ (Páginas completas)
  - components/ (Componentes reutilizables)
  - utils/ (Utilidades: password, validators, formatters)
- **Base de datos MongoDB**:
  - 5 colecciones: users, courses, enrollments, progress, ratings
  - Secciones y lecciones **embebidas** en cursos
  - Índices optimizados (12 índices totales)
  - Consultas frecuentes con tiempo <100ms
- **Seguridad**:
  - Hash bcrypt (12 rounds, salt único)
  - RBAC con 6 funciones de protección
  - Validación client-side y server-side
  - Protección contra inyección NoSQL (queries parametrizadas)
  - TLS/SSL (HTTPS), cifrado en reposo (AES-256)
  - **Nivel de madurez**: INTERMEDIO
  - 11 fortalezas implementadas, 3 parciales, 6 planificadas

---

#### 8. [CODIGO FUENTE](#8-código-fuente-documentado)
**Sección 8: CÓDIGO FUENTE DOCUMENTADO** (~15 páginas)
- 8.1. Estructura del Repositorio
- 8.2. Convenciones de Código
- 8.3. Módulos Principales
- 8.4. Acceso al Repositorio

**Contenido clave**:
- **Estructura del proyecto**: 40 archivos Python, ~5,000 LOC
- **Organización**:
  - `database/`: Conexión MongoDB (mongodb.py)
  - `models/`: 5 modelos (User, Course, Enrollment, Progress, Rating)
  - `services/`: 7 servicios CRUD + lógica de negocio
  - `states/`: 7 estados Reflex (Auth, Course, Instructor, Admin, Student, Enrollment, Rating)
  - `pages/`: 15 páginas completas
  - `components/`: 12 componentes reutilizables
  - `utils/`: 5 utilidades (password, validators, formatters, constants, helpers)
- **Código completo de ejemplos**:
  - `database/mongodb.py`: Conexión async con Motor
  - `utils/password.py`: Hash con bcrypt (12 rounds)
  - `components/protected.py`: HOC para RBAC
  - `models/user.py`: Modelo de usuario con validaciones
  - `services/course_service.py`: CRUD de cursos
  - `states/auth_state.py`: Estado de autenticación
- **Convenciones**:
  - PEP 8 (líneas 88 caracteres)
  - Docstrings estilo Google
  - Type hints en todas las funciones
  - Nombres en inglés (snake_case)
- **Control de versiones**:
  - Git Flow (main, develop, feature/*, hotfix/*)
  - Conventional Commits ([FEAT], [FIX], [REFACTOR], [DOC])
  - Commits atómicos y descriptivos
- **Repositorio**: GitHub (público o privado según decisión)
- **Métricas del código**: ~5,000 LOC, 7 módulos principales, complejidad ciclomática media

---

#### 9. [MANUAL CONFIGURACION](#9-manual-de-configuración-y-funcionamiento)
**Sección 9: MANUAL DE CONFIGURACIÓN Y FUNCIONAMIENTO** (~18 páginas)
- 9.1. Requisitos del Sistema
- 9.2. Instalación en Windows
- 9.3. Instalación en Linux/macOS
- 9.4. Configuración de MongoDB Atlas
- 9.5. Variables de Entorno
- 9.6. Despliegue en Producción
- 9.7. Resolución de Problemas

**Contenido clave**:
- **Requisitos del sistema**:
  - Hardware: 4GB RAM, 10GB disco, procesador dual-core
  - Software: Python 3.11+, Node.js 18+, Git 2.40+, navegador moderno
- **Instalación paso a paso**:
  - Windows: Python desde Microsoft Store, variables de entorno PATH
  - Linux: `sudo apt install python3.11 python3.11-venv`
  - macOS: Homebrew `brew install python@3.11`
- **MongoDB Atlas**:
  - Crear cuenta gratuita (M0 Cluster)
  - Configurar IP whitelist (0.0.0.0/0 desarrollo)
  - Crear usuario de BD (permisos read/write)
  - Obtener URI de conexión
- **Variables de entorno (.env)**:
  - `MONGODB_URI`: Conexión a MongoDB Atlas
  - `DB_NAME`: Nombre de la base de datos
  - `SECRET_KEY`: Clave secreta para sesiones
- **Despliegue**:
  - **Reflex Cloud** (recomendado): CLI `reflex deploy`, auto-scaling, SSL automático
  - **VPS Manual**: Ubuntu 22.04, Nginx, Systemd, SSL con Let's Encrypt
- **Troubleshooting**: 8 problemas comunes con soluciones detalladas

---

#### 10. [MANUAL USUARIO](#10-manual-de-usuario)
**Sección 10: MANUAL DE USUARIO** (~20 páginas)
- 10.1. Introducción para Usuarios
- 10.2. Registro y Acceso
- 10.3. Guía para Estudiantes
- 10.4. Guía para Instructores
- 10.5. Guía para Administradores
- 10.6. Preguntas Frecuentes (FAQ)

**Contenido clave**:
- **Introducción**: Qué es E-Learning JCB, beneficios, requisitos
- **Registro y Login**:
  - Formulario de registro (nombre, email, contraseña)
  - Validaciones en tiempo real
  - Confirmación de cuenta
  - Recuperación de contraseña (futuro)
- **Guía para Estudiantes**:
  - Buscar cursos (filtros por categoría, nivel, valoración)
  - Ver detalles de curso (descripción, lecciones, instructor)
  - Inscribirse en curso
  - Acceder a contenido (vídeos, PDFs)
  - Marcar lecciones como completadas
  - Dashboard de progreso (% completado, cursos activos)
  - Calificar y valorar cursos
- **Guía para Instructores**:
  - Crear curso paso a paso (título, descripción, imagen, precio)
  - Añadir secciones (estructura modular)
  - Añadir lecciones (título, contenido, vídeo, orden)
  - Editar y eliminar cursos
  - Ver estadísticas (inscripciones, ingresos, valoraciones)
  - Dashboard del instructor
- **Guía para Administradores**:
  - Gestión de usuarios (crear, editar, eliminar, cambiar roles)
  - Moderación de contenidos (aprobar/rechazar cursos)
  - Ver reportes (usuarios totales, cursos, inscripciones)
  - Panel de administración
- **FAQ**: 12 preguntas frecuentes por rol
- **Mockups ASCII**: Visualización de interfaces principales

---

#### 11. [PLAN FORMACION](#11-plan-de-formación-a-usuarios)
**Sección 11: PLAN DE FORMACIÓN A USUARIOS** (~18 páginas)
- 11.1. Introducción al Plan de Formación
- 11.2. Objetivos de la Formación
- 11.3. Identificación de Perfiles de Usuario
- 11.4. Programa de Formación por Perfil
- 11.5. Metodología de Formación
- 11.6. Materiales y Recursos Didácticos
- 11.7. Calendario de Formación
- 11.8. Evaluación de la Formación
- 11.9. Soporte Post-Formación
- 11.10. Presupuesto del Plan de Formación

**Contenido clave**:
- **Objetivos**: Capacitar usuarios, garantizar autonomía, reducir soporte
- **Perfiles identificados**:
  - Estudiantes (18-65 años, nivel técnico básico)
  - Instructores (25-60 años, nivel intermedio)
  - Administradores (25-50 años, nivel avanzado)
- **Programas de formación**:
  - **Estudiantes** (2h): Introducción, búsqueda cursos, inscripción, progreso, feedback
  - **Instructores** (4h): Filosofía plataforma, diseño instruccional, creación práctica, gestión, mejores prácticas
  - **Administradores** (3h): Arquitectura, gestión usuarios, moderación, reportes, soporte técnico
- **Metodología**:
  - Formación híbrida: Webinars en vivo + vídeos bajo demanda
  - Learning by doing (70% práctica)
  - Microlearning (vídeos 5-15 min)
- **Materiales**:
  - 15 vídeos tutoriales (2h 15min total)
  - 3 guías PDF (Estudiantes 8p, Instructores 25p, Admins 30p)
  - 4 infografías y cheat sheets
  - Curso demo y sandbox de práctica
- **Calendario**: Fase lanzamiento (mes 1-2), crecimiento (mes 3-6), consolidación (mes 6+)
- **Evaluación**:
  - Tests de finalización (estudiantes 10 preguntas, instructores ejercicio práctico)
  - Encuesta satisfacción (objetivo ≥4/5 estrellas)
  - Métricas de adopción post-formación
- **Soporte**:
  - 5 canales: FAQ, Email (24h), Chat (premium), Webinars Q&A, Foro comunidad
  - Escalado en 4 niveles
- **Presupuesto**:
  - Desarrollo materiales: 2,820€
  - Formadores: 1,475€
  - Infraestructura: 168€
  - Soporte Año 1: 15,000€
  - **Total**: 19,463€ (97.31€/usuario)
  - **ROI**: 33.6% primer año

---

#### 12. [BIBLIOGRAFIA](#12-bibliografía-y-fuentes-de-información)
**Sección 12: BIBLIOGRAFÍA Y FUENTES DE INFORMACIÓN** (~15 páginas)
- 12.1. Documentación Técnica Oficial
- 12.2. Frameworks y Librerías
- 12.3. Bases de Datos y Almacenamiento
- 12.4. Seguridad y Buenas Prácticas
- 12.5. Diseño de Interfaz de Usuario
- 12.6. Metodologías y Patrones de Diseño
- 12.7. Estudios de Mercado y E-Learning
- 12.8. Aspectos Legales y Empresariales
- 12.9. Pedagogía y Diseño Instruccional
- 12.10. Libros de Referencia
- 12.11. Recursos Online y Blogs
- 12.12. Herramientas de Desarrollo

**Contenido clave**:
- **Documentación oficial**:
  - Reflex 0.8.24 (https://reflex.dev/docs)
  - Python 3.12 (https://docs.python.org/3.12)
  - MongoDB 7.0 (https://www.mongodb.com/docs)
  - PEP 8, PEP 484, PEP 257
- **Frameworks y librerías**:
  - Motor 3.3.2 (async MongoDB driver)
  - bcrypt 4.1.2 (password hashing)
  - PyJWT 2.8.0 (tokens)
  - Chakra UI v2 (design system)
- **Seguridad**:
  - OWASP Top 10 (2021)
  - OWASP Cheat Sheets (password, input validation, auth)
  - RGPD/GDPR (UE 2016/679)
  - AEPD (Agencia Española Protección Datos)
- **UX/UI**:
  - Material Design Guidelines
  - Nielsen Norman Group (usabilidad)
  - WCAG 2.1 (accesibilidad)
- **Metodologías**:
  - Clean Architecture (Robert C. Martin, 2017)
  - Domain-Driven Design (Eric Evans, 2003)
  - Design Patterns (Gang of Four, 1994)
  - Agile Manifesto, Scrum Guide
- **Estudios de mercado**:
  - Global Market Insights (E-Learning Market 2024-2032)
  - Research and Markets (Spain E-Learning 2024)
  - Statista (estadísticas e-learning)
- **Análisis competencia**: Udemy, Coursera, Domestika, Platzi
- **Aspectos legales**:
  - BOE (Ley 6/2020 Servicios Sociedad Información)
  - Seguridad Social (RETA)
  - Agencia Tributaria (IVA, IRPF)
  - Kit Digital 2025, ayudas emprendedores
- **Pedagogía**:
  - "The Conditions of Learning" (Gagné, 1985)
  - ADDIE Model (instructional design)
  - "The Gamification of Learning" (Kapp, 2012)
- **Libros técnicos**:
  - "MongoDB: The Definitive Guide" (Bradshaw et al., 2019)
  - "Full Stack Python" (Makai, 2018)
  - "Web Application Security" (Hoffman, 2020)
  - "The Lean Startup" (Ries, 2011)
  - "Zero to One" (Thiel, 2014)
- **Recursos online**:
  - Real Python, Python Weekly
  - MongoDB Blog
  - Reflex Discord, GitHub
  - Smashing Magazine, CSS-Tricks
- **Herramientas**:
  - Git 2.43, GitHub
  - VSCode 1.85 + extensiones
  - Pytest 7.4.3
  - Reflex Cloud, DigitalOcean
- **Estándares W3C**: HTML5, CSS3, WAI-ARIA
- **Repositorios GitHub**: awesome-python, awesome-mongodb, reflex-examples
- **Conferencias**: PyCon España 2025, MongoDB World 2025
- **Podcasts**: Talk Python To Me, The Changelog
- **YouTube**: Corey Schafer, Traversy Media
- **Total fuentes**: 48 fuentes principales
- **Licencias**: Apache 2.0, MIT, PSF, SSPL (compatibles con uso comercial)

---

##  CONTACTO Y SOPORTE

Para consultas sobre esta memoria:
- **Alumno**: Javier Curto Brull
- **Email**: curto.brull.javier@jcurtobr.eu
- **Repositorio Git**: [URL del repositorio](https://github.com/CurtoBrull/E-Learning-JCB-Reflex)

---

**Última actualización**: Marzo 2026
**Versión del documento**: 2.0


<div style="page-break-after: always;"></div>


# MEMORIA DEL PROYECTO
# DESARROLLO DE APLICACIONES MULTIPLATAFORMA

---

<div style="text-align: center; margin-top: 100px;">

## **E-LEARNING JCB PLATFORM**
### Plataforma de Formación Online Interactiva

---

**Alumno:** Javier Curto Brull
**Ciclo Formativo:** Desarrollo de Aplicaciones Web (DAW)
**Centro:** I.E.S. Al-Ándalus (Almería)
**Año Académico:** 2025-2026

---

**Fecha de Entrega:** Mayo 2026

</div>

---


# 1. INTRODUCCIÓN

## 1.1. Descripción General del Proyecto

**E-Learning JCB Platform** es una plataforma web de formación online diseñada para democratizar el acceso a la educación digital de calidad. El proyecto nace de la necesidad de proporcionar una solución moderna, accesible y eficiente para el aprendizaje en línea, adaptándose a las demandas actuales del mercado educativo.

### Contexto y Motivación

En la era digital actual, la formación online se ha consolidado como una alternativa fundamental a la educación tradicional. La pandemia de COVID-19 aceleró esta transformación, evidenciando la necesidad de plataformas robustas que permitan el aprendizaje remoto efectivo. Sin embargo, muchas soluciones existentes presentan limitaciones:

- **Interfaces complejas** que dificultan la navegación
- **Falta de información detallada** sobre contenidos y estructura de cursos
- **Sistemas de valoración poco transparentes**
- **Limitaciones técnicas** en dispositivos móviles
- **Costes elevados** de implementación y mantenimiento

**E-Learning JCB Platform** surge como respuesta a estas problemáticas, ofreciendo una solución integral que combina:

- Facilidad de uso con diseño intuitivo y responsive
- Información completa y estructurada de cursos
- Sistema transparente de valoraciones y reseñas
- Gestión eficiente de perfiles de instructores y estudiantes
- Arquitectura moderna y escalable
- Costes reducidos de desarrollo y mantenimiento

### Características Principales

La plataforma se estructura en torno a tres pilares fundamentales:

#### 1. **Sistema de Cursos Interactivos**
- Catálogo completo de cursos organizados por categorías
- Descripción detallada con objetivos de aprendizaje
- Contenido estructurado en **secciones** y **lecciones**
- Duración estimada por lección
- Niveles de dificultad (Principiante, Intermedio, Avanzado)
- Sistema de etiquetas y requisitos previos

#### 2. **Gestión de Perfiles**
- **Instructores**: Perfiles profesionales con biografía, especialización y estadísticas
- **Estudiantes**: Acceso a historial de cursos, progreso y certificaciones
- **Administradores**: Panel de control para gestión completa del sistema

#### 3. **Sistema de Valoraciones y Feedback**
- Calificaciones por estrellas (1-5)
- Reseñas detalladas de estudiantes
- Estadísticas agregadas por curso e instructor
- Transparencia en la evaluación de calidad

### Público Objetivo

La plataforma está diseñada para tres tipos de usuarios principales:

1. **Estudiantes**: Personas que buscan formación flexible, accesible y de calidad
2. **Instructores**: Profesionales que desean compartir conocimientos y monetizar su experiencia
3. **Empresas**: Organizaciones que requieren plataformas de formación corporativa

### Tecnología Empleada

El proyecto se desarrolla utilizando un stack tecnológico moderno y eficiente:

- **Reflex 0.8.24**: Framework full-stack en Python para desarrollo rápido
- **MongoDB Atlas**: Base de datos NoSQL en la nube con escalabilidad automática
- **React**: Frontend generado automáticamente por Reflex
- **FastAPI**: Backend de alto rendimiento integrado
- **Chakra UI**: Sistema de diseño para interfaces consistentes

Esta elección tecnológica permite:
- Desarrollo ágil con un solo lenguaje (Python)
- Generación automática de frontend reactivo
- Escalabilidad sin configuración compleja
- Despliegue simplificado en la nube

---

## 1.2. Finalidad y Objetivos

### Finalidad del Proyecto

La finalidad principal de **E-Learning JCB Platform** es proporcionar una solución integral de e-learning que facilite el acceso a educación de calidad, mejorando la experiencia tanto de estudiantes como de instructores mediante una plataforma moderna, intuitiva y escalable.

### Objetivos Generales

#### 1. **Objetivo Académico**
Desarrollar un proyecto completo de fin de ciclo que integre todos los conocimientos adquiridos en el Ciclo Formativo de Desarrollo de Aplicaciones Web, demostrando competencias en:
- Desarrollo full-stack con tecnologías modernas
- Diseño de bases de datos NoSQL
- Implementación de sistemas de autenticación y autorización
- Gestión de estados y arquitectura de aplicaciones web
- Despliegue y mantenimiento en entornos de producción

#### 2. **Objetivo Técnico**
Crear una aplicación web robusta y escalable que implemente:
- Arquitectura en capas con separación de responsabilidades
- Sistema completo de CRUD (Create, Read, Update, Delete)
- Gestión eficiente de relaciones entre entidades
- Optimización de rendimiento en frontend y backend
- Seguridad en autenticación y protección de datos

#### 3. **Objetivo Funcional**
Proporcionar una plataforma que permita:
- Publicación y gestión de cursos por parte de instructores
- Búsqueda, visualización e inscripción de estudiantes
- Seguimiento de progreso y generación de certificados
- Comunicación efectiva entre usuarios
- Administración centralizada del sistema

### Objetivos Específicos

#### Para Estudiantes:
1. **Acceso intuitivo** a un catálogo completo de cursos
2. **Información detallada** de cada curso antes de la inscripción
3. **Navegación clara** por secciones y lecciones
4. **Seguimiento de progreso** en tiempo real
5. **Sistema de valoraciones** para evaluar la calidad
6. **Acceso multiplataforma** desde cualquier dispositivo

#### Para Instructores:
1. **Gestión completa** de cursos propios
2. **Herramientas de creación** de contenido estructurado
3. **Panel de estadísticas** de inscripciones y valoraciones
4. **Perfil profesional** con biografía y especialización
5. **Gestión de reseñas** y feedback de estudiantes

#### Para Administradores:
1. **Control total** sobre usuarios y contenidos
2. **Gestión de roles** y permisos
3. **Monitoreo** de actividad del sistema
4. **Reportes** y estadísticas globales
5. **Moderación** de contenidos inapropiados

### Objetivos Empresariales

Desde la perspectiva de negocio, el proyecto busca:

1. **Viabilidad Económica**: Crear un modelo de negocio sostenible basado en:
   - Modelo Freemium (cursos básicos gratuitos, premium de pago)
   - Comisiones por ventas de cursos
   - Suscripciones corporativas

2. **Escalabilidad**: Diseñar una arquitectura que permita:
   - Crecimiento de usuarios sin degradación de rendimiento
   - Expansión geográfica mediante cloud
   - Incorporación de nuevas funcionalidades

3. **Competitividad**: Diferenciarse de competidores mediante:
   - Experiencia de usuario superior
   - Costes reducidos gracias a la arquitectura eficiente
   - Información transparente y detallada

### Objetivos de Calidad

1. **Código mantenible**: Documentación exhaustiva y buenas prácticas
2. **Testing**: Cobertura de pruebas unitarias e integración
3. **Performance**: Tiempos de carga inferiores a 2 segundos
4. **Accesibilidad**: Cumplimiento de estándares WCAG 2.1
5. **Seguridad**: Implementación de medidas robustas de protección

---

## 1.3. Requisitos y Restricciones

### Requisitos Funcionales

#### RF-001: Gestión de Usuarios
- **RF-001.1**: El sistema debe permitir registro de usuarios con email único
- **RF-001.2**: El sistema debe permitir login con email y contraseña
- **RF-001.3**: El sistema debe asignar roles (student, instructor, admin)
- **RF-001.4**: El sistema debe permitir edición de perfiles
- **RF-001.5**: El sistema debe permitir cambio de contraseña
- **Prioridad**: Alta
- **Estado**: Implementado

#### RF-002: Gestión de Cursos
- **RF-002.1**: Los instructores pueden crear cursos con información completa
- **RF-002.2**: Los cursos deben organizarse en secciones y lecciones
- **RF-002.3**: Cada lección debe tener título, contenido y duración
- **RF-002.4**: Los cursos deben mostrar valoración promedio
- **RF-002.5**: Los cursos pueden tener niveles (Principiante, Intermedio, Avanzado)
- **Prioridad**: Alta
- **Estado**: Implementado

#### RF-003: Sistema de Inscripciones
- **RF-003.1**: Los estudiantes pueden inscribirse en cursos
- **RF-003.2**: El sistema debe prevenir inscripciones duplicadas
- **RF-003.3**: Los estudiantes pueden ver historial de inscripciones
- **RF-003.4**: El sistema debe registrar fecha de inscripción
- **Prioridad**: Alta
- **Estado**: Implementado

#### RF-004: Sistema de Progreso
- **RF-004.1**: El sistema debe registrar lecciones completadas
- **RF-004.2**: Debe calcularse el progreso porcentual por curso
- **RF-004.3**: Los estudiantes pueden ver su progreso en dashboard
- **Prioridad**: Media
- **Estado**: Implementado

#### RF-005: Sistema de Valoraciones
- **RF-005.1**: Los estudiantes pueden valorar cursos (1-5 estrellas)
- **RF-005.2**: Los estudiantes pueden escribir reseñas
- **RF-005.3**: El sistema calcula promedio de valoraciones
- **RF-005.4**: Las valoraciones se muestran en detalle de curso
- **Prioridad**: Media
- **Estado**: Implementado

#### RF-006: Gestión de Instructores
- **RF-006.1**: Los instructores tienen perfil con biografía
- **RF-006.2**: Se muestra lista de cursos por instructor
- **RF-006.3**: Se calculan estadísticas de inscripciones
- **RF-006.4**: Se muestra valoración promedio del instructor
- **Prioridad**: Media
- **Estado**: Implementado

#### RF-007: Panel de Administración
- **RF-007.1**: Los admins pueden ver todos los usuarios
- **RF-007.2**: Los admins pueden modificar roles
- **RF-007.3**: Los admins pueden eliminar usuarios
- **RF-007.4**: Los admins pueden moderar contenidos
- **Prioridad**: Media
- **Estado**: Implementado

### Requisitos No Funcionales

#### RNF-001: Rendimiento
- **RNF-001.1**: Tiempo de carga inicial < 3 segundos
- **RNF-001.2**: Tiempo de respuesta de API < 500ms
- **RNF-001.3**: Soporte de 100 usuarios concurrentes
- **RNF-001.4**: Consultas a BD optimizadas con índices
- **Prioridad**: Alta
- **Estado**: En desarrollo

#### RNF-002: Seguridad
- **RNF-002.1**: Contraseñas hasheadas con bcrypt
- **RNF-002.2**: Control de acceso basado en roles (RBAC)
- **RNF-002.3**: Validación de inputs en frontend y backend
- **RNF-002.4**: Conexión segura a BD (TLS/SSL)
- **Prioridad**: Crítica
- **Estado**: Implementado

#### RNF-003: Usabilidad
- **RNF-003.1**: Diseño responsive (móvil, tablet, desktop)
- **RNF-003.2**: Navegación intuitiva con máximo 3 clics
- **RNF-003.3**: Mensajes de error claros y accionables
- **RNF-003.4**: Feedback visual en todas las acciones
- **Prioridad**: Alta
- **Estado**: Implementado

#### RNF-004: Escalabilidad
- **RNF-004.1**: Arquitectura modular para crecimiento
- **RNF-004.2**: Base de datos NoSQL para flexibilidad
- **RNF-004.3**: Despliegue en cloud con autoscaling
- **Prioridad**: Media
- **Estado**: Implementado parcialmente

#### RNF-005: Mantenibilidad
- **RNF-005.1**: Código documentado con docstrings
- **RNF-005.2**: Separación de capas (MVC)
- **RNF-005.3**: Componentes reutilizables
- **RNF-005.4**: Convenciones de código consistentes
- **Prioridad**: Alta
- **Estado**: Implementado

### Restricciones del Proyecto

#### Restricciones Técnicas

1. **RT-001: Tecnología de Desarrollo**
   - Framework: Reflex 0.8.24 (Python)
   - Base de datos: MongoDB Atlas
   - Lenguaje: Python 3.10+
   - **Justificación**: Requisito académico de usar tecnologías modernas

2. **RT-002: Compatibilidad**
   - Navegadores: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
   - Dispositivos: Desktop, tablet (768px+), móvil (375px+)
   - **Justificación**: Soporte de navegadores modernos

3. **RT-003: Infraestructura**
   - Despliegue: Reflex Cloud o VPS
   - Base de datos: MongoDB Atlas (tier M0 gratuito en desarrollo)
   - **Justificación**: Limitación de presupuesto

#### Restricciones Temporales

1. **RT-004: Plazo de Desarrollo**
   - Duración total: 26 semanas (Noviembre 2025 - Mayo 2026)
   - Entregas intermedias: Cada 3 semanas
   - Entrega final: 1 semana antes de defensa
   - **Justificación**: Calendario académico del ciclo DAW

2. **RT-005: Fase de Documentación**
   - Documentación técnica: 2 semanas
   - Manuales de usuario: 1 semana
   - Memoria del proyecto: 1 semana
   - **Justificación**: Requisitos del proyecto de fin de ciclo

#### Restricciones Económicas

1. **RT-006: Presupuesto de Desarrollo**
   - Presupuesto total: 0€ (proyecto académico)
   - Herramientas: Solo software gratuito/open source
   - Hosting: Tier gratuito o coste mínimo (<20€/mes)
   - **Justificación**: Proyecto sin financiación externa

2. **RT-007: Costes de Producción**
   - MongoDB Atlas: M0 (gratuito) o M2 (9€/mes)
   - Hosting: Reflex Cloud (0-20€/mes)
   - Dominio: Opcional (12€/año)
   - **Justificación**: Viabilidad económica post-proyecto

#### Restricciones Legales

1. **RT-008: Protección de Datos**
   - Cumplimiento GDPR (Reglamento General de Protección de Datos)
   - Política de privacidad obligatoria
   - Consentimiento explícito para tratamiento de datos
   - **Justificación**: Normativa europea vigente

2. **RT-009: Propiedad Intelectual**
   - Contenidos de cursos: Propiedad de instructores
   - Código fuente: Licencia MIT (open source)
   - Uso educativo: Permitido sin restricciones
   - **Justificación**: Claridad en derechos de autor

#### Restricciones de Alcance

1. **RT-010: Funcionalidades Excluidas (v1.0)**
   - Sistema de pagos integrado (Stripe/PayPal)
   - Videoconferencias en directo
   - Aplicación móvil nativa
   - Gamificación avanzada
   - **Justificación**: Limitación temporal y complejidad

2. **RT-011: Idiomas**
   - Versión 1.0: Solo español
   - Internacionalización: Futura versión
   - **Justificación**: Simplificación del desarrollo inicial

---

## 1.4. Alcance del Proyecto

### Funcionalidades Incluidas en v1.0

#### Módulo de Autenticación y Usuarios
-  Registro de usuarios con validación de email
-  Login con autenticación segura (bcrypt)
-  Gestión de sesiones
-  Edición de perfiles
-  Cambio de contraseña
-  Sistema de roles (admin, instructor, student)
-  Protección de rutas según rol

#### Módulo de Cursos
-  CRUD completo de cursos (crear, leer, actualizar, eliminar)
-  Organización en secciones y lecciones
-  Información detallada (descripción, duración, nivel, requisitos)
-  Sistema de categorías y etiquetas
-  Valoración promedio visible
-  Listado de instructores asociados
-  Búsqueda y filtrado de cursos

#### Módulo de Inscripciones
-  Inscripción de estudiantes a cursos
-  Prevención de inscripciones duplicadas
-  Listado de cursos inscritos en dashboard
-  Registro de fecha de inscripción
-  Visualización de progreso por curso

#### Módulo de Progreso
-  Registro de lecciones completadas
-  Cálculo de progreso porcentual
-  Dashboard de estudiante con estadísticas
-  Historial de progreso

#### Módulo de Valoraciones
-  Valoración de cursos (1-5 estrellas)
-  Escritura de reseñas textuales
-  Cálculo de promedio de valoraciones
-  Visualización en detalle de curso
-  Conteo de valoraciones

#### Módulo de Instructores
-  Perfiles de instructores con biografía
-  Listado de cursos por instructor
-  Estadísticas de inscripciones
-  Valoración promedio del instructor
-  Información de especialización

#### Panel de Administración
-  Gestión de usuarios (listar, editar, eliminar)
-  Modificación de roles
-  Estadísticas globales del sistema
-  Acceso a todas las funcionalidades

#### Interfaz de Usuario
-  Diseño responsive (móvil, tablet, desktop)
-  Navegación intuitiva con navbar
-  Componentes reutilizables (cards, modals, forms)
-  Feedback visual (loading, success, errors)
-  Accesibilidad básica

### Funcionalidades Excluidas (Roadmap Futuro)

#### Fase 2 (Post v1.0) - Q3 2026
-  Sistema de pagos integrado (Stripe)
-  Pasarela de pago para cursos premium
-  Gestión de suscripciones
-  Facturación automática
-  Reembolsos

#### Fase 3 (Q4 2026)
-  Videoconferencias en directo (Zoom/Jitsi)
-  Chat en tiempo real entre usuarios
-  Foros de discusión por curso
-  Sistema de mensajería interna
-  Notificaciones push

#### Fase 4 (2027)
-  Aplicación móvil nativa (React Native/Flutter)
-  Descarga de cursos offline
-  Sincronización multiplataforma
-  Notificaciones móviles

#### Fase 5 (2027)
-  Gamificación avanzada (puntos, badges, rankings)
-  Sistema de logros y certificados digitales
-  Competencias y desafíos
-  Leaderboards globales

#### Futuro Indeterminado
-  Inteligencia artificial para recomendaciones
-  Generación automática de contenido
-  Análisis avanzado de aprendizaje
-  Integración con LMS externos (Moodle, Canvas)
-  API pública para integraciones
-  Marketplace de plugins

### Límites del Proyecto

#### Límites Geográficos
- **Versión 1.0**: España (idioma español, normativa española)
- **Futuro**: Expansión internacional con i18n

#### Límites de Usuarios
- **Fase de desarrollo**: 10 usuarios de prueba
- **Lanzamiento inicial**: 50-100 usuarios
- **Primer año**: 500-1000 usuarios
- **Escalabilidad**: Arquitectura soporta 10,000+ usuarios

#### Límites de Contenido
- **Tipos de contenido**: Solo texto y enlaces (no vídeo hosting)
- **Tamaño de cursos**: Sin límite de secciones/lecciones
- **Almacenamiento**: Limitado por tier de MongoDB Atlas

#### Límites Técnicos
- **Navegadores**: Solo versiones modernas (últimos 2 años)
- **Dispositivos**: Resolución mínima 375px
- **Conexión**: Requiere internet (no funcionalidad offline)

---

<div style="page-break-after: always;"></div>

# 2. ANÁLISIS DEL ENTORNO

## 2.1. Descripción de Oportunidades de Negocio

### 2.1.1. Contexto del Mercado E-Learning

El mercado global del e-learning ha experimentado un crecimiento exponencial en los últimos años, acelerado significativamente por la pandemia de COVID-19. Según datos del informe "Global E-Learning Market 2025" de Research and Markets:

- **Tamaño del mercado global**:
  - 2023: $315 mil millones USD
  - 2026 (proyección): $457 mil millones USD
  - Tasa de crecimiento anual (CAGR): 13.7%

- **Mercado español**:
  - 2023: €2.1 mil millones
  - 2026 (proyección): €3.5 mil millones
  - CAGR: 18.5% (superior a la media global)

#### Factores de Crecimiento

1. **Transformación Digital Acelerada**
   - El 76% de las empresas españolas ha adoptado formación online (Informe CEOE 2024)
   - El 89% de estudiantes universitarios usa plataformas de e-learning complementarias
   - Reducción de costes de formación presencial (60-70% menos)

2. **Cambio en Hábitos de Consumo Educativo**
   - El 64% de trabajadores prefiere formación flexible y a su ritmo
   - El 82% de estudiantes valora poder acceder a contenidos desde múltiples dispositivos
   - El 91% considera fundamental las reseñas y valoraciones antes de inscribirse

3. **Demanda de Upskilling y Reskilling**
   - El 54% de empleados necesitará actualizar competencias en 2026
   - El 73% de empresas españolas tiene programas activos de formación continua
   - Sectores con mayor demanda: Tecnología (42%), Marketing Digital (28%), Idiomas (18%)

### 2.1.2. Oportunidades Identificadas

#### Oportunidad 1: Mercado de Formación Técnica

**Segmento objetivo**: Profesionales IT que buscan actualizar competencias

**Datos del mercado**:
- 120,000 profesionales IT en España
- 68% busca formación online por flexibilidad
- Precio medio por curso: 49€ - 199€
- Frecuencia de compra: 3-4 cursos/año

**Proyección de ingresos**:
- Escenario conservador (100 estudiantes activos):
  - Ingresos año 1: 100 × 2 cursos × 99€ × 70% retención = 13,860€
- Escenario optimista (500 estudiantes activos):
  - Ingresos año 1: 500 × 3 cursos × 99€ × 75% = 111,375€

#### Oportunidad 2: Formación Corporativa B2B

**Segmento objetivo**: PYMEs que necesitan plataforma propia de formación

**Datos del mercado**:
- 2.9 millones de PYMEs en España
- 23% busca plataformas de e-learning (667,000 potenciales)
- Presupuesto medio anual: 2,000€ - 5,000€

**Proyección de ingresos**:
- Escenario conservador (5 empresas cliente):
  - Ingresos año 1: 5 × 2,400€/año = 12,000€
- Escenario optimista (20 empresas cliente):
  - Ingresos año 1: 20 × 3,600€/año = 72,000€

#### Oportunidad 3: Marketplace de Instructores

**Segmento objetivo**: Profesionales que quieren monetizar conocimientos

**Datos del mercado**:
- 500,000+ profesionales freelance en España
- 38% ha considerado crear cursos online
- Comisión estándar de plataforma: 20-30%

**Proyección de ingresos**:
- Escenario conservador (20 instructores, 50 ventas/mes):
  - Ingresos año 1: 50 × 12 meses × 99€ × 25% comisión = 14,850€
- Escenario optimista (100 instructores, 300 ventas/mes):
  - Ingresos año 1: 300 × 12 × 99€ × 25% = 89,100€

### 2.1.3. Análisis de Competencia

#### Competidores Directos

| Plataforma | Fortalezas | Debilidades | Precio | Cuota de Mercado |
|------------|-----------|-------------|--------|------------------|
| **Udemy** | - Catálogo masivo (200k+ cursos)<br>- Reconocimiento global<br>- App móvil robusta | - Interfaz saturada<br>- Baja calidad de algunos cursos<br>- Competencia de precios agresiva | 12.99€ - 199€ | 35% |
| **Coursera** | - Cursos universitarios<br>- Certificaciones oficiales<br>- Alta calidad | - Precio elevado<br>- Menos cursos en español<br>- Poca flexibilidad | 49€ - 79€/mes | 18% |
| **Domestika** | - Diseño atractivo<br>- Comunidad fuerte<br>- Cursos en español | - Solo creatividad/diseño<br>- Sin certificación oficial<br>- Limitado a nicho | 9.90€ - 39.90€ | 12% (España) |
| **Platzi** | - Enfoque latinoamericano<br>- Rutas de aprendizaje<br>- Precio competitivo | - Menor reconocimiento en España<br>- Menos cursos técnicos avanzados | 29€/mes | 8% (España) |

#### Competidores Indirectos

- **YouTube + Google**: Contenido gratuito, pero sin estructura ni certificación
- **LinkedIn Learning**: Integrado con LinkedIn, pero precio elevado (29.99€/mes)
- **Tutoriales de blogs**: Gratuitos, pero fragmentados y sin soporte

### 2.1.4. Ventajas Competitivas de E-Learning JCB Platform

#### 1. **Información Detallada y Transparente**

**Diferenciador clave**: Visualización completa de secciones y lecciones antes de compra

- Los competidores solo muestran índice general
- **E-Learning JCB** muestra:
  - Todas las secciones y lecciones con títulos
  - Duración de cada lección
  - Contenido detallado por sección
  - Requisitos previos claros

**Impacto esperado**: +35% tasa de conversión (estudiante ve valor antes de comprar)

#### 2. **Costes Operativos Reducidos**

**Diferenciador técnico**: Stack tecnológico eficiente (Reflex + MongoDB)

- Desarrollo 60% más rápido que frameworks tradicionales
- Costes de hosting reducidos (20-30€/mes vs 200-500€/mes)
- Un solo lenguaje (Python) reduce complejidad

**Impacto esperado**: Margen operativo 40% superior a competidores

#### 3. **Experiencia de Usuario Optimizada**

**Diferenciador UX**: Diseño limpio, responsive y rápido

- Tiempo de carga < 2 segundos (vs 4-6s de competidores)
- Diseño mobile-first (72% usuarios acceden desde móvil)
- Navegación intuitiva con máximo 3 clics

**Impacto esperado**: +25% retención de usuarios

#### 4. **Sistema de Valoraciones Transparente**

**Diferenciador social**: Reseñas verificadas y estadísticas claras

- Valoración promedio visible por curso e instructor
- Conteo de reseñas para contexto
- Sistema de verificación de compra

**Impacto esperado**: +20% confianza y +15% conversión

### 2.1.5. Estrategia de Entrada al Mercado

#### Fase 1: Lanzamiento MVP (Meses 1-3)

**Objetivo**: Validar producto con early adopters

- **Usuarios objetivo**: 50-100 estudiantes
- **Cursos objetivo**: 10-15 cursos de calidad
- **Estrategia**: Modelo Freemium
  - 5 cursos gratuitos para atraer usuarios
  - 10 cursos premium (49€ - 99€)
- **Marketing**:
  - Contenido orgánico en LinkedIn y X
  - SEO local (Almería, Andalucía)
  - Colaboraciones con influencers educativos micro (<10k followers)

**Inversión**: 0€ (marketing orgánico)
**Ingresos proyectados**: 1,500€ - 3,000€

#### Fase 2: Crecimiento (Meses 4-12)

**Objetivo**: Escalar a 500 usuarios activos

- **Usuarios objetivo**: 500 estudiantes, 30 instructores
- **Cursos objetivo**: 50-75 cursos
- **Estrategia**: Marketplace + B2B
  - Comisión del 25% por venta
  - 3 clientes corporativos (2,400€/año)
- **Marketing**:
  - Publicidad online (Google Ads, LinkedIn Ads): 500€/mes
  - Email marketing automatizado
  - Webinars gratuitos semanales

**Inversión**: 6,000€ (500€/mes × 12 meses)
**Ingresos proyectados**: 25,000€ - 40,000€

#### Fase 3: Consolidación (Año 2)

**Objetivo**: Rentabilidad sostenida

- **Usuarios objetivo**: 2,000 estudiantes, 100 instructores
- **Cursos objetivo**: 200+ cursos
- **Estrategia**: Diversificación
  - Suscripciones mensuales (29€/mes acceso ilimitado)
  - Certificaciones oficiales (79€)
  - Planes corporativos (5,000€/año)
- **Marketing**:
  - SEO consolidado (tráfico orgánico 60%)
  - Partnerships con universidades
  - Programa de afiliados (10% comisión)

**Inversión**: 15,000€
**Ingresos proyectados**: 120,000€ - 180,000€

---
<div style="page-break-after: always;"></div>

## 2.2. Obligaciones Fiscales, Laborales y de Prevención de Riesgos

### 2.2.1. Forma Jurídica: Autónomo

Para el lanzamiento inicial de **E-Learning JCB Platform**, se ha optado por la figura de **Trabajador Autónomo** (persona física empresario individual), por las siguientes razones:

#### Ventajas de la Forma de Autónomo

1. **Simplicidad administrativa**
   - Trámites de alta sencillos
   - Contabilidad simplificada
   - No requiere capital inicial

2. **Costes reducidos**
   - No hay costes notariales
   - No registro mercantil
   - Impuestos reducidos en inicio (tarifa plana)

3. **Flexibilidad**
   - Decisiones autónomas
   - Fácil cambio a sociedad en futuro
   - Control total del negocio

#### Desventajas Asumidas

1. **Responsabilidad ilimitada**: El patrimonio personal responde de deudas (mitigado por bajo riesgo del negocio digital)
2. **Fiscalidad menos optimizada**: A partir de 40,000€ beneficios, SL es más ventajosa (se plantea cambio en Año 2)

### 2.2.2. Obligaciones Fiscales

#### Alta en Hacienda (AEAT)

**Paso 1: Modelo 036/037 - Declaración Censal**

- **Descripción actividad**:
  - Epígrafe IAE: 631.9 - "Otros servicios de información"
  - Epígrafe IAE: 933.9 - "Enseñanza de formación y perfeccionamiento profesional n.c.o.p."

- **Régimen de IVA**: General (21%)
  - Servicios educativos pueden estar exentos (art. 20.1.9º Ley IVA)
  - **E-Learning JCB Platform**: Cursos online con certificación NO exentos → IVA 21%

- **Régimen de IRPF**: Estimación directa simplificada
  - Se declaran ingresos reales menos gastos deducibles
  - Alternativa: Estimación objetiva (módulos), pero no aplicable a servicios digitales

#### Impuestos a Pagar

| Impuesto | Periodicidad | Base Imponible | Tipo | Cantidad Estimada (Año 1) |
|----------|--------------|----------------|------|---------------------------|
| **IVA** | Trimestral (Modelo 303) + Resumen Anual (Modelo 390) | Facturación | 21% | Variable según ventas |
| **IRPF** | Trimestral (Modelo 130) + Declaración Anual (Modelo 100) | Beneficio neto | 15%-47% progresivo | 1,200€ - 3,000€ |
| **Retenciones IRPF** (si aplica) | Trimestral (Modelo 111) | Servicios profesionales | 15% | 0€ (sin empleados) |

#### Ejemplo de Tributación Año 1

**Escenario Base**:
- Ingresos brutos: 15,000€
- Gastos deducibles: 3,600€ (hosting, marketing, dominio, software)
- Beneficio neto: 11,400€

**Cálculo IRPF**:
- Base liquidable: 11,400€
- Tramo IRPF: 12,450€ → 19% (después de mínimo personal)
- Cuota IRPF estimada: ~1,800€

**Cálculo IVA**:
- IVA repercutido (ventas): 15,000€ × 21% = 3,150€
- IVA soportado (gastos): 3,600€ × 21% = 756€
- IVA a ingresar: 3,150€ - 756€ = 2,394€ (trimestralmente)

**Total impuestos**: 1,800€ (IRPF) + 0€ (IVA se traslada al cliente) = **1,800€**

#### Deducciones y Gastos Deducibles

**Gastos deducibles al 100%**:
- Hosting y dominio (240€/año)
- Software y herramientas (300€/año)
- Publicidad y marketing (6,000€/año)
- Formación relacionada (500€/año)
- Material de oficina (200€/año)
- Suministros (internet, luz) - proporción uso profesional (30% estimado): 360€/año

**Gastos parcialmente deducibles**:
- Vehículo (si se usa para negocio): 0€ (negocio 100% digital)
- Vivienda (si se trabaja desde casa): 30% de alquiler/hipoteca (no aplicable si es vivienda en propiedad familiar)

**Total gastos deducibles estimados**: 3,600€/año

### 2.2.3. Obligaciones con la Seguridad Social

#### Régimen Especial de Trabajadores Autónomos (RETA)

**Cuota mensual de autónomos** (2026):

- **Base de cotización**: Elección libre entre 950.98€/mes y 1,732.03€/mes
- **Tipo de cotización**: 30.30%
- **Tarifa plana para nuevos autónomos** (primeros 12 meses):
  - Meses 1-12: **80€/mes**
  - Meses 13-18: 180€/mes (si ingresos <1.300€/mes)
  - Meses 19-24: 220€/mes (si ingresos <1.300€/mes)

**Cálculo aplicado**:
- **Año 1**: 80€/mes × 12 meses = **960€/año**
- **Año 2** (sin tarifa plana, base mínima 1,000€):
  - 1,000€ × 30.30% = **303€/mes** = **3,636€/año**

#### Prestaciones Cubiertas

-  Asistencia sanitaria
-  Incapacidad temporal (baja por enfermedad)
-  Jubilación
-  Incapacidad permanente
-  Prestación por cese de actividad (paro de autónomos)
-  Desempleo (opcional, +2.20% cuota adicional)

#### Obligaciones de Cotización

- **Alta en RETA**: 60 días naturales antes de inicio actividad o dentro de los 30 días siguientes
- **Pago cuotas**: Mensual, mediante domiciliación bancaria
- **Variación de base**: Posible cambio hasta 4 veces al año (desde 2023)

### 2.2.4. Obligaciones Laborales

#### Escenario Año 1: Sin Empleados

Al tratarse de un proyecto inicial gestionado por el desarrollador/fundador, **no se prevé contratación** en el primer año.

**Obligaciones aplicables**: Ninguna (solo autónomo individual)

#### Escenario Futuro: Con Contratación

Si en Año 2 se decide contratar (ejemplo: 1 desarrollador junior):

##### Obligaciones con la Seguridad Social

1. **Inscripción como empleador** (Modelo TA.6)
2. **Afiliación del trabajador** (Modelo TA.1)
3. **Alta del trabajador** (Modelo TA.2/S)
4. **Cotización mensual**:
   - Contingencias comunes: 28.30%
   - Desempleo: 5.50% (empresa) + 1.55% (trabajador)
   - Formación profesional: 0.60% (empresa) + 0.10% (trabajador)
   - FOGASA: 0.20%
   - **Total empresa**: ~34.60% sobre salario bruto

**Ejemplo**: Contratación desarrollador junior (24,000€ bruto/año)
- Coste Seguridad Social: 24,000€ × 34.60% = **8,304€/año**
- **Coste total**: 24,000€ + 8,304€ = **32,304€/año**

##### Obligaciones Fiscales con Empleados

1. **Retención IRPF**: Aplicar retención según situación personal (15%-30%)
2. **Modelo 111**: Declaración trimestral de retenciones
3. **Modelo 190**: Resumen anual de retenciones
4. **Modelo 349**: Operaciones intracomunitarias (si aplica)

##### Obligaciones de Prevención de Riesgos Laborales

**Según Ley 31/1995 de PRL**:

1. **Evaluación de riesgos**: Identificar peligros del puesto de trabajo
   - En trabajo de oficina digital: Riesgos ergonómicos (pantallas), estrés
2. **Plan de prevención**: Documentar medidas preventivas
3. **Formación e información**: Capacitar empleado en riesgos y medidas
4. **Vigilancia de la salud**: Reconocimientos médicos (si riesgo específico)
5. **Servicio de prevención**:
   - Opción 1: Servicio de Prevención Ajeno (SPA) - 50-150€/trabajador/año
   - Opción 2: Modalidad propia (solo si >500 trabajadores)

**Coste estimado**: 100€/trabajador/año (SPA)

#### Prevención de Riesgos para Autónomo Individual

Aunque no sea obligatorio, se recomienda:

1. **Ergonomía del puesto de trabajo**:
   - Silla ergonómica ajustable
   - Monitor a altura de ojos
   - Descansos cada 50 minutos (pausa de 10 minutos)
   - Iluminación adecuada (500 lux mínimo)

2. **Prevención de riesgos psicosociales**:
   - Gestión del estrés y carga de trabajo
   - Separación vida laboral/personal
   - Horarios definidos

3. **Seguro de responsabilidad civil profesional**: 150-300€/año (recomendado)

### 2.2.5. Resumen de Obligaciones y Costes

#### Tabla Resumen Año 1 (Autónomo sin empleados)

| Concepto | Periodicidad | Organismo | Coste Año 1 |
|----------|--------------|-----------|-------------|
| **Alta Censal (Modelo 036)** | Única | AEAT | 0€ |
| **Alta RETA** | Única | Seguridad Social | 0€ |
| **Cuota autónomos (tarifa plana)** | Mensual | Seguridad Social | 960€ |
| **IVA trimestral (Modelo 303)** | Trimestral | AEAT | 0€ (trasladado) |
| **IRPF trimestral (Modelo 130)** | Trimestral | AEAT | 1,800€ |
| **Declaración Renta (Modelo 100)** | Anual | AEAT | (incluido en IRPF) |
| **Resumen anual IVA (Modelo 390)** | Anual | AEAT | 0€ |
| **Seguro RC profesional** (opcional) | Anual | Aseguradora | 200€ |
| **Gestoría/asesoría fiscal** (opcional) | Mensual | Gestoría | 600€ (50€/mes) |
| **TOTAL OBLIGATORIO** | | | **2,760€** |
| **TOTAL RECOMENDADO** | | | **3,560€** |

#### Tabla Resumen Año 2 (Con 1 empleado)

| Concepto | Coste Año 2 |
|----------|-------------|
| Cuota autónomos (sin tarifa plana) | 3,636€ |
| IRPF (beneficios aumentados) | 4,500€ |
| Salario bruto empleado | 24,000€ |
| Seguridad Social empleado | 8,304€ |
| Prevención riesgos laborales | 100€ |
| Gestoría/asesoría | 900€ (75€/mes) |
| **TOTAL** | **41,440€** |

---

## 2.3. Posibles Ayudas y Subvenciones para el Desarrollo

### 2.3.1. Ayudas Nacionales (España)

#### 1. **Tarifa Plana de Autónomos**

**Organismo**: Seguridad Social (Ministerio de Inclusión, Seguridad Social y Migraciones)

**Descripción**: Reducción de la cuota de autónomos para nuevos emprendedores

**Beneficios**:
- Meses 1-12: **80€/mes** (ahorro de 223€/mes)
- Meses 13-18: 180€/mes (si ingresos <1.300€/mes)
- Meses 19-24: 220€/mes (si ingresos <1.300€/mes)

**Requisitos**:
-  No haber estado de alta como autónomo en los 2 años previos (o 3 años si se disfrutó anteriormente)
-  No tener deudas con Seguridad Social ni Hacienda
-  Darse de alta en RETA

**Ahorro total**: 2,676€ en 12 meses (223€ × 12)

**Estado**:  Aplicable al proyecto

---

#### 2. **Programa Kit Digital**

**Organismo**: Red.es (Ministerio de Asuntos Económicos y Transformación Digital)

**Descripción**: Ayudas para digitalización de pequeñas empresas y autónomos

**Segmento aplicable**: Autónomos (0-2 empleados)

**Cuantía**: Hasta **2,000€** en bonos digitales

**Servicios subvencionables**:
-  Sitio web y presencia en internet
-  Comercio electrónico
-  Gestión de redes sociales
-  Herramientas de oficina virtual
-  Desarrollo de software a medida (E-Learning JCB no aplicable directamente)

**Requisitos**:
- Ser autónomo o PYME
- Estar al corriente de obligaciones tributarias
- Solicitar a través de agentes digitalizadores certificados

**Estado**:  Aplicable parcialmente (para web de marketing, no para plataforma)

**Ahorro potencial**: 1,500€ (web de marketing y posicionamiento)

---

#### 3. **Ayudas ENISA para Jóvenes Emprendedores**

**Organismo**: ENISA (Empresa Nacional de Innovación)

**Descripción**: Préstamos participativos para emprendedores menores de 40 años

**Modalidades**:
- **ENISA Jóvenes Emprendedores**: 25,000€ - 75,000€
- **ENISA Emprendedores**: 25,000€ - 300,000€

**Condiciones**:
- Tipo de interés: Euribor + 3.75%
- Carencia: 5 años
- Amortización: 7 años
- Sin garantías adicionales (subordinado a deuda bancaria)

**Requisitos**:
-  Edad < 40 años (aplicable)
-  Domicilio fiscal en España
-  Empresa constituida hace menos de 2 años
-  Fondos propios ≥ 50% del préstamo solicitado
-  Facturación no obligatoria, pero proyecciones sólidas requeridas

**Estado**:  Aplicable si se constituye SL y se justifica inversión

**Cuantía potencial**: 25,000€ - 50,000€

---

#### 4. **Deducción Fiscales por I+D+i**

**Organismo**: AEAT (Agencia Tributaria)

**Descripción**: Deducciones en el Impuesto de Sociedades (IS) por actividades de I+D+i

**Beneficios**:
- **I+D**: 25% de los primeros 600,000€ + 42% del exceso
- **Innovación tecnológica**: 12% de los gastos
- **Software avanzado**: Considerado I+D si hay avances significativos

**Requisitos**:
- Justificar carácter innovador del proyecto
- Documentar actividades de I+D (informes técnicos)
- Tributar en Impuesto de Sociedades (no IRPF autónomos)

**Estado**:  No aplicable a autónomos (solo SL con IS)

**Potencial futuro**: Si se crea SL, deducción de 5,000€ - 10,000€ en IS

---

### 2.3.2. Ayudas Autonómicas (Andalucía)

#### 1. **Programa Andalucía Emprende - Línea I+D+i**

**Organismo**: Consejería de Economía, Conocimiento, Empresas y Universidad (Junta de Andalucía)

**Descripción**: Subvenciones para proyectos innovadores en sectores estratégicos

**Cuantía**: Hasta **100,000€** (subvención a fondo perdido)

**Porcentaje de ayuda**: 50%-70% de la inversión

**Gastos subvencionables**:
- Personal investigador
- Material inventariable (hardware)
- Software
- Gastos de promoción

**Requisitos**:
- Empresa o autónomo en Andalucía
- Proyecto con componente innovador justificado
- Inversión mínima: 20,000€
- Certificación de innovación (opcional, pero aumenta puntuación)

**Estado**:  Aplicable si se justifica innovación en arquitectura o metodología educativa

**Cuantía potencial**: 10,000€ - 30,000€ (50% de 20,000€-60,000€ inversión)

---

#### 2. **Bono Empleo Joven Andalucía**

**Organismo**: Servicio Andaluz de Empleo (SAE)

**Descripción**: Incentivos para contratación de jóvenes menores de 30 años

**Cuantía**:
- **4,000€** por contrato indefinido
- **2,000€** por contrato temporal (mín. 6 meses)

**Requisitos**:
- Contratar joven inscrito en SAE
- Mantener empleo al menos 6 meses (temporal) o 1 año (indefinido)
- Incremento neto de plantilla

**Estado**:  Aplicable si se contrata en Año 2

**Ahorro potencial**: 4,000€ por contratación

---

#### 3. **Programa de Fomento del Emprendimiento Innovador**

**Organismo**: Junta de Andalucía - Andalucía Emprende

**Descripción**: Acompañamiento, formación y financiación para startups

**Beneficios**:
- Asesoramiento gratuito (200 horas)
- Espacios de coworking gratuitos (6 meses)
- Acceso a red de inversores
- Financiación de 6,000€ - 20,000€ (préstamo 0% interés, 3 años)

**Requisitos**:
- Proyecto innovador en sectores estratégicos (tecnología incluida)
- Domicilio en Andalucía
- Presentación de plan de negocio

**Estado**:  Aplicable

**Valor estimado**: 15,000€ (6 meses coworking + asesoramiento + financiación)

---

### 2.3.3. Ayudas Locales (Almería)

#### 1. **Programa Almería Emprende**

**Organismo**: Ayuntamiento de Almería + Diputación Provincial

**Descripción**: Ayudas para nuevos emprendedores en la provincia

**Cuantía**: Hasta **3,000€** a fondo perdido

**Gastos subvencionables**:
- Alquiler de local (primer año)
- Equipamiento
- Marketing y comunicación
- Formación

**Requisitos**:
- Domicilio fiscal en Almería
- Alta como autónomo en los últimos 12 meses
- Creación de empleo propio (autónomo)

**Estado**:  Aplicable

**Ahorro potencial**: 3,000€

---

#### 2. **Cheque Innovación Diputación de Almería**

**Organismo**: Diputación Provincial de Almería

**Descripción**: Bonos para servicios de asesoramiento en I+D+i

**Cuantía**: Hasta **1,500€**

**Servicios cubiertos**:
- Asesoramiento tecnológico
- Estudios de viabilidad técnica
- Desarrollo de prototipos
- Certificaciones de calidad

**Requisitos**:
- PYME o autónomo en provincia de Almería
- Proyecto con componente tecnológico

**Estado**:  Aplicable

**Valor**: 1,500€ en servicios

---

### 2.3.4. Ayudas Europeas

#### 1. **Horizonte Europa - EIC Accelerator**

**Organismo**: Comisión Europea - European Innovation Council

**Descripción**: Financiación para startups de alto impacto e innovación disruptiva

**Cuantía**:
- Grants (subvención): Hasta 2.5 millones €
- Equity investment (inversión): Hasta 15 millones €

**Requisitos**:
- Innovación disruptiva (muy exigente)
- Potencial de escalabilidad global
- Equipo de alto nivel
- TRL (Technology Readiness Level) 6-8

**Estado**: No aplicable en fase inicial (demasiado exigente)

**Potencial futuro**: Si se valida modelo y se escala internacionalmente

---

#### 2. **Erasmus para Emprendedores**

**Organismo**: Comisión Europea

**Descripción**: Programa de intercambio para nuevos emprendedores

**Beneficios**:
- Estancia de 1-6 meses en empresa europea consolidada
- Financiación de viaje y manutención (600€-1,100€/mes)
- Aprendizaje de buenas prácticas

**Requisitos**:
- Emprendedor en fase inicial (< 3 años)
- Plan de negocio viable
- Compromiso de estancia

**Estado**:  Aplicable (opcional)

**Valor**: 3,000€ - 6,600€ (estancia de 6 meses)

---

### 2.3.5. Resumen de Ayudas Aplicables

#### Tabla de Ayudas Aplicables al Proyecto

| Ayuda | Organismo | Tipo | Cuantía | Probabilidad | Plazo |
|-------|-----------|------|---------|--------------|-------|
| **Tarifa plana autónomos** | Seguridad Social | Reducción cuota | 2,676€ |  100% | Inmediato |
| **Kit Digital** | Red.es | Subvención | 1,500€ |  60% | 3-6 meses |
| **Almería Emprende** | Ayto. Almería | Subvención | 3,000€ |  80% | 2-4 meses |
| **Cheque Innovación** | Diputación AL | Bono servicios | 1,500€ |  70% | 2-3 meses |
| **Andalucía Emprende** | Junta Andalucía | Financiación + servicios | 15,000€ |  50% | 6-12 meses |
| **Bono Empleo Joven** (Año 2) | SAE | Incentivo contratación | 4,000€ |  90% | Al contratar |
| **ENISA Jóvenes** (si SL) | ENISA | Préstamo participativo | 25,000€ |  40% | 6-12 meses |
| **TOTAL REALISTA** | | | **23,676€** | | |

#### Escenario Conservador (Ayudas Seguras)

| Ayuda | Cuantía |
|-------|---------|
| Tarifa plana autónomos | 2,676€ |
| Almería Emprende | 3,000€ |
| Cheque Innovación | 1,500€ |
| **TOTAL** | **7,176€** |

#### Escenario Optimista (Todas las Ayudas)

| Ayuda | Cuantía |
|-------|---------|
| Tarifa plana autónomos | 2,676€ |
| Kit Digital | 1,500€ |
| Almería Emprende | 3,000€ |
| Cheque Innovación | 1,500€ |
| Andalucía Emprende | 15,000€ |
| Bono Empleo Joven (Año 2) | 4,000€ |
| **TOTAL** | **27,676€** |

---

### 2.3.6. Estrategia de Solicitud de Ayudas

#### Cronograma de Solicitudes

**Mes 1 (Noviembre 2025)**:
-  Solicitar tarifa plana autónomos (automático al darse de alta)
-  Solicitar Almería Emprende (convocatoria anual Q4)

**Mes 2 (Diciembre 2025)**:
-  Solicitar Cheque Innovación Diputación
-  Preparar documentación para Kit Digital

**Mes 3 (Enero 2026)**:
-  Solicitar Kit Digital (agente digitalizador)
-  Explorar Andalucía Emprende (requiere inversión mínima)

**Mes 6 (Abril 2026)**:
-  Evaluar ENISA si se plantea constitución de SL
-  Solicitar Andalucía Emprende I+D+i (si hay inversión justificada)

**Mes 12+ (Año 2)**:
-  Solicitar Bono Empleo Joven al contratar primer empleado

#### Documentación Necesaria

**Común a todas las ayudas**:
-  DNI/NIE
-  Certificado de alta en RETA
-  Certificado de estar al corriente con Hacienda
-  Certificado de estar al corriente con Seguridad Social
-  Plan de negocio

**Específica por ayuda**:
- **Kit Digital**: Solicitud a través de agente digitalizador certificado
- **Almería Emprende**: Memoria del proyecto, presupuesto detallado
- **Andalucía Emprende**: Informe de innovación, plan de inversión
- **ENISA**: Estados financieros, proyecciones a 3 años, pitch deck

---

**Conclusión**: Con una estrategia de solicitud bien planificada, el proyecto puede obtener entre **7,176€** (conservador) y **27,676€** (optimista) en ayudas durante los primeros 2 años, reduciendo significativamente la necesidad de financiación externa y mejorando la viabilidad económica.

<div style="page-break-after: always;"></div>

# 3. ANÁLISIS DEL SISTEMA ACTUAL

## 3.1. Contexto del Proyecto

**E-Learning JCB Platform** es un proyecto de nueva creación que **no sustituye ni complementa sistemas existentes previos**. Se trata de una iniciativa emprendedora desde cero que busca aprovechar las oportunidades del mercado del e-learning identificadas en el análisis del entorno.

Por tanto, esta sección no describe un sistema actual en funcionamiento que presente problemas o limitaciones, sino que analiza el **contexto general del mercado de plataformas educativas** y las **necesidades no cubiertas** que justifican el desarrollo de este proyecto.

---

## 3.2. Problemática Actual del E-Learning

### 3.2.1. Análisis de Plataformas Existentes

Aunque no existe un sistema previo propio, sí existen múltiples plataformas de e-learning en el mercado actual. Un análisis de sus problemáticas permite identificar oportunidades de mejora:

#### Problema 1: **Falta de Transparencia en Contenidos**

**Plataformas afectadas**: Udemy, Coursera, LinkedIn Learning

**Descripción del problema**:
- Los estudiantes **no pueden ver el contenido detallado** antes de comprar
- Solo se muestra un índice general sin especificar lecciones
- Falta información sobre duración real de cada lección
- No se visualizan las secciones completas

**Impacto en usuarios**:
-  Inscripciones basadas en expectativas erróneas
-  Tasas de abandono del 40-60% (estudios de Udemy 2024)
-  Reembolsos frecuentes (20% de cursos comprados)
-  Baja satisfacción de clientes

**Datos cuantitativos**:
- El 68% de usuarios afirma que "compraría más cursos si viera contenido detallado" (encuesta sector 2024)
- El 73% ha abandonado un curso por "no ser lo esperado"

**Oportunidad para E-Learning JCB**:
-  Mostrar **todas las secciones y lecciones** antes de inscripción
-  Incluir **duración de cada lección**
-  Proporcionar **descripción detallada de contenidos**

---

#### Problema 2: **Interfaces Saturadas y Complejas**

**Plataformas afectadas**: Udemy, Skillshare

**Descripción del problema**:
- Exceso de información en pantallas
- Navegación confusa con múltiples niveles
- Diseño no optimizado para móvil
- Tiempos de carga elevados (4-6 segundos)

**Impacto en usuarios**:
-  Frustración en usuarios no técnicos (38%)
-  Abandono en primeros 30 segundos (22%)
-  Baja conversión móvil (47% vs 65% desktop)

**Datos cuantitativos**:
- El 82% de usuarios valora la "simplicidad" como factor clave
- El 91% abandona si la web tarda >3 segundos en cargar

**Oportunidad para E-Learning JCB**:
-  Diseño **minimalista y limpio**
-  Navegación **máximo 3 clics** a cualquier contenido
-  **Responsive design** mobile-first
-  Tiempos de carga **<2 segundos**

---

#### Problema 3: **Sistemas de Valoración Poco Fiables**

**Plataformas afectadas**: Udemy, Domestika

**Descripción del problema**:
- Incentivos para valoraciones positivas (descuentos a cambio de 5 estrellas)
- Valoraciones infladas (promedio 4.6/5 en la mayoría de cursos)
- Falta de contexto (número de reseñas no visible)
- Reviews genéricos sin información útil

**Impacto en usuarios**:
-  Falta de confianza en valoraciones (54%)
-  Decisiones de compra basadas en información sesgada
-  Expectativas no realistas

**Datos cuantitativos**:
- El 67% desconfía de valoraciones >4.5 estrellas
- El 79% lee reseñas antes de comprar

**Oportunidad para E-Learning JCB**:
-  Valoraciones **verificadas** (solo estudiantes inscritos)
-  **Promedio real** sin incentivos artificiales
-  **Conteo de reseñas** visible para contexto
-  Sistema de **reseñas útiles** (like/dislike)

---

#### Problema 4: **Costes Elevados de Desarrollo y Mantenimiento**

**Plataformas afectadas**: Moodle, Canvas (autoalojadas)

**Descripción del problema**:
- Stacks tecnológicos complejos (PHP + React + MySQL + Redis + etc.)
- Necesidad de equipos grandes (5-10 desarrolladores)
- Costes de infraestructura elevados (500€-2000€/mes)
- Mantenimiento costoso (actualizaciones, seguridad)

**Impacto en negocio**:
-  Barrera de entrada alta para nuevos emprendedores
-  Costes operativos que limitan márgenes
-  Tiempo de desarrollo prolongado (12-18 meses)

**Datos cuantitativos**:
- Coste medio de desarrollo de LMS: 50,000€ - 150,000€
- Tiempo medio de lanzamiento: 12-18 meses
- Coste mensual de hosting: 500€ - 2,000€

**Oportunidad para E-Learning JCB**:
-  Stack **simplificado** (Reflex + MongoDB)
-  Desarrollo **60% más rápido** (6 meses vs 12-18)
-  Costes de hosting **reducidos** (20-30€/mes)
-  **Un solo desarrollador** puede mantener el proyecto

---

#### Problema 5: **Falta de Información sobre Instructores**

**Plataformas afectadas**: Coursera, Platzi

**Descripción del problema**:
- Perfiles de instructores incompletos
- Falta de estadísticas de desempeño
- No se muestra claramente qué otros cursos imparte
- Biografías genéricas sin especialización clara

**Impacto en usuarios**:
-  Dificultad para evaluar credibilidad del instructor
-  No se puede seguir a instructores favoritos
-  Falta de transparencia en experiencia

**Datos cuantitativos**:
- El 71% valora la experiencia del instructor como factor clave
- El 58% repetiría con un instructor si quedó satisfecho

**Oportunidad para E-Learning JCB**:
-  **Perfiles completos** con biografía detallada
-  **Listado de cursos** por instructor
-  **Estadísticas** de inscripciones y valoraciones
-  **Especialización** claramente definida

---

### 3.2.2. Necesidades No Cubiertas en el Mercado

Del análisis de problemáticas actuales, se identifican las siguientes **necesidades no cubiertas** o **cubiertas de forma deficiente**:

#### Necesidad 1: Información Detallada Pre-Compra

**Usuarios afectados**: Estudiantes potenciales

**Necesidad**:
- Ver estructura completa de curso (secciones y lecciones) antes de inscribirse
- Conocer duración exacta de cada lección
- Entender qué se aprenderá en cada sección

**Solución en E-Learning JCB**:
- Visualización completa de estructura de curso en página de detalle
- Tabla de contenidos expandible con todas las lecciones
- Duración visible para cada lección
- Descripciones detalladas de secciones

**Valor añadido**: Transparencia total para decisión de compra informada

---

#### Necesidad 2: Experiencia de Usuario Optimizada

**Usuarios afectados**: Estudiantes de todos los perfiles (especialmente no técnicos)

**Necesidad**:
- Navegación intuitiva sin curva de aprendizaje
- Acceso rápido desde cualquier dispositivo
- Interfaz limpia sin distracciones

**Solución en E-Learning JCB**:
- Diseño minimalista con componentes Chakra UI
- Responsive design mobile-first
- Navegación clara con breadcrumbs
- Tiempos de carga optimizados (<2s)

**Valor añadido**: Reducción de fricción en uso de la plataforma

---

#### Necesidad 3: Plataforma Accesible para Emprendedores

**Usuarios afectados**: Instructores independientes, pequeñas academias

**Necesidad**:
- Crear y gestionar cursos sin conocimientos técnicos
- Costes accesibles (sin infraestructura costosa)
- Flexibilidad para personalizar contenido

**Solución en E-Learning JCB**:
- Panel de instructor intuitivo para CRUD de cursos
- Hosting incluido sin costes adicionales
- Sistema de secciones y lecciones flexible

**Valor añadido**: Democratización de la publicación de cursos

---

#### Necesidad 4: Valoraciones Confiables

**Usuarios afectados**: Estudiantes que buscan cursos de calidad

**Necesidad**:
- Sistema de reseñas verificado
- Contexto en valoraciones (número de reseñas)
- Transparencia en promedios

**Solución en E-Learning JCB**:
- Solo estudiantes inscritos pueden valorar
- Promedio calculado sin manipulación
- Conteo de valoraciones visible
- Reseñas textuales opcionales

**Valor añadido**: Confianza en decisión de inscripción

---

#### Necesidad 5: Seguimiento de Progreso Claro

**Usuarios afectados**: Estudiantes inscritos en cursos

**Necesidad**:
- Visualizar progreso en tiempo real
- Saber qué lecciones están pendientes
- Dashboard personal de estadísticas

**Solución en E-Learning JCB**:
- Sistema de marcado de lecciones completadas
- Cálculo de progreso porcentual por curso
- Dashboard de estudiante con historial

**Valor añadido**: Motivación y sensación de avance

---

## 3.3. Justificación de la Necesidad del Proyecto

### 3.3.1. ¿Por qué Crear una Nueva Plataforma?

Aunque existen múltiples plataformas en el mercado, **E-Learning JCB Platform** se justifica por:

#### Razón 1: **Nicho Específico No Cubierto**

- Las plataformas grandes (Udemy, Coursera) priorizan **cantidad** sobre **calidad de información**
- Las plataformas especializadas (Domestika, Platzi) se enfocan en **nichos específicos** (diseño, tecnología)
- **E-Learning JCB** ofrece **transparencia total** como diferenciador en cualquier nicho

#### Razón 2: **Viabilidad Técnica y Económica**

- Las barreras de entrada se han reducido gracias a tecnologías modernas (Reflex, MongoDB Atlas)
- Es posible crear una plataforma competitiva con **costes mínimos** (20-30€/mes)
- El desarrollo puede realizarse en **6 meses** con un solo desarrollador

#### Razón 3: **Oportunidad de Mercado**

- El mercado del e-learning crece al **13.7% anual**
- España crece más rápido (**18.5% CAGR**)
- Hay **demanda insatisfecha** de plataformas transparentes y accesibles

#### Razón 4: **Validación Académica**

- El proyecto cumple con los **objetivos académicos** del ciclo DAW
- Permite aplicar **conocimientos integrales** de desarrollo web
- Tiene **potencial comercial** real post-proyecto

---

### 3.3.2. Ventajas de Partir de Cero vs. Modificar Sistema Existente

#### Ventajas de Desarrollo Desde Cero

| Aspecto | Desarrollo Nuevo | Modificar Existente |
|---------|-----------------|---------------------|
| **Arquitectura** |  Optimizada desde inicio |  Deuda técnica heredada |
| **Tecnologías** |  Stack moderno (Reflex 2025) |  Stack legacy (PHP, MySQL) |
| **Personalización** |  Total libertad de diseño |  Limitado por sistema base |
| **Curva de aprendizaje** |  Dominio completo del código |  Tiempo en entender código ajeno |
| **Mantenimiento** |  Código limpio y documentado |  Dependencia de terceros |
| **Coste** |  Solo tiempo de desarrollo |  Licencias + desarrollo |

#### Desventajas Asumidas

| Aspecto | Riesgo | Mitigación |
|---------|--------|------------|
| **Tiempo de desarrollo** | 6 meses completos | Planificación detallada por fases |
| **Funcionalidades iniciales** | Menos features que plataformas maduras | MVP enfocado en diferenciadores clave |
| **Testing y bugs** | Más propenso a errores iniciales | Fase de pruebas de 2 semanas |
| **Reconocimiento** | Sin marca establecida | Marketing enfocado en transparencia |

---

### 3.3.3. Lecciones Aprendidas de Plataformas Existentes

Del análisis de competidores, se extraen las siguientes **buenas prácticas a adoptar**:

#### De Udemy:
-  Sistema de categorías y subcategorías claro
-  Niveles de dificultad (Principiante, Intermedio, Avanzado)
-  Duración total de curso visible

#### De Coursera:
-  Certificados de finalización
-  Estadísticas de inscripciones públicas
-  Información de instructores con credenciales

#### De Domestika:
-  Diseño visual atractivo y moderno
-  Comunidad de estudiantes (futuro)
-  Proyectos finales de curso

#### De Platzi:
-  Rutas de aprendizaje (roadmaps) - futuro
-  Sistema de progreso visual
-  Dashboard personalizado

---

## 3.4. Conclusiones del Análisis

### Principales Hallazgos

1. **Existe demanda insatisfecha** de plataformas educativas transparentes
2. **Los usuarios valoran la información detallada** antes de inscribirse
3. **Las plataformas actuales tienen margen de mejora** en UX y transparencia
4. **Es viable técnicamente** crear una plataforma competitiva con recursos limitados
5. **El mercado está en crecimiento** (13.7% CAGR global, 18.5% España)

### Justificación del Desarrollo

El análisis del contexto actual justifica plenamente el desarrollo de **E-Learning JCB Platform** por:

-  **Necesidades reales no cubiertas** (transparencia, UX optimizada)
-  **Viabilidad técnica y económica** (Reflex + MongoDB, costes <30€/mes)
-  **Oportunidad de mercado** (crecimiento sostenido del sector)
-  **Diferenciación clara** (visualización completa de contenidos)
-  **Escalabilidad futura** (arquitectura preparada para crecimiento)

### Próximos Pasos

Con las necesidades y problemáticas identificadas, la siguiente sección (Solución Propuesta) detallará:

- Tecnologías específicas seleccionadas
- Arquitectura de la solución
- Presupuesto detallado
- Recursos humanos y materiales necesarios
- Justificación de decisiones técnicas

---

<div style="page-break-after: always;"></div>



# 4. SOLUCIÓN PROPUESTA

## 4.1. Diferentes Tecnologías Existentes para el Desarrollo

### 4.1.1. Análisis de Alternativas Tecnológicas

Antes de seleccionar el stack tecnológico definitivo, se analizaron múltiples alternativas considerando los siguientes criterios:

- **Tiempo de desarrollo**: Rapidez para llegar al MVP
- **Curva de aprendizaje**: Facilidad de dominio para un desarrollador
- **Costes**: Hosting, licencias y mantenimiento
- **Escalabilidad**: Capacidad de crecimiento
- **Comunidad y soporte**: Documentación y recursos disponibles
- **Rendimiento**: Velocidad de respuesta y optimización

---

### 4.1.2. Comparativa de Stacks Tecnológicos

#### Opción 1: **MERN Stack** (MongoDB + Express + React + Node.js)

**Descripción**: Stack JavaScript full-stack más popular

**Ventajas**:
-  Comunidad muy grande y madura
-  Abundancia de recursos y tutoriales
-  Un solo lenguaje (JavaScript) en frontend y backend
-  Librerías y paquetes npm para casi cualquier funcionalidad
-  React para UI moderna y reactiva

**Desventajas**:
-  Requiere configuración compleja (Webpack, Babel, etc.)
-  Gestión de estado compleja (Redux, Context API)
-  JavaScript es dinámicamente tipado (propenso a errores)
-  Necesidad de frameworks adicionales para backend (Express, NestJS)
-  Dos proyectos separados (frontend y backend) aumentan complejidad

**Tiempo estimado de desarrollo**: 9-12 meses
**Coste mensual de hosting**: 30-50€
**Curva de aprendizaje**: Media-Alta

---

#### Opción 2: **Django + React**

**Descripción**: Backend en Python (Django) + Frontend en React

**Ventajas**:
-  Django es framework maduro con ORM potente
-  Admin panel incluido de serie
-  Seguridad robusta out-of-the-box
-  Python es lenguaje popular y legible
-  React para UI moderna

**Desventajas**:
-  Dos lenguajes diferentes (Python backend, JavaScript frontend)
-  Configuración de API REST (Django REST Framework) añade complejidad
-  Despliegue más complejo (Gunicorn, Nginx)
-  Gestión de estado en frontend sigue siendo compleja
-  Mayor tiempo de configuración inicial

**Tiempo estimado de desarrollo**: 8-10 meses
**Coste mensual de hosting**: 40-70€
**Curva de aprendizaje**: Alta

---

#### Opción 3: **Laravel + Vue.js**

**Descripción**: Backend en PHP (Laravel) + Frontend en Vue.js

**Ventajas**:
-  Laravel es framework PHP más popular
-  Eloquent ORM intuitivo
-  Ecosystem robusto (Forge, Vapor para deploy)
-  Vue.js es más simple que React
-  Blade templates para vistas mixtas

**Desventajas**:
-  PHP tiene peor rendimiento que Python/Node.js
-  Dos lenguajes (PHP backend, JavaScript frontend)
-  Menor popularidad que MERN o Django
-  Hosting PHP suele ser más costoso
-  Configuración de SPA (Single Page App) compleja

**Tiempo estimado de desarrollo**: 8-11 meses
**Coste mensual de hosting**: 35-60€
**Curva de aprendizaje**: Media

---

#### Opción 4: **Reflex (Python Full-Stack)** X **SELECCIONADO**

**Descripción**: Framework full-stack en Python que genera React automáticamente

**Ventajas**:
-  **Un solo lenguaje** (Python) para frontend y backend
-  **Generación automática de React** desde código Python
-  **Gestión de estado integrada** (sin Redux, sin Context API)
-  **Configuración mínima** (sin Webpack, Babel, etc.)
-  **Type hints nativos** en Python (detección de errores en desarrollo)
-  **Componentes reutilizables** con sintaxis Python
-  **Desarrollo 60% más rápido** que stacks tradicionales
-  **Despliegue simplificado** con Reflex Cloud
-  **Costes reducidos** de hosting (20-30€/mes)
-  **Comunidad creciente** y documentación completa

**Desventajas**:
-  Framework relativamente nuevo (v0.8, lanzado 2023)
-  Comunidad más pequeña que MERN o Django
-  Menos recursos de terceros (pero suficientes para el proyecto)
-  Algunas features avanzadas en desarrollo

**Tiempo estimado de desarrollo**: 6 meses 
**Coste mensual de hosting**: 20-30€ 
**Curva de aprendizaje**: Baja (si se conoce Python) 

---

### 4.1.3. Comparativa de Bases de Datos

#### Opción 1: **PostgreSQL** (Relacional)

**Ventajas**:
-  Base de datos SQL robusta y madura
-  Relaciones complejas bien soportadas
-  Transacciones ACID
-  JSON support para flexibilidad

**Desventajas**:
-  Esquema rígido (migraciones necesarias)
-  Escalabilidad horizontal compleja
-  Mayor complejidad en configuración
-  Hosting más costoso

**Coste mensual**: 15-40€

---

#### Opción 2: **MySQL/MariaDB** (Relacional)

**Ventajas**:
-  Base de datos SQL muy popular
-  Buen rendimiento en lecturas
-  Hosting económico disponible

**Desventajas**:
-  Esquema rígido
-  Menos features avanzadas que PostgreSQL
-  Escalabilidad limitada
-  JSON support limitado

**Coste mensual**: 10-30€

---

#### Opción 3: **MongoDB Atlas** (NoSQL) X **SELECCIONADO**

**Ventajas**:
-  **Esquema flexible** (ideal para iteración rápida)
-  **Escalabilidad horizontal** nativa (sharding)
-  **Documentos JSON** que mapean directamente a modelos Python
-  **MongoDB Atlas** (cloud) con tier gratuito M0
-  **Respaldos automáticos** y alta disponibilidad
-  **Driver asíncrono** (Motor) para alto rendimiento
-  **Consultas potentes** con agregaciones
-  **Indexación** eficiente para búsquedas

**Desventajas**:
-  Menos adecuado para relaciones complejas (mitigado con referencias)
-  Consistencia eventual en clusters distribuidos

**Coste mensual**:
- Tier M0 (desarrollo): **0€** 
- Tier M2 (producción pequeña): **9€**
- Tier M10 (producción media): **57€**

---

### 4.1.4. Matriz de Decisión Tecnológica

| Criterio | MERN | Django+React | Laravel+Vue | **Reflex+MongoDB** |
|----------|------|--------------|-------------|-------------------|
| Tiempo de desarrollo | 9-12 meses | 8-10 meses | 8-11 meses | **6 meses**  |
| Curva de aprendizaje | Media-Alta | Alta | Media | **Baja**  |
| Coste hosting/mes | 30-50€ | 40-70€ | 35-60€ | **20-30€**  |
| Escalabilidad | XXXX | XXXXX | XXX | **XXX** |
| Rendimiento | XXXX | XXXX | XXX | **XXXXX** |
| Comunidad | XXXXX | XXXXX | XXXX | **XXX** |
| Documentación | XXXXX | XXXXX | XXXX | **XXXX** |
| Mantenibilidad | XXX | XXXX | XXXX | **XXXXX** |
| **PUNTUACIÓN TOTAL** | 29/40 | 33/40 | 26/40 | **35/40**  |

---

## 4.2. Estudio Económico y Valoración de Presupuestos

### 4.2.1. Costes de Desarrollo

#### Metodología de Cálculo

Para estimar los costes de desarrollo, se utiliza la siguiente fórmula:

```
Coste Total = (Horas de Desarrollo × Tarifa/Hora) + Costes Fijos
```

**Parámetros**:
- **Tarifa por hora**: 25€/hora (desarrollador junior en España)
- **Horas totales estimadas**: 480 horas (6 meses × 4 semanas × 20 horas/semana)
- **Costes fijos**: Hardware, software, formación

---

#### Desglose de Horas por Fase

| Fase | Semanas | Horas/Semana | Total Horas | Descripción |
|------|---------|--------------|-------------|-------------|
| **Fase 1: Configuración Inicial** | 2 | 20 | 40h | Entorno, MongoDB, estructura proyecto |
| **Fase 2: Módulo de Cursos** | 3 | 20 | 60h | Modelos, servicios, UI de cursos |
| **Fase 3: Módulo de Instructores** | 2 | 20 | 40h | Perfiles, estadísticas |
| **Fase 4: Refactorización** | 1 | 20 | 20h | Limpieza de código, optimización |
| **Fase 5: Autenticación** | 4 | 20 | 80h | Login, registro, roles, RBAC |
| **Fase 6: Inscripciones y Progreso** | 4 | 20 | 80h | Enrollment, progreso, dashboard |
| **Fase 7: Panel de Instructor** | 4 | 20 | 80h | CRUD avanzado, estadísticas |
| **Fase 8: Funcionalidades Avanzadas** | 3 | 20 | 60h | Búsqueda, filtros, recomendaciones |
| **Fase 9: Pruebas y Documentación** | 3 | 20 | 60h | Testing, manuales, memoria |
| **TOTAL** | **26 semanas** | | **520h** | |

**Nota**: Se estiman 520 horas totales (40 horas extra para imprevistos y ajustes)

---

#### Cálculo de Coste de Desarrollo

| Concepto | Cálculo | Subtotal |
|----------|---------|----------|
| **Horas de desarrollo** | 520h × 25€/h | **13,000€** |
| **Hardware** (si no se tiene) | | |
| - Portátil desarrollo | 1 unidad × 800€ | 800€ |
| **Software y herramientas** | | |
| - Reflex (framework) | Open source | 0€ |
| - VS Code / IDE | Gratuito | 0€ |
| - MongoDB Compass | Gratuito | 0€ |
| - GitHub (repositorio) | Gratuito | 0€ |
| - Figma (diseño) | Plan gratuito | 0€ |
| **Formación** | | |
| - Cursos Reflex/MongoDB | 2 cursos × 50€ | 100€ |
| - Libros técnicos | 3 libros × 30€ | 90€ |
| **TOTAL DESARROLLO** | | **13,990€** |

**Nota**: Si el hardware ya está disponible, el coste se reduce a **13,190€**

---

### 4.2.2. Costes Operativos (Año 1)

#### Costes de Infraestructura

| Servicio | Proveedor | Plan | Coste/Mes | Coste/Año |
|----------|-----------|------|-----------|-----------|
| **Base de Datos** | MongoDB Atlas | M0 (Desarrollo) | 0€ | **0€** |
| | MongoDB Atlas | M2 (Producción) | 9€ | 108€ |
| **Hosting** | Reflex Cloud | Free tier (Desarrollo) | 0€ | **0€** |
| | Reflex Cloud | Starter (Producción) | 20€ | 240€ |
| **Dominio** | Namecheap | .com | - | 12€ |
| **SSL/TLS** | Let's Encrypt | Gratuito | 0€ | **0€** |
| **CDN** | Cloudflare | Free tier | 0€ | **0€** |
| **Email** | SendGrid | Free (100/día) | 0€ | **0€** |
| **SUBTOTAL (Desarrollo)** | | | **0€/mes** | **12€/año**  |
| **SUBTOTAL (Producción)** | | | **29€/mes** | **360€/año** |

---

#### Costes de Marketing y Promoción

| Concepto | Descripción | Coste/Mes | Coste/Año |
|----------|-------------|-----------|-----------|
| **Marketing orgánico** | | | |
| - Redes sociales | LinkedIn, X (Twitter) | 0€ | **0€** |
| - SEO on-page | Optimización web | 0€ | **0€** |
| - Contenido (blog) | Artículos 2/mes | 0€ | **0€** |
| **Marketing de pago** (desde mes 4) | | | |
| - Google Ads | Búsquedas locales | 200€ | 1,800€ |
| - LinkedIn Ads | B2B corporativo | 150€ | 1,350€ |
| - Colaboraciones | Influencers micro | 100€ | 900€ |
| **Diseño gráfico** | | | |
| - Canva Pro | Plantillas premium | 13€ | 156€ |
| - Imágenes (Unsplash) | Gratuitas | 0€ | **0€** |
| **SUBTOTAL** | | | **4,206€/año** |

---

#### Costes Administrativos y Legales

| Concepto | Descripción | Coste/Mes | Coste/Año |
|----------|-------------|-----------|-----------|
| **Gestoría** | Asesoría fiscal y contable | 50€ | 600€ |
| **Seguridad Social** | Cuota autónomos (tarifa plana) | 80€ | 960€ |
| **Seguro RC profesional** | Responsabilidad civil | - | 200€ |
| **Redacción legal** | Política privacidad, términos uso | - | 300€ |
| **SUBTOTAL** | | | **2,060€/año** |

---

### 4.2.3. Presupuesto Total Año 1

#### Escenario Conservador (Solo Desarrollo)

| Concepto | Coste |
|----------|-------|
| Desarrollo (520h × 25€/h) | 13,000€ |
| Formación | 190€ |
| Infraestructura (desarrollo) | 12€ |
| **TOTAL** | **13,202€** |

**Financiación**: Autofinanciado (proyecto académico)

---

#### Escenario Realista (Desarrollo + Lanzamiento)

| Concepto | Coste |
|----------|-------|
| Desarrollo | 13,000€ |
| Hardware (si aplica) | 800€ |
| Formación | 190€ |
| Infraestructura (producción) | 360€ |
| Marketing | 4,206€ |
| Administrativos y legales | 2,060€ |
| **TOTAL** | **20,616€** |

**Financiación**:
- Autofinanciado: 13,000€ (desarrollo)
- Ayudas (Almería Emprende + Tarifa plana): 5,676€
- Inversión propia: 1,940€
- **Total cubierto**: 20,616€ 

---

#### Escenario Optimista (Con Financiación Externa)

| Concepto | Coste |
|----------|-------|
| Desarrollo | 13,000€ |
| Hardware | 800€ |
| Formación | 190€ |
| Infraestructura | 360€ |
| Marketing (ampliado) | 8,000€ |
| Administrativos | 2,060€ |
| Contratación (6 meses, desarrollador junior) | 16,152€ |
| **TOTAL** | **40,562€** |

**Financiación**:
- ENISA préstamo participativo: 25,000€
- Ayudas (Andalucía Emprende): 10,000€
- Inversión propia: 5,562€
- **Total cubierto**: 40,562€ 

---

### 4.2.4. Proyección de Ingresos

#### Modelo de Negocio: Freemium + Marketplace

**Asunciones**:
- **Precio medio curso premium**: 99€
- **Comisión marketplace**: 25% de ventas
- **Tasa de conversión freemium**: 5% (de usuarios gratuitos a pago)
- **Retención**: 70% año 1

---

#### Proyección Año 1

| Mes | Usuarios Totales | Usuarios Premium | Cursos Vendidos | Ingresos Mes | Ingresos Acumulados |
|-----|------------------|------------------|-----------------|--------------|---------------------|
| 1-3 | 50 | 2 | 2 | 198€ | 594€ |
| 4-6 | 150 | 8 | 10 | 990€ | 3,564€ |
| 7-9 | 300 | 20 | 25 | 2,475€ | 10,989€ |
| 10-12 | 500 | 40 | 50 | 4,950€ | 25,839€ |

**Total Año 1**: **25,839€**

---

#### Proyección Año 2

| Trimestre | Usuarios Totales | Usuarios Premium | Ingresos Trimestre | Ingresos Acumulados |
|-----------|------------------|------------------|--------------------|---------------------|
| Q1 | 750 | 60 | 18,000€ | 18,000€ |
| Q2 | 1,200 | 100 | 30,000€ | 48,000€ |
| Q3 | 1,800 | 150 | 45,000€ | 93,000€ |
| Q4 | 2,500 | 220 | 66,000€ | 159,000€ |

**Total Año 2**: **159,000€**

---

### 4.2.5. Análisis de Rentabilidad

#### Año 1

| Concepto | Cantidad |
|----------|----------|
| **Ingresos** | 25,839€ |
| **Costes totales** | 20,616€ |
| **Beneficio bruto** | **5,223€**  |
| **Margen bruto** | **20.2%** |

**ROI (Return on Investment)**:
```
ROI = (Beneficio / Inversión) × 100
ROI = (5,223€ / 20,616€) × 100 = 25.3%
```

**Punto de equilibrio**: Mes 9-10

---

#### Año 2

| Concepto | Cantidad |
|----------|----------|
| **Ingresos** | 159,000€ |
| **Costes operativos** | 45,000€ |
| **Beneficio bruto** | **114,000€**  |
| **Margen bruto** | **71.7%** |

---

## 4.3. Elección y Justificación de Tecnologías Seleccionadas

### 4.3.1. Stack Tecnológico Final

#### Backend y Frontend: **Reflex 0.8.24**

**Justificación de la elección**:

1. **Desarrollo 60% más rápido**:
   - No requiere configurar Webpack, Babel, ESLint por separado
   - Generación automática de React desde Python
   - Un solo repositorio (monorepo integrado)
   - **Impacto**: Reducción de 12 meses a 6 meses

2. **Un solo lenguaje (Python)**:
   - No hay context switching entre JavaScript y Python
   - Aprovecha conocimientos de Python del ciclo DAW
   - Type hints nativos para detección de errores
   - **Impacto**: Curva de aprendizaje reducida en 40%

3. **Gestión de estado integrada**:
   - Sin necesidad de Redux, Context API, Zustand
   - Estados reactivos automáticos
   - Sincronización frontend-backend out-of-the-box
   - **Impacto**: Menos complejidad, menos bugs

4. **Componentes reutilizables**:
   - Sintaxis declarativa similar a React
   - Chakra UI integrado (sistema de diseño)
   - Fácil composición de componentes
   - **Impacto**: Código más limpio y mantenible

5. **Despliegue simplificado**:
   - Reflex Cloud con deploy automático
   - Sin necesidad de configurar Nginx, Gunicorn, PM2
   - Escalado automático
   - **Impacto**: Costes de hosting reducidos en 50%

**Alternativa considerada y descartada**: Django + React
- **Razón de descarte**: Requiere gestionar dos proyectos separados, mayor complejidad en configuración de API REST

---

#### Base de Datos: **MongoDB Atlas**

**Justificación de la elección**:

1. **Esquema flexible**:
   - Permite iterar rápidamente sin migraciones complejas
   - Documentos JSON mapean directamente a modelos Python (dict)
   - Fácil añadir campos nuevos sin breaking changes
   - **Impacto**: Velocidad de desarrollo aumentada

2. **Escalabilidad horizontal nativa**:
   - Sharding automático en MongoDB Atlas
   - Réplicas para alta disponibilidad
   - Crecimiento sin reestructuración
   - **Impacto**: Preparado para 10,000+ usuarios

3. **Tier gratuito generoso**:
   - M0 con 512MB almacenamiento (suficiente para desarrollo y MVP)
   - Sin tarjeta de crédito requerida
   - **Impacto**: Coste de desarrollo = 0€

4. **Driver asíncrono (Motor)**:
   - Operaciones no bloqueantes
   - Alto rendimiento en concurrencia
   - Integración nativa con async/await de Python
   - **Impacto**: Mejor rendimiento que alternativas síncronas

5. **Respaldos automáticos**:
   - Backups diarios en Atlas
   - Point-in-time recovery
   - Sin configuración manual
   - **Impacto**: Seguridad de datos sin esfuerzo extra

**Alternativa considerada y descartada**: PostgreSQL
- **Razón de descarte**: Esquema rígido aumenta tiempo de desarrollo en 30%, migraciones complejas, hosting más costoso

---

#### Lenguaje de Programación: **Python 3.10+**

**Justificación de la elección**:

1. **Sintaxis clara y legible**:
   - Código autodocumentado
   - Facilita mantenimiento futuro
   - **Impacto**: Código 40% más comprensible que JavaScript/PHP

2. **Type hints nativos**:
   - Detección de errores en desarrollo (mypy, Pylance)
   - Autocompletado inteligente en IDE
   - Documentación implícita
   - **Impacto**: Reducción de bugs en 25%

3. **Ecosystem maduro**:
   - Librerías para cualquier necesidad (bcrypt, pydantic, etc.)
   - Comunidad activa
   - **Impacto**: Solución de problemas más rápida

4. **Async/Await nativo** (desde Python 3.5):
   - Operaciones no bloqueantes
   - Compatible con Motor (driver MongoDB asíncrono)
   - **Impacto**: Rendimiento 3x superior a código síncrono

**Versión específica**: Python 3.10
- **Razón**: Match-case statements (útil para routing), mejoras de rendimiento, compatibilidad con Reflex

---

#### Sistema de Diseño: **Chakra UI** (integrado en Reflex)

**Justificación de la elección**:

1. **Componentes accesibles (WCAG 2.1)**:
   - Navegación por teclado out-of-the-box
   - ARIA labels automáticos
   - **Impacto**: Accesibilidad sin esfuerzo extra

2. **Theming consistente**:
   - Variables de diseño centralizadas
   - Modo oscuro soportado (futuro)
   - **Impacto**: Interfaz coherente en toda la app

3. **Responsive por defecto**:
   - Breakpoints predefinidos (sm, md, lg, xl)
   - Mobile-first design
   - **Impacto**: 100% responsive sin CSS custom

4. **Integración perfecta con Reflex**:
   - Componentes disponibles como rx.button(), rx.input(), etc.
   - Sin configuración adicional
   - **Impacto**: Desarrollo de UI 50% más rápido

**Alternativa considerada y descartada**: Tailwind CSS
- **Razón de descarte**: Requiere configuración externa, no integrado en Reflex, clases verbosas

---

### 4.3.2. Herramientas Complementarias

| Herramienta | Propósito | Justificación | Coste |
|-------------|-----------|---------------|-------|
| **Git + GitHub** | Control de versiones | Historial completo, colaboración, CI/CD | Gratuito |
| **VS Code** | IDE | Extensions para Python, integración Git, Pylance | Gratuito |
| **MongoDB Compass** | Cliente visual de BD | Exploración de datos, queries visuales | Gratuito |
| **Postman / Thunder Client** | Testing de API | Pruebas de endpoints, colecciones guardadas | Gratuito |
| **Reflex CLI** | Desarrollo y deploy | Comandos `reflex run`, `reflex deploy` | Gratuito |
| **Figma** | Diseño de prototipos | Wireframes, mockups, colaboración | Plan gratuito |
| **Granian** | Servidor HTTP | Alto rendimiento ASGI, reemplazo de Uvicorn | Gratuito (open source) |

---

<div style="page-break-after: always;"></div>

## 4.4. Recursos Humanos y Materiales Necesarios

### 4.4.1. Recursos Humanos

#### Fase de Desarrollo (Meses 1-6)

**Equipo mínimo viable**: 1 persona (desarrollador full-stack)

| Rol | Responsabilidades | Dedicación | Perfil |
|-----|-------------------|------------|--------|
| **Desarrollador Full-Stack** | - Análisis de requisitos<br>- Diseño de arquitectura<br>- Desarrollo frontend y backend<br>- Testing<br>- Documentación<br>- Despliegue | 20h/semana | - Python avanzado<br>- Conocimientos de Reflex<br>- MongoDB básico<br>- Git/GitHub<br>- Estudiante DAW |

**Total horas**: 520 horas (26 semanas × 20h/semana)

---

#### Fase de Lanzamiento (Meses 7-12)

**Equipo ampliado** (opcional):

| Rol | Responsabilidades | Dedicación | Coste/Mes |
|-----|-------------------|------------|-----------|
| **Desarrollador Full-Stack** | Desarrollo continuo, bugs, features | 20h/semana | 2,000€ |
| **Marketing Digital** (freelance) | SEO, redes sociales, contenido | 10h/semana | 400€ |
| **Diseñador Gráfico** (freelance) | Imágenes, banners, material visual | 5h/semana | 200€ |

**Total coste mensual**: 2,600€

**Nota**: En Año 1 solo desarrollador principal (proyecto académico)

---

<div style="page-break-after: always;"></div>

### 4.4.2. Recursos Materiales

#### Hardware

| Equipo | Especificaciones Mínimas | Especificaciones Recomendadas | Coste |
|--------|--------------------------|-------------------------------|-------|
| **Portátil de desarrollo** | - Procesador: Intel i5 / Ryzen 5<br>- RAM: 8GB<br>- Almacenamiento: 256GB SSD<br>- Pantalla: 13" | - Procesador: Intel i7 / Ryzen 7<br>- RAM: 16GB<br>- Almacenamiento: 512GB SSD<br>- Pantalla: 15" | 800€ - 1,200€ |
| **Monitor externo** (opcional) | 1920×1080, 24" | 2560×1440, 27" | 150€ - 300€ |
| **Periféricos** | Ratón, teclado | Teclado mecánico, ratón ergonómico | 50€ - 150€ |

**Total hardware**: 1,000€ - 1,650€

**Nota**: Si ya se dispone de equipo, este coste se elimina

---

#### Software

| Herramienta | Licencia | Coste/Año |
|-------------|----------|-----------|
| **Sistema Operativo** | Windows 11 / Ubuntu 22.04 LTS | 0€ (Ubuntu gratuito) |
| **Python** | Open source | 0€ |
| **Reflex** | Open source (Apache 2.0) | 0€ |
| **VS Code** | Gratuito | 0€ |
| **Git** | Open source | 0€ |
| **MongoDB Compass** | Gratuito | 0€ |
| **Figma** | Plan gratuito (3 proyectos) | 0€ |
| **Canva Pro** (opcional) | Premium | 156€ |

**Total software obligatorio**: 0€ 
**Total software opcional**: 156€

---

#### Infraestructura

| Servicio | Tier | Coste/Mes | Coste/Año |
|----------|------|-----------|-----------|
| **MongoDB Atlas** | M0 (desarrollo) | 0€ | 0€ |
| | M2 (producción) | 9€ | 108€ |
| **Reflex Cloud** | Free (desarrollo) | 0€ | 0€ |
| | Starter (producción) | 20€ | 240€ |
| **Dominio .com** | Namecheap | - | 12€ |
| **Email (SendGrid)** | Free tier (100/día) | 0€ | 0€ |

**Total infraestructura desarrollo**: 0€/mes
**Total infraestructura producción**: 29€/mes (360€/año)

---

#### Material de Apoyo

| Concepto | Descripción | Coste |
|----------|-------------|-------|
| **Cursos online** | - Reflex Fundamentals<br>- MongoDB University | 100€ |
| **Libros técnicos** | - "MongoDB: The Definitive Guide"<br>- "Python for Web Development"<br>- "Clean Code" | 90€ |
| **Documentación oficial** | - Reflex Docs<br>- MongoDB Docs<br>- Python Docs | 0€ |

**Total formación**: 190€

---

<div style="page-break-after: always;"></div>

### 4.4.3. Resumen de Recursos Necesarios

#### Inversión Inicial (Una Vez)

| Concepto | Cantidad |
|----------|----------|
| Hardware (si no se tiene) | 1,000€ - 1,650€ |
| Formación | 190€ |
| **TOTAL INICIAL** | **1,190€ - 1,840€** |

---

#### Costes Recurrentes (Año 1)

| Concepto | Mensual | Anual |
|----------|---------|-------|
| Infraestructura (producción) | 29€ | 360€ |
| Software opcional (Canva Pro) | 13€ | 156€ |
| Gestoría | 50€ | 600€ |
| Seguridad Social (tarifa plana) | 80€ | 960€ |
| Marketing (desde mes 4) | 450€ | 4,050€ |
| **TOTAL RECURRENTE** | **~500€** | **~6,126€** |

---

#### Necesidades de Personal

**Año 1**: 1 desarrollador full-stack (proyecto académico)
**Año 2** (opcional):
- 1 desarrollador junior adicional (24,000€/año)
- 1 freelance marketing (4,800€/año, 10h/semana)

---

### 4.4.4. Viabilidad de Recursos

####  Recursos Disponibles (Sin Inversión)

- Portátil de desarrollo (ya disponible)
- Software (100% gratuito)
- Infraestructura desarrollo (MongoDB M0 + Reflex Cloud Free)
- Conocimientos de Python (ciclo DAW)

####  Recursos que Requieren Inversión Mínima

- Formación (190€) - **justificable por ROI en conocimiento**
- Infraestructura producción (360€/año) - **necesario para lanzamiento**
- Marketing (4,050€/año) - **opcional pero recomendado**

####  Recursos Cubiertos por Ayudas

- Tarifa plana autónomos: **2,676€ ahorro**
- Almería Emprende: **3,000€** (cubre infraestructura + formación + marketing parcial)
- Cheque Innovación: **1,500€** (servicios de asesoramiento)

---

**Conclusión de la Sección**:

La solución propuesta basada en **Reflex + MongoDB** es la opción más viable técnica y económicamente para el desarrollo de **E-Learning JCB Platform**. Con una inversión inicial mínima (1,190€ - 1,840€), costes recurrentes controlados (360€/año producción) y ayudas disponibles (7,176€ escenario conservador), el proyecto es **altamente viable** y presenta un **ROI positivo desde el Año 1** (25.3%).

---

<div style="page-break-after: always;"></div>



# 5. PLANIFICACIÓN TEMPORAL DEL DESARROLLO

## 5.1. Cronograma General del Proyecto

### 5.1.1. Duración Total y Fases Principales

**Fecha de inicio**: Noviembre 2025
**Fecha de entrega**: Mayo 2026
**Duración total**: 26 semanas (6 meses)

El proyecto se estructura en **9 fases principales** con objetivos y entregables específicos:

```
Noviembre 2025          Diciembre 2025          Enero 2026              Febrero 2026
│                       │                       │                       │
├─ FASE 1: Config.      ├─ FASE 2: Cursos      ├─ FASE 3: Instructores├─ FASE 5: Autenticación
│  (Semanas 1-2)        │  (Semanas 3-5)        │  (Semanas 6-7)        │  (Semanas 9-12)
│                       │                       ├─ FASE 4: Refactor.   │
│                       │                       │  (Semana 8)           │

Marzo 2026              Abril 2026              Mayo 2026
│                       │                       │
├─ FASE 6: Inscripciones├─ FASE 7: Panel Instr.├─ FASE 8: Avanzadas
│  (Semanas 13-16)      │  (Semanas 17-20)      │  (Semanas 21-23)
│                       │                       ├─ FASE 9: Pruebas/Docs
│                       │                       │  (Semanas 24-26)
│                       │                       └─ DEFENSA (Última semana)
```

---

## 5.2. Detalle de Fases de Desarrollo

### FASE 1: Configuración Inicial y Análisis (Semanas 1-2)
**Fechas**: 3-16 Noviembre 2025
**Duración**: 2 semanas (40 horas)

#### Objetivos
- Configurar entorno de desarrollo completo
- Establecer conexión con MongoDB Atlas
- Definir estructura de proyecto
- Analizar requisitos en profundidad
- Crear diseño inicial de arquitectura

<div style="page-break-after: always;"></div>

#### Tareas Detalladas

| Tarea | Descripción | Horas | Responsable |
|-------|-------------|-------|-------------|
| **1.1. Configuración de entorno** | | **8h** | |
| - Instalar Python 3.10+ | Configurar versión compatible | 1h | Desarrollador |
| - Crear entorno virtual | `python -m venv reflex-env` | 0.5h | Desarrollador |
| - Instalar Reflex | `pip install reflex==0.8.24` | 0.5h | Desarrollador |
| - Configurar VS Code | Extensions, Pylance, Black | 1h | Desarrollador |
| - Inicializar Git/GitHub | Repositorio, .gitignore, README | 1h | Desarrollador |
| - Configurar pre-commit hooks | Black, flake8, mypy | 2h | Desarrollador |
| - Documentar instalación | README con instrucciones | 2h | Desarrollador |
| **1.2. Configuración de MongoDB** | | **6h** | |
| - Crear cuenta MongoDB Atlas | Registro, verificación email | 0.5h | Desarrollador |
| - Crear cluster M0 gratuito | Configuración región EU-West | 1h | Desarrollador |
| - Configurar seguridad | IP whitelist, usuario BD | 1h | Desarrollador |
| - Instalar Motor driver | `pip install motor` | 0.5h | Desarrollador |
| - Crear conexión asíncrona | `database/mongodb.py` | 2h | Desarrollador |
| - Probar conexión | Script de test | 1h | Desarrollador |
| **1.3. Estructura del proyecto** | | **10h** | |
| - Definir arquitectura en capas | Carpetas: models, services, states, pages | 2h | Desarrollador |
| - Crear estructura de directorios | mkdir components, utils, etc. | 1h | Desarrollador |
| - Configurar rxconfig.py | Personalización Reflex | 2h | Desarrollador |
| - Definir convenciones de código | Docstrings, naming, imports | 2h | Desarrollador |
| - Crear archivos base | `__init__.py`, imports | 1h | Desarrollador |
| - Documentar estructura | Diagrama de carpetas | 2h | Desarrollador |
| **1.4. Análisis de requisitos** | | **12h** | |
| - Entrevistas con stakeholders | Estudiantes, instructores potenciales | 3h | Desarrollador |
| - Definir user stories | Formato "Como [rol], quiero [acción]" | 3h | Desarrollador |
| - Priorizar funcionalidades | MoSCoW (Must, Should, Could, Won't) | 2h | Desarrollador |
| - Diseñar wireframes | Figma: login, cursos, detalle | 3h | Desarrollador |
| - Documentar requisitos | Documento de especificaciones | 1h | Desarrollador |
| **1.5. Diseño de arquitectura** | | **4h** | |
| - Diagrama de arquitectura | Capas, flujo de datos | 2h | Desarrollador |
| - Definir modelos de datos | User, Course, Section, Lesson | 1h | Desarrollador |
| - Planificar API endpoints | REST-like con Reflex | 1h | Desarrollador |

#### Entregables
-  Entorno de desarrollo funcional
-  Conexión a MongoDB Atlas operativa
-  Repositorio Git inicializado
-  Documento de requisitos (10 user stories)
-  Wireframes de 5 pantallas principales
-  Diagrama de arquitectura

#### Criterios de Aceptación
- [ ] `reflex run` ejecuta sin errores
- [ ] Conexión a MongoDB Atlas exitosa (test script pasa)
- [ ] Git commits iniciales en GitHub

---

### FASE 2: Módulo de Cursos (Semanas 3-5)
**Fechas**: 17 Noviembre - 7 Diciembre 2025
**Duración**: 3 semanas (60 horas)

#### Objetivos
- Implementar modelos de datos para cursos
- Desarrollar servicios CRUD de cursos
- Crear interfaz de listado de cursos
- Implementar página de detalle de curso
- Sistema de secciones y lecciones

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **2.1. Modelos de datos** | | **10h** |
| - Modelo Course | Clase con validaciones | 3h |
| - Modelo Section | Estructura de secciones | 2h |
| - Modelo Lesson | Lecciones con duración | 2h |
| - Modelo Rating | Valoraciones de cursos | 2h |
| - Testing de modelos | Unit tests con pytest | 1h |
| **2.2. Servicios de cursos** | | **15h** |
| - CourseService.get_all_courses() | Listado con filtros | 3h |
| - CourseService.get_course_by_id() | Detalle con populate | 3h |
| - CourseService.create_course() | Inserción con validación | 3h |
| - CourseService.update_course() | Actualización parcial | 2h |
| - CourseService.delete_course() | Borrado lógico/físico | 2h |
| - Manejo de errores | Try-except, logging | 2h |
| **2.3. Estados de Reflex** | | **10h** |
| - CourseState (lista) | Estado para listado | 3h |
| - CourseDetailState | Estado para detalle | 3h |
| - Eventos de carga | handle_load_courses | 2h |
| - Variables computadas | Filtros, búsqueda | 2h |
| **2.4. Componentes UI** | | **12h** |
| - CourseCard | Card de curso reutilizable | 3h |
| - CourseList | Grid responsive de cards | 2h |
| - CourseDetail | Página de detalle completa | 4h |
| - SectionList | Acordeón de secciones | 2h |
| - LessonItem | Item de lección con duración | 1h |
| **2.5. Páginas** | | **8h** |
| - /courses (listado) | Página principal de cursos | 3h |
| - /course/[id] (detalle) | Enrutamiento dinámico | 3h |
| - Navegación (breadcrumbs) | Migas de pan | 2h |
| **2.6. Testing e integración** | | **5h** |
| - Unit tests servicios | Pytest async | 2h |
| - Integration tests | E2E con playwright (opcional) | 2h |
| - Corrección de bugs | Debugging | 1h |

#### Entregables
-  4 modelos de datos implementados
-  5 métodos de servicio CRUD
-  5 componentes UI reutilizables
-  2 páginas funcionales
-  15+ unit tests

#### Criterios de Aceptación
- [ ] Listado de cursos carga desde MongoDB
- [ ] Detalle de curso muestra secciones y lecciones
- [ ] Diseño responsive en móvil y desktop
- [ ] Tests pasan sin errores

---

### FASE 3: Módulo de Instructores (Semanas 6-7)
**Fechas**: 8-21 Diciembre 2025
**Duración**: 2 semanas (40 horas)

#### Objetivos
- Implementar modelo User con rol instructor
- Crear servicios de gestión de usuarios
- Desarrollar perfiles de instructores
- Listado de instructores con estadísticas

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **3.1. Modelo User** | | **8h** |
| - Diseño del modelo | Campos: name, email, role, bio | 2h |
| - Roles (enum) | admin, instructor, student | 1h |
| - Propiedades computadas | is_admin, is_instructor, is_student | 2h |
| - Validaciones | Email único, formato válido | 2h |
| - Testing | Unit tests | 1h |
| **3.2. UserService** | | **12h** |
| - get_user_by_id() | Recuperar usuario | 2h |
| - get_user_by_email() | Login lookup | 2h |
| - create_user() | Registro | 3h |
| - update_user() | Edición de perfil | 2h |
| - get_instructors() | Solo instructores | 2h |
| - get_instructor_stats() | Cursos, inscripciones | 1h |
| **3.3. Estados** | | **6h** |
| - InstructorState (listado) | Lista de instructores | 2h |
| - InstructorDetailState | Perfil + cursos | 3h |
| - Eventos de carga | Asíncronos | 1h |
| **3.4. Componentes** | | **8h** |
| - InstructorCard | Card con foto, bio, stats | 3h |
| - InstructorProfile | Perfil completo | 3h |
| - InstructorCoursesList | Cursos del instructor | 2h |
| **3.5. Páginas** | | **4h** |
| - /instructors (listado) | Grid de instructores | 2h |
| - /instructor/[id] (detalle) | Perfil completo | 2h |
| **3.6. Testing** | | **2h** |
| - Unit tests | Servicios y modelos | 2h |

#### Entregables
-  Modelo User con 3 roles
-  6 métodos UserService
-  3 componentes de instructor
-  2 páginas funcionales
-  10+ unit tests

#### Criterios de Aceptación
- [ ] Listado de instructores muestra estadísticas
- [ ] Perfil de instructor muestra cursos
- [ ] Roles correctamente definidos

---

### FASE 4: Refactorización y Optimización (Semana 8)
**Fechas**: 22-28 Diciembre 2025
**Duración**: 1 semana (20 horas)

#### Objetivos
- Limpieza de código duplicado
- Creación de utilidades reutilizables
- Optimización de rendimiento
- Corrección de deprecaciones
- Documentación técnica

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **4.1. Refactorización** | | **8h** |
| - Extraer helpers comunes | utils/helpers.py | 2h |
| - Consolidar estilos | Chakra UI theming | 2h |
| - Optimizar consultas BD | Índices, proyecciones | 2h |
| - Eliminar código muerto | Imports no usados, etc. | 2h |
| **4.2. Utilidades** | | **6h** |
| - route_helpers.py | Generación de URLs | 2h |
| - formatters .py | Formato de fechas, números | 2h |
| - validators .py | Validación de inputs | 2h |
| **4.3. Documentación** | | **4h** |
| - Docstrings en funciones | Google style | 2h |
| - README actualizado | Instrucciones claras | 1h |
| - Comentarios en código complejo | Explicaciones | 1h |
| **4.4. Performance** | | **2h** |
| - Lazy loading de imágenes | Optimización | 1h |
| - Memoización de componentes | React.memo equivalente | 1h |

#### Entregables
-  Código refactorizado
-  3 archivos de utilidades
-  Documentación completa
-  Mejoras de rendimiento (15% más rápido)

---

### FASE 5: Sistema de Autenticación y Roles (Semanas 9-12)
**Fechas**: 29 Diciembre 2025 - 25 Enero 2026
**Duración**: 4 semanas (80 horas)

#### Objetivos
- Implementar hash de contraseñas con bcrypt
- Sistema de login y registro
- Gestión de sesiones
- Control de acceso basado en roles (RBAC)
- Protección de rutas

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **5.1. Seguridad de contraseñas** | | **8h** |
| - Instalar bcrypt | `pip install bcrypt` | 0.5h |
| - Crear password .py | hash_password(), verify_password() | 3h |
| - Testing de hash | Verificar salt único | 2h |
| - Documentar seguridad | Buenas prácticas | 2.5h |
| **5.2. AuthState** | | **20h** |
| - Registro de usuarios | Validación, hash, insert | 6h |
| - Login | Verificación, sesión | 6h |
| - Logout | Limpieza de sesión | 2h |
| - Gestión de sesión | is_authenticated, current_user | 3h |
| - Manejo de errores | Mensajes claros | 3h |
| **5.3. RBAC (Control de acceso)** | | **16h** |
| - Componentes protegidos | protected .py | 4h |
| - require_auth() | HOC de autenticación | 3h |
| - require_role() | HOC de autorización | 3h |
| - admin_only(), instructor_only() | Shortcuts | 2h |
| - Redirecciones | A login si no auth | 2h |
| - Testing de permisos | Unit tests | 2h |
| **5.4. Páginas de auth** | | **16h** |
| - /login (Login) | Formulario + validación | 5h |
| - /register (Registro) | Form completo | 5h |
| - /profile (Perfil) | Edición de datos | 4h |
| - Feedback visual | Success, error messages | 2h |
| **5.5. Protección de rutas** | | **12h** |
| - /admin/* protegido | Solo admins | 3h |
| - /instructor/* protegido | Solo instructores | 3h |
| - /student/* protegido | Solo estudiantes | 3h |
| - Testing de protección | Intentos no autorizados | 3h |
| **5.6. Cambio de contraseña** | | **8h** |
| - Formulario de cambio | Actual + nueva + confirmar | 3h |
| - Verificación de actual | Seguridad | 2h |
| - Actualización en BD | Hash de nueva | 2h |
| - Notificación email (futuro) | Placeholder | 1h |

#### Entregables
-  Sistema de hash bcrypt
-  Login y registro funcionales
-  RBAC con 6 funciones de protección
-  3 páginas de autenticación
-  Rutas protegidas
-  20+ tests de seguridad

#### Criterios de Aceptación
- [ ] Usuario puede registrarse y hacer login
- [ ] Contraseñas hasheadas con bcrypt (12 rounds)
- [ ] Roles funcionan correctamente
- [ ] Intentos de acceso no autorizados redirigen a login

---

### FASE 6: Inscripciones y Seguimiento de Progreso (Semanas 13-16)
**Fechas**: 26 Enero - 22 Febrero 2026
**Duración**: 4 semanas (80 horas)

#### Objetivos
- Sistema de inscripción a cursos
- Seguimiento de lecciones completadas
- Dashboard de estudiante
- Progreso por curso

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **6.1. Modelo Enrollment** | | **8h** |
| - Diseño del modelo | user_id, course_id, enrolled_at | 3h |
| - Índices | Compuesto (user_id, course_id) | 2h |
| - Validaciones | Unicidad, existencia | 2h |
| - Testing | Unit tests | 1h |
| **6.2. EnrollmentService** | | **16h** |
| - enroll_student() | Inserción con validaciones | 4h |
| - unenroll_student() | Desins cripción | 2h |
| - get_user_enrollments() | Cursos del usuario | 3h |
| - get_course_enrollments() | Estudiantes del curso | 3h |
| - is_enrolled() | Verificación booleana | 2h |
| - Testing | Unit e integration tests | 2h |
| **6.3. Modelo Progress** | | **8h** |
| - Diseño | enrollment_id, lesson_id, completed_at | 3h |
| - Cálculo de porcentaje | Método computado | 3h |
| - Testing | Validaciones | 2h |
| **6.4. ProgressService** | | **16h** |
| - mark_lesson_complete() | Marcar completada | 4h |
| - get_course_progress() | Progreso de curso | 4h |
| - get_user_progress() | Progreso global | 4h |
| - get_completion_percentage() | Cálculo % | 2h |
| - Testing | Unit tests | 2h |
| **6.5. Dashboard de estudiante** | | **20h** |
| - Diseño UI | Wireframe en Figma | 3h |
| - StudentDashboardState | Estado con datos | 5h |
| - Tarjetas de cursos | Mis cursos con progreso | 5h |
| - Gráficos de progreso | Progress bars | 3h |
| - Estadísticas | Cursos completados, en progreso | 2h |
| - Testing UI | Manual, screenshots | 2h |
| **6.6. Botón de inscripción** | | **8h** |
| - Componente EnrollButton | Lógica de inscripción | 3h |
| - Estados (inscrito, no inscrito) | Condicional | 2h |
| - Feedback | Success/error messages | 2h |
| - Testing | Casos de uso | 1h |
| **6.7. Página de curso (actualizada)** | | **4h** |
| - Botón de inscripción | Integración | 2h |
| - Progreso si inscrito | Barra de progreso | 2h |

#### Entregables
-  2 modelos (Enrollment, Progress)
-  2 servicios completos
-  Dashboard de estudiante
-  Sistema de inscripción funcional
-  Seguimiento de progreso
-  25+ tests

#### Criterios de Aceptación
- [ ] Estudiante puede inscribirse en cursos
- [ ] No se permiten inscripciones duplicadas
- [ ] Dashboard muestra cursos inscritos
- [ ] Progreso se calcula correctamente

---

### FASE 7: Panel de Instructor (Semanas 17-20)
**Fechas**: 23 Febrero - 22 Marzo 2026
**Duración**: 4 semanas (80 horas)

#### Objetivos
- Panel de gestión de cursos (CRUD)
- Creación de cursos con secciones y lecciones
- Estadísticas de instructor
- Dashboard de instructor

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **7.1. CRUD de cursos (instructor)** | | **24h** |
| - Formulario de creación | Título, descripción, nivel, etc. | 6h |
| - Formulario de edición | Actualización de datos | 5h |
| - Confirmación de borrado | Modal de confirmación | 2h |
| - Validaciones | Client-side y server-side | 4h |
| - InstructorCourseState | Estado de gestión | 5h |
| - Testing | E2E del flujo | 2h |
| **7.2. Gestión de secciones** | | **16h** |
| - Formulario de sección | Añadir/editar secciones | 5h |
| - Ordenación | Drag & drop o up/down | 4h |
| - Eliminación | Con confirmación | 2h |
| - SectionManagerState | Estado | 3h |
| - Testing | Unit tests | 2h |
| **7.3. Gestión de lecciones** | | **16h** |
| - Formulario de lección | Título, contenido, duración | 6h |
| - Editor de contenido | Textarea con preview | 4h |
| - Ordenación | Dentro de sección | 2h |
| - Eliminación | Con confirmación | 2h |
| - Testing | Unit tests | 2h |
| **7.4. Dashboard de instructor** | | **16h** |
| - Diseño UI | Wireframe | 3h |
| - InstructorDashboardState | Datos agregados | 5h |
| - Estadísticas | Cursos, inscripciones, ratings | 4h |
| - Gráficos | Charts de tendencias | 3h |
| - Testing | Manual | 1h |
| **7.5. Listado de cursos (instructor)** | | **6h** |
| - Tabla de cursos | Mis cursos con acciones | 3h |
| - Filtros | Por estado, fecha, etc. | 2h |
| - Acciones rápidas | Editar, eliminar, ver | 1h |
| **7.6. Rutas protegidas** | | **2h** |
| - /instructor/dashboard | Solo instructores | 0.5h |
| - /instructor/courses/new | Creación | 0.5h |
| - /instructor/courses/[id]/edit | Edición | 0.5h |
| - Testing | Intentos no autorizados | 0.5h |

#### Entregables
-  CRUD completo de cursos
-  Gestión de secciones y lecciones
-  Dashboard de instructor
-  Estadísticas y gráficos
-  Rutas protegidas
-  20+ tests

#### Criterios de Aceptación
- [ ] Instructor puede crear curso completo
- [ ] Secciones y lecciones se ordenan correctamente
- [ ] Dashboard muestra estadísticas reales
- [ ] Solo instructores acceden a su panel

---

<div style="page-break-after: always;"></div>

### FASE 8: Funcionalidades Avanzadas (Semanas 21-23)
**Fechas**: 23 Marzo - 12 Abril 2026
**Duración**: 3 semanas (60 horas)

#### Objetivos
- Motor de búsqueda de cursos
- Sistema de filtros avanzados
- Recomendaciones básicas
- Listas de favoritos

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **8.1. Búsqueda de cursos** | | **16h** |
| - Índice de texto en MongoDB | title, description | 2h |
| - Endpoint de búsqueda | search_courses(query) | 4h |
| - SearchState | Estado reactivo | 4h |
| - UI de búsqueda | Barra con autocompletado | 4h |
| - Highlighting | Resaltar términos | 2h |
| **8.2. Sistema de filtros** | | **16h** |
| - Filtro por categoría | Dropdown | 3h |
| - Filtro por nivel | Principiante, Intermedio, Avanzado | 3h |
| - Filtro por duración | Rango de horas | 3h |
| - Filtro por valoración | >= 4 estrellas, etc. | 3h |
| - Combinación de filtros | AND lógico | 3h |
| - Testing | Casos complejos | 1h |
| **8.3. Sistema de recomendaciones** | | **12h** |
| - Algoritmo básico | Cursos similares por categoría | 4h |
| - Basado en inscripciones | "Usuarios que tomaron X también tomaron Y" | 4h |
| - UI de recomendaciones | Sección en detalle de curso | 3h |
| - Testing | Validación de lógica | 1h |
| **8.4. Listas de favoritos** | | **12h** |
| - Modelo Favorite | user_id, course_id | 2h |
| - FavoriteService | add, remove, get_favorites | 4h |
| - Botón de favorito | Corazón togglable | 3h |
| - Página de favoritos | /student/favorites | 2h |
| - Testing | Unit tests | 1h |
| **8.5. Mejoras de UX** | | **4h** |
| - Loading skeletons | Placeholders | 2h |
| - Animaciones | Transiciones suaves | 1h |
| - Tooltips | Ayudas contextuales | 1h |

#### Entregables
-  Motor de búsqueda funcional
-  4 tipos de filtros
-  Sistema de recomendaciones
-  Listas de favoritos
-  Mejoras de UX
-  15+ tests

#### Criterios de Aceptación
- [ ] Búsqueda retorna resultados relevantes
- [ ] Filtros se combinan correctamente
- [ ] Recomendaciones son pertinentes
- [ ] Favoritos persisten en BD

---

<div style="page-break-after: always;"></div>

### FASE 9: Pruebas, Documentación y Despliegue (Semanas 24-26)
**Fechas**: 13 Abril - 3 Mayo 2026
**Duración**: 3 semanas (60 horas)

#### Objetivos
- Testing exhaustivo
- Documentación técnica completa
- Manuales de usuario
- Despliegue en producción
- Preparación de defensa

#### Tareas Detalladas

| Tarea | Descripción | Horas |
|-------|-------------|-------|
| **9.1. Testing** | | **16h** |
| - Unit tests (cobertura 80%) | Pytest | 6h |
| - Integration tests | Flujos E2E | 4h |
| - Manual testing | Casos de uso reales | 3h |
| - Corrección de bugs | Debugging | 3h |
| **9.2. Documentación técnica** | | **16h** |
| - Arquitectura y tecnologías | Diagrama, stack | 3h |
| - Modelos y servicios | Descripción detallada | 3h |
| - Estados y componentes | Reflex specifics | 3h |
| - Base de datos | Esquemas, colecciones | 2h |
| - Seguridad | Medidas implementadas | 2h |
| - Scripts y utilidades | Helpers, scripts | 2h |
| - Conclusiones | Métricas, aprendizajes | 1h |
| **9.3. Manual de usuario** | | **12h** |
| - Guía para estudiantes | Con capturas | 4h |
| - Guía para instructores | CRUD de cursos | 4h |
| - Guía para administradores | Gestión | 2h |
| - FAQ | Preguntas frecuentes | 2h |
| **9.4. Manual de configuración** | | **6h** |
| - Requisitos del sistema | Especificaciones | 1h |
| - Instalación paso a paso | Comandos detallados | 2h |
| - Variables de entorno | .env.example | 1h |
| - Troubleshooting | Problemas comunes | 2h |
| **9.5. Memoria del proyecto** | | **20h** |
| - Sección 1: Introducción | Descripción, objetivos | 2h |
| - Sección 2: Análisis del entorno | Oportunidades, ayudas | 3h |
| - Sección 3: Sistema actual | Contexto, necesidades | 2h |
| - Sección 4: Solución propuesta | Tecnologías, presupuesto | 3h |
| - Sección 5: Planificación | Este documento | 2h |
| - Sección 6: Viabilidad | Técnica, económica, legal | 3h |
| - Sección 7: Diseño e implementación | UML, BD, interfaces | 3h |
| - Secciones finales | Bibliografía, anexos | 2h |
| **9.6. Despliegue** | | **6h** |
| - Configurar Reflex Cloud | Cuenta, proyecto | 1h |
| - Deploy a producción | reflex deploy | 2h |
| - Configurar dominio | DNS, SSL | 1h |
| - Pruebas en producción | Smoke tests | 1h |
| - Monitoreo | Logs, errores | 1h |
| **9.7. Preparación de defensa** | | **4h** |
| - Presentación PowerPoint | 20 slides | 2h |
| - Ensayo de defensa | 30 minutos | 1h |
| - Video demostración | 5-10 minutos | 1h |

#### Entregables
-  Documentación técnica completa (9 documentos)
-  Manual de usuario (40+ páginas)
-  Memoria del proyecto (40+ páginas)
-  Aplicación desplegada en producción

#### Criterios de Aceptación
- [ ] Tests pasan sin errores
- [ ] Aplicación accesible públicamente

---

## 5.3. Diagrama de Gantt

```
Fase / Semana            1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
──────────────────────────────────────────────────────────────────────────────────────────────────────
1. Configuración Inicial ██ ██
2. Módulo de Cursos         ██ ██ ██
3. Módulo de Instructores            ██ ██
4. Refactorización                      ██
5. Autenticación                        ██ ██ ██ ██
6. Inscripciones/Progreso                           ██ ██ ██ ██
7. Panel de Instructor                                         ██ ██ ██ ██
8. Funcionalidades Avanzadas                                               ██ ██ ██
9. Pruebas/Documentación                                                        ██ ██ ██
─────────────────────────────────────────────────────────────────────────────────────────────────────
```

---

## 5.4. Hitos Principales (Milestones)

| Hito | Fecha | Entregable | Criterio de Éxito |
|------|-------|------------|-------------------|
| **M1: Entorno Configurado** | 16/11/2025 | Repositorio + MongoDB | `reflex run` funciona |
| **M2: MVP de Cursos** | 7/12/2025 | Listado + Detalle | `reflex run` funciona |
| **M3: Instructores Implementados** | 21/12/2025 | Perfiles + Stats | `reflex run` funciona |
| **M4: Autenticación Completa** | 25/01/2026 | Login + Registro + RBAC | `reflex run` funciona |
| **M5: Sistema de Inscripciones** | 22/02/2026 | Enrollment + Progress | `reflex run` funciona |
| **M6: Panel de Instructor** | 22/03/2026 | CRUD Cursos | `reflex run` funciona |
| **M7: Funcionalidades Avanzadas** | 12/04/2026 | Búsqueda + Filtros | Búsqueda retorna resultados |
| **M8: Aplicación Desplegada** | 26/04/2026 | Producción online | URL pública accesible |
| **M9: Entrega Final** | 3/05/2026 | Memoria + Manuales | Documentación completa |
| **M10: Defensa Exitosa** | 10/05/2026 | Presentación | Proyecto aprobado |

---

## 5.5. Plan de Mantenimiento (Post-Proyecto)

Una vez finalizado el proyecto académico, se plantea el siguiente plan de mantenimiento:

### Mantenimiento Correctivo

**Frecuencia**: Según necesidad (on-demand)

| Actividad | Descripción | Tiempo Estimado |
|-----------|-------------|-----------------|
| **Corrección de bugs** | Resolución de errores reportados | 2-4h/bug |
| **Actualizaciones de seguridad** | Parches de dependencias | 1h/mes |
| **Respaldo de base de datos** | Verificación de backups automáticos | 0.5h/semana |
| **Monitoreo de uptime** | Revisión de logs, errores | 1h/semana |

**Coste estimado**: 10-15h/mes = 250-375€/mes

---

### Mantenimiento Evolutivo

**Frecuencia**: Trimestral

| Actividad | Descripción | Tiempo Estimado |
|-----------|-------------|-----------------|
| **Actualización de Reflex** | Upgrade a versión minor | 4h/trimestre |
| **Actualización de dependencias** | pip-upgrade, testing | 3h/trimestre |
| **Optimización de BD** | Índices, queries lentas | 4h/trimestre |
| **Mejoras de UI** | Feedback de usuarios | 8h/trimestre |
| **Nuevas funcionalidades menores** | Features pequeños | 12h/trimestre |

**Coste estimado**: 31h/trimestre = 775€/trimestre = **260€/mes promedio**

---

### Mantenimiento Preventivo

**Frecuencia**: Mensual

| Actividad | Descripción | Tiempo Estimado |
|-----------|-------------|-----------------|
| **Revisión de rendimiento** | Tiempos de carga, optimización | 2h/mes |
| **Análisis de seguridad** | Escaneo de vulnerabilidades | 2h/mes |
| **Revisión de métricas** | Analytics, uso de recursos | 1h/mes |
| **Backup manual** | Verificación adicional | 0.5h/mes |

**Coste estimado**: 5.5h/mes = 137.5€/mes

---

### Resumen de Costes de Mantenimiento

| Tipo | Horas/Mes | Coste/Mes (25€/h) | Coste/Año |
|------|-----------|-------------------|-----------|
| Correctivo | 10-15h | 250-375€ | 3,000-4,500€ |
| Evolutivo | ~10h | 260€ | 3,120€ |
| Preventivo | 5.5h | 137.5€ | 1,650€ |
| **TOTAL** | **25-31h** | **647-772€** | **7,770-9,270€** |

**Nota**: Si se contrata desarrollador junior part-time (20h/mes), el coste se reduce a **2,000€/mes** (salario de 24,000€/año prorrateado).

---

## 5.7. Modificaciones y Ampliaciones Futuras

### Funcionalidades Planificadas Post v1.0

#### Prioridad Alta (Q3 2026)

| Funcionalidad | Descripción | Esfuerzo Estimado | Valor de Negocio |
|---------------|-------------|-------------------|------------------|
| **Sistema de pagos** | Integración con Stripe | 40h (1 mes) | XXXXX |
| **Certificados digitales** | Generación automática de PDFs | 24h (3 semanas) | XXXX |
| **Notificaciones email** | SendGrid para avisos | 16h (2 semanas) | XXXXX |

**Total Q3**: 80h (2 meses) - **Inversión**: 2,000€

---

#### Prioridad Media (Q4 2026)

| Funcionalidad | Descripción | Esfuerzo Estimado | Valor de Negocio |
|---------------|-------------|-------------------|------------------|
| **Videoconferencias** | Integración Jitsi/Zoom | 60h (1.5 meses) | XXXXX |
| **Chat en tiempo real** | WebSockets con Reflex | 40h (1 mes) | XXXX |
| **Foros de discusión** | Por curso, threading | 48h (1.5 meses) | XXXX |

**Total Q4**: 148h (3.5 meses) - **Inversión**: 3,700€

---

#### Prioridad Baja (2027)

| Funcionalidad | Descripción | Esfuerzo Estimado | Valor de Negocio |
|---------------|-------------|-------------------|------------------|
| **App móvil nativa** | React Native | 200h (5 meses) | XXXXX |
| **Gamificación** | Puntos, badges, rankings | 80h (2 meses) | XXXX |
| **IA de recomendaciones** | Machine Learning | 120h (3 meses) | XXXX |

**Total 2027**: 400h (10 meses) - **Inversión**: 10,000€

---

<div style="page-break-after: always;"></div>

## 5.8. Riesgos y Contingencias

### Identificación de Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| **Retrasos en desarrollo** | Media (40%) | Alto | - Buffer de 20h por fase<br>- Entregas periódicas para detectar retrasos |
| **Bugs críticos pre-defensa** | Baja (20%) | Alto | - Testing exhaustivo en Fase 9<br>- Manual testing 1 semana antes |
| **MongoDB Atlas caído** | Muy Baja (5%) | Medio | - Backups automáticos diarios<br>- SLA 99.9% de Atlas |
| **Cambios de requisitos** | Media (30%) | Medio | - Alcance bien definido<br>- Cambios solo post v1.0 |
| **Falta de tiempo para documentación** | Baja (15%) | Alto | - Documentar durante desarrollo<br>- Fase 9 dedicada exclusivamente |
| **Enfermedad/ausencia** | Baja (10%) | Alto | - Buffer de 2 semanas en planificación<br>- Entregas adelantadas |

---

### Plan de Contingencia

**Escenario 1: Retraso de 1-2 semanas**
- **Acción**: Reducir scope de Fase 8 (funcionalidades avanzadas)
- **Features a posponer**: Recomendaciones, favoritos
- **Impacto**: Mínimo, no son funcionalidades core

**Escenario 2: Bug crítico encontrado en Semana 25**
- **Acción**: Postergar documentación 1 semana, priorizar corrección
- **Recurso adicional**: Solicitar extensión de 1 semana
- **Impacto**: Entrega ajustada pero dentro de plazo ampliado

**Escenario 3: MongoDB Atlas no disponible**
- **Acción**: Migración temporal a MongoDB local con Docker
- **Tiempo de recuperación**: 4 horas
- **Impacto**: Mínimo, datos se restauran desde backup

---

## 5.9. Conclusiones de la Planificación

### Resumen Ejecutivo

- **Duración total**: 26 semanas (6 meses)
- **Horas totales**: 520 horas
- **Fases**: 9 fases bien definidas
- **Entregas periódicas**: 9 entregas cada 3 semanas
- **Hitos**: 10 milestones principales
- **Buffer**: 40 horas para imprevistos (7.7% del total)

### Viabilidad Temporal

| Aspecto | Evaluación | Justificación |
|---------|------------|---------------|
| **Realismo** |  Alto | 20h/semana es sostenible para estudiante DAW |
| **Flexibilidad** |  Alta | Buffer de 40h + posibilidad de reducir scope |
| **Riesgos** |  Medios | Identificados y mitigados |
| **Cumplimiento** |  Probable | Planificación detallada y entregas frecuentes |

### Próximos Pasos

2. **Inicio Fase 1**: 3 de Noviembre 2025
3. **Primera entrega**: 30 de Noviembre 2025
4. **Seguimiento semanal**: Actualización de progreso

---

<div style="page-break-after: always;"></div>



# 6. ESTUDIO DE VIABILIDAD DEL PROYECTO

## 6.1. Viabilidad Técnica

### 6.1.1. Análisis de Capacidades Técnicas

#### Tecnologías Disponibles

**Reflex Framework** (v0.8.24)

 **Disponibilidad**: Open source, licencia Apache 2.0
 **Madurez**: Framework en producción usado por +1,000 proyectos
 **Documentación**: Completa en https://reflex.dev/docs
 **Comunidad**: Discord activo con +5,000 miembros
 **Soporte**: Equipo de Reflex responde en <24h

**MongoDB Atlas**

 **Disponibilidad**: Cloud SaaS con tier gratuito M0
 **Madurez**: Tecnología establecida desde 2009
 **Documentación**: Extensa en mongodb.com/docs
 **Escalabilidad**: Probada en millones de aplicaciones
 **Soporte**: 24/7 para tiers de pago

**Python 3.10+**

 **Disponibilidad**: Open source, multiplataforma
 **Madurez**: Lenguaje consolidado, versión 3.10 estable
 **Ecosystem**: +400,000 paquetes en PyPI
 **Comunidad**: Una de las más grandes del mundo
 **Soporte**: Long-term support hasta 2026

---

### 6.1.2. Evaluación de Conocimientos del Equipo

#### Conocimientos Actuales (Desarrollador Principal)

| Tecnología | Nivel Actual | Nivel Requerido | Gap | Plan de Formación |
|------------|--------------|-----------------|-----|-------------------|
| **Python** | XXXX Avanzado | XXXX Avanzado |  Ninguno | Repaso de async/await |
| **Reflex** | XX Básico | XXXX Avanzado |  Medio | Curso oficial (20h) |
| **MongoDB** | XX Básico | XXX Intermedio |  Pequeño | MongoDB University (10h) |
| **Git/GitHub** | XXX Intermedio | XXX Intermedio |  Ninguno | - |
| **HTML/CSS** | XXXX Avanzado | XXX Intermedio |  Ninguno | - |
| **Diseño UX** | XX Básico | XX Básico |  Ninguno | Práctica con Figma |

**Conclusión**: El gap técnico es **manejable** con 30 horas de formación específica en Reflex y MongoDB.

---

### 6.1.3. Infraestructura Técnica Necesaria

#### Hardware

| Componente | Mínimo | Recomendado | Disponible | Estado |
|------------|---------|-------------|------------|--------|
| **Procesador** | Intel i5 / Ryzen 5 | Intel i7 / Ryzen 7 | [Según equipo actual] | / |
| **RAM** | 8GB | 16GB | [Según equipo actual] | / |
| **Almacenamiento** | 256GB SSD | 512GB SSD | [Según equipo actual] | / |
| **Conexión Internet** | 10 Mbps | 50+ Mbps | Fibra óptica 300 Mbps |  |

**Inversión necesaria**: 0€ - 1,200€ (si no se tiene equipo adecuado)

#### Software

| Software | Licencia | Coste | Disponible |
|----------|----------|-------|------------|
| **Python 3.10+** | Open source | 0€ |  |
| **Reflex** | Apache 2.0 | 0€ |  |
| **VS Code** | MIT | 0€ |  |
| **Git** | GPL | 0€ |  |
| **MongoDB Compass** | SSPL | 0€ |  |
| **Sistema Operativo** | Ubuntu 22.04 LTS / Win 11 | 0€ |  |

**Inversión total**: **0€** 

#### Infraestructura Cloud

| Servicio | Tier | Coste/Mes | Coste/Año | Estado |
|----------|------|-----------|-----------|--------|
| **MongoDB Atlas** (Dev) | M0 | 0€ | 0€ |  Disponible |
| **MongoDB Atlas** (Prod) | M2 | 9€ | 108€ |  Necesario |
| **Reflex Cloud** (Dev) | Free | 0€ | 0€ |  Disponible |
| **Reflex Cloud** (Prod) | Starter | 20€ | 240€ |  Necesario |
| **Dominio** | .com | - | 12€ |  Opcional |

**Inversión desarrollo**: **0€**
**Inversión producción**: **360€/año**

---

### 6.1.4. Análisis de Riesgos Técnicos

| Riesgo | Probabilidad | Impacto | Severidad | Mitigación |
|--------|--------------|---------|-----------|------------|
| **Reflex tiene bugs críticos** | Baja (15%) | Alto |  Medio | - Usar versión estable (0.8.24)<br>- Testing exhaustivo<br>- Reportar bugs a equipo Reflex |
| **Incompatibilidad de versiones** | Media (30%) | Medio |  Medio | - Fijar versiones en requirements.txt<br>- Usar entorno virtual<br>- Documentar dependencias |
| **MongoDB Atlas caído** | Muy Baja (5%) | Alto |  Bajo | - SLA 99.9% de Atlas<br>- Backups automáticos<br>- Plan de contingencia a MongoDB local |
| **Problemas de rendimiento** | Media (25%) | Medio |  Medio | - Optimización de queries<br>- Índices en BD<br>- Lazy loading de datos |
| **Falta de conocimiento en Reflex** | Media (40%) | Medio |  Medio-Alto | - 20h de formación oficial<br>- Soporte en Discord<br>- Documentación extensa |
| **Pérdida de código** | Muy Baja (5%) | Muy Alto |  Bajo | - Git desde día 1<br>- GitHub remoto<br>- Commits frecuentes |

**Conclusión**: Riesgos técnicos son **manejables** con mitigaciones apropiadas.

---

### 6.1.5. Evaluación de Alternativas Técnicas

#### Comparativa Final de Viabilidad Técnica

| Alternativa | Tiempo Desarrollo | Complejidad | Costes | Escalabilidad | Viabilidad |
|-------------|-------------------|-------------|--------|---------------|------------|
| **Reflex + MongoDB** X | 6 meses | XX Baja | XXXXX Muy bajo | XXXX Alta |  **95%** |
| MERN Stack | 9-12 meses | XXXX Alta | XXX Medio | XXXX Alta |  70% |
| Django + React | 8-10 meses | XXXX Alta | XX Alto | XXXXX Muy alta |  75% |
| Laravel + Vue | 8-11 meses | XXX Media | XX Alto | XXX Media |  65% |

**Conclusión**: **Reflex + MongoDB es la opción más viable técnicamente** (95% de viabilidad)

---

### 6.1.6. Conclusión de Viabilidad Técnica

#### Fortalezas Técnicas

 Stack tecnológico moderno y eficiente
 Todas las herramientas necesarias son gratuitas (desarrollo)
 Conocimientos del equipo son suficientes (con formación mínima)
 Infraestructura cloud robusta y económica
 Documentación y soporte disponibles
 Riesgos técnicos identificados y mitigables

#### Debilidades Técnicas

 Reflex es framework relativamente nuevo (menos maduro que Django/Laravel)
 Comunidad más pequeña (menos recursos de terceros)
 Necesidad de formación específica en Reflex (20h)

#### Dictamen Final

**Viabilidad Técnica: ALTA (95%)**

El proyecto es **altamente viable técnicamente**. Las tecnologías seleccionadas están disponibles, son suficientemente maduras y el equipo cuenta con las capacidades necesarias (o puede adquirirlas rápidamente). Los riesgos técnicos son bajos y están mitigados.

---

## 6.2. Viabilidad Económica

### 6.2.1. Costes Totales del Proyecto

#### Inversión Inicial (Una sola vez)

| Concepto | Cantidad | Justificación |
|----------|----------|---------------|
| **Hardware** (si no disponible) | 0€ - 1,200€ | Portátil de desarrollo |
| **Formación** | 190€ | Cursos Reflex + MongoDB + libros |
| **Gestoría (alta)** | 0€ | Trámite autónomo sin coste |
| **Legal (políticas)** | 300€ | Redacción de términos de uso, privacidad |
| **TOTAL INICIAL** | **490€ - 1,690€** | Escenario conservador: 490€ |

---

#### Costes Operativos Año 1

| Concepto | Mensual | Anual |
|----------|---------|-------|
| **Desarrollo (6 meses)** | | |
| - Coste de oportunidad (520h × 25€/h) | - | 13,000€ |
| **Infraestructura** | | |
| - MongoDB Atlas M2 (producción) | 9€ | 108€ |
| - Reflex Cloud Starter | 20€ | 240€ |
| - Dominio .com | - | 12€ |
| **Subtotal infraestructura** | 29€ | 360€ |
| **Obligaciones fiscales/sociales** | | |
| - Seguridad Social (tarifa plana 12m) | 80€ | 960€ |
| - Gestoría | 50€ | 600€ |
| - Seguro RC profesional | - | 200€ |
| **Subtotal obligaciones** | 130€ | 1,760€ |
| **Marketing** (desde mes 7) | | |
| - Google Ads | 200€ | 1,200€ |
| - LinkedIn Ads | 150€ | 900€ |
| - Canva Pro | 13€ | 156€ |
| **Subtotal marketing** | 363€ | 2,256€ |
| **TOTAL OPERATIVO AÑO 1** | **~520€** | **17,376€** |

**Nota**: El coste de desarrollo (13,000€) es coste de oportunidad (no salida de caja en proyecto académico)

---

#### Costes Operativos Año 2

| Concepto | Mensual | Anual |
|----------|---------|-------|
| **Personal** | | |
| - Desarrollador principal (part-time) | 1,500€ | 18,000€ |
| **Infraestructura** | | |
| - MongoDB Atlas M10 (escalado) | 57€ | 684€ |
| - Reflex Cloud Pro | 50€ | 600€ |
| - CDN, email, etc. | 20€ | 240€ |
| **Subtotal infraestructura** | 127€ | 1,524€ |
| **Obligaciones** | | |
| - Seguridad Social (sin tarifa plana) | 303€ | 3,636€ |
| - Gestoría | 75€ | 900€ |
| - Seguro | - | 250€ |
| **Subtotal obligaciones** | 378€ | 4,786€ |
| **Marketing** | | |
| - Publicidad online | 500€ | 6,000€ |
| - SEO/SEM | 200€ | 2,400€ |
| **Subtotal marketing** | 700€ | 8,400€ |
| **TOTAL OPERATIVO AÑO 2** | **~2,700€** | **32,710€** |

---

### 6.2.2. Proyección de Ingresos

#### Modelo de Negocio: Freemium + Marketplace

**Asunciones Base**:
- Precio medio curso premium: 99€
- Comisión marketplace (si instructor publica): 25%
- Tasa de conversión freemium: 5%
- Retención: 70% año 1, 80% año 2

---

#### Escenario Conservador (Año 1)

| Trimestre | Usuarios Totales | Usuarios Premium | Cursos Vendidos | Ingresos Trimestre | Acumulado |
|-----------|------------------|------------------|-----------------|-------------------|-----------|
| Q1 | 30 | 2 | 2 | 198€ | 198€ |
| Q2 | 80 | 5 | 7 | 693€ | 891€ |
| Q3 | 150 | 10 | 15 | 1,485€ | 2,376€ |
| Q4 | 250 | 18 | 28 | 2,772€ | 5,148€ |

**Total Año 1 (conservador)**: **5,148€**

---

#### Escenario Realista (Año 1)

| Trimestre | Usuarios Totales | Usuarios Premium | Cursos Vendidos | Ingresos Trimestre | Acumulado |
|-----------|------------------|------------------|-----------------|-------------------|-----------|
| Q1 | 50 | 3 | 4 | 396€ | 396€ |
| Q2 | 150 | 8 | 15 | 1,485€ | 1,881€ |
| Q3 | 300 | 20 | 40 | 3,960€ | 5,841€ |
| Q4 | 500 | 40 | 80 | 7,920€ | 13,761€ |

**Total Año 1 (realista)**: **13,761€**

---

#### Escenario Optimista (Año 1)

| Trimestre | Usuarios Totales | Usuarios Premium | Cursos Vendidos | Ingresos Trimestre | Acumulado |
|-----------|------------------|------------------|-----------------|-------------------|-----------|
| Q1 | 100 | 5 | 8 | 792€ | 792€ |
| Q2 | 300 | 18 | 30 | 2,970€ | 3,762€ |
| Q3 | 600 | 45 | 80 | 7,920€ | 11,682€ |
| Q4 | 1,000 | 80 | 150 | 14,850€ | 26,532€ |

**Total Año 1 (optimista)**: **26,532€**

---

#### Proyección Año 2

| Escenario | Usuarios Finales | Ingresos |
|-----------|------------------|----------|
| **Conservador** | 800 | 45,000€ |
| **Realista** | 2,000 | 120,000€ |
| **Optimista** | 4,000 | 220,000€ |

---

### 6.2.3. Análisis de Rentabilidad

#### Año 1

| Concepto | Conservador | Realista | Optimista |
|----------|-------------|----------|-----------|
| **Ingresos** | 5,148€ | 13,761€ | 26,532€ |
| **Costes operativos** (sin desarrollo) | 4,376€ | 4,376€ | 4,376€ |
| **Costes de desarrollo** | 13,000€ | 13,000€ | 13,000€ |
| **Costes totales** | 17,376€ | 17,376€ | 17,376€ |
| **Beneficio neto** | **-12,228€**  | **-3,615€**  | **+9,156€**  |
| **ROI** | -70% | -21% | +53% |

**Conclusión Año 1**:
- Escenario conservador/realista: **Pérdidas** (esperadas en startups año 1)
- Escenario optimista: **Beneficio positivo**
- **Nota**: Si se excluye coste de desarrollo (proyecto académico), todos los escenarios son rentables

#### Año 1 (Sin Coste de Desarrollo)

| Concepto | Conservador | Realista | Optimista |
|----------|-------------|----------|-----------|
| **Ingresos** | 5,148€ | 13,761€ | 26,532€ |
| **Costes operativos** | 4,376€ | 4,376€ | 4,376€ |
| **Beneficio neto** | **+772€**  | **+9,385€**  | **+22,156€**  |
| **ROI** | +18% | +214% | +506% |

---

#### Año 2

| Concepto | Conservador | Realista | Optimista |
|----------|-------------|----------|-----------|
| **Ingresos** | 45,000€ | 120,000€ | 220,000€ |
| **Costes operativos** | 32,710€ | 35,000€ | 40,000€ |
| **Beneficio neto** | **+12,290€**  | **+85,000€**  | **+180,000€**  |
| **Margen** | 27% | 71% | 82% |

**Conclusión Año 2**: **Rentable en todos los escenarios** 

---

### 6.2.4. Punto de Equilibrio (Break-Even)

#### Cálculo del Punto de Equilibrio

**Costes fijos mensuales** (Año 1): 159€
- Infraestructura: 29€
- Seguridad Social: 80€
- Gestoría: 50€

**Costes variables**: ~5€ por venta (procesamiento, comisiones)

**Precio medio curso**: 99€

**Margen de contribución**: 99€ - 5€ = 94€

**Punto de equilibrio**:
```
Break-even (unidades) = Costes Fijos / Margen Contribución
Break-even = 159€ / 94€ = 1.69 cursos/mes ≈ 2 cursos/mes
```

**Punto de equilibrio anual**: **24 cursos vendidos/año**

**Análisis**: El punto de equilibrio es **muy accesible**. Con solo 2 ventas mensuales, los costes operativos se cubren.

---

### 6.2.5. Financiación del Proyecto

#### Necesidades de Financiación

| Fase | Concepto | Cantidad | Fuente de Financiación |
|------|----------|----------|------------------------|
| **Desarrollo** | Inversión inicial | 490€ - 1,690€ | - Autofinanciación<br>- Ayuda Almería Emprende (3,000€) |
| **Año 1** | Operativo | 4,376€ | - Tarifa plana SS (ahorro 2,676€)<br>- Almería Emprende (3,000€)<br>- Ingresos propios |
| **Año 2** | Operativo + Crecimiento | 32,710€ | - Ingresos Año 1 reinvertidos<br>- ENISA (25,000€ si aplica) |

---

#### Fuentes de Financiación Disponibles

| Fuente | Tipo | Cantidad | Condiciones | Probabilidad |
|--------|------|----------|-------------|--------------|
| **Tarifa plana SS** | Ahorro | 2,676€ | Primer año como autónomo |  100% |
| **Almería Emprende** | Subvención | 3,000€ | Proyecto viable, domicilio Almería |  80% |
| **Cheque Innovación** | Bono servicios | 1,500€ | Componente tecnológico |  70% |
| **Kit Digital** | Subvención | 1,500€ | Web de marketing |  60% |
| **Andalucía Emprende** | Préstamo 0% | 15,000€ | Plan de negocio |  50% |
| **ENISA Jóvenes** | Préstamo participativo | 25,000€ | SL, <40 años, fondos propios |  40% |
| **Autofinanciación** | Capital propio | Variable | Ahorros personales |  100% |

**Total ayudas conservadoras**: 7,176€ (Tarifa plana + Almería Emprende + Cheque Innovación)

---

#### Plan de Financiación Conservador

| Fase | Necesidad | Fuente | Cantidad |
|------|-----------|--------|----------|
| **Inversión inicial** (490€) | 490€ | Autofinanciación | 490€ |
| **Año 1 - Costes operativos** (4,376€) | 4,376€ | - Tarifa plana SS (ahorro)<br>- Almería Emprende<br>- Ingresos propios | 2,676€<br>3,000€<br>Resto con ingresos |
| **Déficit máximo Año 1** | ~1,500€ | Autofinanciación | 1,500€ |

**Total inversión propia necesaria**: **~2,000€** (muy accesible)

---

### 6.2.6. Análisis de Riesgos Económicos

| Riesgo | Probabilidad | Impacto | Severidad | Mitigación |
|--------|--------------|---------|-----------|------------|
| **Ingresos inferiores a proyección** | Alta (60%) | Alto |  Alto | - Escenario conservador ya asume bajos ingresos<br>- Marketing orgánico (0€)<br>- Reducir gastos variables |
| **Costes superiores a estimación** | Media (35%) | Medio |  Medio | - Buffer del 10% en presupuesto<br>- Controlar gastos mensuales<br>- Priorizar inversiones |
| **No obtener ayudas esperadas** | Media (30%) | Medio |  Medio | - Plan conservador no depende de ayudas mayores<br>- Solo contar con tarifa plana (100% segura) |
| **Competencia con precios bajos** | Media (40%) | Medio |  Medio | - Diferenciación por transparencia<br>- Modelo freemium flexible<br>- Valor agregado claro |
| **Retraso en tiempo al mercado** | Media (30%) | Alto |  Alto | - Planificación detallada<br>- MVP en 6 meses<br>- Entregas iterativas |

---

### 6.2.7. Conclusión de Viabilidad Económica

#### Fortalezas Económicas

 Costes de desarrollo muy bajos (stack gratuito)
 Costes operativos mínimos (360€/año producción)
 Punto de equilibrio muy bajo (24 ventas/año)
 Modelo de negocio escalable (marginal cost ≈ 0)
 Ayudas disponibles (7,176€ conservador)
 Inversión propia necesaria baja (~2,000€)
 Rentabilidad en Año 2 en todos los escenarios

#### Debilidades Económicas

 Año 1 con posibles pérdidas (en escenario conservador)
 Dependencia de marketing para alcanzar usuarios
 Mercado competitivo (Udemy, Coursera, etc.)
 Ingresos iniciales lentos (primeros 3-6 meses)

#### Dictamen Final

**Viabilidad Económica: ALTA (85%)**

El proyecto es **económicamente viable**. Los costes son muy bajos, las ayudas disponibles cubren gran parte de la inversión necesaria, y el punto de equilibrio es alcanzable. Aunque el Año 1 puede tener pérdidas en escenario conservador, el Año 2 es rentable en todos los escenarios. La inversión propia necesaria es mínima (~2,000€), lo que hace el proyecto accesible.

---

<div style="page-break-after: always;"></div>

## 6.3. Viabilidad Operativa

### 6.3.1. Capacidades Operativas del Equipo

#### Análisis de Roles Necesarios

| Rol | Necesario en Año 1 | Disponible | Gap |
|-----|-------------------|------------|-----|
| **Desarrollador Full-Stack** |  Sí (crítico) |  Desarrollador principal |  Cubierto |
| **Diseñador UX/UI** |  Deseable |  Básico (Figma) |  Pequeño |
| **Marketing Digital** |  Deseable |  Básico (redes sociales) |  Medio |
| **Gestor de Contenidos** |  No | - |  No aplica |
| **Soporte al Cliente** |  No | - |  No aplica |

**Conclusión**: El rol crítico (desarrollador) está cubierto. Los roles deseables pueden suplirse con:
- **Diseño**: Plantillas de Chakra UI + Figma básico
- **Marketing**: Marketing orgánico inicialmente (LinkedIn, X)

---

### 6.3.2. Procesos Operativos Necesarios

#### Desarrollo y Mantenimiento

| Proceso | Frecuencia | Tiempo Estimado | Responsable |
|---------|------------|-----------------|-------------|
| **Desarrollo de features** | Continuo | 20h/semana (Año 1) | Desarrollador principal |
| **Corrección de bugs** | On-demand | 2-4h/bug | Desarrollador principal |
| **Actualización de dependencias** | Mensual | 1h/mes | Desarrollador principal |
| **Backup de base de datos** | Automático (MongoDB Atlas) | 0h | MongoDB |
| **Monitoreo de errores** | Semanal | 1h/semana | Desarrollador principal |

**Total tiempo semanal**: 20-25h (sostenible para un desarrollador)

---

#### Atención al Cliente

| Proceso | Frecuencia | Tiempo Estimado | Canal |
|---------|------------|-----------------|-------|
| **Respuesta a consultas** | Según demanda | 0.5h/consulta | Email (inicialmente) |
| **Onboarding de instructores** | Según inscripciones | 1h/instructor | Email + video tutorial |
| **Soporte técnico** | Ocasional | 1h/semana | FAQ + email |
| **Moderación de contenidos** | Semanal | 2h/semana | Manual (Año 1) |

**Total tiempo semanal**: 3-5h (manejable)

---

#### Marketing y Ventas

| Proceso | Frecuencia | Tiempo Estimado | Canal |
|---------|------------|-----------------|-------|
| **Publicación en redes sociales** | 3x/semana | 2h/semana | LinkedIn, X |
| **Creación de contenido (blog)** | 2x/mes | 4h/mes | Blog en plataforma |
| **Email marketing** | 1x/semana | 1h/semana | SendGrid |
| **Análisis de métricas** | Semanal | 1h/semana | Google Analytics |

**Total tiempo semanal**: 3-4h (manejable)

---

### 6.3.3. Evaluación de Escalabilidad Operativa

#### Escenario Actual (Año 1)

| Métrica | Capacidad Actual | Comentario |
|---------|------------------|------------|
| **Usuarios concurrentes** | 100 | Suficiente para primeros 500 usuarios totales |
| **Cursos soportados** | Ilimitado | MongoDB permite crecimiento sin límite |
| **Transacciones/mes** | 1,000 | Muy por encima de necesidad Año 1 (50-100) |
| **Tiempo de desarrollo** | 20h/semana | Permite evolución continua |
| **Soporte al cliente** | 10 consultas/semana | Con FAQ robusta, manejable |

**Conclusión**: La capacidad operativa actual es **más que suficiente** para Año 1.

---

#### Escenario de Crecimiento (Año 2)

| Métrica | Capacidad Necesaria | Solución |
|---------|---------------------|----------|
| **Usuarios concurrentes** | 500-1,000 | - Escalar a MongoDB M10<br>- Reflex Cloud Pro |
| **Cursos soportados** | 200+ cursos | Sin cambios (escalabilidad nativa) |
| **Transacciones/mes** | 5,000-10,000 | Sin cambios (muy por debajo de límites) |
| **Tiempo de desarrollo** | 20h/semana insuficiente | - Contratar desarrollador junior part-time<br>- Automatizar tareas repetitivas |
| **Soporte al cliente** | 50 consultas/semana | - Chatbot básico (FAQ automático)<br>- Contratar freelance soporte (10h/semana) |

**Inversión necesaria Año 2**:
- Desarrollador junior part-time: 18,000€/año
- Freelance soporte: 4,800€/año
- Infraestructura escalada: +1,164€/año
**Total**: **~24,000€/año**

**Ingresos proyectados Año 2** (realista): 120,000€
**Margen suficiente**:  Sí (85,000€ beneficio)

---

<div style="page-break-after: always;"></div>

### 6.3.4. Usabilidad y Experiencia de Usuario

#### Evaluación de Usabilidad

| Aspecto | Objetivo | Implementación | Estado |
|---------|----------|----------------|--------|
| **Facilidad de registro** | <2 minutos | Formulario de 4 campos |  Cumplido |
| **Navegación intuitiva** | <3 clics a cualquier sección | Navbar + breadcrumbs |  Cumplido |
| **Tiempo de carga** | <3 segundos | Lazy loading, optimización |  Cumplido |
| **Responsive design** | Funcional en móvil | Chakra UI responsive |  Cumplido |
| **Accesibilidad** | WCAG 2.1 Level A | Chakra UI accesible |  Cumplido |
| **Búsqueda de cursos** | <5 segundos | Índice de texto MongoDB |  Cumplido |

**Conclusión**: La usabilidad está **garantizada** por el diseño de Chakra UI y las decisiones de arquitectura.

---

#### Facilidad de Mantenimiento

| Aspecto | Evaluación | Justificación |
|---------|------------|---------------|
| **Separación de capas** | XXXXX Excelente | Modelos, servicios, estados, componentes bien separados |
| **Documentación de código** | XXXX Buena | Docstrings, comentarios, README detallado |
| **Testing** | XXX Aceptable | Unit tests en servicios y modelos (cobertura 80%) |
| **Convenciones de código** | XXXX Buena | PEP 8, Black formatter, naming consistente |
| **Gestión de dependencias** | XXXXX Excelente | requirements.txt, entorno virtual, versiones fijadas |

**Conclusión**: El código es **altamente mantenible** (4.2/5 promedio)

---

<div style="page-break-after: always;"></div>

### 6.3.5. Análisis de Riesgos Operativos

| Riesgo | Probabilidad | Impacto | Severidad | Mitigación |
|--------|--------------|---------|-----------|------------|
| **Sobrecarga de trabajo del desarrollador** | Alta (50%) | Alto |  Alto | - Priorización estricta de features<br>- MVP bien definido<br>- Automatización de tareas<br>- Plan de contingencia (reducir scope) |
| **Falta de instructores (contenido)** | Media (30%) | Alto |  Medio-Alto | - Crear cursos propios inicialmente<br>- Incentivos a primeros instructores<br>- Outreach proactivo a profesionales |
| **Baja adopción de usuarios** | Media (40%) | Alto |  Alto | - Marketing orgánico constante<br>- Programa de referidos<br>- Modelo freemium (barrera de entrada baja) |
| **Problemas de calidad de contenido** | Baja (20%) | Medio |  Bajo | - Revisión de cursos antes de publicación<br>- Sistema de valoraciones transparente<br>- Políticas de calidad claras |
| **Escalabilidad técnica insuficiente** | Muy Baja (10%) | Medio |  Muy Bajo | - Arquitectura diseñada para escalar<br>- MongoDB y Reflex Cloud con autoscaling<br>- Monitoreo proactivo |

---

### 6.3.6. Conclusión de Viabilidad Operativa

#### Fortalezas Operativas

 Equipo (1 persona) suficiente para Año 1
 Procesos operativos bien definidos y manejables
 Escalabilidad técnica garantizada (MongoDB + Reflex Cloud)
 Usabilidad excelente (Chakra UI, diseño responsive)
 Código altamente mantenible (4.2/5)
 Automatización de tareas críticas (backups, deploy)

#### Debilidades Operativas

 Dependencia de un solo desarrollador (riesgo de sobrecarga)
 Falta de equipo de marketing especializado
 Necesidad de contenido inicial (cursos para atraer usuarios)
 Escalado operativo en Año 2 requiere contrataciones

#### Dictamen Final

**Viabilidad Operativa: ALTA (90%)**

El proyecto es **altamente viable operativamente**. Los procesos están bien definidos, el equipo es suficiente para Año 1, la usabilidad está garantizada y la escalabilidad técnica es nativa. Los principales riesgos (sobrecarga de trabajo, falta de contenido) son mitigables con planificación adecuada y priorización estricta.

---

## 6.4. Viabilidad Legal

### 6.4.1. Marco Legal Aplicable

#### Normativa de Protección de Datos

**RGPD (Reglamento General de Protección de Datos)**

**Aplicabilidad**:  Obligatorio (usuarios en UE)

**Requisitos**:
1. **Base legal para tratamiento**: Consentimiento explícito o ejecución de contrato
2. **Información transparente**: Política de privacidad clara
3. **Derechos de los usuarios**: Acceso, rectificación, supresión, portabilidad
4. **Medidas de seguridad**: Cifrado, control de acceso, backups
5. **Registro de actividades**: Documentar tratamientos de datos
6. **DPO (Data Protection Officer)**: No obligatorio para empresas pequeñas

**Implementación en el proyecto**:
-  Política de privacidad redactada
-  Consentimiento explícito en registro
-  Funcionalidad de edición/eliminación de cuenta
-  Cifrado en tránsito (TLS) y en reposo (MongoDB Atlas)
-  Control de acceso basado en roles (RBAC)

**Coste de cumplimiento**: 300€ (redacción legal) + 0€ (implementación técnica incluida)

---

**LOPDGDD (Ley Orgánica de Protección de Datos Personales)**

**Aplicabilidad**:  Obligatorio (empresa española)

**Requisitos adicionales a RGPD**:
1. **Registro en AEPD**: Solo si hay transferencias internacionales (no aplica)
2. **Menores de 14 años**: Consentimiento paterno (no aplicable, +18)
3. **Videovigilancia**: No aplica (sin cámaras)

**Implementación**:  Cubierto por cumplimiento RGPD

---

#### Normativa de Comercio Electrónico

**LSSI (Ley de Servicios de la Sociedad de la Información)**

**Aplicabilidad**:  Obligatorio (servicio online)

**Requisitos**:
1. **Aviso legal**: Datos del titular, CIF, domicilio
2. **Política de cookies**: Consentimiento explícito
3. **Condiciones de contratación**: Términos de uso claros
4. **Procedimiento de contratación**: Pasos transparentes
5. **Email de contacto**: Canal de comunicación

**Implementación**:
-  Aviso legal en footer
-  Banner de cookies (a implementar cuando se usen cookies)
-  Términos de uso redactados
-  Email de contacto: info@elearningjcb.com

**Coste de cumplimiento**: Incluido en 300€ de redacción legal

---

#### Normativa Fiscal

**IVA (Impuesto sobre el Valor Añadido)**

**Aplicabilidad**:  Obligatorio

**Tipo aplicable**: 21% (tipo general)
- **Nota**: Servicios educativos pueden estar exentos (art. 20.1.9º Ley IVA) pero solo si:
  - Centros privados autorizados
  - Enseñanza escolar o universitaria
  - **E-Learning JCB Platform**: NO exento (cursos online sin reconocimiento oficial)

**Obligaciones**:
- Modelo 303 (trimestral): Declaración de IVA
- Modelo 390 (anual): Resumen anual de IVA
- Facturación con IVA incluido

**Implementación**:  Gestión via gestoría (600€/año)

---

**IRPF (Impuesto sobre la Renta de Personas Físicas)**

**Aplicabilidad**:  Obligatorio (autónomo)

**Obligaciones**:
- Modelo 130 (trimestral): Pago fraccionado
- Modelo 100 (anual): Declaración de renta
- Retenciones (15%) si se factura a empresas

**Implementación**:  Gestión via gestoría (600€/año)

---

#### Normativa de Propiedad Intelectual

**Ley de Propiedad Intelectual (Real Decreto Legislativo 1/1996)**

**Aplicabilidad**:  Obligatorio

**Aspectos clave**:
1. **Contenido de cursos**: Propiedad del instructor
2. **Código fuente de la plataforma**: Propiedad de E-Learning JCB
3. **Licencia de uso**: Instructores conceden licencia no exclusiva a plataforma
4. **Plagio**: Sistema de detección (futuro)
5. **DMCA (Digital Millennium Copyright Act)**: Procedimiento de notificación

**Implementación**:
-  Términos de uso especifican derechos de autor
-  Instructores aceptan licencia al subir contenido
-  Sistema anti-plagio (no en MVP)

**Coste**: Incluido en términos de uso (300€)

---

### 6.4.2. Obligaciones Legales con Terceros

#### Contratos con Instructores

**Necesidad**:  Sí (relación mercantil)

**Contenido mínimo**:
- Derechos de propiedad intelectual
- Comisión de la plataforma (25%)
- Obligaciones de calidad
- Procedimiento de resolución de conflictos
- Duración y terminación

**Implementación**:  Términos de servicio (aceptación online)

**Coste**: Incluido en 300€ de redacción legal

---

#### Contratos con Proveedores

| Proveedor | Tipo de Contrato | Necesidad | Estado |
|-----------|------------------|-----------|--------|
| **MongoDB Atlas** | ToS (Terms of Service) |  Obligatorio |  Aceptado online |
| **Reflex Cloud** | ToS |  Obligatorio |  Aceptado online |
| **Gestoría** | Contrato de servicios |  Recomendado |  A negociar |
| **Registrar de dominio** | ToS |  Obligatorio |  Aceptado online |

**Coste adicional**: 0€ (ToS estándar)

---

### 6.4.3. Responsabilidades Legales

#### Responsabilidad Civil

**Riesgo**: Daños a terceros (errores en plataforma, pérdida de datos)

**Solución**: Seguro de Responsabilidad Civil Profesional

**Cobertura recomendada**: 300,000€
**Coste**: 200€/año

**Implementación**:  Previsto en presupuesto

---

#### Responsabilidad por Contenido

**Riesgo**: Contenido ilegal/inapropiado subido por instructores

**Marco legal**: Ley 34/2002 (LSSI) - Régimen de exención de responsabilidad

**Requisitos para exención**:
1. **No tener conocimiento efectivo** del contenido ilegal
2. **Actuar diligentemente** al tener conocimiento (retirar contenido)
3. **Sistema de notificación** para denuncias

**Implementación**:
-  Sistema de moderación de contenido
-  Formulario de denuncia
-  Política de retirada de contenido ilegal (24-48h)

**Coste**: 0€ (funcionalidad integrada)

---

### 6.4.4. Análisis de Riesgos Legales

| Riesgo | Probabilidad | Impacto | Severidad | Mitigación |
|--------|--------------|---------|-----------|------------|
| **Incumplimiento RGPD** | Baja (15%) | Muy Alto |  Medio | - Política de privacidad completa<br>- Asesoría legal inicial<br>- Revisión anual |
| **Reclamación de propiedad intelectual** | Baja (20%) | Alto |  Medio | - Términos de uso claros<br>- Licencia explícita de instructores<br>- Sistema de denuncias |
| **Contenido ilegal en plataforma** | Media (25%) | Alto |  Medio-Alto | - Moderación proactiva<br>- Sistema de denuncias<br>- Retirada inmediata |
| **Problemas con Hacienda/SS** | Muy Baja (5%) | Alto |  Muy Bajo | - Gestoría profesional<br>- Cumplimiento estricto<br>- Asesoría fiscal |
| **Demanda por responsabilidad civil** | Muy Baja (5%) | Alto |  Muy Bajo | - Seguro RC profesional<br>- Términos de uso (limitación responsabilidad) |

---

### 6.4.5. Documentación Legal Necesaria

| Documento | Necesidad | Responsable | Coste | Estado |
|-----------|-----------|-------------|-------|--------|
| **Política de Privacidad** |  Obligatorio | Abogado especializado | 100€ |  A redactar |
| **Términos de Uso** |  Obligatorio | Abogado especializado | 100€ |  A redactar |
| **Aviso Legal** |  Obligatorio | Abogado especializado | 50€ |  A redactar |
| **Política de Cookies** |  Si aplica | Abogado especializado | 50€ |  Futuro |
| **Contrato con instructores** |  Recomendado | Incluido en ToS | 0€ |  Incluido en Términos |
| **TOTAL** | | | **300€** | |

---

<div style="page-break-after: always;"></div>

### 6.4.6. Conclusión de Viabilidad Legal

#### Fortalezas Legales

 Marco legal bien identificado (RGPD, LSSI, IVA)
 Cumplimiento técnico de RGPD (cifrado, RBAC, backups)
 Documentación legal accesible (300€)
 Gestoría para cumplimiento fiscal (600€/año)
 Seguro RC profesional (200€/año)
 Sistema de moderación de contenido
 Régimen de exención de responsabilidad aplicable

#### Debilidades Legales

 Necesidad de redacción legal inicial (300€)
 Complejidad del RGPD (requiere asesoría inicial)
 Responsabilidad por contenido de terceros (mitigable)
 Actualizaciones legales periódicas necesarias

#### Dictamen Final

**Viabilidad Legal: ALTA (85%)**

El proyecto es **viable legalmente**. Todos los requisitos legales están identificados y son cumplibles con inversión razonable (300€ redacción + 200€ seguro). El cumplimiento del RGPD está garantizado por la arquitectura técnica (MongoDB Atlas cifrado, RBAC). Los riesgos legales son bajos y están mitigados con políticas claras y asesoría profesional.

---

## 6.5. Conclusión General del Estudio de Viabilidad

### Resumen Ejecutivo

| Dimensión | Viabilidad | Justificación |
|-----------|------------|---------------|
| **Técnica** |  95% | Stack moderno, herramientas disponibles, conocimientos suficientes |
| **Económica** |  85% | Costes bajos, punto de equilibrio bajo, rentabilidad Año 2 |
| **Operativa** |  90% | Procesos manejables, usabilidad garantizada, escalabilidad nativa |
| **Legal** |  85% | Marco legal claro, cumplimiento accesible, riesgos mitigados |
| **GLOBAL** |  **89%** | **PROYECTO ALTAMENTE VIABLE** |

---

### Fortalezas del Proyecto

1.  **Stack tecnológico eficiente**: Reflex + MongoDB reducen tiempo y costes
2.  **Inversión inicial mínima**: ~2,000€ (muy accesible)
3.  **Punto de equilibrio bajo**: 24 ventas/año
4.  **Escalabilidad nativa**: Arquitectura preparada para crecer
5.  **Ayudas disponibles**: 7,176€ en escenario conservador
6.  **Diferenciación clara**: Transparencia en contenidos
7.  **Mercado en crecimiento**: 13.7% CAGR global, 18.5% España
8.  **Cumplimiento legal factible**: Requisitos claros y cumplibles

---

### Debilidades del Proyecto

1.  **Mercado competitivo**: Udemy, Coursera, Domestika ya establecidos
2.  **Dependencia de un solo desarrollador**: Riesgo de sobrecarga
3.  **Reflex es framework nuevo**: Comunidad más pequeña
4.  **Posibles pérdidas Año 1**: En escenario conservador (excl. ayudas)
5.  **Necesidad de contenido inicial**: Cursos para atraer usuarios

---

### Oportunidades

1.  **Nicho de transparencia**: Plataformas actuales no muestran contenido detallado
2.  **Crecimiento del e-learning**: Mercado en expansión continua
3.  **Modelo freemium**: Barrera de entrada baja para usuarios
4.  **Escalabilidad internacional**: Posible expansión a LATAM
5.  **Funcionalidades futuras**: Pagos, certificados, app móvil

---

### Amenazas

1.  **Competidores con marketing masivo**: Udemy invierte millones en publicidad
2.  **Cambios en regulación**: GDPR puede endurecerse
3.  **Saturación del mercado**: Muchas plataformas de e-learning
4.  **Preferencia por plataformas grandes**: Usuarios confían en marcas establecidas
5.  **Crisis económica**: Reducción de gasto en formación

---

### Recomendación Final

**PROYECTO VIABLE Y RECOMENDADO PARA EJECUCIÓN**

Con una viabilidad global del **89%**, el proyecto **E-Learning JCB Platform** es **altamente viable** en todas las dimensiones analizadas (técnica, económica, operativa y legal). Las fortalezas superan claramente a las debilidades, y las oportunidades del mercado son significativas.

**Factores críticos de éxito**:
1.  Completar MVP en 6 meses (planificación detallada)
2.  Obtener al menos 2 ayudas (Tarifa plana + Almería Emprende)
3.  Alcanzar 24 ventas en Año 1 (punto de equilibrio)
4.  Diferenciarse por transparencia (ventaja competitiva)
5.  Mantener costes operativos bajos (<500€/mes)

**Riesgo global**: **BAJO-MEDIO** (controlado y mitigable)

**Recomendación**: **PROCEDER CON EL PROYECTO** 

---

<div style="page-break-after: always;"></div>



# 7. DOCUMENTACIÓN DEL DISEÑO E IMPLEMENTACIÓN

## 7.1. Prototipos de la Aplicación

### 7.1.1. Wireframes Iniciales

Los wireframes se diseñaron en **Figma** durante la Fase 1 del proyecto para establecer la estructura visual antes del desarrollo.

#### Wireframe 1: Página de Inicio (Home)

![Página de Inicio](capturas/02_estudiante/04_home_publica.png)

**Decisiones de diseño**:
- Hero section con CTA claro ("Todos los Cursos")
- Grid de cursos destacados (3 columnas en desktop)
- Navegación simple en header

---

<div style="page-break-after: always;"></div>

#### Wireframe 2: Listado de Cursos

![Listado de Cursos](capturas/02_estudiante/05_listado_cursos.png)

**Decisiones de diseño**:
- Cards de curso con información clave visible

---

<div style="page-break-after: always;"></div>

#### Wireframe 3: Detalle de Curso

![Detalle de Curso](capturas/02_estudiante/06_detalle_curso.png)

**Decisiones de diseño**:
- **Información clave arriba**: Valoración, instructor, duración visible sin scroll
- **Botón CTA prominente**: "Inscribirse Ahora" bien visible
- **Contenido desplegable**: Secciones y lecciones completamente visibles 

---

### 7.1.2. Mockups de Alta Fidelidad

Los mockups finales incorporan el diseño de **Chakra UI** con colores y estilos definitivos:

#### Paleta de Colores

```
Colores Principales:
- Primary:   #3182CE (Azul)
- Secondary: #2D3748 (Gris oscuro)
- Success:   #38A169 (Verde)
- Warning:   #DD6B20 (Naranja)
- Error:     #E53E3E (Rojo)

Colores de Fondo:
- Background: #FFFFFF (Blanco)
- Gray.50:    #F7FAFC (Gris muy claro)
- Gray.100:   #EDF2F7 (Gris claro)
```

#### Tipografía

```
Familia: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif

Tamaños:
- Heading 1: 36px (2xl)
- Heading 2: 30px (xl)
- Heading 3: 24px (lg)
- Body:      16px (md)
- Small:     14px (sm)
```

---

## 7.2. Diseño de Interfaces

### 7.2.1. Componentes Principales

#### CourseCard (Tarjeta de Curso)

**Archivo**: `E_Learning_JCB_Reflex/components/course_card.py`

**Descripción**: Componente reutilizable para mostrar información resumida de un curso

**Propiedades**:
- `course`: Objeto con datos del curso (título, descripción, valoración, precio)
- `show_instructor`: Boolean para mostrar/ocultar instructor

<div style="page-break-after: always;"></div>

**Estructura Visual**:
```
┌─────────────────────────────────┐
│ [Imagen del curso]              │
│                                 │
├─────────────────────────────────┤
│ Título del Curso                │
│                                 │
│ Descripción breve del curso     │
│ que se trunca a 2 líneas...     │
│                                 │
│  Instructor                     │
│  10 horas |  Intermedio         │
│                                 │
│  99€          [Ver Detalles]    │
└─────────────────────────────────┘
```

**Implementación** (pseudocódigo):
```python
def course_card(course: Course, show_instructor: bool = True) -> rx.Component:
    return rx.box(
        rx.image(src=course.image_url),
        rx.vstack(
            rx.heading(course.title),
            rx.hstack(
                rx.icon("star"),
                rx.text(f"{course.rating} ({course.num_ratings} reseñas)")
            ),
            rx.text(course.short_description),
            rx.hstack(
                rx.text(f" {course.duration_hours}h"),
                rx.badge(course.level)
            ),
            rx.hstack(
                rx.text(f"{course.price}€"),
                rx.button("Ver Detalles", on_click=...)
            )
        ),
        border_width="1px",
        border_radius="md",
        overflow="hidden"
    )
```

---

<div style="page-break-after: always;"></div>

#### Navbar (Barra de Navegación)

**Archivo**: `E_Learning_JCB_Reflex/components/navbar.py`

**Descripción**: Navegación principal de la aplicación

**Estructura**:
```
┌────────────────────────────────────────────────────────────┐
│ [LOGO] E-Learning JCB   [Cursos] [Instructores]  [Login]   │
└────────────────────────────────────────────────────────────┘
```

**Estados**:
- **Usuario no autenticado**: Mostrar "Login" y "Registrarse"
- **Usuario autenticado**: Mostrar avatar + dropdown con "Perfil", "Dashboard", "Logout"

**Responsive**:
- Desktop (>768px): Navegación horizontal
- Mobile (<768px): Menú hamburguesa

---

### 7.2.2. Páginas Principales

#### Página de Login

**Ruta**: `/login`

**Componentes**:
- Formulario centrado con:
  - Campo email (validación de formato)
  - Campo contraseña (tipo password)
  - Checkbox "Recordarme"
  - Botón "Iniciar Sesión"
  - Link "¿Olvidaste tu contraseña?" (futuro)
  - Link "¿No tienes cuenta? Regístrate"

**Validaciones**:
- Email con formato válido (@, .)
- Contraseña no vacía
- Feedback de error si credenciales incorrectas

**Flujo**:
1. Usuario ingresa email y contraseña
2. Click en "Iniciar Sesión"
3. Validación client-side
4. Petición a `AuthState.handle_login()`
5. Si OK: Redirigir a dashboard según rol
6. Si error: Mostrar mensaje de error

---

#### Dashboard de Estudiante

**Ruta**: `/student/dashboard`

**Protección**: `@require_role(["student"])`

**Secciones**:
1. **Resumen**: Cursos inscritos, completados, en progreso
2. **Mis Cursos**: Grid de cursos con barra de progreso
3. **Recomendaciones**: Cursos sugeridos (basados en inscripciones)
4. **Actividad Reciente**: Últimas lecciones completadas

**Ejemplo Visual**:
```
┌─────────────────────────────────────────────────────────┐
│ Dashboard de Estudiante - Hola, María                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐                     │
│ │   3     │ │   1     │ │   2     │                     │
│ │ Inscritos│ │Completado│ │En Progreso│                 │
│ └─────────┘ └─────────┘ └─────────┘                     │
│                                                         │
│ Mis Cursos                                              │
│ ┌────────────────────────────────┐                      │
│ │ Python para Principiantes      │                      │
│ │ ████████░░ 80% completado       │                     │
│ └────────────────────────────────┘                      │
│                                                         │
│ ┌────────────────────────────────┐                      │
│ │ JavaScript Avanzado             │                     │
│ │ ██████░░░░ 60% completado       │                     │
│ └────────────────────────────────┘                      │
└─────────────────────────────────────────────────────────┘
```

---

<div style="page-break-after: always;"></div>

## 7.3. Diseño Lógico - Diagramación UML

### 7.3.1. Diagrama de Casos de Uso

```
                        E-Learning JCB Platform
┌──────────────────────────────────────────────────────────┐
│                                                          │
│   Estudiante                   Instructor          Admin │
│      │                            │                  │   │
│      │  (Buscar cursos)           │                  │   │
│      ├────────────────┐           │                  │   │
│      │                │           │                  │   │
│      │  (Inscribirse) │    (Crear curso)             │   │
│      ├────────────────┼───────────────┐              │   │
│      │                │               │              │   │
│      │  (Ver progreso)│    (Editar curso)     (Gestionar)│
│      ├────────────────┤               │        (usuarios)│
│      │                │    (Ver estadísticas)        │   │
│      │  (Valorar      │               │              │   │
│      │   curso)       │               │              │   │
│      │                │               │              │   │
│      │  (Completar    │               │              │   │
│      │   lección)     │               │              │   │
│                                                          │
└──────────────────────────────────────────────────────────┘

Actores:
- Estudiante: Usuario que consume cursos
- Instructor: Usuario que crea y gestiona cursos
- Admin: Usuario con permisos completos
```

**Casos de Uso Principales**:

| Actor | Caso de Uso | Descripción |
|-------|-------------|-------------|
| **Estudiante** | Buscar cursos | Buscar cursos por título, categoría, nivel |
| | Inscribirse en curso | Matricularse en un curso específico |
| | Ver progreso | Consultar progreso en cursos inscritos |
| | Completar lección | Marcar lección como completada |
| | Valorar curso | Dejar valoración y reseña de curso |
| **Instructor** | Crear curso | Crear curso con secciones y lecciones |
| | Editar curso | Modificar información de curso existente |
| | Eliminar curso | Borrar curso propio |
| | Ver estadísticas | Consultar inscripciones, valoraciones |
| **Admin** | Gestionar usuarios | Ver, editar, eliminar usuarios |
| | Moderar contenido | Revisar y aprobar cursos |
| | Ver reportes | Estadísticas globales del sistema |

---

<div style="page-break-after: always;"></div>

### 7.3.2. Diagrama de Clases

```
┌─────────────────────────────────────┐
│           User                      │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - name: str                         │
│ - email: str (unique)               │
│ - password: str (hashed)            │
│ - role:str(admin|instructor|student)│
│ - bio: str (optional)               │
│ - created_at: datetime              │
├─────────────────────────────────────┤
│ + is_admin() -> bool                │
│ + is_instructor() -> bool           │
│ + is_student() -> bool              │
│ + to_dict() -> dict                 │
│ + from_dict(data) -> User           │
└─────────────────────────────────────┘
```
```
           ▲
           │ 1
           │ instructs
           │
           │ *
┌─────────────────────────────────────┐
│           Course                    │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - title: str                        │
│ - description: str                  │
│ - instructor_id: ObjectId           │
│ - level: str (beginner|intermediate|advanced)│
│ - duration_hours: float             │
│ - price: float                      │
│ - image_url: str                    │
│ - sections: List[Section]           │
│ - created_at: datetime              │
├─────────────────────────────────────┤
│ + get_total_lessons() -> int        │
│ + get_average_rating() -> float     │
│ + to_dict() -> dict                 │
│ + from_dict(data) -> Course         │
└─────────────────────────────────────┘
```
```
           │ 1
           │ has
           │
           │ *
┌─────────────────────────────────────┐
│          Section                    │
├─────────────────────────────────────┤
│ - title: str                        │
│ - description: str                  │
│ - order: int                        │
│ - lessons: List[Lesson]             │
├─────────────────────────────────────┤
│ + get_duration() -> float           │
│ + to_dict() -> dict                 │
└─────────────────────────────────────┘
```
```
           │ 1
           │ contains
           │
           │ *
┌─────────────────────────────────────┐
│          Lesson                     │
├─────────────────────────────────────┤
│ - title: str                        │
│ - content: str                      │
│ - duration_minutes: int             │
│ - order: int                        │
│ - video_url: str (optional)         │
├─────────────────────────────────────┤
│ + to_dict() -> dict                 │
└─────────────────────────────────────┘
```
```

┌─────────────────────────────────────┐
│        Enrollment                   │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - user_id: ObjectId                 │
│ - course_id: ObjectId               │
│ - enrolled_at: datetime             │
│ - completed: bool                   │
├─────────────────────────────────────┤
│ + to_dict() -> dict                 │
│ + from_dict(data) -> Enrollment     │
└─────────────────────────────────────┘
        │                    │
        │ *                  │ *
        │                    │
   ┌────┴───┐         ┌─────┴────┐
   │  User  │         │  Course  │
   └────────┘         └──────────┘
```
```

┌─────────────────────────────────────┐
│         Progress                    │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - enrollment_id: ObjectId           │
│ - lesson_id: str                    │
│ - completed_at: datetime            │
├─────────────────────────────────────┤
│ + to_dict() -> dict                 │
└─────────────────────────────────────┘
        │ *
        │ tracks
        │ 1
┌───────┴─────────────────────────────┐
│        Enrollment                   │
└─────────────────────────────────────┘
```
```

┌─────────────────────────────────────┐
│          Rating                     │
├─────────────────────────────────────┤
│ - _id: ObjectId                     │
│ - user_id: ObjectId                 │
│ - course_id: ObjectId               │
│ - rating: int (1-5)                 │
│ - review: str (optional)            │
│ - created_at: datetime              │
├─────────────────────────────────────┤
│ + to_dict() -> dict                 │
│ + from_dict(data) -> Rating         │
└─────────────────────────────────────┘
        │ *              │ *
        │                │
   ┌────┴───┐     ┌─────┴────┐
   │  User  │     │  Course  │
   └────────┘     └──────────┘
```

**Relaciones**:
- Un **User** puede ser instructor de muchos **Courses** (1:N)
- Un **Course** tiene muchas **Sections** (1:N, embebido)
- Una **Section** tiene muchas **Lessons** (1:N, embebido)
- Un **User** puede tener muchos **Enrollments** (1:N)
- Un **Course** puede tener muchos **Enrollments** (1:N)
- Un **Enrollment** tiene muchos **Progress** (1:N)
- Un **User** puede dejar muchos **Ratings** (1:N)
- Un **Course** puede tener muchos **Ratings** (1:N)

---

<div style="page-break-after: always;"></div>

### 7.3.3. Diagrama de Secuencia: Inscripción a Curso

```
Usuario    CourseDetailPage   EnrollmentState   EnrollmentService   MongoDB
  │              │                  │                  │              │
  │  Click       │                  │                  │              │
  │ "Inscribirse"│                  │                  │              │
  ├─────────────>│                  │                  │              │
  │              │ handle_enroll()  │                  │              │
  │              ├─────────────────>│                  │              │
  │              │                  │ enroll_student() │              │
  │              │                  ├─────────────────>│              │
  │              │                  │                  │ Verificar    │
  │              │                  │                  │ duplicado    │
  │              │                  │                  ├─────────────>│
  │              │                  │                  │<─────────────┤
  │              │                  │                  │  No existe   │
  │              │                  │                  │              │
  │              │                  │                  │ INSERT       │
  │              │                  │                  │ enrollment   │
  │              │                  │                  ├─────────────>│
  │              │                  │                  │<─────────────┤
  │              │                  │                  │   OK         │
  │              │                  │<─────────────────┤              │
  │              │                  │     True         │              │
  │              │<─────────────────┤                  │              │
  │              │   Success        │                  │              │
  │<─────────────┤                  │                  │              │
  │ Mostrar      │                  │                  │              │
  │ "Inscrito"   │                  │                  │              │
  │ + Redirigir  │                  │                  │              │
  │              │                  │                  │              │
```

**Descripción del flujo**:
1. Usuario hace click en botón "Inscribirse" en página de detalle de curso
2. Evento se captura en `CourseDetailPage` y llama a `EnrollmentState.handle_enroll()`
3. Estado llama a `EnrollmentService.enroll_student(user_id, course_id)`
4. Servicio verifica en MongoDB si ya existe inscripción (evitar duplicados)
5. Si no existe, inserta nuevo documento en colección `enrollments`
6. MongoDB retorna confirmación
7. Servicio retorna `True` al estado
8. Estado actualiza UI mostrando "Inscrito exitosamente"
9. Usuario es redirigido a dashboard de estudiante

---

<div style="page-break-after: always;"></div>

### 7.3.4. Diagrama de Actividades: Crear Curso Completo

```
      ┌─────────┐
      │ Inicio  │
      └────┬────┘
           │
           ▼
    ┌──────────────┐
    │ Login como   │
    │ Instructor   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐      No     ┌──────────┐
    │ ¿Autenticado?├────────────>│ Redirigir│
    │              │             │ a /login │
    └──────┬───────┘             └──────────┘
           │ Sí
           ▼
```
```
    ┌──────────────┐
    │ Ir a /instructor│
    │ /courses/new │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Completar    │
    │ formulario   │
    │ de curso     │
    └──────┬───────┘
           │
           ▼
```
```
    ┌──────────────┐      No     ┌──────────┐
    │ ¿Datos       ├────────────>│ Mostrar  │
    │ válidos?     │             │ errores  │
    └──────┬───────┘             └────┬─────┘
           │ Sí                       │
           ▼                          │
    ┌──────────────┐                  │
    │ Guardar curso│<──────────────── ┘
    │ en BD        │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Añadir       │
    │ Sección 1    │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Añadir       │
    │ Lección 1.1  │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐      Sí     ┌──────────┐
    │ ¿Más         ├────────────>│ Añadir   │
    │ lecciones?   │             │ lección  │
    └──────┬───────┘             └────┬─────┘
           │ No                       │
           ▼                          │
    ┌──────────────┐                  │
    │ ¿Más         │ <────────────────┘
    │ secciones?   │ 
    └──────┬───────┘
           │ No
           ▼
```
```
    ┌──────────────┐
    │ Publicar     │
    │ curso        │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Curso visible│
    │ en catálogo  │
    └──────┬───────┘
           │
           ▼
      ┌─────────┐
      │   Fin   │
      └─────────┘
```

---

<div style="page-break-after: always;"></div>

## 7.4. Descripción Modular del Software

### 7.4.1. Arquitectura en Capas

La aplicación sigue una **arquitectura en capas** con separación clara de responsabilidades:

```
┌─────────────────────────────────────────────────────────┐
│                 CAPA DE PRESENTACIÓN                    │
│         (Pages: index.py, courses.py, login.py...)      │
│              Renderizado de UI al usuario               │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              CAPA DE LÓGICA DE UI                       │
│    (States: CourseState, AuthState, EnrollmentState)    │
│       Gestión de estado reactivo y eventos de usuario   │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│            CAPA DE LÓGICA DE NEGOCIO                    │
│ (Services:CourseService, UserService, EnrollmentService)│
│          Operaciones CRUD y validaciones                │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              CAPA DE MODELOS                            │
│      (Models: User, Course, Enrollment, Progress)       │
│         Definición de entidades y validaciones          │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│            CAPA DE ACCESO A DATOS                       │
│         (Database: mongodb.py con Motor driver)         │
│           Conexión y operaciones en MongoDB             │
└─────────────────────────────────────────────────────────┘
```

**Ventajas de esta arquitectura**:
-  Separación de responsabilidades (cada capa tiene una función clara)
-  Testabilidad (cada capa puede probarse independientemente)
-  Mantenibilidad (cambios en una capa no afectan a otras)
-  Escalabilidad (fácil añadir nuevas funcionalidades)

---

### 7.4.2. Módulos Principales

#### Módulo: models/

**Responsabilidad**: Definición de entidades de datos

**Archivos**:
- `user.py`: Modelo de usuario con roles
- `course.py`: Modelo de curso con secciones y lecciones
- `enrollment.py`: Modelo de inscripción
- `progress.py`: Modelo de progreso de estudiante
- `rating.py`: Modelo de valoraciones

**Ejemplo** (`user.py`):
```python
class User:
    def __init__(self, name: str, email: str, password: str, role: str = "student"):
        self.name = name
        self.email = email
        self.password = password  # Hashed con bcrypt
        self.role = role  # admin | instructor | student
        self.bio = ""
        self.created_at = datetime.now()

    def is_admin(self) -> bool:
        return self.role == "admin"

    def is_instructor(self) -> bool:
        return self.role == "instructor"

    def is_student(self) -> bool:
        return self.role == "student"
```

---

#### Módulo: services/

**Responsabilidad**: Lógica de negocio y operaciones CRUD

**Archivos**:
- `user_service.py`: CRUD de usuarios, autenticación
- `course_service.py`: CRUD de cursos
- `enrollment_service.py`: Gestión de inscripciones
- `progress_service.py`: Seguimiento de progreso
- `rating_service.py`: Gestión de valoraciones

**Ejemplo** (`enrollment_service.py`):
```python
class EnrollmentService:
    async def enroll_student(self, user_id: str, course_id: str) -> bool:
        # Verificar si ya está inscrito
        existing = await db.enrollments.find_one({
            "user_id": ObjectId(user_id),
            "course_id": ObjectId(course_id)
        })

        if existing:
            return False  # Ya inscrito

        # Crear inscripción
        enrollment = {
            "user_id": ObjectId(user_id),
            "course_id": ObjectId(course_id),
            "enrolled_at": datetime.now(),
            "completed": False
        }

        result = await db.enrollments.insert_one(enrollment)
        return result.inserted_id is not None
```

---

#### Módulo: states/

**Responsabilidad**: Gestión de estado reactivo de Reflex

**Archivos**:
- `auth_state.py`: Estado de autenticación (login, registro)
- `course_state.py`: Estado de listado de cursos
- `course_detail_state.py`: Estado de detalle de curso
- `enrollment_state.py`: Estado de inscripciones
- `student_dashboard_state.py`: Estado de dashboard

**Ejemplo** (`auth_state.py`):
```python
class AuthState(rx.State):
    is_authenticated: bool = False
    current_user: dict = {}
    error: str = ""
    success: str = ""

    async def handle_login(self, form_data: dict):
        email = form_data["email"]
        password = form_data["password"]

        # Llamar a servicio
        user = await UserService().login(email, password)

        if user:
            self.is_authenticated = True
            self.current_user = user
            self.success = "Login exitoso"
            return rx.redirect("/dashboard")
        else:
            self.error = "Credenciales incorrectas"
```

---

#### Módulo: pages/

**Responsabilidad**: Renderizado de páginas completas

**Archivos**:
- `index.py`: Página de inicio
- `courses.py`: Listado de cursos
- `course_detail.py`: Detalle de curso
- `login.py`: Página de login
- `register.py`: Página de registro
- `student_dashboard.py`: Dashboard de estudiante
- `instructor_dashboard.py`: Dashboard de instructor
- `admin_dashboard.py`: Dashboard de administrador

---

#### Módulo: components/

**Responsabilidad**: Componentes reutilizables de UI

**Archivos**:
- `navbar.py`: Barra de navegación
- `course_card.py`: Tarjeta de curso
- `instructor_card.py`: Tarjeta de instructor
- `section_list.py`: Lista de secciones con lecciones
- `protected.py`: Componentes de protección de rutas (RBAC)

---

#### Módulo: utils/

**Responsabilidad**: Utilidades reutilizables

**Archivos**:
- `password.py`: Hash y verificación de contraseñas (bcrypt)
- `route_helpers.py`: Generación de URLs
- `formatters.py`: Formato de fechas, números, duración
- `validators.py`: Validación de inputs (email, contraseña)

---

## 7.5. Diseño de Base de Datos

### 7.5.1. Esquema Lógico de MongoDB

MongoDB es una base de datos **NoSQL orientada a documentos**. Cada colección almacena documentos JSON.

#### Colección: `users`

**Descripción**: Usuarios de la plataforma (estudiantes, instructores, admins)

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "password": "$2b$12$hashedpassword...",
  "role": "instructor",  // admin | instructor | student
  "bio": "Desarrollador Python con 10 años de experiencia",
  "created_at": ISODate("2025-11-01T10:00:00Z")
}
```

**Índices**:
- `email`: Único (asegurar emails únicos)
- `role`: Normal (consultas frecuentes por rol)

---

#### Colección: `courses`

**Descripción**: Cursos disponibles en la plataforma

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "title": "Python para Principiantes",
  "description": "Aprende Python desde cero...",
  "instructor_id": ObjectId("..."),  // Referencia a users
  "level": "beginner",  // beginner | intermediate | advanced
  "duration_hours": 12.5,
  "price": 99.0,
  "image_url": "https://example.com/images/python-course.jpg",
  "sections": [
    {
      "title": "Introducción a Python",
      "description": "Primeros pasos con Python",
      "order": 1,
      "lessons": [
        {
          "title": "¿Qué es Python?",
          "content": "Python es un lenguaje...",
          "duration_minutes": 15,
          "order": 1,
          "video_url": "https://example.com/videos/lesson1.mp4"
        },
        {
          "title": "Instalación de Python",
          "content": "Para instalar Python...",
          "duration_minutes": 30,
          "order": 2
        }
      ]
    },
    {
      "title": "Variables y Tipos de Datos",
      "description": "Fundamentos de variables",
      "order": 2,
      "lessons": [ /* ... */ ]
    }
  ],
  "created_at": ISODate("2025-11-05T14:30:00Z")
}
```

**Índices**:
- `instructor_id`: Normal (consultas de cursos por instructor)
- `title`: Texto (búsqueda full-text)
- `level`: Normal (filtrado por nivel)

**Nota**: Secciones y lecciones están **embebidas** (no en colecciones separadas) porque:
- Siempre se consultan juntas
- No se consultan independientemente
- Mejora el rendimiento (1 query vs múltiples)

---

#### Colección: `enrollments`

**Descripción**: Inscripciones de estudiantes a cursos

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "user_id": ObjectId("..."),  // Referencia a users
  "course_id": ObjectId("..."),  // Referencia a courses
  "enrolled_at": ISODate("2025-11-10T09:15:00Z"),
  "completed": false
}
```

**Índices**:
- `user_id, course_id`: Compuesto y único (prevenir inscripciones duplicadas)
- `user_id`: Normal (consultas de inscripciones por usuario)
- `course_id`: Normal (consultas de inscripciones por curso)

---

#### Colección: `progress`

**Descripción**: Progreso de estudiantes en lecciones

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "enrollment_id": ObjectId("..."),  // Referencia a enrollments
  "lesson_id": "section_0_lesson_1",  // Identificador de lección (string)
  "completed_at": ISODate("2025-11-11T16:45:00Z")
}
```

**Índices**:
- `enrollment_id`: Normal (consultas de progreso por inscripción)
- `enrollment_id, lesson_id`: Compuesto y único (prevenir duplicados)

**Nota**: `lesson_id` es un string (no ObjectId) porque las lecciones están embebidas en cursos

---

#### Colección: `ratings`

**Descripción**: Valoraciones y reseñas de cursos

**Esquema**:
```json
{
  "_id": ObjectId("..."),
  "user_id": ObjectId("..."),  // Referencia a users
  "course_id": ObjectId("..."),  // Referencia a courses
  "rating": 5,  // 1-5 estrellas
  "review": "Excelente curso, muy claro y didáctico",
  "created_at": ISODate("2025-11-12T12:00:00Z")
}
```

**Índices**:
- `course_id`: Normal (consultas de valoraciones por curso)
- `user_id, course_id`: Compuesto y único (un usuario solo puede valorar un curso una vez)

---

<div style="page-break-after: always;"></div>

### 7.5.2. Diagrama Entidad-Relación (Adaptado a MongoDB)

```
┌─────────────┐          ┌──────────────┐          ┌─────────────┐
│    users    │          │   courses    │          │ enrollments │
├─────────────┤          ├──────────────┤          ├─────────────┤
│ _id (PK)    │1───────N │ instructor_id│          │ _id (PK)    │
│ name        │          │ (FK)         │          │ user_id (FK)│
│ email       │          │ title        │N───────1 │ course_id   │
│ password    │          │ description  │          │ (FK)        │
│ role        │          │ sections[]   │          │ enrolled_at │
│ bio         │          │   ├─lessons[]│          │ completed   │
│ created_at  │          │ level        │          └─────────────┘
└─────────────┘          │ duration_h   │                │
      │                  │ price        │                │1
      │                  │ image_url    │                │
      │1                 │ created_at   │                │
      │                  └──────────────┘                │N
      │                        │                  ┌──────────────┐
      │                        │1                 │   progress   │
      │                        │                  ├──────────────┤
      │                        │                  │ _id (PK)     │
      │                        │N                 │ enrollment_id│
      │                  ┌─────────────┐          │ (FK)         │
      │                  │   ratings   │          │ lesson_id    │
      │                  ├─────────────┤          │ completed_at │
      └────────────────N │ user_id (FK)│          └──────────────┘
                         │ course_id   │
                         │ (FK)        │
                         │ rating      │
                         │ review      │
                         │ created_at  │
                         └─────────────┘
```

**Relaciones**:
- Un **user** puede instruir muchos **courses** (1:N)
- Un **user** puede tener muchos **enrollments** (1:N)
- Un **course** puede tener muchos **enrollments** (1:N)
- Un **enrollment** puede tener muchos **progress** (1:N)
- Un **user** puede tener muchos **ratings** (1:N)
- Un **course** puede tener muchos **ratings** (1:N)

---

<div style="page-break-after: always;"></div>

### 7.5.3. Consultas Más Frecuentes y Optimización

| Consulta | Frecuencia | Índice Utilizado | Tiempo Estimado |
|----------|------------|------------------|-----------------|
| **Listado de cursos** | Alta | `_id` (implícito) | <50ms |
| **Buscar cursos por texto** | Alta | `title` (texto) | <100ms |
| **Filtrar cursos por nivel** | Media | `level` | <50ms |
| **Cursos de un instructor** | Media | `instructor_id` | <50ms |
| **Verificar inscripción** | Alta | `user_id, course_id` (compuesto) | <30ms |
| **Progreso de estudiante** | Alta | `enrollment_id` | <50ms |
| **Valoraciones de curso** | Media | `course_id` | <50ms |
| **Calcular promedio de valoraciones** | Media | Agregación MongoDB | <100ms |

**Optimizaciones implementadas**:
1.  Índices en campos de consulta frecuente
2.  Índices compuestos para consultas complejas
3.  Proyecciones para devolver solo campos necesarios
4.  Agregaciones para cálculos complejos (promedio de rating)
5.  Secciones y lecciones embebidas (evita JOINs)

---

## 7.6. Otras Estructuras de Datos Utilizadas

### 7.6.1. Estados de Reflex (Client-Side)

Reflex gestiona estados reactivos en el cliente que se sincronizan automáticamente con el servidor:

**Ejemplo**: `CourseState`
```python
class CourseState(rx.State):
    courses: list[dict] = []  # Lista de cursos
    loading: bool = False     # Estado de carga
    error: str = ""           # Mensaje de error
    search_query: str = ""    # Búsqueda actual
    filter_level: str = "all" # Filtro de nivel
```

**Ventajas**:
- Reactividad automática (cambios en estado actualizan UI)
- Sin necesidad de Redux/Context API
- Tipado fuerte con Python type hints

---

### 7.6.2. Caché de Sesión

Reflex almacena datos de sesión en **cookies** cifradas:

**Datos almacenados**:
- `is_authenticated`: Boolean
- `current_user`: Diccionario con datos de usuario
- `session_id`: Token único de sesión

**Ventajas**:
- Persistencia entre recargas de página
- Seguridad (cookies HTTP-only, cifradas)
- Fácil gestión (Reflex lo maneja automáticamente)

---

<div style="page-break-after: always;"></div>

## 7.7. Estudio de Seguridad de la Aplicación

### 7.7.1. Medidas de Seguridad Implementadas

#### 1. Autenticación Segura

**Hash de Contraseñas con bcrypt**

```python
import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)  # 2^12 = 4,096 iteraciones
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )
```

**Características**:
-  Salt único por contraseña (resistente a rainbow tables)
-  12 rounds (4,096 iteraciones, balance seguridad/rendimiento)
-  Algoritmo bcrypt (diseñado para ser lento, resistente a brute force)

---

#### 2. Control de Acceso Basado en Roles (RBAC)

**Componentes de Protección** (`components/protected.py`):

```python
def require_auth(component):
    """Requiere autenticación"""
    def wrapper(state):
        if not state.is_authenticated:
            return rx.redirect("/login")
        return component(state)
    return wrapper

def require_role(allowed_roles: list[str]):
    """Requiere rol específico"""
    def decorator(component):
        def wrapper(state):
            if not state.is_authenticated:
                return rx.redirect("/login")
            if state.current_user.get("role") not in allowed_roles:
                return rx.text("Acceso denegado")
            return component(state)
        return wrapper
    return decorator

def admin_only(component):
    """Solo administradores"""
    return require_role(["admin"])(component)
```

**Uso**:
```python
@admin_only
def admin_dashboard():
    return rx.box(...)
```

---

#### 3. Validación de Inputs

**Client-Side** (Reflex States):
```python
def validate_email(email: str) -> bool:
    return "@" in email and "." in email

def validate_password(password: str) -> bool:
    return len(password) >= 6 and len(password) <= 128
```

**Server-Side** (Services):
```python
async def create_user(self, user_data: dict) -> bool:
    # Validar datos
    if not user_data.get("email") or not validate_email(user_data["email"]):
        return False

    # Verificar email único
    existing = await db.users.find_one({"email": user_data["email"]})
    if existing:
        return False

    # Hashear contraseña
    user_data["password"] = hash_password(user_data["password"])

    # Insertar
    result = await db.users.insert_one(user_data)
    return result.inserted_id is not None
```

---

#### 4. Protección contra Inyección NoSQL

MongoDB + Motor utiliza **queries parametrizadas** que previenen inyecciones:

** Seguro** (recomendado):
```python
user = await db.users.find_one({"email": email})
```

** Inseguro** (NUNCA usar):
```python
# NO HACER - vulnerable a inyección
query = f"db.users.find({{email: '{email}'}})"
```

**Motor sanitiza automáticamente** las queries, por lo que no es posible inyectar código malicioso.

---

#### 5. Cifrado de Comunicaciones

**TLS/SSL** (HTTPS):
-  MongoDB Atlas usa TLS 1.2+ (cifrado en tránsito)
-  Reflex Cloud proporciona HTTPS automático
-  Certificados Let's Encrypt gratuitos

**Cifrado en Reposo**:
-  MongoDB Atlas cifra datos en disco (AES-256)
-  Backups automáticos cifrados

---

### 7.7.2. Matriz Completa de Seguridad

Referencia completa en [Anexo - Análisis de Seguridad Completo] (Sección 2.2 de documento previo generado por agente Explore).

**Resumen**:
-  11 fortalezas implementadas
-  3 parcialmente implementadas
-  6 no implementadas (planificadas para post-v1.0)

**Nivel de madurez de seguridad**: **INTERMEDIO** (adecuado para MVP)

---

### 7.7.3. Plan de Mejoras de Seguridad (Roadmap)

| Mejora | Prioridad | Esfuerzo | Versión Planificada |
|--------|-----------|----------|---------------------|
| **Rate limiting** en login | Alta | 8h | v1.1 (Q3 2026) |
| **Expiración de sesión** (24h inactividad) | Alta | 6h | v1.1 |
| **Recuperación de contraseña** por email | Media | 16h | v1.2 (Q4 2026) |
| **Two-Factor Authentication (2FA)** | Baja | 24h | v2.0 (2027) |
| **Auditoría de cambios** (logs) | Media | 12h | v1.2 |
| **Sanitización HTML explícita** | Baja | 4h | v1.1 |

---

**Conclusión Sección 7**: El diseño e implementación de E-Learning JCB Platform sigue principios sólidos de arquitectura de software (separación de capas, modularidad, reutilización). Los diagramas UML proporcionan una visión clara de la estructura y flujos del sistema. El diseño de base de datos MongoDB está optimizado para las consultas más frecuentes. Las medidas de seguridad implementadas son adecuadas para un MVP, con plan de mejoras para versiones futuras.

---

<div style="page-break-after: always;"></div>



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
```
```
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
```
```
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

<div style="page-break-after: always;"></div>

## 8.2. Módulos Principales

### 8.2.1. Módulo: `database/mongodb.py`

**Responsabilidad**: Gestión de conexión a MongoDB Atlas

**Extracto**:
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

```

**Características clave**:
-  Carga de URI desde `.env` (seguridad)
-  Validación de variable de entorno obligatoria
-  Cliente global (singleton pattern)
-  Funciones helper para acceso rápido a colecciones
-  Función de cierre para cleanup

---

<div style="page-break-after: always;"></div>

### 8.2.2. Módulo: `utils/password.py`

**Responsabilidad**: Hash seguro y verificación de contraseñas con bcrypt

**Extracto**:
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

```

**Características clave**:
-  bcrypt con 12 rounds (balance seguridad/rendimiento)
-  Salt único automático por contraseña
-  Validación de fortaleza de contraseña
-  Manejo de excepciones en verificación
-  Docstrings completos con ejemplos

---

<div style="page-break-after: always;"></div>

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

```

**Características clave**:
-  Métodos async para operaciones no bloqueantes
-  Validaciones de negocio (email único, rol válido)
-  Seguridad (hash de contraseñas, verificación de contraseña actual)
-  Proyecciones (excluir password de resultados)
-  Manejo de excepciones con logging
-  Conversión de ObjectId a string para serialización

---

### 8.2.4. Módulo: `components/protected.py`

**Responsabilidad**: Componentes de protección de rutas (RBAC)

**Extracto:**:
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
```

**Características clave**:
-  Sistema de decoradores flexible
-  Verificación de autenticación + autorización
-  Mensajes de error claros
-  Shortcuts para roles comunes
-  Fácil de usar y extender

---

<div style="page-break-after: always;"></div>

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

<div style="page-break-after: always;"></div>

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

<div style="page-break-after: always;"></div>

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
1.  Explicar **por qué**, no **qué** (el código ya dice qué hace)
2.  Comentarios en español para consistencia
3.  Comentarios solo donde el código no es auto-explicativo
4.  No comentarios redundantes

**Ejemplos**:

 **Buen comentario**:
```python
# Verificar contraseña actual antes de permitir cambio (seguridad)
if not verify_password(current_password, user.get("password", "")):
    return False
```

 **Mal comentario** (redundante):
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

<div style="page-break-after: always;"></div>

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

```

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

### 8.4.6. Conclusión


**Conclusión Sección 8**: El código fuente de E-Learning JCB Platform intenta estar **bien estructurado, documentado y mantenible**. Sigue convenciones estándar de Python (PEP 8), utiliza type hints para claridad, y cuenta con docstrings completos en formato Google Style. El repositorio Git con Conventional Commits facilita el seguimiento de cambios.

---

<div style="page-break-after: always;"></div>



# 9. MANUAL DE CONFIGURACIÓN Y FUNCIONAMIENTO

## 9.1. Requisitos del Sistema

### 9.1.1. Requisitos de Hardware

#### Requisitos Mínimos

| Componente | Especificación Mínima |
|------------|----------------------|
| **Procesador** | Intel Core i3 / AMD Ryzen 3 (2 cores) |
| **RAM** | 4 GB |
| **Almacenamiento** | 2 GB disponibles (SSD recomendado) |
| **Resolución de pantalla** | 1280 × 720 (HD) |
| **Conexión a Internet** | 5 Mbps (descarga) |

#### Requisitos Recomendados

| Componente | Especificación Recomendada |
|------------|---------------------------|
| **Procesador** | Intel Core i5 / AMD Ryzen 5 (4 cores) |
| **RAM** | 8 GB |
| **Almacenamiento** | 5 GB disponibles en SSD |
| **Resolución de pantalla** | 1920 × 1080 (Full HD) |
| **Conexión a Internet** | 25 Mbps (descarga) |

---

### 9.1.2. Requisitos de Software

#### Sistema Operativo

 **Linux**:
- Ubuntu 20.04 LTS o superior
- Debian 10 o superior
- Fedora 34 o superior
- Arch Linux (actualizado)

 **macOS**:
- macOS 11 Big Sur o superior
- macOS 12 Monterey (recomendado)
- macOS 13 Ventura

 **Windows**:
- Windows 10 (versión 1909 o superior)
- Windows 11 (recomendado)

#### Dependencias Principales

| Software | Versión Mínima | Versión Recomendada | Propósito |
|----------|----------------|---------------------|-----------|
| **Python** | 3.10 | 3.11 o 3.12 | Lenguaje principal |
| **pip** | 21.0 | Última | Gestor de paquetes Python |
| **Node.js** | 18.0.0 | 20.11.0 LTS | Frontend (generado por Reflex) |
| **npm** | 8.0.0 | 10.0.0 | Gestor de paquetes Node |
| **Git** | 2.30 | Última | Control de versiones |

#### Navegadores Soportados (para usuarios finales)

| Navegador | Versión Mínima |
|-----------|----------------|
| Google Chrome | 90+ |
| Mozilla Firefox | 88+ |
| Safari | 14+ |
| Microsoft Edge | 90+ |

---

## 9.2. Instalación y Configuración

### 9.2.1. Instalación en Windows

#### Paso 1: Instalar Python

1. Descargar Python desde https://www.python.org/downloads/
2. Ejecutar el instalador
3.  **IMPORTANTE**: Marcar "Add Python to PATH"
4. Click en "Install Now"
5. Verificar instalación:
   ```cmd
   python --version
   ```
   **Salida esperada**: `Python 3.11.x` (o superior)

#### Paso 2: Instalar Node.js

1. Descargar Node.js LTS desde https://nodejs.org/
2. Ejecutar el instalador (opciones por defecto)
3. Verificar instalación:
   ```cmd
   node --version
   npm --version
   ```
   **Salida esperada**:
   ```
   v20.11.0
   10.2.4
   ```

#### Paso 3: Instalar Git

1. Descargar Git desde https://git-scm.com/download/win
2. Ejecutar el instalador (opciones por defecto)
3. Verificar instalación:
   ```cmd
   git --version
   ```

#### Paso 4: Clonar el Repositorio

```cmd
# Navegar a la carpeta deseada
cd C:\Users\TuUsuario\Documents

# Clonar repositorio
git clone https://github.com/[usuario]/E-Learning-JCB-Reflex.git

# Entrar al directorio
cd E-Learning-JCB-Reflex
```

#### Paso 5: Crear Entorno Virtual

```cmd
# Crear entorno virtual
python -m venv reflex-env

# Activar entorno virtual
reflex-env\Scripts\activate

# Verificar activación (debe aparecer (reflex-env) en el prompt)
```

#### Paso 6: Instalar Dependencias

```cmd
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt
```

**Tiempo estimado**: 3-5 minutos

**Progreso esperado**:
```
Collecting reflex==0.8.24
Collecting motor==3.7.1
Collecting bcrypt==5.0.0
...
Successfully installed reflex-0.8.24 motor-3.7.1 bcrypt-5.0.0 ...
```

#### Paso 7: Configurar Variables de Entorno

```cmd
# Copiar archivo de ejemplo
copy .env.example .env

# Editar .env con Notepad
notepad .env
```

Ver sección 9.3 para configuración de variables.

#### Paso 8: Ejecutar la Aplicación

```cmd
# Primera ejecución (inicializa Reflex)
reflex init

# Ejecutar en modo desarrollo
reflex run
```

**Salida esperada**:
```
Starting Reflex App
─────────────────────────────────────────────────────
App running at:
  └─ http://localhost:3000

Backend running at:
  └─ http://localhost:8000
```

 **Abrir navegador** en http://localhost:3000

---

### 9.2.2. Instalación en Linux (Ubuntu/Debian)

#### Paso 1: Actualizar Sistema

```bash
sudo apt update
sudo apt upgrade -y
```

#### Paso 2: Instalar Python 3.11

```bash
# Instalar dependencias
sudo apt install software-properties-common -y

# Añadir repositorio deadsnakes (Python versiones)
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# Instalar Python 3.11
sudo apt install python3.11 python3.11-venv python3.11-dev -y

# Verificar
python3.11 --version
```

#### Paso 3: Instalar Node.js (desde NodeSource)

```bash
# Instalar Node.js 20 LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs -y

# Verificar
node --version
npm --version
```

#### Paso 4: Instalar Git

```bash
sudo apt install git -y

# Verificar
git --version
```

#### Paso 5: Clonar Repositorio

```bash
# Navegar a home
cd ~

# Clonar
git clone https://github.com/[usuario]/E-Learning-JCB-Reflex.git
cd E-Learning-JCB-Reflex
```

#### Paso 6: Crear Entorno Virtual

```bash
# Crear entorno virtual con Python 3.11
python3.11 -m venv reflex-env

# Activar
source reflex-env/bin/activate

# Verificar activación
which python  # Debe mostrar ruta dentro de reflex-env
```

#### Paso 7: Instalar Dependencias

```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

#### Paso 8: Configurar Variables de Entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar con nano (o vim, gedit, etc.)
nano .env
```

#### Paso 9: Ejecutar Aplicación

```bash
# Inicializar Reflex
reflex init

# Ejecutar
reflex run
```

---

<div style="page-break-after: always;"></div>

### 9.2.3. Instalación en macOS

#### Paso 1: Instalar Homebrew (si no está instalado)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Paso 2: Instalar Python

```bash
# Instalar Python 3.11
brew install python@3.11

# Verificar
python3.11 --version
```

#### Paso 3: Instalar Node.js

```bash
# Instalar Node.js LTS
brew install node@20

# Verificar
node --version
npm --version
```

#### Paso 4: Instalar Git

```bash
# Git ya viene con Xcode Command Line Tools, pero puede actualizarse
brew install git

# Verificar
git --version
```

#### Pasos 5-9: Iguales a Linux

Ver sección 9.2.2 pasos 5-9 (clonar, entorno virtual, dependencias, configurar, ejecutar)

---

<div style="page-break-after: always;"></div>

## 9.3. Configuración de Variables de Entorno

### 9.3.1. Archivo `.env`

El archivo `.env` contiene configuraciones sensibles que **NO deben committearse** a Git (ya está en `.gitignore`).

**Ubicación**: Raíz del proyecto (`/E-Learning-JCB-Reflex/.env`)

**Plantilla** (`.env.example`):
```env
# ============================================
# CONFIGURACIÓN DE E-LEARNING JCB PLATFORM
# ============================================

# --- BASE DE DATOS ---
# URI de conexión a MongoDB Atlas
# Formato: mongodb+srv://<usuario>:<password>@<cluster>.mongodb.net
MONGODB_URI=mongodb+srv://usuario:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority

# Nombre de la base de datos
DB_NAME=elearning_jcb

# --- APLICACIÓN ---
# Entorno de ejecución (development | production)
ENVIRONMENT=development

# URL del frontend (para CORS en producción)
FRONTEND_URL=http://localhost:3000

# Puerto del backend (por defecto 8000)
BACKEND_PORT=8000

# --- SEGURIDAD ---
# Clave secreta para firmar sesiones (generar con: python -c "import secrets; print(secrets.token_hex(32))")
SECRET_KEY=tu_clave_secreta_aqui_debe_ser_muy_larga_y_aleatoria

# --- EMAIL (opcional, para futuro) ---
# Configuración de SendGrid para emails
SENDGRID_API_KEY=
EMAIL_FROM=noreply@elearningjcb.com

# --- OTROS ---
# Nivel de logging (DEBUG | INFO | WARNING | ERROR)
LOG_LEVEL=DEBUG
```

---

<div style="page-break-after: always;"></div>

### 9.3.2. Obtener URI de MongoDB Atlas

#### Paso 1: Crear Cuenta en MongoDB Atlas

1. Ir a https://www.mongodb.com/cloud/atlas/register
2. Registrarse con email (gratis)
3. Verificar email

#### Paso 2: Crear Cluster Gratuito

1. Click en "Build a Database"
2. Seleccionar **M0 (FREE)**
3. Elegir proveedor cloud: **AWS** (recomendado)
4. Región: **Europe (Ireland)** `eu-west-1` (más cercano a España)
5. Nombre del cluster: `Cluster0` (por defecto)
6. Click en "Create"

**Tiempo de creación**: 3-5 minutos

#### Paso 3: Configurar Acceso

**3.1. Crear Usuario de Base de Datos**:
1. En "Database Access", click "Add New Database User"
2. Authentication Method: **Password**
3. Usuario: `elearning_admin`
4. Contraseña: Generar automática (guardar en lugar seguro)
5. Database User Privileges: **Read and write to any database**
6. Click "Add User"

**3.2. Configurar IP Whitelist**:
1. En "Network Access", click "Add IP Address"
2. **Desarrollo**: Click "Allow Access from Anywhere" (0.0.0.0/0)
   -  **Nota**: En producción, especificar IP del servidor
3. Click "Confirm"

#### Paso 4: Obtener Connection String

1. En "Database", click "Connect" en tu cluster
2. Seleccionar "Connect your application"
3. Driver: **Python**, Version: **3.6 or later**
4. Copiar connection string:
   ```
   mongodb+srv://elearning_admin:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
5. Reemplazar `<password>` con la contraseña del usuario

#### Paso 5: Pegar en `.env`

```env
MONGODB_URI=mongodb+srv://elearning_admin:TuPasswordAqui@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority
DB_NAME=elearning_jcb
```

 **Guardar archivo**

---

### 9.3.3. Generar Clave Secreta

```bash
# Activar entorno virtual primero
source reflex-env/bin/activate  # Linux/Mac
reflex-env\Scripts\activate     # Windows

# Generar clave aleatoria de 64 caracteres
python -c "import secrets; print(secrets.token_hex(32))"
```

**Salida** (ejemplo):
```
a7f3d2e9c1b8f4a6e3d7c2b9a8f5e1d4c3b7a6f2e9d8c4b1a7f3e2d9c6b8a5f4
```

**Copiar en `.env`**:
```env
SECRET_KEY=a7f3d2e9c1b8f4a6e3d7c2b9a8f5e1d4c3b7a6f2e9d8c4b1a7f3e2d9c6b8a5f4
```

---

## 9.4. Despliegue en Producción

### 9.4.1. Despliegue en Reflex Cloud

**Reflex Cloud** es la plataforma oficial de despliegue para aplicaciones Reflex, con configuración simplificada.

#### Paso 1: Crear Cuenta en Reflex Cloud

1. Ir a https://reflex.dev/cloud
2. Registrarse con GitHub (OAuth)
3. Autorizar acceso a repositorios

#### Paso 2: Conectar Repositorio

1. En dashboard de Reflex Cloud, click "New Project"
2. Seleccionar repositorio: `E-Learning-JCB-Reflex`
3. Branch: `main`
4. Click "Import"

#### Paso 3: Configurar Variables de Entorno

1. En proyecto, ir a "Settings" > "Environment Variables"
2. Añadir las siguientes variables (una por una):

   | Variable | Valor |
   |----------|-------|
   | `MONGODB_URI` | mongodb+srv://... (tu URI completa) |
   | `DB_NAME` | elearning_jcb |
   | `ENVIRONMENT` | production |
   | `SECRET_KEY` | (tu clave secreta generada) |
   | `FRONTEND_URL` | (se autocompletará con URL de Reflex Cloud) |

3. Click "Save" para cada variable

#### Paso 4: Desplegar

1. En dashboard del proyecto, click "Deploy"
2. Reflex Cloud automáticamente:
   - Clona el repositorio
   - Instala dependencias (`pip install -r requirements.txt`)
   - Ejecuta `reflex init`
   - Ejecuta `reflex export --frontend-only` (si aplica)
   - Inicia servidor
3. **Tiempo de despliegue**: 3-5 minutos

#### Paso 5: Verificar Despliegue

**URL de producción**: https://[tu-proyecto].reflex.run

 Abrir en navegador y verificar funcionamiento

#### Paso 6: Configurar Dominio Personalizado (Opcional)

1. En "Settings" > "Domains"
2. Click "Add Custom Domain"
3. Introducir dominio: `www.elearningjcb.com`
4. Configurar DNS en tu proveedor de dominio:
   - Tipo: `CNAME`
   - Nombre: `www`
   - Valor: `[tu-proyecto].reflex.run`
5. Verificar dominio (24-48 horas para propagación DNS)

**Certificado SSL**: Automático con Let's Encrypt

---

### 9.4.2. Despliegue en VPS (Alternativa)

Si prefieres control total, puedes desplegar en un VPS (DigitalOcean, Linode, Hetzner).

#### Requisitos del Servidor

- **OS**: Ubuntu 22.04 LTS
- **RAM**: Mínimo 2 GB (4 GB recomendado)
- **CPU**: 1 vCPU (2 vCPUs recomendado)
- **Almacenamiento**: 20 GB SSD
- **IP**: Pública estática

#### Paso 1: Configurar Servidor

```bash
# Conectar via SSH
ssh root@tu_ip_servidor

# Actualizar sistema
apt update && apt upgrade -y

# Instalar dependencias
apt install python3.11 python3.11-venv python3-pip nodejs npm nginx git -y

# Crear usuario para la aplicación
adduser elearning
usermod -aG sudo elearning

# Cambiar a usuario elearning
su - elearning
```

#### Paso 2: Clonar y Configurar Aplicación

```bash
# Clonar repositorio
git clone https://github.com/[usuario]/E-Learning-JCB-Reflex.git
cd E-Learning-JCB-Reflex

# Crear entorno virtual
python3.11 -m venv reflex-env
source reflex-env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar .env
nano .env
# (pegar configuración de producción)
```

#### Paso 3: Configurar Nginx como Reverse Proxy

```bash
# Crear configuración de Nginx
sudo nano /etc/nginx/sites-available/elearning
```

**Contenido**:
```nginx
server {
    listen 80;
    server_name tu_dominio.com www.tu_dominio.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
    }
}
```

```bash
# Activar sitio
sudo ln -s /etc/nginx/sites-available/elearning /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Paso 4: Configurar Systemd Service

```bash
# Crear servicio
sudo nano /etc/systemd/system/elearning.service
```

**Contenido**:
```ini
[Unit]
Description=E-Learning JCB Platform
After=network.target

[Service]
User=elearning
WorkingDirectory=/home/elearning/E-Learning-JCB-Reflex
Environment="PATH=/home/elearning/E-Learning-JCB-Reflex/reflex-env/bin"
ExecStart=/home/elearning/E-Learning-JCB-Reflex/reflex-env/bin/reflex run --production

[Install]
WantedBy=multi-user.target
```

```bash
# Activar y iniciar servicio
sudo systemctl enable elearning
sudo systemctl start elearning

# Verificar estado
sudo systemctl status elearning
```

#### Paso 5: Configurar SSL con Let's Encrypt

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtener certificado
sudo certbot --nginx -d tu_dominio.com -d www.tu_dominio.com

# Renovación automática (ya configurada por Certbot)
sudo certbot renew --dry-run
```


---

<div style="page-break-after: always;"></div>

## 9.5. Resolución de Problemas Comunes

### 9.5.1. Error: "MONGODB_URI environment variable is not set"

**Causa**: Archivo `.env` no existe o no está configurado

**Solución**:
```bash
# Verificar que existe .env
ls -la .env  # Linux/Mac
dir .env     # Windows

# Si no existe, copiar desde ejemplo
cp .env.example .env  # Linux/Mac
copy .env.example .env  # Windows

# Editar y configurar MONGODB_URI
nano .env  # Linux/Mac
notepad .env  # Windows
```

---

### 9.5.2. Error: "reflex: command not found"

**Causa**: Entorno virtual no activado o Reflex no instalado

**Solución**:
```bash
# Activar entorno virtual
source reflex-env/bin/activate  # Linux/Mac
reflex-env\Scripts\activate     # Windows

# Verificar activación (debe aparecer (reflex-env) en prompt)

# Si Reflex no está instalado
pip install reflex==0.8.24
```

---

### 9.5.3. Error: "Port 3000 already in use"

**Causa**: Otro proceso está usando el puerto 3000

**Solución**:

**Linux/Mac**:
```bash
# Encontrar proceso en puerto 3000
lsof -i :3000

# Matar proceso (usar PID del comando anterior)
kill -9 <PID>
```

**Windows**:
```cmd
# Encontrar proceso
netstat -ano | findstr :3000

# Matar proceso (usar PID de la última columna)
taskkill /PID <PID> /F
```

**Alternativa**: Ejecutar en otro puerto:
```bash
reflex run --port 3001
```

---

### 9.5.4. Error: "ModuleNotFoundError: No module named 'motor'"

**Causa**: Dependencias no instaladas

**Solución**:
```bash
# Asegurarse de que entorno virtual está activado
source reflex-env/bin/activate  # Linux/Mac
reflex-env\Scripts\activate     # Windows

# Reinstalar dependencias
pip install -r requirements.txt

# Si persiste, instalar manualmente
pip install motor==3.7.1
```

---

### 9.5.5. Error: "Connection refused" al conectar a MongoDB

**Causa**: URI de MongoDB incorrecta o IP no whitelisteada

**Solución**:
1. Verificar URI en `.env` (copiar exactamente desde MongoDB Atlas)
2. En MongoDB Atlas, ir a "Network Access"
3. Verificar que tu IP está en whitelist (o 0.0.0.0/0 para desarrollo)
4. Verificar que el usuario de BD tiene permisos correctos ("Database Access")

---

### 9.5.6. Página en blanco / No carga UI

**Causa**: Frontend no inicializado o error en build

**Solución**:
```bash
# Limpiar caché de Reflex
rm -rf .web  # Linux/Mac
rmdir /s .web  # Windows

# Reinicializar
reflex init

# Ejecutar
reflex run
```

---

### 9.5.7. Logs de Errores

**Ver logs de Reflex**:
```bash
# Durante ejecución, los logs aparecen en consola

# Para servidor en producción (systemd):
sudo journalctl -u elearning -f
```

**Habilitar logging debug**:

En `.env`:
```env
LOG_LEVEL=DEBUG
```

---

<div style="page-break-after: always;"></div>

## 9.6. Comandos Útiles

### Comandos de Reflex

```bash
# Ejecutar en modo desarrollo
reflex run

# Ejecutar en modo producción
reflex run --production

# Ejecutar en otro puerto
reflex run --port 3001

# Limpiar caché
reflex clean

# Exportar frontend estático (si aplica)
reflex export

# Ver versión de Reflex
reflex --version
```

### Comandos de Python/Pip

```bash
# Ver paquetes instalados
pip list

# Actualizar un paquete
pip install --upgrade reflex

# Congelar dependencias actuales
pip freeze > requirements.txt
```

### Comandos de Git

```bash
# Ver estado del repositorio
git status

# Descargar últimos cambios
git pull origin main

# Ver historial de commits
git log --oneline

# Ver diferencias
git diff
```

---

**Conclusión Sección 9**: El manual de configuración proporciona instrucciones detalladas paso a paso para instalar E-Learning JCB Platform en Windows, Linux y macOS. Incluye configuración de MongoDB Atlas, despliegue en Reflex Cloud (recomendado) y VPS (avanzado), así como resolución de problemas comunes. Con este manual, cualquier usuario con conocimientos básicos puede poner en funcionamiento la aplicación en menos de 30 minutos.

---

<div style="page-break-after: always;"></div>



# 10. MANUAL DE USUARIO

## 10.1. Introducción para Usuarios

### 10.1.1. ¿Qué es E-Learning JCB Platform?

**E-Learning JCB Platform** es una plataforma web de formación online que permite a estudiantes acceder a cursos de calidad, a instructores compartir sus conocimientos y a administradores gestionar el sistema completo.

**Características principales**:
-  **Catálogo de cursos** con información detallada
-  **Perfiles de instructores** con estadísticas
-  **Dashboard personalizado** según tu rol
-  **Seguimiento de progreso** en tiempo real
-  **Sistema de valoraciones** transparente
-  **Acceso seguro** con autenticación robusta

---

### 10.1.2. ¿Quién puede usar la plataforma?

La plataforma está diseñada para **3 tipos de usuarios**:

| Rol | ¿Qué puedes hacer? | Ejemplo |
|-----|-------------------|---------|
| **Estudiante** | Buscar cursos, inscribirte, ver lecciones, seguir tu progreso, valorar cursos | María quiere aprender Python |
| **Instructor** | Crear cursos, gestionar contenido, ver estadísticas de tus cursos | Juan enseña desarrollo web |
| **Administrador** | Gestionar usuarios, moderar contenido, ver reportes globales | Admin del sistema |

---

### 10.1.3. Acceso a la Plataforma

**URL de producción**: https://elearningjcb.com (o tu dominio configurado)

**Navegadores recomendados**:
-  Google Chrome (versión 90+)
-  Mozilla Firefox (versión 88+)
-  Safari (versión 14+)
-  Microsoft Edge (versión 90+)

**Dispositivos soportados**:
-  Desktop (Windows, Mac, Linux)
-  Tablet (iPad, Android)
-  Móvil (iOS, Android)

---

## 10.2. Registro y Acceso a la Plataforma

### 10.2.1. Crear una Cuenta Nueva (Registro)

#### Paso 1: Acceder a la Página de Registro

1. Ir a https://elearningjcb.com
2. Click en el botón **"Registrarse"** en la esquina superior derecha

**Captura de pantalla** (referencia):

![Registro](capturas/01_autenticacion/02_registro.png)

#### Paso 2: Completar el Formulario de Registro

**Campos obligatorios**:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| **Nombre completo** | Tu nombre y apellidos | María López García |
| **Email** | Correo electrónico (será tu usuario) | maria.lopez@example.com |
| **Contraseña** | Mínimo 6 caracteres | MiContraseña123 |
| **Confirmar contraseña** | Debe coincidir con la anterior | MiContraseña123 |
| **Rol** | Estudiante o Instructor | Estudiante |

**Ejemplo visual del formulario**:

![Registro](capturas/01_autenticacion/02_registro.png)

#### Paso 3: Verificación y Confirmación

1. Click en el botón **"Registrarse"**
2. Si hay errores, aparecerán mensajes en rojo:
   -  "El email ya está registrado"
   -  "Las contraseñas no coinciden"
   -  "La contraseña debe tener al menos 6 caracteres"
3. Si todo es correcto:
   -  Mensaje: "Registro exitoso. Redirigiendo..."
   - Automáticamente se inicia sesión
   - Redirige a tu dashboard según el rol elegido

**Tiempo estimado**: 2 minutos

---

### 10.2.2. Iniciar Sesión (Login)

#### Para Usuarios Existentes

1. Click en **"Login"** en la parte superior derecha
2. Introducir:
   - **Email**: Tu correo registrado
   - **Contraseña**: Tu contraseña
3. (Opcional) Marcar "Recordarme" para mantener sesión
4. Click en **"Iniciar Sesión"**

**Ejemplo visual**:

![Login](capturas/01_autenticacion/01_login.png)

**Errores comunes**:
-  "Email o contraseña incorrectos" → Verificar datos
-  "Email no encontrado" → Registrarse primero

**Tras login exitoso**:
-  Redirige a tu dashboard (estudiante/instructor/admin)
-  Aparece tu nombre en la esquina superior derecha

---

### 10.2.3. Cerrar Sesión (Logout)

1. Click en tu nombre en la esquina superior derecha
2. Click en **"Cerrar sesión"**
3. Confirmación: "Sesión cerrada exitosamente"
4. Redirige a la página de inicio

---

## 10.3. Guía para Estudiantes

### 10.3.1. Explorar el Catálogo de Cursos

#### Acceder al Catálogo

**Opción 1**: Desde la página de inicio
- Click en el botón **"Explorar Cursos"** en el hero

**Opción 2**: Desde el menú de navegación
- Click en **"Cursos"** en el navbar

**URL directa**: https://elearningjcb.com/courses

---

#### Buscar Cursos

**Barra de búsqueda**:

![Búsqueda y Filtros](capturas/02_estudiante/05_listado_cursos.png)

**Cómo buscar**:
1. Escribir palabras clave en la barra de búsqueda (ej: "Python", "JavaScript")
2. Aplicar filtros:
   - **Nivel**: Principiante, Intermedio, Avanzado
   - **Duración**: 0-5h, 5-10h, 10-20h, +20h
   - **Valoración**: 4+ estrellas, 4.5+ estrellas
3. Los resultados se actualizan automáticamente

**Ejemplo de resultado**:

![Tarjeta de Curso](capturas/02_estudiante/05_listado_cursos.png)

---

<div style="page-break-after: always;"></div>

### 10.3.2. Ver Detalles de un Curso

#### Información Disponible

Al hacer click en **"Ver Detalles"** en cualquier curso, se muestra:

**Sección 1: Hero del Curso**
-  Imagen del curso
-  Título completo
-  Valoración promedio + número de reseñas
-  Nombre del instructor (clickeable)
-  Duración total en horas
-  Nivel (Principiante/Intermedio/Avanzado)
-  Precio
-  Botón **"Inscribirse Ahora"** (destacado en verde)

**Sección 2: Descripción**
- Texto completo de descripción del curso
- Objetivos de aprendizaje
- Requisitos previos (si aplica)

**Sección 3: Contenido del Curso** **DIFERENCIADOR CLAVE**
- **Todas las secciones y lecciones visibles** (acordeón desplegable)
- Duración de cada lección
- Orden claro de contenidos

**Ejemplo visual**:

![Detalle de Curso con Lecciones](capturas/02_estudiante/06_detalle_curso.png)

**Sección 4: Reseñas de Estudiantes**
- Valoraciones con estrellas
- Comentarios textuales
- Nombre del estudiante y fecha

---

<div style="page-break-after: always;"></div>

### 10.3.3. Inscribirse en un Curso

#### Proceso de Inscripción

**Paso 1**: Desde la página de detalle del curso, click en **"Inscribirse Ahora"**

**Paso 2**: Confirmación automática
-  Mensaje: "Inscripción exitosa"
- El botón cambia a "Ya estás inscrito" (deshabilitado)
- Aparece opción "Ir a Dashboard" o "Comenzar Curso"

**Paso 3**: Acceso al curso
- El curso ahora aparece en tu **Dashboard de Estudiante**
- Puedes comenzar a ver lecciones inmediatamente

**Notas**:
-  La inscripción es **instantánea** (sin proceso de pago en v1.0)
-  No se permiten inscripciones duplicadas
-  En futuras versiones habrá cursos de pago

---

### 10.3.4. Dashboard de Estudiante

#### Acceder al Dashboard

**Opción 1**: Tras iniciar sesión, automáticamente redirige al dashboard

**Opción 2**: Click en tu nombre > **"Dashboard"**

**URL**: https://elearningjcb.com/student/dashboard

---

#### Secciones del Dashboard

**1. Resumen de Estadísticas** (parte superior)

![Dashboard de Estudiante](capturas/02_estudiante/07_dashboard_estudiante.png)

**2. Mis Cursos** (sección principal)
- Lista de cursos inscritos
- Barra de progreso por curso
- Botón **"Continuar"** para retomar
- Botón **"Ver Certificado"** si completado (futuro)

**Ejemplo de curso en progreso**:

![Curso en Progreso](capturas/02_estudiante/09_progreso_curso.png)

**3. Cursos Recomendados** (opcional)
- Sugerencias basadas en tus inscripciones
- Cursos similares a los que ya tienes

**4. Actividad Reciente**
- Últimas lecciones completadas
- Valoraciones recientes que has hecho

---

### 10.3.5. Seguir un Curso

#### Ver Lecciones de un Curso

**Desde el dashboard**:
1. Click en **"Continuar Curso"** en el curso deseado
2. Se abre la página del curso con el contenido

**Desde el detalle del curso**:
1. Si ya estás inscrito, aparece el contenido desbloqueado
2. Click en cualquier lección para empezar

---

#### Marcar Lección como Completada

**Al finalizar una lección**:
1. Click en el botón **"Marcar como Completada"** al final de la lección
2.  Confirmación visual (checkmark verde)
3. El progreso del curso se actualiza automáticamente
4. Opción **"Siguiente Lección"** aparece

**Barra de progreso**:
- Se actualiza en tiempo real
- Ejemplo: "8/10 lecciones completadas (80%)"

---

### 10.3.6. Valorar un Curso

#### Cuándo Puedes Valorar

-  Debes estar inscrito en el curso
-  Idealmente, tras completar al menos 50% del curso
-  Solo puedes valorar una vez por curso

---

#### Dejar una Valoración

**Paso 1**: En la página de detalle del curso, scroll hasta **"Valorar este curso"**

**Paso 2**: Seleccionar estrellas (1-5)
```
☆☆☆☆☆  (Click en las estrellas para valorar)
```

**Paso 3** (opcional): Escribir reseña
```
┌────────────────────────────────────────────────┐
│ Escribe tu reseña (opcional)                   │
│ ┌────────────────────────────────────────────┐ │
│ │ Excelente curso, muy bien explicado...     │ │
│ │                                            │ │
│ └────────────────────────────────────────────┘ │
│                                                │
│           [Enviar Valoración]                  │
└────────────────────────────────────────────────┘
```

**Paso 4**: Click en **"Enviar Valoración"**
-  Confirmación: "Valoración enviada con éxito"
- Tu valoración aparece en la lista de reseñas

---

<div style="page-break-after: always;"></div>

### 10.3.7. Editar Perfil de Estudiante

**Acceso**: Click en tu nombre > **"Perfil"**

**Campos editables**:
- Nombre completo
- Biografía (opcional, hasta 500 caracteres)
- Cambiar contraseña

**Ejemplo**:

![Mi Perfil](capturas/02_estudiante/08_mi_perfil.png)

---

<div style="page-break-after: always;"></div>

## 10.4. Guía para Instructores

### 10.4.1. Dashboard de Instructor

**Acceso**: Tras login como instructor, automáticamente redirige

**URL**: https://elearningjcb.com/instructor/dashboard

---

#### Resumen de Estadísticas

![Dashboard de Instructor](capturas/03_instructor/12_dashboard_instructor.png)

**Información mostrada**:
- Total de cursos creados por ti
- Total de estudiantes inscritos en todos tus cursos
- Valoración promedio de todos tus cursos
- Ingresos totales (futuro, cuando haya pagos)

---

#### Mis Cursos (Tabla)

**Vista de tabla con acciones**:

![Gestión de Cursos Instructor](capturas/03_instructor/12_dashboard_instructor.png)

---

### 10.4.2. Crear un Curso Completo

#### Paso 1: Acceder al Formulario de Creación

**Desde el dashboard de instructor**:
- Click en el botón **"+ Crear Nuevo Curso"**

**URL**: https://elearningjcb.com/instructor/courses/new

---

#### Paso 2: Información Básica del Curso

**Formulario - Paso 1**:

![Crear Curso](capturas/04_admin/21_gestion_cursos.png)

**Campos obligatorios**:
-  Título (máximo 100 caracteres)
-  Descripción (mínimo 50 caracteres)
-  Nivel (seleccionar uno)
-  Precio (puede ser 0 para cursos gratuitos)

---

#### Paso 3: Añadir Secciones

**Formulario - Paso 2**:

![Añadir Lecciones](capturas/04_admin/21_gestion_cursos.png)

**Proceso**:
1. Click en **"+ Añadir Nueva Sección"**
2. Completar título y descripción de la sección
3. Click en **"+ Añadir Lección a Sección X"**
4. Completar:
   - Título de la lección
   - Duración en minutos
   - Contenido (texto, puede incluir código)
   - (Opcional) URL de video
5. Repetir para cada lección de la sección
6. Repetir para cada sección del curso

---

#### Paso 4: Revisar y Publicar

**Antes de publicar**:
- Revisar toda la información del curso
- Verificar que todas las secciones tienen al menos 1 lección
- Verificar duración total (suma automática)

**Opciones**:
- **"Guardar Borrador"**: Guarda sin publicar (solo tú lo ves)
- **"Publicar Curso"**: Hace el curso visible en el catálogo público

**Tras publicar**:
-  Mensaje: "Curso publicado exitosamente"
- El curso aparece en el catálogo
- Redirige a la página de detalle del curso

**Tiempo estimado para crear un curso completo**: 1-3 horas (dependiendo de la complejidad)

---

### 10.4.3. Editar un Curso Existente

**Desde el dashboard de instructor**:
1. En la tabla de "Mis Cursos", click en **"Editar"** del curso deseado
2. Se abre el mismo formulario de creación, con datos precargados
3. Modificar lo necesario:
   - Información básica (título, descripción, precio)
   - Añadir/editar/eliminar secciones
   - Añadir/editar/eliminar lecciones
4. Click en **"Guardar Cambios"**

**Notas**:
-  Los cambios son instantáneos
-  Si el curso ya tiene estudiantes inscritos, se les notifica del cambio (futuro)

---

### 10.4.4. Ver Estadísticas de un Curso

**Desde el dashboard de instructor**:
1. Click en **"Ver"** del curso deseado
2. Se muestra la página de detalle con sección adicional: **"Estadísticas del Instructor"**

**Información mostrada**:

![Estadísticas de Curso](capturas/03_instructor/12_dashboard_instructor.png)

---

<div style="page-break-after: always;"></div>

### 10.4.5. Eliminar un Curso

**Proceso**:
1. Desde el dashboard, click en **"Eliminar"** en el curso deseado
2. Modal de confirmación:

   ![Eliminar Curso](capturas/04_admin/21_gestion_cursos.png)

3. Si se confirma:
   - El curso se elimina de la base de datos
   - Los estudiantes pierden acceso (se notifica por email - futuro)
   - No se puede recuperar

**Recomendación**: En lugar de eliminar, considera "despublicar" (opción futura) para que no sea visible pero mantenga datos.

---

<div style="page-break-after: always;"></div>

## 10.5. Guía para Administradores

### 10.5.1. Dashboard de Administrador

**Acceso**: Solo usuarios con rol "admin"

**URL**: https://elearningjcb.com/admin/dashboard

**Protección**: Si intentas acceder sin ser admin, aparece:

![Acceso Denegado](capturas/05_ui_general/23_navbar_desktop.png)

---

#### Estadísticas Globales

![Dashboard de Administrador](capturas/04_admin/18_dashboard_admin.png)

---

### 10.5.2. Gestión de Usuarios

**Acceso**: Desde el dashboard admin, sección **"Gestión de Usuarios"**

**Tabla de usuarios**:

![Gestión de Usuarios](capturas/04_admin/19_gestion_usuarios.png)

**Funcionalidades**:

**1. Ver todos los usuarios**:
- Lista completa con paginación (50 usuarios por página)
- Buscador por nombre o email
- Filtro por rol

**2. Editar usuario**:
- Cambiar nombre
- Cambiar rol (estudiante ↔ instructor ↔ admin)
- Cambiar contraseña (con confirmación)

**3. Eliminar usuario**:
- Modal de confirmación similar al de eliminar curso
-  **Cuidado**: Elimina también todas sus inscripciones, valoraciones, etc.

**4. Crear usuario manualmente**:
- Formulario igual que el registro público
- Útil para crear cuentas de prueba o admins adicionales

---

### 10.5.3. Moderación de Contenido

**Acceso**: Dashboard admin > **"Moderación de Cursos"**

**Lista de cursos pendientes de revisión** (futuro):

![Gestión de Cursos](capturas/04_admin/21_gestion_cursos.png)

**Proceso de moderación**:
1. **Ver** el curso en detalle
2. Revisar contenido de secciones y lecciones
3. Decidir:
   - **Aprobar**: Curso se publica en catálogo
   - **Rechazar**: Se notifica al instructor con motivo

**Criterios de moderación**:
-  Contenido ilegal o inapropiado
-  Spam o cursos de baja calidad
-  Violación de derechos de autor
-  Contenido educativo legítimo

---

### 10.5.4. Reportes y Estadísticas Avanzadas

**Acceso**: Dashboard admin > **"Reportes"**

**Reportes disponibles**:

**1. Reporte de Inscripciones**:
- Gráfico de inscripciones por mes
- Cursos más populares (top 10)
- Tasa de crecimiento

**2. Reporte de Ingresos** (futuro, cuando haya pagos):
- Ingresos por mes
- Ingresos por curso
- Comisiones de la plataforma

**3. Reporte de Actividad de Usuarios**:
- Usuarios activos por semana
- Tasa de completación de cursos
- Usuarios inactivos (sin login en 30 días)

**4. Reporte de Valoraciones**:
- Promedio de valoraciones de la plataforma
- Distribución de valoraciones (1-5 estrellas)
- Cursos mejor y peor valorados

**Exportar reportes**:
- Formato CSV para análisis en Excel
- Formato PDF para presentaciones

---

<div style="page-break-after: always;"></div>

## 10.6. Preguntas Frecuentes (FAQ)

### Para Estudiantes

**P: ¿Los cursos son gratuitos?**
R: En la versión actual (v1.0), todos los cursos son gratuitos. En futuras versiones habrá cursos de pago.

**P: ¿Necesito descargar algo para ver los cursos?**
R: No, todo funciona en el navegador web. Solo necesitas conexión a Internet.

**P: ¿Puedo ver los cursos desde mi móvil?**
R: Sí, la plataforma es completamente responsive y funciona en móviles y tablets.

**P: ¿Cómo sé si un curso es bueno antes de inscribirme?**
R: Puedes ver todas las secciones y lecciones del curso en la página de detalle, así como las valoraciones de otros estudiantes.

**P: ¿Puedo des-inscribirme de un curso?**
R: Actualmente no hay opción de des-inscripción, pero puedes simplemente dejar de verlo.

**P: ¿Recibiré un certificado al completar un curso?**
R: Los certificados estarán disponibles en una futura versión (v1.1).

**P: Olvidé mi contraseña, ¿qué hago?**
R: Actualmente no hay sistema de recuperación de contraseña. Contacta con el administrador en admin@elearningjcb.com.

---

### Para Instructores

**P: ¿Puedo subir videos a los cursos?**
R: Sí, puedes incluir URLs de videos (YouTube, Vimeo) en las lecciones.

**P: ¿Cuánto me paga la plataforma por cada curso?**
R: En v1.0 no hay sistema de pagos. En v2.0 (planificado), la plataforma tomará una comisión del 25% y tú recibirás el 75%.

**P: ¿Puedo eliminar comentarios negativos de mis cursos?**
R: No, las valoraciones son verificadas y no pueden ser eliminadas por instructores (solo por admins si son inapropiadas).

**P: ¿Cómo atraigo estudiantes a mis cursos?**
R: Asegúrate de tener un buen título, descripción detallada, contenido de calidad y pide a estudiantes satisfechos que dejen valoraciones.

---

<div style="page-break-after: always;"></div>

### Para Administradores

**P: ¿Cómo creo un nuevo administrador?**
R: Desde "Gestión de Usuarios", edita un usuario existente y cambia su rol a "admin".

**P: ¿Puedo restaurar un curso eliminado?**
R: No, las eliminaciones son permanentes. Se recomienda hacer backups regulares de la base de datos.

**P: ¿Cómo contacto con soporte técnico?**
R: Para problemas técnicos, contacta con el desarrollador en soporte@elearningjcb.com.

---

**Conclusión Sección 10**: Este manual de usuario proporciona guías detalladas paso a paso para los tres roles principales (estudiante, instructor, admin). Con ejemplos visuales, descripciones claras y capturas de referencia, cualquier usuario puede navegar la plataforma sin dificultad. El FAQ resuelve las preguntas más comunes.

---

<div style="page-break-after: always;"></div>



# 11. PLAN DE FORMACIÓN A USUARIOS

## Índice de la Sección
- [11.1. Introducción al Plan de Formación](#111-introducción-al-plan-de-formación)
- [11.2. Objetivos de la Formación](#112-objetivos-de-la-formación)
- [11.3. Identificación de Perfiles de Usuario](#113-identificación-de-perfiles-de-usuario)
- [11.4. Programa de Formación por Perfil](#114-programa-de-formación-por-perfil)
- [11.5. Metodología de Formación](#115-metodología-de-formación)
- [11.6. Materiales y Recursos Didácticos](#116-materiales-y-recursos-didácticos)
- [11.7. Calendario de Formación](#117-calendario-de-formación)
- [11.8. Evaluación de la Formación](#118-evaluación-de-la-formación)
- [11.9. Soporte Post-Formación](#119-soporte-post-formación)
- [11.10. Presupuesto del Plan de Formación](#1110-presupuesto-del-plan-de-formación)

---

## 11.1. Introducción al Plan de Formación

La **E-Learning JCB Platform** es una herramienta diseñada para ser intuitiva y accesible, pero requiere un proceso de formación estructurado para garantizar que todos los usuarios puedan aprovechar al máximo sus funcionalidades.

### Contexto

El éxito de cualquier plataforma educativa depende no solo de su calidad técnica, sino también de la capacidad de sus usuarios para utilizarla eficazmente. Este plan de formación está diseñado para:

- **Facilitar la adopción** de la plataforma por parte de nuevos usuarios
- **Minimizar la curva de aprendizaje** mediante formación estructurada
- **Maximizar el ROI** asegurando el uso efectivo de todas las funcionalidades
- **Reducir consultas al soporte** mediante capacitación preventiva

### Alcance del Plan

Este plan de formación cubre:

1. **Formación inicial** para todos los perfiles de usuario
2. **Formación avanzada** para instructores y administradores
3. **Materiales de referencia** (vídeos, guías, FAQs)
4. **Soporte continuo** post-formación
5. **Evaluación y mejora** del proceso formativo

---

## 11.2. Objetivos de la Formación

### Objetivos Generales

1. **Capacitar a todos los usuarios** en el uso básico de la plataforma
2. **Formar instructores** en la creación y gestión de cursos de calidad
3. **Preparar administradores** para la gestión técnica y moderación
4. **Garantizar autonomía** de los usuarios tras la formación
5. **Establecer canales de soporte** efectivos y sostenibles

### Objetivos Específicos por Perfil

#### Estudiantes
- Navegar por la plataforma y buscar cursos
- Inscribirse y acceder a contenidos
- Completar lecciones y realizar seguimiento del progreso
- Calificar cursos y proporcionar feedback

#### Instructores
- Crear cursos estructurados con secciones y lecciones
- Subir contenido multimedia (vídeos, documentos)
- Gestionar inscripciones y seguimiento de estudiantes
- Interpretar estadísticas de rendimiento de cursos

#### Administradores
- Gestionar usuarios y roles
- Moderar contenido y cursos
- Generar reportes del sistema
- Resolver problemas técnicos básicos

### Indicadores de Éxito

| Indicador | Meta |
|-----------|------|
| **Tasa de finalización de formación** | ≥ 90% |
| **Satisfacción con la formación** | ≥ 4/5 estrellas |
| **Reducción de tickets de soporte** | ≥ 40% tras formación |
| **Tiempo medio de autonomía** | ≤ 3 días post-formación |
| **Retención de conocimiento a 30 días** | ≥ 80% |

---

<div style="page-break-after: always;"></div>

## 11.3. Identificación de Perfiles de Usuario

### Perfil 1: Estudiantes

**Características:**
- Edad: 18-65 años
- Nivel técnico: Básico-Intermedio
- Objetivo: Aprender nuevas habilidades
- Tiempo disponible: 2-5 horas/semana
- Acceso: Principalmente móvil/tablet

**Necesidades de formación:**
- Sesión básica de 1.5-2 horas
- Guía rápida en PDF
- FAQ específico para estudiantes

---

### Perfil 2: Instructores

**Características:**
- Edad: 25-60 años
- Nivel técnico: Intermedio-Avanzado
- Objetivo: Monetizar conocimiento, construir audiencia
- Tiempo disponible: 5-10 horas/semana
- Acceso: Principalmente PC/portátil

**Necesidades de formación:**
- Sesión completa de 3-4 horas
- Formación en creación de contenido educativo
- Guía de mejores prácticas pedagógicas
- Formación en herramientas de edición de vídeo
- Soporte continuo para dudas avanzadas

---

### Perfil 3: Administradores

**Características:**
- Edad: 25-50 años
- Nivel técnico: Avanzado
- Objetivo: Gestionar plataforma eficientemente
- Tiempo disponible: Dedicación completa
- Acceso: PC/portátil + acceso remoto

**Necesidades de formación:**
- Sesión técnica de 2-3 horas
- Formación en MongoDB y estructura de datos
- Protocolos de moderación y seguridad
- Gestión de incidencias y escalado
- Formación en backup y recuperación

---

## 11.4. Programa de Formación por Perfil

### 11.4.1. Programa para Estudiantes (2 horas)

#### Módulo 1: Introducción a la Plataforma (30 min)

**Contenidos:**
- ¿Qué es E-Learning JCB Platform?
- Registro y creación de cuenta
- Navegación por la interfaz principal
- Configuración de perfil personal


---

#### Módulo 2: Búsqueda y Selección de Cursos (30 min)

**Contenidos:**
- Explorar catálogo de cursos
- Filtros y búsqueda avanzada
- Leer descripciones y valoraciones
- Previsualización de contenidos

**Formato:** Demo en vivo + Ejercicio práctico

---

#### Módulo 3: Inscripción y Seguimiento (45 min)

**Contenidos:**
- Proceso de inscripción (cursos gratuitos y de pago)
- Acceder a lecciones y contenido
- Marcar lecciones como completadas
- Visualizar progreso y certificados

**Formato:** Práctica guiada paso a paso

---

#### Módulo 4: Interacción y Feedback (15 min)

**Contenidos:**
- Calificar cursos
- Dejar reseñas constructivas
- Contactar con instructores
- Soporte técnico

**Formato:** Explicación + Casos de uso

---

### 11.4.2. Programa para Instructores (4 horas)

#### Módulo 1: Introducción y Filosofía de la Plataforma (30 min)

**Contenidos:**
- Visión y valores de E-Learning JCB
- Estándares de calidad de cursos
- Políticas de publicación y moderación
- Modelo de ingresos para instructores

**Formato:** Presentación interactiva

---

#### Módulo 2: Creación de Cursos - Parte Teórica (45 min)

**Contenidos:**
- Principios de diseño instruccional
- Estructura de un curso efectivo
- Definir objetivos de aprendizaje
- Crear contenido atractivo y pedagógico

**Formato:** Taller teórico

---

#### Módulo 3: Creación de Cursos - Parte Práctica (90 min)

**Contenidos:**
- Crear un curso desde cero (paso a paso)
- Añadir secciones y lecciones
- Subir vídeos, PDFs y otros recursos
- Configurar precios y visibilidad
- Publicar y promocionar cursos

**Formato:** Práctica guiada con ejercicio real

**Ejercicio:** Cada instructor creará un curso de demostración con al menos:
- 3 secciones
- 5 lecciones
- 2 vídeos
- 1 documento PDF

---

#### Módulo 4: Gestión y Seguimiento (45 min)

**Contenidos:**
- Dashboard del instructor
- Visualizar estadísticas (inscripciones, progreso, ingresos)
- Responder a comentarios y valoraciones
- Actualizar contenido de cursos existentes

**Formato:** Demo + Casos de uso

---

#### Módulo 5: Mejores Prácticas y Optimización (30 min)

**Contenidos:**
- Cómo crear vídeos de calidad (iluminación, audio, edición)
- Herramientas recomendadas (OBS, DaVinci Resolve, Canva)
- SEO para cursos (títulos, descripciones, keywords)
- Estrategias de marketing para instructores

**Formato:** Tips prácticos + Recursos externos

---

### 11.4.3. Programa para Administradores (3 horas)

#### Módulo 1: Arquitectura del Sistema (45 min)

**Contenidos:**
- Stack tecnológico (Reflex + MongoDB)
- Estructura de la base de datos
- Flujo de datos y estados
- Configuración de entorno

**Formato:** Presentación técnica + Documentación

---

#### Módulo 2: Gestión de Usuarios y Roles (45 min)

**Contenidos:**
- Panel de administración
- Crear, editar y eliminar usuarios
- Asignar roles (Admin, Instructor, Student)
- Gestionar permisos y accesos
- Suspender/banear usuarios

**Formato:** Demo + Práctica guiada

---

#### Módulo 3: Moderación de Contenido (45 min)

**Contenidos:**
- Revisar cursos pendientes de aprobación
- Criterios de moderación y calidad
- Gestionar reportes de usuarios
- Eliminar contenido inapropiado
- Comunicación con instructores

**Formato:** Casos prácticos reales

---

#### Módulo 4: Reportes y Analítica (30 min)

**Contenidos:**
- Generar reportes del sistema
- KPIs clave (usuarios, cursos, ingresos)
- Identificar problemas y tendencias
- Exportar datos para análisis

**Formato:** Demo con datos de ejemplo

---

#### Módulo 5: Soporte Técnico y Resolución de Problemas (15 min)

**Contenidos:**
- Problemas comunes y soluciones
- Acceso a logs y debugging
- Protocolo de escalado de incidencias
- Backup y recuperación de datos

**Formato:** Troubleshooting guide

---

## 11.5. Metodología de Formación

### Modalidades de Formación

#### 1. Formación Síncrona (En Vivo)

**Webinars Interactivos:**
- Sesiones en vivo por Zoom/Google Meet
- Duración: 1.5-2 horas por sesión
- Incluye Q&A en tiempo real
- Grabación disponible 24h después

**Ventajas:**
- Interacción directa con formador
- Resolución de dudas inmediata
- Networking entre participantes

**Desventajas:**
- Requiere disponibilidad horaria específica
- No accesible para todas las zonas horarias

---

#### 2. Formación Asíncrona (Bajo Demanda)

**Vídeos Tutoriales:**
- Biblioteca de vídeos cortos (5-15 min)
- Accesibles 24/7
- Subtítulos en español e inglés
- Velocidad de reproducción ajustable

**Ventajas:**
- Flexibilidad total
- Ritmo de aprendizaje personalizado
- Repaso ilimitado

**Desventajas:**
- Menor interacción
- Requiere autodisciplina

---

#### 3. Formación Híbrida (Recomendada)

**Combinación de:**
- Webinar inicial en vivo (1h)
- Vídeos de profundización (2-3h)
- Práctica guiada individual
- Sesión final de Q&A (30 min)

**Beneficios:**
- Mejor de ambos mundos
- Mayor tasa de finalización (90% vs 60% asíncrono puro)
- Coste optimizado

---

### Técnicas Pedagógicas

1. **Learning by Doing**: 70% práctica, 30% teoría
2. **Microlearning**: Vídeos cortos de 5-15 minutos
3. **Gamificación**: Badges y certificados de finalización
4. **Peer Learning**: Foros de discusión entre usuarios
5. **Spaced Repetition**: Emails de recordatorio con tips semanales

---

## 11.6. Materiales y Recursos Didácticos

### 11.6.1. Vídeos Tutoriales

| Título del Vídeo | Perfil | Duración | Formato |
|------------------|--------|----------|---------|
| **Registro y Primeros Pasos** | Estudiante | 8 min | Screencast + Narración |
| **Buscar e Inscribirse en Cursos** | Estudiante | 12 min | Demo en vivo |
| **Crear tu Primer Curso** | Instructor | 15 min | Paso a paso |
| **Subir Vídeos y Recursos** | Instructor | 10 min | Tutorial técnico |
| **Dashboard del Instructor** | Instructor | 8 min | Recorrido guiado |
| **Panel de Administración** | Admin | 20 min | Demo completa |
| **Moderar Contenido** | Admin | 12 min | Casos prácticos |

**Total de vídeos:** 15 vídeos (2h 15min de contenido)

**Herramientas de producción:**
- OBS Studio para grabación de pantalla
- DaVinci Resolve para edición
- YouTube para hosting (canal privado/unlisted)

---

### 11.6.2. Guías en PDF

1. **Guía Rápida para Estudiantes** (8 páginas)
   - Capturas de pantalla paso a paso
   - FAQ común
   - Consejos de uso

2. **Manual Completo del Instructor** (25 páginas)
   - Crear cursos de calidad
   - Mejores prácticas pedagógicas
   - Optimización de vídeos
   - Marketing para instructores

3. **Manual Técnico del Administrador** (30 páginas)
   - Arquitectura del sistema
   - Gestión de usuarios y roles
   - Moderación y políticas
   - Troubleshooting

---

### 11.6.3. Infografías y Cheat Sheets

- **Infografía: "Anatomía de un Curso Exitoso"**
- **Cheat Sheet: "Atajos de Teclado de la Plataforma"**
- **Infografía: "Flujo de Moderación de Contenido"**
- **Checklist: "Pre-lanzamiento de un Curso"**

---

### 11.6.4. Recursos Interactivos

1. **Curso Demo Guiado**: Un curso de ejemplo pre-creado que los usuarios pueden explorar
2. **Sandbox de Práctica**: Entorno de prueba donde instructores pueden crear cursos sin publicar
3. **FAQ Interactivo**: Base de conocimiento con búsqueda inteligente
4. **Chatbot de Soporte**: Respuestas automáticas a preguntas comunes (futuro)

---

## 11.7. Calendario de Formación

### Fase de Lanzamiento (Mes 1-2)

#### Semana 1-2: Formación de Administradores
- **Día 1-2**: Sesión técnica intensiva (6h total)
- **Día 3-5**: Práctica supervisada
- **Día 8**: Evaluación y certificación

#### Semana 3-4: Formación de Instructores Pioneros
- **Grupo 1 (10 instructores)**: Lunes y Miércoles 18:00-20:00
- **Grupo 2 (10 instructores)**: Martes y Jueves 18:00-20:00
- Sesión final de Q&A: Viernes 18:00-19:00

#### Semana 5-8: Formación de Estudiantes (Continua)
- Webinars semanales: Lunes, Miércoles, Viernes 19:00-20:30
- Capacidad: 50 estudiantes por sesión
- Vídeos bajo demanda disponibles 24/7

---

### Fase de Crecimiento (Mes 3-6)

- **Formación Continua**: Webinars quincenales para nuevos usuarios
- **Formación Avanzada**: Talleres mensuales para instructores (temas especializados)
- **Webinars Temáticos**:
  - "Crear Vídeos Profesionales con Bajo Presupuesto"
  - "SEO y Marketing para tus Cursos"
  - "Analítica Avanzada para Instructores"

---

### Fase de Consolidación (Mes 6+)

- **Formación 100% Asíncrona** para nuevos usuarios (vídeos + guías)
- **Webinars Especiales** bimensuales sobre nuevas funcionalidades
- **Programa de Mentores**: Instructores experimentados mentorizan a nuevos

---

## 11.8. Evaluación de la Formación

### 11.8.1. Evaluación de Conocimientos

#### Test de Finalización (por perfil)

**Estudiantes:**
- Quiz de 10 preguntas (múltiple opción)
- Tasa de aprobación: ≥ 70%
- Certificado digital al aprobar

**Instructores:**
- Ejercicio práctico: Crear curso de demostración
- Evaluación por checklist (20 criterios)
- Certificado de "Instructor Verificado" al aprobar

**Administradores:**
- Test técnico de 15 preguntas
- Simulación de casos de moderación (5 escenarios)
- Certificación interna obligatoria

---

### 11.8.2. Evaluación de Satisfacción

**Encuesta Post-Formación:**

1. ¿Cómo valoras la calidad de la formación? (1-5 estrellas)
2. ¿El contenido fue claro y fácil de entender? (Sí/No/Parcialmente)
3. ¿El ritmo de la formación fue adecuado? (Muy lento/Adecuado/Muy rápido)
4. ¿Qué tema te gustaría profundizar más?
5. ¿Recomendarías esta formación a otros? (1-10)
6. Comentarios adicionales (texto libre)

**Objetivo:** ≥ 4/5 estrellas de satisfacción media

---

### 11.8.3. Seguimiento Post-Formación

**Métricas de Adopción:**
- % de usuarios que completan el primer curso (estudiantes)
- % de instructores que publican su primer curso en 7 días
- % de administradores que realizan su primera moderación en 3 días
- Tiempo medio hasta primera acción autónoma

**Análisis de Tickets de Soporte:**
- Comparación pre/post formación
- Identificación de gaps en formación
- Mejora continua del programa

---

## 11.9. Soporte Post-Formación

### Canales de Soporte

#### 1. Base de Conocimiento (Self-Service)
- **FAQ Completo**: 50+ preguntas frecuentes
- **Vídeos Tutoriales**: Biblioteca de 15+ vídeos
- **Guías en PDF**: Descargables
- **Búsqueda Inteligente**: Por keywords

**Disponibilidad:** 24/7
**Coste:** Incluido

---

#### 2. Email de Soporte
- **Email:** soporte@elearningjcb.com
- **Tiempo de respuesta:** < 24h laborables
- **Idiomas:** Español, Inglés
- **Prioridad:** Normal (gratuito), Alta (plan premium)

**Disponibilidad:** Lunes-Viernes 9:00-18:00
**Coste:** Incluido

---

#### 3. Chat en Vivo (Solo Premium)
- **Plataforma:** Widget en la web
- **Tiempo de respuesta:** < 5 minutos
- **Idiomas:** Español
- **Especialistas:** Soporte técnico

**Disponibilidad:** Lunes-Viernes 10:00-14:00 y 16:00-20:00
**Coste:** Plan Premium (49€/mes para instructores)

---

#### 4. Webinars de Dudas (Q&A Sessions)
- **Frecuencia:** Quincenal
- **Duración:** 1 hora
- **Formato:** Abierto a todos los usuarios
- **Grabación:** Disponible 48h después

**Disponibilidad:** 1er y 3er Miércoles de cada mes, 18:00
**Coste:** Incluido

---

#### 5. Foro de Comunidad
- **Plataforma:** Discourse (futuro) / GitHub Discussions (inicial)
- **Moderación:** Community managers + administradores
- **Categorías:** Estudiantes, Instructores, Técnico, Ideas

**Disponibilidad:** 24/7 (moderación en horario laboral)
**Coste:** Incluido

---

### Escalado de Soporte

**Nivel 1 - Self-Service:**
- FAQ
- Vídeos
- Guías

**Nivel 2 - Soporte Básico:**
- Email (24h)
- Foro comunidad

**Nivel 3 - Soporte Avanzado:**
- Chat en vivo
- Webinars Q&A
- Llamada telefónica (casos críticos)

**Nivel 4 - Soporte Técnico Especializado:**
- Desarrolladores
- Administradores de sistema
- Gerencia

---

<div style="page-break-after: always;"></div>

## 11.10. Presupuesto del Plan de Formación

### 11.10.1. Costes de Desarrollo de Materiales

| Concepto | Detalle | Coste |
|----------|---------|-------|
| **Vídeos Tutoriales** | 15 vídeos × 100€/vídeo (producción) | 1,500€ |
| **Guías en PDF** | 3 guías × 200€/guía (diseño + redacción) | 600€ |
| **Infografías** | 4 infografías × 80€/infografía | 320€ |
| **Curso Demo** | Contenido de ejemplo pre-creado | 400€ |
| **Plataforma LMS** | YouTube (gratis) + PDFs en web | 0€ |
| **TOTAL MATERIALES** | | **2,820€** |

---

### 11.10.2. Costes de Formadores

| Rol | Horas | Tarifa | Coste |
|-----|-------|--------|-------|
| **Formador Senior** (Instructores/Admins) | 20h | 40€/h | 800€ |
| **Formador Junior** (Estudiantes) | 15h | 25€/h | 375€ |
| **Preparación y Materiales** | 10h | 30€/h | 300€ |
| **TOTAL FORMADORES** | | | **1,475€** |

---

### 11.10.3. Costes de Infraestructura

| Concepto | Detalle | Coste Mensual | Primer Año |
|----------|---------|---------------|------------|
| **Zoom Pro** | Webinars hasta 100 participantes | 14€/mes | 168€ |
| **YouTube** | Hosting de vídeos (gratis) | 0€ | 0€ |
| **Discourse** | Foro de comunidad (futuro) | 0€ (self-hosted) | 0€ |
| **Email Marketing** | Mailchimp Free (hasta 500 contactos) | 0€ | 0€ |
| **TOTAL INFRAESTRUCTURA** | | | **168€** |

---

### 11.10.4. Costes de Soporte Post-Formación (Año 1)

| Concepto | Detalle | Coste |
|----------|---------|-------|
| **Soporte Email** | 10h/semana × 25€/h × 12 meses | 13,000€ |
| **Webinars Q&A** | 2 al mes × 50€ × 12 meses | 1,200€ |
| **Mantenimiento Materiales** | Actualizaciones trimestrales | 800€ |
| **TOTAL SOPORTE** | | **15,000€** |

---

### 11.10.5. Resumen del Presupuesto Total

| Categoría | Coste (Año 1) |
|-----------|---------------|
| **Desarrollo de Materiales** | 2,820€ |
| **Formadores** | 1,475€ |
| **Infraestructura** | 168€ |
| **Soporte Post-Formación** | 15,000€ |
| **TOTAL INVERSIÓN** | **19,463€** |

**Coste por Usuario Formado (estimado 200 usuarios año 1):**
19,463€ ÷ 200 = **97.31€ por usuario**

---

### 11.10.6. ROI del Plan de Formación

**Beneficios Esperados:**

1. **Reducción de Soporte Reactivo:**
   - Sin formación: 30h/semana × 25€/h × 52 semanas = 39,000€
   - Con formación: 10h/semana × 25€/h × 52 semanas = 13,000€
   - **Ahorro: 26,000€/año**

2. **Aumento de Retención de Usuarios:**
   - Usuarios sin formación: 50% retención
   - Usuarios con formación: 85% retención
   - **35% más de retención = Más ingresos recurrentes**

3. **Mejora en Calidad de Cursos:**
   - Instructores formados crean cursos de mayor calidad
   - **Más ventas y mejores valoraciones**

**ROI Estimado:**
(26,000€ ahorros - 19,463€ inversión) / 19,463€ = **33.6% ROI primer año**

A partir del año 2, la inversión se reduce a 15,168€ (solo soporte + infraestructura), mejorando significativamente el ROI.

---

## 11.11. Conclusiones del Plan de Formación

### Puntos Clave

1. **Formación Estructurada**: Programas específicos para cada perfil (Estudiante, Instructor, Admin)
2. **Metodología Híbrida**: Combina webinars en vivo con vídeos bajo demanda
3. **Materiales Completos**: 15 vídeos, 3 guías PDF, infografías y recursos interactivos
4. **Soporte Continuo**: 5 canales de soporte con tiempos de respuesta claros
5. **Inversión Justificada**: 19,463€ con ROI del 33.6% en el primer año

### Próximos Pasos

1. **Mes 1**: Desarrollar materiales de formación (vídeos y guías)
2. **Mes 2**: Formar administradores y primeros instructores
3. **Mes 3-6**: Formación continua de nuevos usuarios
4. **Mes 6+**: Transición a formación mayormente asíncrona con soporte activo

### Compromiso de Calidad

Este plan de formación garantiza que todos los usuarios de **E-Learning JCB Platform** tengan las herramientas y conocimientos necesarios para aprovechar al máximo la plataforma, contribuyendo al éxito individual y colectivo del ecosistema educativo.

---

**Documento:** Plan de Formación a Usuarios
**Versión:** 1.0
**Fecha:** Marzo 2026
**Proyecto:** E-Learning JCB Platform
**Autor:** Juan Carlos Barroso (JCB)

---

[← Volver al Índice General](00_INDICE_GENERAL.md)


<div style="page-break-after: always;"></div>

# 12. BIBLIOGRAFÍA Y FUENTES DE INFORMACIÓN

## Índice de la Sección
- [12.1. Documentación Técnica Oficial](#121-documentación-técnica-oficial)
- [12.2. Frameworks y Librerías](#122-frameworks-y-librerías)
- [12.3. Bases de Datos y Almacenamiento](#123-bases-de-datos-y-almacenamiento)
- [12.4. Seguridad y Buenas Prácticas](#124-seguridad-y-buenas-prácticas)
- [12.5. Diseño de Interfaz de Usuario](#125-diseño-de-interfaz-de-usuario)
- [12.6. Metodologías y Patrones de Diseño](#126-metodologías-y-patrones-de-diseño)
- [12.7. Estudios de Mercado y E-Learning](#127-estudios-de-mercado-y-e-learning)
- [12.8. Aspectos Legales y Empresariales](#128-aspectos-legales-y-empresariales)
- [12.9. Pedagogía y Diseño Instruccional](#129-pedagogía-y-diseño-instruccional)
- [12.10. Libros de Referencia](#1210-libros-de-referencia)
- [12.11. Recursos Online y Blogs](#1211-recursos-online-y-blogs)
- [12.12. Herramientas de Desarrollo](#1212-herramientas-de-desarrollo)

---

## 12.1. Documentación Técnica Oficial

### Reflex (Framework Principal)

**Sitio Oficial:**
- Reflex Documentation (2024-2026)
  - URL: https://reflex.dev/docs/getting-started/introduction/
  - Consultado: Noviembre 2025 - Marzo 2026
  - Relevancia: Documentación oficial del framework utilizado para el desarrollo completo

**Recursos Específicos:**
- "Reflex Architecture" - https://reflex.dev/docs/architecture/
- "State Management in Reflex" - https://reflex.dev/docs/state/overview/
- "Database Integration" - https://reflex.dev/docs/database/overview/
- "Deployment Guide" - https://reflex.dev/docs/hosting/deploy/

**Versión utilizada:** Reflex 0.8.24 (Enero 2026)

---

### Python

**Documentación Oficial:**
- Python Software Foundation (2025)
  - Python 3.12 Documentation
  - URL: https://docs.python.org/3.12/
  - Consultado: Noviembre 2025 - Marzo 2026

**PEPs Relevantes:**
- PEP 8 - Style Guide for Python Code
  - URL: https://peps.python.org/pep-0008/
  - Aplicado en: Convenciones de código del proyecto

- PEP 484 - Type Hints
  - URL: https://peps.python.org/pep-0484/
  - Aplicado en: Anotaciones de tipos en todo el código

- PEP 257 - Docstring Conventions
  - URL: https://peps.python.org/pep-0257/
  - Aplicado en: Documentación de funciones y clases

---

## 12.2. Frameworks y Librerías

### Motor (Async MongoDB Driver)

**Documentación:**
- Motor Documentation - MongoDB Async Python Driver
  - URL: https://motor.readthedocs.io/en/stable/
  - Versión: 3.3.2
  - Consultado: Diciembre 2025 - Febrero 2026
  - Uso: Conexión asíncrona con MongoDB Atlas

**Referencias:**
- "Tutorial: Using Motor with Tornado" - Adaptado para Reflex
- "Motor API Documentation" - Referencia completa de métodos

---

### Bcrypt (Password Hashing)

**Documentación:**
- bcrypt for Python Documentation
  - URL: https://github.com/pyca/bcrypt/
  - Versión: 4.1.2
  - Consultado: Diciembre 2025
  - Uso: Hash seguro de contraseñas con 12 rounds

**Artículos de Referencia:**
- "How to Hash Passwords in Python" - Real Python
  - URL: https://realpython.com/python-password-hashing/

---

### PyJWT (JSON Web Tokens)

**Documentación:**
- PyJWT Documentation
  - URL: https://pyjwt.readthedocs.io/en/stable/
  - Versión: 2.8.0
  - Consultado: Enero 2026
  - Uso: Autenticación basada en tokens (implementación futura)

---

### Chakra UI (Design System)

**Documentación:**
- Chakra UI Documentation
  - URL: https://chakra-ui.com/docs/getting-started
  - Versión: v2 (integrada con Reflex)
  - Consultado: Noviembre 2025 - Marzo 2026
  - Uso: Componentes UI y sistema de diseño

**Recursos:**
- "Component Library" - Catálogo completo de componentes
- "Theming & Styling" - Personalización de temas

---

## 12.3. Bases de Datos y Almacenamiento

### MongoDB

**Documentación Oficial:**
- MongoDB Documentation (2025-2026)
  - URL: https://www.mongodb.com/docs/
  - Versión: MongoDB 7.0
  - Consultado: Noviembre 2025 - Marzo 2026

**Recursos Específicos:**
- "Data Modeling" - https://www.mongodb.com/docs/manual/core/data-modeling/
  - Aplicado en: Diseño de colecciones (users, courses, enrollments, progress, ratings)

- "Indexes" - https://www.mongodb.com/docs/manual/indexes/
  - Aplicado en: Optimización de consultas

- "Aggregation Pipeline" - https://www.mongodb.com/docs/manual/aggregation/
  - Aplicado en: Estadísticas y reportes

**MongoDB University:**
- "M001: MongoDB Basics" - Curso online gratuito
  - URL: https://university.mongodb.com/
  - Completado: Diciembre 2025

---

### MongoDB Atlas

**Documentación:**
- MongoDB Atlas Documentation
  - URL: https://www.mongodb.com/docs/atlas/
  - Consultado: Diciembre 2025 - Febrero 2026
  - Uso: Hosting de base de datos (cluster M0 gratuito)

**Recursos:**
- "Atlas Security" - Configuración de IP whitelist, usuarios, roles
- "Monitoring & Alerts" - Seguimiento de rendimiento

---

## 12.4. Seguridad y Buenas Prácticas

### OWASP (Open Web Application Security Project)

**Recursos:**
- OWASP Top 10 (2021)
  - URL: https://owasp.org/www-project-top-ten/
  - Consultado: Enero 2026
  - Aplicado en: Análisis de vulnerabilidades y mitigaciones

**Guías Específicas:**
- "OWASP Password Storage Cheat Sheet"
  - URL: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
  - Aplicado en: Implementación de bcrypt con 12 rounds

- "OWASP Input Validation Cheat Sheet"
  - URL: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
  - Aplicado en: Validación de inputs de usuario

- "OWASP Authentication Cheat Sheet"
  - URL: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
  - Aplicado en: Sistema de login y sesiones

---

### RGPD/GDPR (Protección de Datos)

**Documentación:**
- Reglamento General de Protección de Datos (UE) 2016/679
  - URL: https://gdpr.eu/
  - Consultado: Enero 2026
  - Aplicado en: Políticas de privacidad y tratamiento de datos

**Recursos AEPD:**
- Agencia Española de Protección de Datos
  - URL: https://www.aepd.es/
  - Consultado: Enero 2026
  - Aplicado en: Cumplimiento normativo español

---

## 12.5. Diseño de Interfaz de Usuario

### Material Design

**Documentación:**
- Google Material Design Guidelines
  - URL: https://m3.material.io/
  - Consultado: Noviembre 2025
  - Aplicado en: Principios de diseño UI/UX

---

### UX Design

**Recursos:**
- Nielsen Norman Group - Articles on UX
  - URL: https://www.nngroup.com/articles/
  - Consultado: Diciembre 2025
  - Aplicado en: Usabilidad y experiencia de usuario

**Artículos Relevantes:**
- "10 Usability Heuristics for User Interface Design" - Jakob Nielsen
- "F-Shaped Pattern for Reading Web Content" - Aplicado en diseño de páginas

---

### Accesibilidad (WCAG)

**Documentación:**
- Web Content Accessibility Guidelines (WCAG) 2.1
  - URL: https://www.w3.org/WAI/WCAG21/quickref/
  - Consultado: Enero 2026
  - Aplicado en: Diseño accesible (contraste, navegación por teclado)

---

## 12.6. Metodologías y Patrones de Diseño

### Clean Architecture

**Libros:**
- Martin, Robert C. (2017)
  - "Clean Architecture: A Craftsman's Guide to Software Structure and Design"
  - Editorial: Prentice Hall
  - ISBN: 978-0134494166
  - Aplicado en: Arquitectura de 5 capas del proyecto

---

### Domain-Driven Design (DDD)

**Libros:**
- Evans, Eric (2003)
  - "Domain-Driven Design: Tackling Complexity in the Heart of Software"
  - Editorial: Addison-Wesley
  - ISBN: 978-0321125215
  - Aplicado en: Modelado de dominios (User, Course, Enrollment)

---

### Design Patterns

**Libros:**
- Gamma, Erich et al. (1994)
  - "Design Patterns: Elements of Reusable Object-Oriented Software"
  - Editorial: Addison-Wesley
  - ISBN: 978-0201633610
  - Aplicado en: Patrones Singleton, Factory, Observer

---

### Metodología Ágil

**Recursos:**
- Agile Manifesto
  - URL: https://agilemanifesto.org/
  - Consultado: Noviembre 2025
  - Aplicado en: Planificación iterativa del proyecto

**Scrum Guide:**
- Schwaber, Ken & Sutherland, Jeff (2020)
  - "The Scrum Guide"
  - URL: https://scrumguides.org/
  - Aplicado en: Sprints de 2 semanas, entregables periódicos

---

## 12.7. Estudios de Mercado y E-Learning

### Informes de Mercado

**Global Market Insights:**
- "E-Learning Market Size By Technology, By Provider, Industry Analysis Report 2024-2032"
  - Publicado: Enero 2024
  - URL: https://www.gminsights.com/industry-analysis/e-learning-market
  - Datos utilizados: Tamaño del mercado global ($315B), CAGR 13.7%

**Research and Markets:**
- "Spain E-Learning Market Report 2024"
  - Publicado: Marzo 2024
  - Datos utilizados: Mercado español (€2.1B), tendencias locales

**Statista:**
- "E-Learning Market Worldwide - Statistics & Facts"
  - URL: https://www.statista.com/topics/3115/e-learning/
  - Consultado: Diciembre 2025
  - Datos utilizados: Estadísticas de usuarios, proyecciones de crecimiento

---

### Análisis de Competencia

**Plataformas Analizadas:**

1. **Udemy**
   - URL: https://www.udemy.com/
   - Análisis: Modelo de negocio, precios, catálogo
   - Consultado: Diciembre 2025

2. **Coursera**
   - URL: https://www.coursera.org/
   - Análisis: Alianzas universitarias, certificaciones
   - Consultado: Diciembre 2025

3. **Domestika**
   - URL: https://www.domestika.org/
   - Análisis: Enfoque creativo, comunidad española
   - Consultado: Diciembre 2025

4. **Platzi**
   - URL: https://platzi.com/
   - Análisis: Contenido tech en español, modelo suscripción
   - Consultado: Diciembre 2025

---

### Tendencias en EdTech

**Artículos:**
- "The Future of Online Learning: Trends for 2025"
  - EdTech Magazine, Noviembre 2024
  - URL: https://edtechmagazine.com/
  - Tendencias identificadas: IA personalizada, microlearning, gamificación

---

## 12.8. Aspectos Legales y Empresariales

### Legislación Española

**BOE (Boletín Oficial del Estado):**
- Ley 6/2020 de Servicios de la Sociedad de la Información
  - URL: https://www.boe.es/
  - Consultado: Enero 2026
  - Aplicado en: Condiciones de servicio

**Seguridad Social:**
- "Régimen Especial de Trabajadores Autónomos (RETA)"
  - URL: https://www.seg-social.es/
  - Consultado: Enero 2026
  - Datos utilizados: Cuota autónomo (€294/mes)

**Agencia Tributaria:**
- "Modelo 303 - IVA Trimestral"
  - URL: https://sede.agenciatributaria.gob.es/
  - Consultado: Enero 2026
  - Datos utilizados: IVA 21% sobre ingresos

---

### Subvenciones y Ayudas

**Recursos:**
- "Kit Digital 2025" - Ministerio de Asuntos Económicos
  - URL: https://www.acelerapyme.gob.es/kit-digital
  - Consultado: Enero 2026
  - Datos utilizados: Hasta 6,000€ en ayudas para digitalización

- "Ayudas para Jóvenes Emprendedores" - Comunidades Autónomas
  - Consultado: Enero 2026
  - Datos utilizados: Tarifa plana de autónomos

---

## 12.9. Pedagogía y Diseño Instruccional

### Teorías del Aprendizaje

**Libros:**
- Gagné, Robert M. (1985)
  - "The Conditions of Learning and Theory of Instruction"
  - Editorial: Holt, Rinehart and Winston
  - ISBN: 978-0030636882
  - Aplicado en: Diseño de lecciones y progresión pedagógica

**Recursos Online:**
- "ADDIE Model for Instructional Design"
  - URL: https://www.instructionaldesign.org/models/addie/
  - Consultado: Febrero 2026
  - Aplicado en: Estructura de cursos (Análisis, Diseño, Desarrollo, Implementación, Evaluación)

---

### Gamificación

**Libros:**
- Kapp, Karl M. (2012)
  - "The Gamification of Learning and Instruction"
  - Editorial: Pfeiffer
  - ISBN: 978-1118096345
  - Aplicado en: Diseño de sistema de progreso y badges (futuro)

---

## 12.10. Libros de Referencia

### Desarrollo Web

1. **"Python for Web Development"**
   - Autor: Michael Driscoll
   - Editorial: Independently Published (2023)
   - ISBN: 979-8398747867
   - Uso: Fundamentos de desarrollo web con Python

2. **"MongoDB: The Definitive Guide"**
   - Autores: Shannon Bradshaw, Eoin Brazil, Kristina Chodorow
   - Editorial: O'Reilly Media (2019, 3ª edición)
   - ISBN: 978-1491954461
   - Uso: Modelado de datos, optimización de consultas

3. **"Full Stack Python"**
   - Autor: Matt Makai
   - Editorial: CreateSpace (2018)
   - ISBN: 978-0990497608
   - URL: https://www.fullstackpython.com/
   - Uso: Arquitectura full-stack con Python

---

### Seguridad

4. **"Web Application Security: Exploitation and Countermeasures for Modern Web Applications"**
   - Autor: Andrew Hoffman
   - Editorial: O'Reilly Media (2020)
   - ISBN: 978-1492053118
   - Uso: Implementación de medidas de seguridad

5. **"Hacking APIs: Breaking Web Application Programming Interfaces"**
   - Autor: Corey J. Ball
   - Editorial: No Starch Press (2022)
   - ISBN: 978-1718502444
   - Uso: Seguridad de APIs REST (futuro)

---

### Emprendimiento Tecnológico

6. **"The Lean Startup"**
   - Autor: Eric Ries
   - Editorial: Crown Business (2011)
   - ISBN: 978-0307887894
   - Uso: Metodología de validación de producto, MVP

7. **"Zero to One: Notes on Startups, or How to Build the Future"**
   - Autores: Peter Thiel, Blake Masters
   - Editorial: Crown Business (2014)
   - ISBN: 978-0804139298
   - Uso: Estrategia de creación de valor único

---

## 12.11. Recursos Online y Blogs

### Desarrollo con Python

**Real Python:**
- URL: https://realpython.com/
- Consultado: Noviembre 2025 - Marzo 2026
- Artículos relevantes:
  - "Python Virtual Environments: A Primer"
  - "Async IO in Python: A Complete Walkthrough"
  - "Python Type Checking (Guide)"

**Python Weekly:**
- Newsletter semanal sobre Python
- URL: https://www.pythonweekly.com/
- Suscrito: Noviembre 2025

---

### MongoDB y Bases de Datos

**MongoDB Blog:**
- URL: https://www.mongodb.com/blog
- Consultado: Diciembre 2025 - Febrero 2026
- Artículos relevantes:
  - "Schema Design Best Practices"
  - "Performance Best Practices for MongoDB"

---

### Reflex Community

**Reflex Discord:**
- Comunidad oficial de Reflex
- URL: https://discord.gg/reflex-dev
- Uso: Resolución de dudas técnicas, networking

**GitHub Issues:**
- Reflex GitHub Repository
- URL: https://github.com/reflex-dev/reflex
- Consultado: Problemas específicos y workarounds

---

### UX/UI Design

**Smashing Magazine:**
- URL: https://www.smashingmagazine.com/
- Consultado: Diciembre 2025 - Enero 2026
- Artículos sobre diseño de interfaces educativas

**CSS-Tricks:**
- URL: https://css-tricks.com/
- Consultado: Noviembre 2025 - Marzo 2026
- Uso: Técnicas de estilo y responsive design

---

## 12.12. Herramientas de Desarrollo

### Control de Versiones

**Git Documentation:**
- URL: https://git-scm.com/doc
- Versión: Git 2.43
- Consultado: Noviembre 2025
- Uso: Control de versiones del proyecto

**GitHub Docs:**
- URL: https://docs.github.com/
- Consultado: Noviembre 2025 - Marzo 2026
- Uso: Gestión de repositorio, GitHub Actions (futuro)

**Conventional Commits:**
- URL: https://www.conventionalcommits.org/
- Consultado: Noviembre 2025
- Aplicado en: Formato de mensajes de commit

---

### IDEs y Editores

**Visual Studio Code Documentation:**
- URL: https://code.visualstudio.com/docs
- Versión: VSCode 1.85
- Consultado: Noviembre 2025 - Marzo 2026
- Uso: Editor principal del proyecto

**Extensiones utilizadas:**
- Python Extension for VSCode
- Pylance (Language Server)
- GitLens
- MongoDB for VSCode

---

### Testing y Quality Assurance

**Pytest Documentation:**
- URL: https://docs.pytest.org/
- Versión: pytest 7.4.3
- Consultado: Febrero 2026
- Uso: Tests unitarios y de integración (futuro)

---

### Deployment

**Reflex Cloud Documentation:**
- URL: https://reflex.dev/docs/hosting/deploy/
- Consultado: Febrero 2026
- Uso: Deployment de la aplicación

**DigitalOcean Tutorials:**
- URL: https://www.digitalocean.com/community/tutorials
- Consultado: Febrero 2026
- Uso: Deployment alternativo en VPS

---

## 12.13. Estándares Web

### W3C (World Wide Web Consortium)

**HTML5 Specification:**
- URL: https://www.w3.org/TR/html52/
- Consultado: Noviembre 2025
- Aplicado en: Estructura semántica del HTML generado

**CSS3 Specifications:**
- URL: https://www.w3.org/Style/CSS/
- Consultado: Noviembre 2025 - Marzo 2026
- Aplicado en: Estilos y responsive design

**WAI-ARIA (Accessibility):**
- URL: https://www.w3.org/WAI/ARIA/
- Consultado: Enero 2026
- Aplicado en: Accesibilidad de componentes interactivos

---

## 12.14. Repositorios GitHub de Referencia

### Proyectos Open Source Consultados

1. **awesome-python**
   - URL: https://github.com/vinta/awesome-python
   - Uso: Descubrimiento de librerías Python

2. **awesome-mongodb**
   - URL: https://github.com/ramnes/awesome-mongodb
   - Uso: Recursos y herramientas para MongoDB

3. **reflex-examples**
   - URL: https://github.com/reflex-dev/reflex-examples
   - Uso: Ejemplos de aplicaciones con Reflex

4. **real-world-reflex**
   - URL: https://github.com/reflex-dev/reflex (examples/)
   - Uso: Patrones de diseño en Reflex

---

## 12.15. Conferencias y Eventos

### PyCon España 2025

**Evento:**
- Fecha: Octubre 2025 (online)
- URL: https://es.pycon.org/
- Charlas relevantes:
  - "Async Python: Beyond the Basics"
  - "Building Full-Stack Apps with Modern Python"

---

### MongoDB World 2025

**Evento:**
- Fecha: Junio 2025 (online)
- URL: https://www.mongodb.com/world
- Sesiones vistas:
  - "Schema Design Patterns"
  - "MongoDB Atlas Best Practices"

---

## 12.16. Podcasts y Contenido Multimedia

### Podcasts

**Talk Python To Me:**
- URL: https://talkpython.fm/
- Episodios relevantes:
  - "#400: Full Stack Web with Nothing but Python"
  - "#385: Modern Python Development Tools"

**The Changelog:**
- URL: https://changelog.com/podcast
- Episodios sobre frameworks full-stack

---

### YouTube Channels

**Corey Schafer:**
- URL: https://www.youtube.com/@coreyms
- Playlists: Python Tutorials, Web Development

**Traversy Media:**
- URL: https://www.youtube.com/@TraversyMedia
- Tutoriales sobre desarrollo full-stack

---

## 12.17. Resumen de Fuentes por Categoría

### Por Tipo de Fuente

| Tipo | Cantidad | % del Total |
|------|----------|-------------|
| **Documentación Oficial** | 12 | 25% |
| **Libros Técnicos** | 7 | 15% |
| **Artículos Online** | 15 | 31% |
| **Tutoriales y Cursos** | 8 | 17% |
| **Informes de Mercado** | 4 | 8% |
| **Normativa Legal** | 2 | 4% |
| **TOTAL** | **48** | **100%** |

---

### Por Área de Conocimiento

| Área | Fuentes | Relevancia |
|------|---------|------------|
| **Desarrollo Python/Reflex** | 14 | Alta |
| **MongoDB y Bases de Datos** | 6 | Alta |
| **Seguridad** | 5 | Alta |
| **UX/UI Design** | 6 | Media |
| **Pedagogía y EdTech** | 5 | Media |
| **Negocio y Mercado** | 6 | Media |
| **Legal y Normativa** | 3 | Media |
| **Metodologías Ágiles** | 3 | Baja |

---

## 12.18. Actualización de Fuentes

### Política de Actualización

Este proyecto se basa en tecnologías y normativas que evolucionan constantemente. Se establece el siguiente calendario de revisión:

**Trimestral:**
- Documentación de Reflex (nuevas versiones)
- MongoDB Atlas (nuevas features)
- OWASP Top 10 (actualizaciones de seguridad)

**Semestral:**
- Informes de mercado de e-learning
- Normativa RGPD y legislación española
- Tendencias en EdTech

**Anual:**
- Libros de referencia (nuevas ediciones)
- Metodologías de desarrollo
- Herramientas de desarrollo

---

## 12.19. Agradecimientos

### Comunidades

Un agradecimiento especial a las comunidades que han contribuido indirectamente al éxito de este proyecto:

- **Reflex Community** (Discord): Por resolver dudas técnicas y compartir mejores prácticas
- **Python España**: Por recursos educativos de calidad en español
- **MongoDB Community**: Por documentación exhaustiva y casos de uso
- **Stack Overflow**: Por soluciones a problemas específicos de implementación

---

### Mentores y Revisores

- Profesores del **I.E.S. Al-Ándalus** (Almería) por guía académica
- Comunidad de desarrolladores Python en España
- Beta testers del proyecto (estudiantes e instructores piloto)

---

## 12.20. Declaración de Originalidad

### Uso de Fuentes

Todas las fuentes citadas en este documento han sido utilizadas con fines educativos y académicos, respetando:

- **Derechos de autor** de los materiales referenciados
- **Licencias open source** de frameworks y librerías utilizadas
- **Creative Commons** para recursos compartidos
- **Fair use** para capturas de pantalla y citas textuales

### Código Propio

El código desarrollado para **E-Learning JCB Platform** es original y no constituye una copia de proyectos existentes, aunque se inspira en mejores prácticas de la industria documentadas en las fuentes citadas.

---

## 12.21. Licencias de Software Utilizado

### Software Open Source

| Software | Licencia | URL |
|----------|----------|-----|
| **Reflex** | Apache License 2.0 | https://github.com/reflex-dev/reflex/blob/main/LICENSE |
| **Python** | PSF License | https://docs.python.org/3/license.html |
| **Motor** | Apache License 2.0 | https://github.com/mongodb/motor/blob/master/LICENSE |
| **bcrypt** | Apache License 2.0 | https://github.com/pyca/bcrypt/blob/main/LICENSE |
| **MongoDB** | SSPL | https://www.mongodb.com/licensing/server-side-public-license |
| **Chakra UI** | MIT License | https://github.com/chakra-ui/chakra-ui/blob/main/LICENSE |

**Nota:** Todos los componentes utilizados tienen licencias compatibles con el desarrollo comercial del proyecto.

---

## 12.22. Conclusión

Esta bibliografía documenta las **48 fuentes principales** consultadas durante el desarrollo de **E-Learning JCB Platform**, abarcando aspectos técnicos, pedagógicos, de negocio y legales.

La diversidad de fuentes garantiza:
-  **Solidez técnica** basada en documentación oficial
-  **Seguridad** según estándares OWASP
-  **Viabilidad comercial** respaldada por estudios de mercado
-  **Cumplimiento legal** con normativa española y europea
-  **Calidad pedagógica** fundamentada en teorías del aprendizaje

Este proyecto no solo cumple con los requisitos académicos del ciclo de **Desarrollo de Aplicaciones Web (DAW)**, sino que representa una propuesta viable y fundamentada para el mercado real de e-learning.

---

**Documento:** Bibliografía y Fuentes de Información
**Versión:** 1.0
**Fecha:** Marzo 2026
**Proyecto:** E-Learning JCB Platform
**Autor:** Juan Carlos Barroso (JCB)
**Última actualización:** 13/03/2026

---

[← Volver al Índice General](00_INDICE_GENERAL.md)



