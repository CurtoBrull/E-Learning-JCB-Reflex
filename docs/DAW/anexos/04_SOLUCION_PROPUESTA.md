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
- ✅ Comunidad muy grande y madura
- ✅ Abundancia de recursos y tutoriales
- ✅ Un solo lenguaje (JavaScript) en frontend y backend
- ✅ Librerías y paquetes npm para casi cualquier funcionalidad
- ✅ React para UI moderna y reactiva

**Desventajas**:
- ❌ Requiere configuración compleja (Webpack, Babel, etc.)
- ❌ Gestión de estado compleja (Redux, Context API)
- ❌ JavaScript es dinámicamente tipado (propenso a errores)
- ❌ Necesidad de frameworks adicionales para backend (Express, NestJS)
- ❌ Dos proyectos separados (frontend y backend) aumentan complejidad

**Tiempo estimado de desarrollo**: 9-12 meses
**Coste mensual de hosting**: 30-50€
**Curva de aprendizaje**: Media-Alta

---

#### Opción 2: **Django + React**

**Descripción**: Backend en Python (Django) + Frontend en React

**Ventajas**:
- ✅ Django es framework maduro con ORM potente
- ✅ Admin panel incluido de serie
- ✅ Seguridad robusta out-of-the-box
- ✅ Python es lenguaje popular y legible
- ✅ React para UI moderna

**Desventajas**:
- ❌ Dos lenguajes diferentes (Python backend, JavaScript frontend)
- ❌ Configuración de API REST (Django REST Framework) añade complejidad
- ❌ Despliegue más complejo (Gunicorn, Nginx)
- ❌ Gestión de estado en frontend sigue siendo compleja
- ❌ Mayor tiempo de configuración inicial

**Tiempo estimado de desarrollo**: 8-10 meses
**Coste mensual de hosting**: 40-70€
**Curva de aprendizaje**: Alta

---

#### Opción 3: **Laravel + Vue.js**

**Descripción**: Backend en PHP (Laravel) + Frontend en Vue.js

**Ventajas**:
- ✅ Laravel es framework PHP más popular
- ✅ Eloquent ORM intuitivo
- ✅ Ecosystem robusto (Forge, Vapor para deploy)
- ✅ Vue.js es más simple que React
- ✅ Blade templates para vistas mixtas

**Desventajas**:
- ❌ PHP tiene peor rendimiento que Python/Node.js
- ❌ Dos lenguajes (PHP backend, JavaScript frontend)
- ❌ Menor popularidad que MERN o Django
- ❌ Hosting PHP suele ser más costoso
- ❌ Configuración de SPA (Single Page App) compleja

**Tiempo estimado de desarrollo**: 8-11 meses
**Coste mensual de hosting**: 35-60€
**Curva de aprendizaje**: Media

---

#### Opción 4: **Reflex (Python Full-Stack)** ⭐ **SELECCIONADO**

**Descripción**: Framework full-stack en Python que genera React automáticamente

**Ventajas**:
- ✅ **Un solo lenguaje** (Python) para frontend y backend
- ✅ **Generación automática de React** desde código Python
- ✅ **Gestión de estado integrada** (sin Redux, sin Context API)
- ✅ **Configuración mínima** (sin Webpack, Babel, etc.)
- ✅ **Type hints nativos** en Python (detección de errores en desarrollo)
- ✅ **Componentes reutilizables** con sintaxis Python
- ✅ **Desarrollo 60% más rápido** que stacks tradicionales
- ✅ **Despliegue simplificado** con Reflex Cloud
- ✅ **Costes reducidos** de hosting (20-30€/mes)
- ✅ **Comunidad creciente** y documentación completa

**Desventajas**:
- ⚠️ Framework relativamente nuevo (v0.8, lanzado 2023)
- ⚠️ Comunidad más pequeña que MERN o Django
- ⚠️ Menos recursos de terceros (pero suficientes para el proyecto)
- ⚠️ Algunas features avanzadas en desarrollo

**Tiempo estimado de desarrollo**: 6 meses ✅
**Coste mensual de hosting**: 20-30€ ✅
**Curva de aprendizaje**: Baja (si se conoce Python) ✅

---

### 4.1.3. Comparativa de Bases de Datos

#### Opción 1: **PostgreSQL** (Relacional)

**Ventajas**:
- ✅ Base de datos SQL robusta y madura
- ✅ Relaciones complejas bien soportadas
- ✅ Transacciones ACID
- ✅ JSON support para flexibilidad

**Desventajas**:
- ❌ Esquema rígido (migraciones necesarias)
- ❌ Escalabilidad horizontal compleja
- ❌ Mayor complejidad en configuración
- ❌ Hosting más costoso

**Coste mensual**: 15-40€

---

#### Opción 2: **MySQL/MariaDB** (Relacional)

**Ventajas**:
- ✅ Base de datos SQL muy popular
- ✅ Buen rendimiento en lecturas
- ✅ Hosting económico disponible

**Desventajas**:
- ❌ Esquema rígido
- ❌ Menos features avanzadas que PostgreSQL
- ❌ Escalabilidad limitada
- ❌ JSON support limitado

**Coste mensual**: 10-30€

---

#### Opción 3: **MongoDB Atlas** (NoSQL) ⭐ **SELECCIONADO**

**Ventajas**:
- ✅ **Esquema flexible** (ideal para iteración rápida)
- ✅ **Escalabilidad horizontal** nativa (sharding)
- ✅ **Documentos JSON** que mapean directamente a modelos Python
- ✅ **MongoDB Atlas** (cloud) con tier gratuito M0
- ✅ **Respaldos automáticos** y alta disponibilidad
- ✅ **Driver asíncrono** (Motor) para alto rendimiento
- ✅ **Consultas potentes** con agregaciones
- ✅ **Indexación** eficiente para búsquedas

**Desventajas**:
- ⚠️ Menos adecuado para relaciones complejas (mitigado con referencias)
- ⚠️ Consistencia eventual en clusters distribuidos

**Coste mensual**:
- Tier M0 (desarrollo): **0€** ✅
- Tier M2 (producción pequeña): **9€**
- Tier M10 (producción media): **57€**

---

### 4.1.4. Matriz de Decisión Tecnológica

| Criterio | MERN | Django+React | Laravel+Vue | **Reflex+MongoDB** |
|----------|------|--------------|-------------|-------------------|
| Tiempo de desarrollo | 9-12 meses | 8-10 meses | 8-11 meses | **6 meses** ✅ |
| Curva de aprendizaje | Media-Alta | Alta | Media | **Baja** ✅ |
| Coste hosting/mes | 30-50€ | 40-70€ | 35-60€ | **20-30€** ✅ |
| Escalabilidad | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | **⭐⭐⭐⭐** |
| Rendimiento | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | **⭐⭐⭐⭐⭐** |
| Comunidad | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | **⭐⭐⭐** |
| Documentación | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | **⭐⭐⭐⭐** |
| Mantenibilidad | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | **⭐⭐⭐⭐⭐** |
| **PUNTUACIÓN TOTAL** | 29/40 | 33/40 | 26/40 | **35/40** ✅ |

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
| **SUBTOTAL (Desarrollo)** | | | **0€/mes** | **12€/año** ✅ |
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
- **Total cubierto**: 20,616€ ✅

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
- **Total cubierto**: 40,562€ ✅

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
| **Beneficio bruto** | **5,223€** ✅ |
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
| **Beneficio bruto** | **114,000€** ✅ |
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

**Total software obligatorio**: 0€ ✅
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

#### ✅ Recursos Disponibles (Sin Inversión)

- Portátil de desarrollo (ya disponible)
- Software (100% gratuito)
- Infraestructura desarrollo (MongoDB M0 + Reflex Cloud Free)
- Conocimientos de Python (ciclo DAW)

#### ⚠️ Recursos que Requieren Inversión Mínima

- Formación (190€) - **justificable por ROI en conocimiento**
- Infraestructura producción (360€/año) - **necesario para lanzamiento**
- Marketing (4,050€/año) - **opcional pero recomendado**

#### ✅ Recursos Cubiertos por Ayudas

- Tarifa plana autónomos: **2,676€ ahorro**
- Almería Emprende: **3,000€** (cubre infraestructura + formación + marketing parcial)
- Cheque Innovación: **1,500€** (servicios de asesoramiento)

---

**Conclusión de la Sección**:

La solución propuesta basada en **Reflex + MongoDB** es la opción más viable técnica y económicamente para el desarrollo de **E-Learning JCB Platform**. Con una inversión inicial mínima (1,190€ - 1,840€), costes recurrentes controlados (360€/año producción) y ayudas disponibles (7,176€ escenario conservador), el proyecto es **altamente viable** y presenta un **ROI positivo desde el Año 1** (25.3%).

---

<div style="page-break-after: always;"></div>
