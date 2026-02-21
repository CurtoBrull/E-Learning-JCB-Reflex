# Usuarios de Ejemplo - E-Learning JCB

Este documento contiene las credenciales de los usuarios de ejemplo creados en la plataforma para propósitos de desarrollo y testing.

## 📋 Usuarios Disponibles

### 👨‍🎓 Estudiante (Student)

**Propósito**: Usuario para aprender cursos y acceder a contenido educativo.

- **Nombre**: María García
- **Email**: `maria.garcia@elearningjcb.com`
- **Contraseña**: `student123`
- **Rol**: `student`

**Permisos**:
- Ver y explorar cursos disponibles
- Inscribirse en cursos
- Acceder a lecciones y materiales
- Completar actividades y evaluaciones
- Ver su progreso personal

---

### 👨‍🏫 Instructor

**Propósito**: Usuario para crear y gestionar cursos en la plataforma.

- **Nombre**: Carlos Rodríguez
- **Email**: `carlos.rodriguez@elearningjcb.com`
- **Contraseña**: `instructor123`
- **Rol**: `instructor`

**Permisos**:
- Crear nuevos cursos
- Editar cursos existentes (propios)
- Agregar y gestionar lecciones
- Ver estadísticas de estudiantes inscritos
- Gestionar materiales del curso

---

### 👨‍💼 Administrador (Admin)

**Propósito**: Usuario con acceso completo para gestión de la plataforma.

- **Nombre**: Ana Martínez
- **Email**: `ana.martinez@elearningjcb.com`
- **Contraseña**: `admin123`
- **Rol**: `admin`

**Permisos**:
- Gestión completa de usuarios
- Gestión completa de cursos (todos)
- Acceso a estadísticas globales
- Configuración de la plataforma
- Moderación de contenido
- Gestión de roles y permisos

---

## 🔐 Seguridad

**IMPORTANTE**: Estas credenciales son solo para desarrollo y testing.

- ⚠️ **NO usar en producción**
- ⚠️ Las contraseñas están hasheadas con bcrypt en la base de datos
- ⚠️ Cambiar todas las contraseñas antes de desplegar en producción

---

## 🚀 Cómo Usar

1. Acceder a la página de login: `http://localhost:3000/login`
2. Seleccionar uno de los usuarios de ejemplo
3. Introducir el email y contraseña correspondiente
4. Hacer clic en "Iniciar Sesión"

---

## 📝 Crear Nuevos Usuarios

### Vía Web (Registro)
1. Ir a `http://localhost:3000/register`
2. Completar el formulario de registro
3. Seleccionar el rol deseado (student, instructor, admin)
4. Hacer clic en "Crear Cuenta"

### Vía Script
Ejecutar el script de creación de usuarios:
```bash
source reflex-env/bin/activate
python scripts/create_sample_users.py
```

---

## 📊 Estado de los Usuarios

| Rol | Nombre | Email | Estado |
|-----|--------|-------|--------|
| Student | María García | maria.garcia@elearningjcb.com | ✅ Activo |
| Instructor | Carlos Rodríguez | carlos.rodriguez@elearningjcb.com | ✅ Activo |
| Admin | Ana Martínez | ana.martinez@elearningjcb.com | ✅ Activo |

---

## 🔄 Resetear Usuarios

Si necesitas resetear los usuarios de ejemplo a su estado inicial, puedes:

1. Eliminar los usuarios de la base de datos MongoDB
2. Volver a ejecutar el script `create_sample_users.py`

```bash
# Resetear usuarios
source reflex-env/bin/activate
python scripts/create_sample_users.py
```

El script automáticamente detecta usuarios existentes y los salta para evitar duplicados.
