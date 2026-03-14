# Capturas de Pantalla - E-Learning JCB Platform

Esta carpeta contiene las capturas de pantalla de la aplicación para incluir en el Manual de Usuario y los Anexos de la memoria del proyecto.

## 📁 Estructura de Carpetas

```
capturas/
├── 01_autenticacion/     # Login, registro, recuperación contraseña
├── 02_estudiante/        # Dashboard y funcionalidades de estudiante
├── 03_instructor/        # Dashboard y funcionalidades de instructor
├── 04_admin/            # Dashboard y funcionalidades de administrador
└── 05_ui_general/       # Elementos generales de UI (navbar, footer, etc.)
```

## 📸 Checklist de Capturas Necesarias

### 01_autenticacion/ (3 capturas)
- [x] `01_login.png` - Página de inicio de sesión
- [x] `02_registro.png` - Formulario de registro
- [No] `03_recuperar_password.png` - Recuperación de contraseña (NO EXISTE)

### 02_estudiante/ (8 capturas)
- [x] `04_home_publica.png` - Home page (sin login)
- [x] `05_listado_cursos.png` - Catálogo de cursos con filtros
- [x] `06_detalle_curso.png` - Vista detallada de curso
- [x] `07_dashboard_estudiante.png` - Dashboard del estudiante
- [No] `08_mis_cursos.png` - Cursos inscritos (se ve en el dashboard, no es una página aparte)
- [x] `08_mi_perfil.png` - Se sustuye la captura de mis cursos por la del perfil del estudiante donde se pueden modificar datos., cambiar contraseña, etc...
- [x] `09_progreso_curso.png` - Progreso dentro de un curso
- [No] `10_leccion_video.png` - Visualización de lección (Se puede pulsar en la leccion para ir a esa parte pero no es una página aparte)
- [No] `11_valorar_curso.png` - Interface de valoración (Falta imlementar valoración)

### 03_instructor/ (6 capturas)
- [x] `12_dashboard_instructor.png` - Dashboard del instructor
- [No] `13_crear_curso_paso1.png` - Datos básicos del curso (No implementado)
- [No] `14_crear_curso_paso2.png` - Añadir secciones (No implementado)
- [No] `15_crear_curso_paso3.png` - Añadir lecciones (No implementado)
- [No] `16_estadisticas_instructor.png` - Estadísticas e ingresos (No implementado)
- [No] `17_editar_curso.png` - Editar curso existente (No implementado)

### 04_admin/ (5 capturas)
- [x] `18_dashboard_admin.png` - Dashboard del administrador
- [x] `19_gestion_usuarios.png` - Lista de usuarios
- [x] `20_editar_usuario.png` - Editar usuario y roles
- [No] `21_moderacion_cursos.png` - Moderación de contenidos (no implementado)
- [x] `21_gestion_cursos.png` - Lista de cursos (sustituye a la captura de moderación de cursos que no se ha implementado por la captura de la página de edición de cursos que sí se ha implementado)
- [No] `22_reportes_sistema.png` - Reportes globales

### 05_ui_general/ (6 capturas)
- [x] `23_navbar_desktop.png` - Barra de navegación desktop
- [x] `24_navbar_mobile.png` - Barra de navegación móvil (opcional)
- [x] `25_footer.png` - Pie de página
- [No] `26_perfil_usuario.png` - Página de perfil
- [No] `27_notificaciones.png` - Sistema de notificaciones (si existe)
- [No] `28_error_404.png` - Página de error 404 (opcional)

**Total: 29 capturas**
**Mínimo recomendado: 15 capturas** (las marcadas como imprescindibles)

## 🎯 Especificaciones Técnicas

### Resolución
- **Recomendada**: 1920x1080 (Full HD)
- **Mínima aceptable**: 1366x768
- **Formato**: PNG (mejor calidad) o JPG (menor tamaño)

### Calidad
- Navegador en zoom 100% (sin zoom)
- Datos de prueba realistas en español
- Sin extensiones visibles en la barra
- Modo claro/oscuro consistente

### Datos Sensibles
- Ocultar URLs locales (localhost)
- Ocultar strings de conexión MongoDB
- Usar emails de prueba (no reales)

## 🚀 Cómo Hacer las Capturas

### En Windows
1. **Windows + Shift + S**: Captura de área seleccionada
2. **Windows + PrtScn**: Captura de pantalla completa
3. **Herramienta Recortes**: Más opciones de edición

### En Linux
1. **PrtScn**: Captura de pantalla completa
2. **Shift + PrtScn**: Captura de área seleccionada
3. **Flameshot**: `flameshot gui` (recomendado)

### En macOS
1. **Cmd + Shift + 3**: Captura de pantalla completa
2. **Cmd + Shift + 4**: Captura de área seleccionada
3. **Cmd + Shift + 5**: Menú de capturas

## 📝 Nomenclatura

Formato: `NN_nombre_descriptivo.png`

Donde:
- `NN` = Número secuencial (01, 02, 03...)
- `nombre_descriptivo` = Descripción en snake_case
- Extensión: `.png` o `.jpg`

Ejemplo: `07_dashboard_estudiante.png`

## ✅ Estado de Capturas

**Fecha de actualización**: 13/03/2026
**Capturas realizadas**: 0 / 29
**Completado**: 0%

---

**Nota**: Una vez realizadas las capturas, actualizar este README con las capturas completadas y marcar los checkboxes correspondientes.
