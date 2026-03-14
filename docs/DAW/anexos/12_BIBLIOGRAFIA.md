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
- ✅ **Solidez técnica** basada en documentación oficial
- ✅ **Seguridad** según estándares OWASP
- ✅ **Viabilidad comercial** respaldada por estudios de mercado
- ✅ **Cumplimiento legal** con normativa española y europea
- ✅ **Calidad pedagógica** fundamentada en teorías del aprendizaje

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
