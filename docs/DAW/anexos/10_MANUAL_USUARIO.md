# 10. MANUAL DE USUARIO

## 10.1. Introducción para Usuarios

### 10.1.1. ¿Qué es E-Learning JCB Platform?

**E-Learning JCB Platform** es una plataforma web de formación online que permite a estudiantes acceder a cursos de calidad, a instructores compartir sus conocimientos y a administradores gestionar el sistema completo.

**Características principales**:
- 📚 **Catálogo de cursos** con información detallada
- 👤 **Perfiles de instructores** con estadísticas
- 📊 **Dashboard personalizado** según tu rol
- ✅ **Seguimiento de progreso** en tiempo real
- ⭐ **Sistema de valoraciones** transparente
- 🔒 **Acceso seguro** con autenticación robusta

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
- ✅ Google Chrome (versión 90+)
- ✅ Mozilla Firefox (versión 88+)
- ✅ Safari (versión 14+)
- ✅ Microsoft Edge (versión 90+)

**Dispositivos soportados**:
- 💻 Desktop (Windows, Mac, Linux)
- 📱 Tablet (iPad, Android)
- 📱 Móvil (iOS, Android)

---

## 10.2. Registro y Acceso a la Plataforma

### 10.2.1. Crear una Cuenta Nueva (Registro)

#### Paso 1: Acceder a la Página de Registro

1. Ir a https://elearningjcb.com
2. Click en el botón **"Registrarse"** en la esquina superior derecha

**Captura de pantalla** (referencia):
```
┌──────────────────────────────────────────────────────┐
│  [LOGO] E-Learning JCB    [Cursos] [Instructores]   │
│                                        [Registrarse] │
│                                              [Login] │
└──────────────────────────────────────────────────────┘
```

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
```
┌─────────────────────────────────────────────┐
│         Registro en E-Learning JCB          │
├─────────────────────────────────────────────┤
│                                             │
│  Nombre completo:                           │
│  [____________________________________]     │
│                                             │
│  Email:                                     │
│  [____________________________________]     │
│                                             │
│  Contraseña:                                │
│  [____________________________________]     │
│                                             │
│  Confirmar contraseña:                      │
│  [____________________________________]     │
│                                             │
│  Rol:                                       │
│  ( ) Estudiante  ( ) Instructor             │
│                                             │
│         [Registrarse]                       │
│                                             │
│  ¿Ya tienes cuenta? [Inicia sesión]        │
└─────────────────────────────────────────────┘
```

#### Paso 3: Verificación y Confirmación

1. Click en el botón **"Registrarse"**
2. Si hay errores, aparecerán mensajes en rojo:
   - ❌ "El email ya está registrado"
   - ❌ "Las contraseñas no coinciden"
   - ❌ "La contraseña debe tener al menos 6 caracteres"
3. Si todo es correcto:
   - ✅ Mensaje: "Registro exitoso. Redirigiendo..."
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
```
┌─────────────────────────────────────────────┐
│         Iniciar Sesión                      │
├─────────────────────────────────────────────┤
│                                             │
│  Email:                                     │
│  [____________________________________]     │
│                                             │
│  Contraseña:                                │
│  [____________________________________]     │
│                                             │
│  [✓] Recordarme                            │
│                                             │
│         [Iniciar Sesión]                    │
│                                             │
│  ¿Olvidaste tu contraseña? [Recuperar]     │
│  ¿No tienes cuenta? [Regístrate]           │
└─────────────────────────────────────────────┘
```

**Errores comunes**:
- ❌ "Email o contraseña incorrectos" → Verificar datos
- ❌ "Email no encontrado" → Registrarse primero

**Tras login exitoso**:
- ✅ Redirige a tu dashboard (estudiante/instructor/admin)
- ✅ Aparece tu nombre en la esquina superior derecha

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
```
┌──────────────────────────────────────────────────────┐
│  Catálogo de Cursos                                  │
├──────────────────────────────────────────────────────┤
│                                                      │
│  [Buscar cursos...........................]  [🔍]   │
│                                                      │
│  Filtros:                                            │
│  [Categoría ▼] [Nivel ▼] [Duración ▼] [Rating ▼]   │
└──────────────────────────────────────────────────────┘
```

**Cómo buscar**:
1. Escribir palabras clave en la barra de búsqueda (ej: "Python", "JavaScript")
2. Aplicar filtros:
   - **Nivel**: Principiante, Intermedio, Avanzado
   - **Duración**: 0-5h, 5-10h, 10-20h, +20h
   - **Valoración**: 4+ estrellas, 4.5+ estrellas
3. Los resultados se actualizan automáticamente

**Ejemplo de resultado**:
```
┌─────────────────────────────────────────────────────┐
│ [IMG] Python para Principiantes          ⭐ 4.8    │
│                                         (127 reseñas)│
│ Aprende Python desde cero con este curso...         │
│                                                      │
│ 👤 Juan Pérez | ⏱️ 12 horas | 📚 Principiante      │
│ 💰 99€                              [Ver Detalles]  │
└─────────────────────────────────────────────────────┘
```

---

### 10.3.2. Ver Detalles de un Curso

#### Información Disponible

Al hacer click en **"Ver Detalles"** en cualquier curso, se muestra:

**Sección 1: Hero del Curso**
- 📷 Imagen del curso
- 📝 Título completo
- ⭐ Valoración promedio + número de reseñas
- 👤 Nombre del instructor (clickeable)
- ⏱️ Duración total en horas
- 📚 Nivel (Principiante/Intermedio/Avanzado)
- 💰 Precio
- 🔘 Botón **"Inscribirse Ahora"** (destacado en verde)

**Sección 2: Descripción**
- Texto completo de descripción del curso
- Objetivos de aprendizaje
- Requisitos previos (si aplica)

**Sección 3: Contenido del Curso** ⭐ **DIFERENCIADOR CLAVE**
- **Todas las secciones y lecciones visibles** (acordeón desplegable)
- Duración de cada lección
- Orden claro de contenidos

**Ejemplo visual**:
```
┌──────────────────────────────────────────────────────┐
│  Contenido del Curso                                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│  ▼ Sección 1: Introducción a Python (3 lecciones)   │
│     1. ¿Qué es Python? (15 min)                     │
│     2. Instalación de Python (30 min)               │
│     3. Primer programa (45 min)                     │
│                                                      │
│  ▶ Sección 2: Variables y Tipos de Datos (5 lecc)   │
│                                                      │
│  ▶ Sección 3: Estructuras de Control (6 lecc)       │
└──────────────────────────────────────────────────────┘
```

**Sección 4: Reseñas de Estudiantes**
- Valoraciones con estrellas
- Comentarios textuales
- Nombre del estudiante y fecha

---

### 10.3.3. Inscribirse en un Curso

#### Proceso de Inscripción

**Paso 1**: Desde la página de detalle del curso, click en **"Inscribirse Ahora"**

**Paso 2**: Confirmación automática
- ✅ Mensaje: "Inscripción exitosa"
- El botón cambia a "Ya estás inscrito" (deshabilitado)
- Aparece opción "Ir a Dashboard" o "Comenzar Curso"

**Paso 3**: Acceso al curso
- El curso ahora aparece en tu **Dashboard de Estudiante**
- Puedes comenzar a ver lecciones inmediatamente

**Notas**:
- ✅ La inscripción es **instantánea** (sin proceso de pago en v1.0)
- ✅ No se permiten inscripciones duplicadas
- ⚠️ En futuras versiones habrá cursos de pago

---

### 10.3.4. Dashboard de Estudiante

#### Acceder al Dashboard

**Opción 1**: Tras iniciar sesión, automáticamente redirige al dashboard

**Opción 2**: Click en tu nombre > **"Dashboard"**

**URL**: https://elearningjcb.com/student/dashboard

---

#### Secciones del Dashboard

**1. Resumen de Estadísticas** (parte superior)
```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│      5      │ │      2      │ │      3      │
│   Cursos    │ │  Cursos     │ │   Cursos    │
│  Inscritos  │ │ Completados │ │ En Progreso │
└─────────────┘ └─────────────┘ └─────────────┘
```

**2. Mis Cursos** (sección principal)
- Lista de cursos inscritos
- Barra de progreso por curso
- Botón **"Continuar"** para retomar
- Botón **"Ver Certificado"** si completado (futuro)

**Ejemplo de curso en progreso**:
```
┌────────────────────────────────────────────────┐
│ Python para Principiantes                      │
│ ████████░░ 80% completado                      │
│                                                │
│ 👤 Juan Pérez | ⏱️ 12h | 📚 Principiante      │
│                                                │
│ Última lección: "Bucles while"                 │
│ Actualizado hace 2 días                        │
│                                                │
│         [Continuar Curso]                      │
└────────────────────────────────────────────────┘
```

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
2. ✅ Confirmación visual (checkmark verde)
3. El progreso del curso se actualiza automáticamente
4. Opción **"Siguiente Lección"** aparece

**Barra de progreso**:
- Se actualiza en tiempo real
- Ejemplo: "8/10 lecciones completadas (80%)"

---

### 10.3.6. Valorar un Curso

#### Cuándo Puedes Valorar

- ✅ Debes estar inscrito en el curso
- ⚠️ Idealmente, tras completar al menos 50% del curso
- ✅ Solo puedes valorar una vez por curso

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
│ │ Excelente curso, muy bien explicado...    │ │
│ │                                            │ │
│ └────────────────────────────────────────────┘ │
│                                                │
│           [Enviar Valoración]                  │
└────────────────────────────────────────────────┘
```

**Paso 4**: Click en **"Enviar Valoración"**
- ✅ Confirmación: "Valoración enviada con éxito"
- Tu valoración aparece en la lista de reseñas

---

### 10.3.7. Editar Perfil de Estudiante

**Acceso**: Click en tu nombre > **"Perfil"**

**Campos editables**:
- Nombre completo
- Biografía (opcional, hasta 500 caracteres)
- Cambiar contraseña

**Ejemplo**:
```
┌──────────────────────────────────────────────────┐
│  Mi Perfil                                       │
├──────────────────────────────────────────────────┤
│                                                  │
│  Nombre:                                         │
│  [María López García________________]            │
│                                                  │
│  Email:                                          │
│  maria.lopez@example.com (no editable)           │
│                                                  │
│  Rol: Estudiante                                 │
│                                                  │
│  Biografía:                                      │
│  ┌──────────────────────────────────────────┐   │
│  │ Apasionada por la programación...        │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
│         [Guardar Cambios]                        │
│                                                  │
│  ─────────────────────────────────────────────   │
│                                                  │
│  Cambiar Contraseña                              │
│  Contraseña actual:   [_______________]          │
│  Nueva contraseña:    [_______________]          │
│  Confirmar:           [_______________]          │
│                                                  │
│         [Cambiar Contraseña]                     │
└──────────────────────────────────────────────────┘
```

---

## 10.4. Guía para Instructores

### 10.4.1. Dashboard de Instructor

**Acceso**: Tras login como instructor, automáticamente redirige

**URL**: https://elearningjcb.com/instructor/dashboard

---

#### Resumen de Estadísticas

```
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│      12      │ │     247      │ │     4.7      │
│    Cursos    │ │ Inscripciones│ │ Valoración   │
│   Creados    │ │    Totales   │ │   Promedio   │
└──────────────┘ └──────────────┘ └──────────────┘
```

**Información mostrada**:
- Total de cursos creados por ti
- Total de estudiantes inscritos en todos tus cursos
- Valoración promedio de todos tus cursos
- Ingresos totales (futuro, cuando haya pagos)

---

#### Mis Cursos (Tabla)

**Vista de tabla con acciones**:
```
┌─────────────────────────────────────────────────────────────────┐
│  Título                | Inscritos | Rating | Estado  | Acciones│
├─────────────────────────────────────────────────────────────────┤
│ Python para Principia..│    87     │ ⭐4.8  │ Activo  │ [Editar]│
│                        │           │        │         │ [Ver]   │
│                        │           │        │         │[Eliminar]│
├─────────────────────────────────────────────────────────────────┤
│ JavaScript Avanzado    │    45     │ ⭐4.9  │ Activo  │ [Editar]│
│                        │           │        │         │ [Ver]   │
│                        │           │        │         │[Eliminar]│
└─────────────────────────────────────────────────────────────────┘

                      [+ Crear Nuevo Curso]
```

---

### 10.4.2. Crear un Curso Completo

#### Paso 1: Acceder al Formulario de Creación

**Desde el dashboard de instructor**:
- Click en el botón **"+ Crear Nuevo Curso"**

**URL**: https://elearningjcb.com/instructor/courses/new

---

#### Paso 2: Información Básica del Curso

**Formulario - Paso 1**:
```
┌──────────────────────────────────────────────────┐
│  Crear Nuevo Curso - Paso 1: Información Básica │
├──────────────────────────────────────────────────┤
│                                                  │
│  Título del curso:                               │
│  [_________________________________________]     │
│  Ejemplo: "Python para Principiantes"            │
│                                                  │
│  Descripción:                                    │
│  ┌──────────────────────────────────────────┐   │
│  │ Describe de qué trata el curso...        │   │
│  │ (mínimo 50 caracteres)                   │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
│  Nivel:                                          │
│  ( ) Principiante  ( ) Intermedio  ( ) Avanzado  │
│                                                  │
│  Precio:                                         │
│  [______] €                                      │
│                                                  │
│  Duración estimada (horas):                      │
│  [______] horas                                  │
│                                                  │
│  URL de imagen:                                  │
│  [_________________________________________]     │
│  (opcional, se puede subir después)              │
│                                                  │
│              [Siguiente: Añadir Contenido]       │
└──────────────────────────────────────────────────┘
```

**Campos obligatorios**:
- ✅ Título (máximo 100 caracteres)
- ✅ Descripción (mínimo 50 caracteres)
- ✅ Nivel (seleccionar uno)
- ✅ Precio (puede ser 0 para cursos gratuitos)

---

#### Paso 3: Añadir Secciones

**Formulario - Paso 2**:
```
┌──────────────────────────────────────────────────┐
│  Crear Nuevo Curso - Paso 2: Contenido          │
├──────────────────────────────────────────────────┤
│                                                  │
│  📚 Sección 1                          [Eliminar]│
│                                                  │
│  Título de la sección:                           │
│  [Introducción a Python______________]           │
│                                                  │
│  Descripción breve:                              │
│  [Primeros pasos con Python_________]            │
│                                                  │
│  ─── Lecciones ───                               │
│                                                  │
│  📄 Lección 1.1                                  │
│  Título: [¿Qué es Python?__________]             │
│  Duración: [15] minutos                          │
│  Contenido:                                      │
│  ┌──────────────────────────────────────────┐   │
│  │ Python es un lenguaje de programación... │   │
│  └──────────────────────────────────────────┘   │
│                                       [Eliminar] │
│                                                  │
│         [+ Añadir Lección a Sección 1]          │
│                                                  │
│  ───────────────────────────────────────────────│
│                                                  │
│         [+ Añadir Nueva Sección]                │
│                                                  │
│         [Guardar Borrador]  [Publicar Curso]    │
└──────────────────────────────────────────────────┘
```

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
- ✅ Mensaje: "Curso publicado exitosamente"
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
- ✅ Los cambios son instantáneos
- ⚠️ Si el curso ya tiene estudiantes inscritos, se les notifica del cambio (futuro)

---

### 10.4.4. Ver Estadísticas de un Curso

**Desde el dashboard de instructor**:
1. Click en **"Ver"** del curso deseado
2. Se muestra la página de detalle con sección adicional: **"Estadísticas del Instructor"**

**Información mostrada**:
```
┌──────────────────────────────────────────────────┐
│  Estadísticas de "Python para Principiantes"     │
├──────────────────────────────────────────────────┤
│                                                  │
│  📊 Inscripciones: 87 estudiantes                │
│  ⭐ Valoración promedio: 4.8 (basado en 23 reseñas)│
│  ✅ Completado por: 45 estudiantes (52%)         │
│  📈 En progreso: 42 estudiantes (48%)            │
│                                                  │
│  ─── Inscripciones por mes ───                   │
│                                                  │
│  [Gráfico de barras o líneas]                   │
│                                                  │
│  ─── Valoraciones detalladas ───                 │
│                                                  │
│  ⭐⭐⭐⭐⭐ (5): 12 (52%)                         │
│  ⭐⭐⭐⭐   (4): 8  (35%)                         │
│  ⭐⭐⭐     (3): 3  (13%)                         │
│  ⭐⭐       (2): 0  (0%)                          │
│  ⭐         (1): 0  (0%)                          │
└──────────────────────────────────────────────────┘
```

---

### 10.4.5. Eliminar un Curso

**Proceso**:
1. Desde el dashboard, click en **"Eliminar"** en el curso deseado
2. Modal de confirmación:
   ```
   ┌──────────────────────────────────────┐
   │  ⚠️ Confirmar Eliminación            │
   ├──────────────────────────────────────┤
   │                                      │
   │  ¿Estás seguro de que quieres       │
   │  eliminar este curso?                │
   │                                      │
   │  "Python para Principiantes"         │
   │                                      │
   │  Esta acción NO se puede deshacer.   │
   │                                      │
   │  87 estudiantes están inscritos.     │
   │                                      │
   │    [Cancelar]  [Sí, Eliminar]       │
   └──────────────────────────────────────┘
   ```
3. Si se confirma:
   - El curso se elimina de la base de datos
   - Los estudiantes pierden acceso (se notifica por email - futuro)
   - No se puede recuperar

**Recomendación**: En lugar de eliminar, considera "despublicar" (opción futura) para que no sea visible pero mantenga datos.

---

## 10.5. Guía para Administradores

### 10.5.1. Dashboard de Administrador

**Acceso**: Solo usuarios con rol "admin"

**URL**: https://elearningjcb.com/admin/dashboard

**Protección**: Si intentas acceder sin ser admin, aparece:
```
┌──────────────────────────────────────────────────┐
│  ⛔ Acceso Denegado                              │
│                                                  │
│  No tienes permisos para acceder a esta página.  │
│  Se requiere rol: admin                          │
│                                                  │
│              [Volver al inicio]                  │
└──────────────────────────────────────────────────┘
```

---

#### Estadísticas Globales

```
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│     1,247    │ │      342     │ │      89      │ │     3,456    │
│   Usuarios   │ │    Cursos    │ │ Instructores │ │Inscripciones │
│   Totales    │ │   Activos    │ │   Activos    │ │   Totales    │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
```

---

### 10.5.2. Gestión de Usuarios

**Acceso**: Desde el dashboard admin, sección **"Gestión de Usuarios"**

**Tabla de usuarios**:
```
┌────────────────────────────────────────────────────────────────┐
│ Nombre          | Email               | Rol        | Acciones  │
├────────────────────────────────────────────────────────────────┤
│ María López     │ maria@example.com   │ Estudiante │ [Editar]  │
│                 │                     │            │ [Eliminar]│
├────────────────────────────────────────────────────────────────┤
│ Juan Pérez      │ juan@example.com    │ Instructor │ [Editar]  │
│                 │                     │            │ [Eliminar]│
├────────────────────────────────────────────────────────────────┤
│ Admin Principal │ admin@example.com   │ Admin      │ [Editar]  │
│                 │                     │            │ [Eliminar]│
└────────────────────────────────────────────────────────────────┘

    [Buscar usuarios...] [Filtrar por rol ▼] [+ Crear Usuario]
```

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
- ⚠️ **Cuidado**: Elimina también todas sus inscripciones, valoraciones, etc.

**4. Crear usuario manualmente**:
- Formulario igual que el registro público
- Útil para crear cuentas de prueba o admins adicionales

---

### 10.5.3. Moderación de Contenido

**Acceso**: Dashboard admin > **"Moderación de Cursos"**

**Lista de cursos pendientes de revisión** (futuro):
```
┌──────────────────────────────────────────────────────────────┐
│ Curso                  | Instructor    | Fecha  | Acciones   │
├──────────────────────────────────────────────────────────────┤
│ Curso de Hacking Ético │ Carlos M.     │ Hoy    │ [Aprobar]  │
│                        │               │        │ [Rechazar] │
│                        │               │        │ [Ver]      │
└──────────────────────────────────────────────────────────────┘
```

**Proceso de moderación**:
1. **Ver** el curso en detalle
2. Revisar contenido de secciones y lecciones
3. Decidir:
   - **Aprobar**: Curso se publica en catálogo
   - **Rechazar**: Se notifica al instructor con motivo

**Criterios de moderación**:
- ❌ Contenido ilegal o inapropiado
- ❌ Spam o cursos de baja calidad
- ❌ Violación de derechos de autor
- ✅ Contenido educativo legítimo

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

### Para Administradores

**P: ¿Cómo creo un nuevo administrador?**
R: Desde "Gestión de Usuarios", edita un usuario existente y cambia su rol a "admin".

**P: ¿Puedo restaurar un curso eliminado?**
R: No, las eliminaciones son permanentes. Se recomienda hacer backups regulares de la base de datos.

**P: ¿Cómo contacto con soporte técnico?**
R: Para problemas técnicos, contacta con el desarrollador en soporte@elearningjcb.com.

---

**Conclusión Sección 10**: Este manual de usuario proporciona guías detalladas paso a paso para los tres roles principales (estudiante, instructor, admin). Con ejemplos visuales en formato ASCII, descripciones claras y capturas de referencia, cualquier usuario puede navegar la plataforma sin dificultad. El FAQ resuelve las preguntas más comunes. **Nota**: En una versión final impresa, se deben reemplazar los diagramas ASCII con capturas de pantalla reales de la aplicación desplegada.

---

<div style="page-break-after: always;"></div>
