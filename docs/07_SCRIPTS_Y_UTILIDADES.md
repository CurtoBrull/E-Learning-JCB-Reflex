de cambios

#### 📊 Utilidades
- Paginación automática
- Sanitización de consultas de búsqueda
- Navegación contextual por rol
- Formateo de URLs específicas

---

*Documentación de Scripts y Utilidades*  
*Proyecto: E-Learning JCB Reflex*  
*Actualizado: 25 de enero de 2025*e

#### 🔐 Seguridad
- Hash seguro de contraseñas con bcrypt
- Validación de fortaleza de contraseñas
- Generación de contraseñas seguras
- Estimación de tiempo de crackeo

#### 🧭 Navegación
- Redirecciones dinámicas por rol
- Construcción de URLs con parámetros
- Validación de ObjectIds de MongoDB
- Generación de breadcrumbs automáticos

#### 🛠️ Mantenimiento
- Verificación de conectividad de base de datos
- Creación automatizada de usuarios de prueba
- Gestión masiva de URLs de video
- Backup automático antes de conectividad MongoDB |
| `create_sample_users.py` | ~300 | 3 funciones | Creación de usuarios de ejemplo |
| `add_video_urls_to_lessons.py` | ~250 | 6 funciones | Gestión de URLs de video |

### Utilidades Disponibles (2 módulos)

| Módulo | Líneas | Funciones | Propósito Principal |
|--------|--------|-----------|-------------------|
| `password.py` | ~200 | 5 funciones | Gestión segura de contraseñas |
| `route_helpers.py` | ~300 | 12 funciones | Helpers de navegación y rutas |

### Funcionalidades Clav": end_item,
        "has_previous": current_page > 1,
        "has_next": current_page < total_pages,
        "previous_page": current_page - 1 if current_page > 1 else None,
        "next_page": current_page + 1 if current_page < total_pages else None
    }
```

---

## 📊 Resumen de Scripts y Utilidades

### Scripts Disponibles (3 archivos)

| Script | Líneas | Funciones | Propósito Principal |
|--------|--------|-----------|-------------------|
| `test_connection.py` | ~150 | 4 funciones | Verificación pages = max(1, (total_items + items_per_page - 1) // items_per_page)
    
    if current_page > total_pages:
        current_page = total_pages
    
    start_item = (current_page - 1) * items_per_page
    end_item = min(start_item + items_per_page, total_items)
    
    return {
        "current_page": current_page,
        "total_pages": total_pages,
        "total_items": total_items,
        "items_per_page": items_per_page,
        "start_item": start_item + 1,  # 1-indexed para mostrar
        "end_itemúltiples
    sanitized = re.sub(r'\s+', ' ', sanitized)
    
    return sanitized.strip()

def get_pagination_info(current_page: int, total_items: int, items_per_page: int = 10) -> dict:
    """
    Calcular información de paginación.
    
    Args:
        current_page: Página actual (1-indexed)
        total_items: Total de elementos
        items_per_page: Elementos por página
        
    Returns:
        dict: Información de paginación
    """
    if current_page < 1:
        current_page = 1
    
    total_itize_search_query(query: str) -> str:
    """
    Sanitizar consulta de búsqueda.
    
    Args:
        query: Consulta de búsqueda
        
    Returns:
        str: Consulta sanitizada
    """
    if not query:
        return ""
    
    # Remover caracteres especiales peligrosos
    import re
    
    # Permitir solo letras, números, espacios y algunos símbolos básicos
    sanitized = re.sub(r'[^\w\s\-\.\+]', '', query)
    
    # Limitar longitud
    sanitized = sanitized[:100]
    
    # Remover espacios m usuario
        action: Acción a realizar ("view", "edit", "delete")
        
    Returns:
        str: URL formateada
    """
    if not is_valid_object_id(user_id):
        raise ValueError(f"ID de usuario inválido: {user_id}")
    
    url_patterns = {
        "view": f"/users/{user_id}",
        "profile": f"/instructors/{user_id}",
        "edit": f"/admin/users/edit/{user_id}",
        "delete": f"/admin/users/delete/{user_id}"
    }
    
    return url_patterns.get(action, f"/users/{user_id}")

def san    raise ValueError(f"ID de curso inválido: {course_id}")
    
    url_patterns = {
        "view": f"/courses/{course_id}",
        "watch": f"/courses/{course_id}/view",
        "edit": f"/admin/courses/edit/{course_id}",
        "delete": f"/admin/courses/delete/{course_id}"
    }
    
    return url_patterns.get(action, f"/courses/{course_id}")

def format_user_url(user_id: str, action: str = "view") -> str:
    """
    Formatear URL de usuario con acción específica.
    
    Args:
        user_id: ID del
    Formatear URL de curso con acción específica.
    
    Args:
        course_id: ID del curso
        action: Acción a realizar ("view", "edit", "delete")
        
    Returns:
        str: URL formateada
        
    Ejemplo:
        >>> format_course_url("64f1a2b3c4d5e6f7g8h9i0j1", "view")
        "/courses/64f1a2b3c4d5e6f7g8h9i0j1"
        >>> format_course_url("64f1a2b3c4d5e6f7g8h9i0j1", "edit")
        "/admin/courses/edit/64f1a2b3c4d5e6f7g8h9i0j1"
    """
    if not is_valid_object_id(course_id):
    "users"},
            {"label": "Cursos", "url": "/admin/courses", "icon": "book"},
            {"label": "Estadísticas", "url": "/admin/stats", "icon": "chart-bar"},
        ]
    }
    
    # Combinar navegación común y específica
    all_items = common_items + role_specific_items.get(role, [])
    
    # Marcar elemento activo
    for item in all_items:
        item["active"] = item["url"] == current_path
    
    return all_items

def format_course_url(course_id: str, action: str = "view") -> str:
    """t-dashboard"},
            {"label": "Mis Cursos", "url": "/student/courses", "icon": "book-open"},
        ],
        "instructor": [
            {"label": "Mi Dashboard", "url": "/instructor/dashboard", "icon": "layout-dashboard"},
            {"label": "Mis Cursos", "url": "/instructor/courses", "icon": "book-open"},
        ],
        "admin": [
            {"label": "Dashboard Admin", "url": "/admin/dashboard", "icon": "layout-dashboard"},
            {"label": "Usuarios", "url": "/admin/users", "icon":         list[dict]: Lista de elementos de navegación
    """
    # Navegación común para todos los usuarios autenticados
    common_items = [
        {"label": "Inicio", "url": "/", "icon": "home"},
        {"label": "Cursos", "url": "/courses", "icon": "book"},
        {"label": "Instructores", "url": "/instructors", "icon": "users"},
    ]
    
    # Navegación específica por rol
    role_specific_items = {
        "student": [
            {"label": "Mi Dashboard", "url": "/student/dashboard", "icon": "layou       # La última ruta no debe ser clickeable
        url = current_url if i < len(segments) - 1 else None
        
        breadcrumbs.append({
            "label": label,
            "url": url
        })
    
    return breadcrumbs

def get_navigation_items_by_role(role: str, current_path: str = "") -> list[dict]:
    """
    Obtener elementos de navegación según el rol del usuario.
    
    Args:
        role: Rol del usuario
        current_path: Ruta actual para marcar como activa
        
    Returns:

        "create": "Crear",
        "view": "Ver"
    }
    
    # Dividir ruta en segmentos
    segments = [s for s in current_path.split("/") if s]
    
    breadcrumbs = [{"label": "Inicio", "url": "/"}]
    
    current_url = ""
    for i, segment in enumerate(segments):
        current_url += f"/{segment}"
        
        # Obtener etiqueta legible
        if is_valid_object_id(segment):
            label = "Detalle"
        else:
            label = route_labels.get(segment, segment.title())
        
 ": None}
        ]
    """
    if not current_path or current_path == "/":
        return [{"label": "Inicio", "url": "/"}]
    
    # Mapeo de rutas a etiquetas legibles
    route_labels = {
        "admin": "Administración",
        "student": "Estudiante",
        "instructor": "Instructor",
        "courses": "Cursos",
        "users": "Usuarios",
        "dashboard": "Dashboard",
        "profile": "Perfil",
        "settings": "Configuración",
        "stats": "Estadísticas",
        "edit": "Editar",t[dict]:
    """
    Generar elementos de breadcrumb basados en la ruta actual.
    
    Args:
        current_path: Ruta actual de la página
        
    Returns:
        list[dict]: Lista de elementos de breadcrumb
        
    Ejemplo:
        >>> get_breadcrumb_items("/admin/courses/edit/64f1a2b3c4d5e6f7g8h9i0j1")
        [
            {"label": "Inicio", "url": "/"},
            {"label": "Admin", "url": "/admin"},
            {"label": "Cursos", "url": "/admin/courses"},
            {"label": "Editar", "url
        
    Returns:
        bool: True si es un ObjectId válido
        
    Ejemplo:
        >>> is_valid_object_id("64f1a2b3c4d5e6f7g8h9i0j1")
        True
        >>> is_valid_object_id("invalid-id")
        False
    """
    import re
    
    if not id_string or not isinstance(id_string, str):
        return False
    
    # ObjectId de MongoDB: 24 caracteres hexadecimales
    pattern = r'^[0-9a-fA-F]{24}$'
    return bool(re.match(pattern, id_string))

def get_breadcrumb_items(current_path: str) -> lisn: Patrón regex para extraer el ID
        
    Returns:
        Optional[str]: ID extraído o None si no se encuentra
        
    Ejemplo:
        >>> extract_id_from_url("/courses/64f1a2b3c4d5e6f7g8h9i0j1")
        "64f1a2b3c4d5e6f7g8h9i0j1"
    """
    import re
    
    match = re.search(pattern, url)
    return match.group(1) if match else None

def is_valid_object_id(id_string: str) -> bool:
    """
    Validar si una cadena es un ObjectId válido de MongoDB.
    
    Args:
        id_string: Cadena a validar  # Filtrar parámetros vacíos
    filtered_params = {k: v for k, v in params.items() if v is not None and v != ""}
    
    if not filtered_params:
        return base_url
    
    # Codificar parámetros
    query_string = urllib.parse.urlencode(filtered_params)
    
    return f"{base_url}?{query_string}"

def extract_id_from_url(url: str, pattern: str = r'/([^/]+)$') -> Optional[str]:
    """
    Extraer ID de una URL usando expresión regular.
    
    Args:
        url: URL de la cual extraer el ID
        patteredirect(dashboard_url)

def build_url_with_params(base_url: str, params: Dict[str, Any]) -> str:
    """
    Construir URL con parámetros de consulta.
    
    Args:
        base_url: URL base
        params: Diccionario de parámetros
        
    Returns:
        str: URL completa con parámetros
        
    Ejemplo:
        >>> build_url_with_params("/courses", {"category": "web", "level": "beginner"})
        "/courses?category=web&level=beginner"
    """
    if not params:
        return base_url
    
  board"
    """
    dashboard_urls = {
        "student": "/student/dashboard",
        "instructor": "/instructor/dashboard",
        "admin": "/admin/dashboard"
    }
    
    return dashboard_urls.get(role, "/")

def redirect_to_dashboard(role: str) -> rx.Component:
    """
    Crear redirección al dashboard según el rol.
    
    Args:
        role: Rol del usuario
        
    Returns:
        rx.Component: Componente de redirección
    """
    dashboard_url = get_dashboard_url_by_role(role)
    return rx.r"""

import reflex as rx
from typing import Optional, Dict, Any
import urllib.parse

def get_dashboard_url_by_role(role: str) -> str:
    """
    Obtener URL del dashboard según el rol del usuario.
    
    Args:
        role: Rol del usuario ("student", "instructor", "admin")
        
    Returns:
        str: URL del dashboard correspondiente
        
    Ejemplo:
        >>> get_dashboard_url_by_role("student")
        "/student/dashboard"
        >>> get_dashboard_url_by_role("admin")
        "/admin/dash": len(password),
        "character_space": char_space,
        "total_combinations": combinations,
        "crack_times": results
    }
```

---

## 🧭 Utilidades de Rutas

### `utils/route_helpers.py`

**Propósito**: Helpers para navegación y validación de rutas.

#### Funciones Principales
```python
"""
Utilidades para gestión de rutas y navegación.

Características:
- Redirecciones dinámicas por rol
- Validación de parámetros de URL
- Construcción de URLs con parámetros
- Helpers para rutas protegidas
e_str = f"{seconds:.1f} segundos"
        elif seconds < 3600:
            time_str = f"{seconds/60:.1f} minutos"
        elif seconds < 86400:
            time_str = f"{seconds/3600:.1f} horas"
        elif seconds < 31536000:
            time_str = f"{seconds/86400:.1f} días"
        else:
            time_str = f"{seconds/31536000:.1f} años"
        
        results[attack_type] = {
            "seconds": seconds,
            "human_readable": time_str
        }
    
    return {
        "password_lengthes de velocidad de ataque (hashes por segundo)
    attack_speeds = {
        "online": 1000,  # Ataques online lentos
        "offline_cpu": 1_000_000,  # CPU moderna
        "offline_gpu": 100_000_000,  # GPU potente
        "offline_cluster": 1_000_000_000  # Cluster de GPUs
    }
    
    results = {}
    for attack_type, speed in attack_speeds.items():
        # Tiempo promedio = combinaciones / (2 * velocidad)
        seconds = combinations / (2 * speed)
        
        if seconds < 60:
            timpo de crackeo estimado
    """
    import math
    
    # Calcular espacio de caracteres
    char_space = 0
    if any(c.islower() for c in password):
        char_space += 26
    if any(c.isupper() for c in password):
        char_space += 26
    if any(c.isdigit() for c in password):
        char_space += 10
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        char_space += 32
    
    # Calcular combinaciones posibles
    combinations = char_space ** len(password)
    
    # Estimacion(symbols)
    ]
    
    # Completar con caracteres aleatorios
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))
    
    # Mezclar la contraseña
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

# Funciones de utilidad adicionales

def estimate_crack_time(password: str) -> dict:
    """
    Estimar tiempo de crackeo de una contraseña.
    
    Args:
        password: Contraseña a evaluar
        
    Returns:
        dict: Información sobre tiem28 caracteres")
    
    # Caracteres disponibles (sin ambiguos)
    lowercase = "abcdefghijkmnpqrstuvwxyz"  # Sin 'l', 'o'
    uppercase = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # Sin 'I', 'O'
    digits = "23456789"  # Sin '0', '1'
    symbols = "!@#$%^&*+-=?_"
    
    all_chars = lowercase + uppercase + digits + symbols
    
    # Garantizar al menos un carácter de cada tipo
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choicegitud de la contraseña (mínimo 8)
        
    Returns:
        str: Contraseña segura generada
        
    Ejemplo:
        >>> password = generate_secure_password(12)
        >>> len(password)
        12
        >>> is_strong, _ = is_password_strong(password)
        >>> print(is_strong)
        True
    """
    import secrets
    import string
    
    if length < 8:
        raise ValueError("La longitud mínima es 8 caracteres")
    
    if length > 128:
        raise ValueError("La longitud máxima es 1omplejidad
    # - Mayúsculas y minúsculas
    # - Números y símbolos
    # - Contraseñas comunes
    # - Patrones repetitivos
    
    return len(issues) == 0, issues

def generate_secure_password(length: int = 16) -> str:
    """
    Generar contraseña segura aleatoria.
    
    Características:
    - Longitud configurable
    - Incluye mayúsculas, minúsculas, números y símbolos
    - Evita caracteres ambiguos (0, O, l, I)
    - Garantiza al menos un carácter de cada tipo
    
    Args:
        length: Lon       >>> print(issues)
        ['La contraseña debe tener al menos 6 caracteres']
    """
    issues = []
    
    if not password:
        issues.append("La contraseña no puede estar vacía")
        return False, issues
    
    if len(password) < 6:
        issues.append("La contraseña debe tener al menos 6 caracteres")
    
    if len(password) > 128:
        issues.append("La contraseña no puede tener más de 128 caracteres")
    
    # Futuras validaciones adicionales
    # TODO: Implementar validaciones de ceres)
    - Longitud máxima (128 caracteres)
    - Presencia de mayúsculas (futuro)
    - Presencia de minúsculas (futuro)
    - Presencia de números (futuro)
    - Presencia de símbolos (futuro)
    - No estar en lista de contraseñas comunes (futuro)
    
    Args:
        password: Contraseña a evaluar
        
    Returns:
        tuple[bool, list[str]]: (es_fuerte, lista_de_problemas)
        
    Ejemplo:
        >>> is_strong, issues = is_password_strong("123")
        >>> print(is_strong)
        False
 traseña usando bcrypt
        return bcrypt.checkpw(
            password.encode('utf-8'),
            hashed.encode('utf-8')
        )
        
    except Exception as e:
        # Log del error para debugging (sin exponer información sensible)
        print(f"Error verificando contraseña: {type(e).__name__}")
        return False

def is_password_strong(password: str) -> tuple[bool, list[str]]:
    """
    Evaluar la fortaleza de una contraseña.
    
    Criterios evaluados:
    - Longitud mínima (6 caracte datos
        
    Returns:
        bool: True si la contraseña es correcta, False en caso contrario
        
    Ejemplo:
        >>> hashed = hash_password("mi_contraseña")
        >>> verify_password("mi_contraseña", hashed)
        True
        >>> verify_password("contraseña_incorrecta", hashed)
        False
    """
    if not password or not hashed:
        return False
    
    if not isinstance(password, str) or not isinstance(hashed, str):
        return False
    
    try:
        # Verificar con   return hashed.decode('utf-8')
        
    except Exception as e:
        raise RuntimeError(f"Error hasheando contraseña: {e}")

def verify_password(password: str, hashed: str) -> bool:
    """
    Verificar contraseña contra hash almacenado.
    
    Características:
    - Verificación en tiempo constante
    - Manejo seguro de errores
    - Compatibilidad con diferentes versiones de bcrypt
    
    Args:
        password: Contraseña en texto plano a verificar
        hashed: Hash almacenado en la base dr("La contraseña no puede estar vacía")
    
    if not isinstance(password, str):
        raise TypeError("La contraseña debe ser una cadena de texto")
    
    if rounds < 4 or rounds > 31:
        raise ValueError("El factor de trabajo debe estar entre 4 y 31")
    
    try:
        # Generar salt con el factor de trabajo especificado
        salt = bcrypt.gensalt(rounds=rounds)
        
        # Hashear contraseña con el salt
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        
     stente a ataques de rainbow table
    - Resistente a ataques de fuerza bruta
    
    Args:
        password: Contraseña en texto plano
        rounds: Factor de trabajo (2^rounds iteraciones)
        
    Returns:
        str: Hash de la contraseña con salt incluido
        
    Ejemplo:
        >>> hashed = hash_password("mi_contraseña_segura")
        >>> print(len(hashed))  # ~60 caracteres
        60
        >>> print(hashed.startswith("$2b$"))
        True
    """
    if not password:
        raise ValueErro
- Factor de trabajo configurable
- Verificación constante en tiempo
- Resistencia a ataques de fuerza bruta
"""

import bcrypt
import os

# Factor de trabajo por defecto (2^12 = 4096 iteraciones)
DEFAULT_ROUNDS = int(os.getenv("BCRYPT_ROUNDS", "12"))

def hash_password(password: str, rounds: int = DEFAULT_ROUNDS) -> str:
    """
    Hashear contraseña con bcrypt.
    
    Características de seguridad:
    - Salt único generado automáticamente
    - Factor de trabajo configurable (por defecto 12)
    - Resi----|-----------|-----------|--------|
| `password.py` | Gestión segura de contraseñas | Hash y verificación con bcrypt | ✅ Funcional |
| `route_helpers.py` | Helpers para rutas y navegación | Redirecciones y validaciones | ✅ Funcional |

---

## 🔐 Utilidades de Contraseñas

### `utils/password.py`

**Propósito**: Gestión segura de contraseñas con bcrypt.

#### Funciones Principales
```python
"""
Utilidades para gestión segura de contraseñas.

Características:
- Hash seguro con bcrypt
- Salt único por contraseñases())
        asyncio.run(add_video_urls_to_courses())
```

#### Uso del Script
```bash
# Añadir URLs de video a lecciones
python scripts/add_video_urls_to_lessons.py

# Crear backup antes de actualizar
python scripts/add_video_urls_to_lessons.py --backup

# Verificar URLs existentes
python scripts/add_video_urls_to_lessons.py --verify
```

---

## 🔧 Utilidades del Sistema

### Directorio `utils/`

El proyecto incluye **2 módulos de utilidades** principales:

| Módulo | Propósito | Funciones | Estado |
|----t argparse
    
    parser = argparse.ArgumentParser(description="Gestionar URLs de video en lecciones")
    parser.add_argument("--verify", action="store_true",
                       help="Verificar URLs de video existentes")
    parser.add_argument("--backup", action="store_true",
                       help="Crear backup antes de actualizar")
    
    args = parser.parse_args()
    
    if args.verify:
        asyncio.run(verify_video_urls())
    else:
        if args.backup:
            asyncio.run(backup_cour     backup_collection = db[backup_name]
        
        # Copiar todos los cursos
        cursor = courses_collection.find({})
        courses = await cursor.to_list(length=None)
        
        if courses:
            await backup_collection.insert_many(courses)
            print(f"💾 Backup creado: {backup_name} ({len(courses)} cursos)")
        
        return backup_name
        
    except Exception as e:
        print(f"❌ Error creando backup: {e}")
        return None

if __name__ == "__main__":
    impor Porcentaje: {(lessons_with_video/total_lessons*100):.1f}%" if total_lessons else "0%")
        
    except Exception as e:
        print(f"❌ Error verificando URLs de video: {e}")

async def backup_courses():
    """
    Crear backup de cursos antes de modificar.
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()
        courses_collection = db.courses
        
        # Crear colección de backup
        backup_name = f"courses_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
      course_videos += 1
                    lessons_with_video += 1
            
            print(f"📚 {course['title']}")
            print(f"   Lecciones: {len(lessons)}")
            print(f"   Con video: {course_videos}")
            print(f"   Porcentaje: {(course_videos/len(lessons)*100):.1f}%" if lessons else "0%")
            print()
        
        print(f"📊 Resumen general:")
        print(f"   Total lecciones: {total_lessons}")
        print(f"   Con video: {lessons_with_video}")
        print(f"  .courses
        
        print("🔍 Verificando URLs de video en cursos...")
        
        cursor = courses_collection.find({})
        courses = await cursor.to_list(length=None)
        
        total_lessons = 0
        lessons_with_video = 0
        
        for course in courses:
            lessons = course.get("lessons", [])
            total_lessons += len(lessons)
            
            course_videos = 0
            for lesson in lessons:
                if lesson.get("videoUrl"):
                 ons}")
        print(f"   🎥 Total de videos añadidos: {sum(len(urls) for urls in COURSE_VIDEO_URLS.values())}")
        
        print("\n🎉 Actualización de videos completada exitosamente!")
        
    except Exception as e:
        print(f"❌ Error actualizando URLs de video: {e}")
        raise

async def verify_video_urls():
    """
    Verificar que las URLs de video se hayan añadido correctamente.
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()
        courses_collection = db                       }
                        },
                        upsert=True
                    )
                    updated_lessons += 1
            
            updated_courses += 1
            print(f"   📊 Curso actualizado con {len([l for l in updated_lessons_in_course if 'videoUrl' in l])} videos")
        
        # Resumen final
        print(f"\n📈 Resumen de actualización:")
        print(f"   ✅ Cursos actualizados: {updated_courses}")
        print(f"   ✅ Lecciones actualizadas: {updated_lessda (si existe)
            for lesson in updated_lessons_in_course:
                if "videoUrl" in lesson:
                    await lessons_collection.update_one(
                        {
                            "courseId": course_id,
                            "title": lesson["title"]
                        },
                        {
                            "$set": {
                                "videoUrl": lesson["videoUrl"],
                                "updatedAt": datetime.now()
                     else:
                    updated_lessons_in_course.append(lesson)
            
            # Actualizar curso en la base de datos
            await courses_collection.update_one(
                {"_id": course_id},
                {
                    "$set": {
                        "lessons": updated_lessons_in_course,
                        "updatedAt": datetime.now()
                    }
                }
            )
            
            # Actualizar lecciones en colección separa    
                    # Convertir a formato embed
                    embed_url = convert_to_embed_url(video_url)
                    
                    # Actualizar lección
                    lesson["videoUrl"] = embed_url
                    lesson["updatedAt"] = datetime.now()
                    
                    updated_lessons_in_course.append(lesson)
                    
                    print(f"   ✅ Lección actualizada: {lesson['title']}")
                    print(f"      Video: {embed_url}")
)
                continue
            
            # Actualizar lecciones con URLs de video
            updated_lessons_in_course = []
            
            for i, lesson in enumerate(lessons):
                if i < len(video_urls):
                    video_url = video_urls[i]
                    
                    # Validar URL
                    if not validate_youtube_url(video_url):
                        print(f"   ❌ URL inválida: {video_url}")
                        continue
                rocesando curso: {course_title}")
            
            # Buscar curso por título
            course = await courses_collection.find_one({"title": course_title})
            
            if not course:
                print(f"   ⚠️  Curso no encontrado: {course_title}")
                continue
            
            course_id = course["_id"]
            lessons = course.get("lessons", [])
            
            if not lessons:
                print(f"   ⚠️  No hay lecciones en el curso: {course_title}"d_video_urls_to_courses():
    """
    Añadir URLs de video a las lecciones de los cursos.
    """
    try:
        # Conectar a MongoDB
        await MongoDB.connect()
        db = MongoDB.get_db()
        courses_collection = db.courses
        lessons_collection = db.lessons
        
        print("🎥 Iniciando actualización de URLs de video...")
        
        updated_courses = 0
        updated_lessons = 0
        
        for course_title, video_urls in COURSE_VIDEO_URLS.items():
            print(f"\n📚 P([^?]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return ""

def convert_to_embed_url(url: str) -> str:
    """
    Convertir URL de YouTube a formato embed.
    
    Args:
        url: URL original de YouTube
        
    Returns:
        str: URL en formato embed
    """
    video_id = extract_video_id(url)
    if video_id:
        return f"https://www.youtube.com/embed/{video_id}"
    return url

async def ad\.com/watch\?v=[\w-]+',
        r'https?://youtu\.be/[\w-]+',
        r'https?://(?:www\.)?youtube\.com/embed/[\w-]+'
    ]
    
    return any(re.match(pattern, url) for pattern in youtube_patterns)

def extract_video_id(url: str) -> str:
    """
    Extraer ID del video de una URL de YouTube.
    
    Args:
        url: URL de YouTube
        
    Returns:
        str: ID del video
    """
    patterns = [
        r'youtube\.com/watch\?v=([^&]+)',
        r'youtu\.be/([^?]+)',
        r'youtube\.com/embed/oFbQ",  # ES6+ Features
        "https://www.youtube.com/watch?v=PoRJizFvM7s",  # Async/Await
        "https://www.youtube.com/watch?v=DHvZLI7Db8E",  # Closures
        "https://www.youtube.com/watch?v=Bv_5Zv5c-Ts",  # Prototypes
    ]
}

def validate_youtube_url(url: str) -> bool:
    """
    Validar que la URL sea de YouTube.
    
    Args:
        url: URL a validar
        
    Returns:
        bool: True si es una URL válida de YouTube
    """
    youtube_patterns = [
        r'https?://(?:www\.)?youtubetch?v=IHZwWFHWa-w",  # Machine Learning
        "https://www.youtube.com/watch?v=R9OHn5ZF4Uo",  # Deep Learning
    ],
    "Diseño UX/UI Moderno": [
        "https://www.youtube.com/watch?v=c9Wg6Cb_YlU",  # UX Principles
        "https://www.youtube.com/watch?v=68w2VwalD5w",  # UI Design
        "https://www.youtube.com/watch?v=YiLUYf4HDh4",  # Prototyping
        "https://www.youtube.com/watch?v=_Hp_dI0DzY4",  # User Research
    ],
    "JavaScript Avanzado": [
        "https://www.youtube.com/watch?v=8aGhZQk"https://www.youtube.com/watch?v=hQAHSlTtcmY",  # React Hooks
        "https://www.youtube.com/watch?v=f55qeKGgB_M",  # Node.js Intro
        "https://www.youtube.com/watch?v=pKd0Rpw7O48",  # Express.js
        "https://www.youtube.com/watch?v=7CqJlxBYj-M",  # MongoDB Integration
    ],
    "Introducción a la Inteligencia Artificial": [
        "https://www.youtube.com/watch?v=ad79nYk2keg",  # AI Fundamentals
        "https://www.youtube.com/watch?v=aircAruvnKk",  # Neural Networks
        "https://www.youtube.com/waaliza tanto colección courses como lessons
- Mantiene sincronización entre colecciones
- Backup automático antes de cambios
"""

import asyncio
import re
from datetime import datetime
from E_Learning_JCB_Reflex.database.mongodb import MongoDB

# URLs de videos de ejemplo por curso
COURSE_VIDEO_URLS = {
    "Desarrollo Web Full Stack con React y Node.js": [
        "https://www.youtube.com/watch?v=w7ejDZ8SWv8",  # React Basics
        "https://www.youtube.com/watch?v=Ke90Tje7VS0",  # React Components
        email.com) - student123
- **Elena Ruiz** (elena.ruiz@email.com) - student123

---

## 🎥 Script de Gestión de Videos

### `scripts/add_video_urls_to_lessons.py`

**Propósito**: Añadir URLs de videos de YouTube a las lecciones de los cursos existentes.

#### Funcionalidades Principales
```python
"""
Script para añadir URLs de videos de YouTube a lecciones de cursos.

Características:
- Actualiza lecciones existentes con URLs de video
- Valida formato de URLs de YouTube
- Convierte URLs a formato embed
- Actuguez@elearning.com) - instructor123
  - Especialidad: Desarrollo Web Full Stack
  - Experiencia: 10 años

- **María García** (maria.garcia@elearning.com) - instructor123
  - Especialidad: Inteligencia Artificial
  - Experiencia: 8 años

- **Ana López** (ana.lopez@elearning.com) - instructor123
  - Especialidad: Diseño UX/UI
  - Experiencia: 6 años

##### Estudiantes
- **Juan Pérez** (juan.perez@email.com) - student123
- **Laura Martínez** (laura.martinez@email.com) - student123
- **David Sánchez** (david.sanchez@el Script
```bash
# Crear usuarios de ejemplo (sin eliminar existentes)
python scripts/create_sample_users.py

# Limpiar y crear usuarios nuevos
python scripts/create_sample_users.py --clean

# Listar usuarios existentes con credenciales
python scripts/create_sample_users.py --list
```

#### Usuarios Creados
El script crea los siguientes usuarios de ejemplo:

##### Administradores
- **Email**: admin@elearning.com
- **Contraseña**: admin123
- **Rol**: admin

##### Instructores
- **Carlos Rodríguez** (carlos.rodri  parser = argparse.ArgumentParser(description="Crear usuarios de ejemplo")
    parser.add_argument("--clean", action="store_true", 
                       help="Limpiar usuarios existentes antes de crear")
    parser.add_argument("--list", action="store_true",
                       help="Listar usuarios existentes")
    
    args = parser.parse_args()
    
    if args.list:
        asyncio.run(list_created_users())
    else:
        asyncio.run(create_sample_users(clean_existing=args.clean))
```

#### Uso d    for sample_user in SAMPLE_USERS:
                if sample_user["email"] == user["email"]:
                    original_password = sample_user["password"]
                    break
            
            print(f"   📧 {user['email']}")
            print(f"   👤 {user['firstName']} {user['lastName']}")
            print(f"   🔑 {original_password}")
            print()
        
    except Exception as e:
        print(f"❌ Error listando usuarios: {e}")

if __name__ == "__main__":
    import argparse
    
  s ordenados por rol
        cursor = users_collection.find({}).sort([("role", 1), ("firstName", 1)])
        users = await cursor.to_list(length=None)
        
        current_role = None
        
        for user in users:
            if user["role"] != current_role:
                current_role = user["role"]
                print(f"\n🏷️  {current_role.upper()}S:")
                print("-" * 30)
            
            # Buscar contraseña original en SAMPLE_USERS
            original_password = "N/A"
        on.count_documents({"role": role})
        print(f"   {role.capitalize()}s: {count}")
    
    # Total
    total = await users_collection.count_documents({})
    print(f"   Total: {total}")

async def list_created_users():
    """Listar todos los usuarios creados con sus credenciales."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()
        users_collection = db.users
        
        print("👥 Usuarios disponibles para testing:")
        print("=" * 60)
        
        # Obtener usuariompletado exitosamente!")
        
    except Exception as e:
        print(f"❌ Error creando usuarios de ejemplo: {e}")
        raise

async def show_user_statistics(db):
    """
    Mostrar estadísticas de usuarios por rol.
    
    Args:
        db: Instancia de la base de datos
    """
    print("\n📈 Estadísticas de usuarios por rol:")
    
    users_collection = db.users
    
    # Contar por rol
    roles = ["admin", "instructor", "student"]
    
    for role in roles:
        count = await users_collectiain_password}")
            print(f"   ID: {result.inserted_id}")
            print()
            
            created_count += 1
        
        # Resumen final
        print("📊 Resumen de creación de usuarios:")
        print(f"   ✅ Creados: {created_count}")
        print(f"   ⏭️  Omitidos (ya existían): {skipped_count}")
        print(f"   📝 Total en SAMPLE_USERS: {len(SAMPLE_USERS)}")
        
        # Mostrar estadísticas por rol
        await show_user_statistics(db)
        
        print("\n🎉 Proceso couser_data["enrollments"],
                "coursesCreated": user_data["coursesCreated"],
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            }
            
            # Insertar usuario
            result = await users_collection.insert_one(user_doc)
            
            print(f"✅ Usuario creado: {user_data['firstName']} {user_data['lastName']} ({user_data['role']})")
            print(f"   Email: {user_data['email']}")
            print(f"   Contraseña: {plpassword = user_data["password"]
            hashed_password = hash_password(plain_password)
            
            # Preparar documento para inserción
            user_doc = {
                "firstName": user_data["firstName"],
                "lastName": user_data["lastName"],
                "email": user_data["email"],
                "password": hashed_password,
                "role": user_data["role"],
                "instructorProfile": user_data["instructorProfile"],
                "enrollments":        
        created_count = 0
        skipped_count = 0
        
        for user_data in SAMPLE_USERS:
            # Verificar si el usuario ya existe
            existing_user = await users_collection.find_one(
                {"email": user_data["email"]}
            )
            
            if existing_user:
                print(f"⏭️  Usuario ya existe: {user_data['email']}")
                skipped_count += 1
                continue
            
            # Hashear contraseña
            plain_ existentes primero
    """
    try:
        # Conectar a MongoDB
        await MongoDB.connect()
        db = MongoDB.get_db()
        users_collection = db.users
        
        print("🚀 Iniciando creación de usuarios de ejemplo...")
        
        # Limpiar usuarios existentes si se solicita
        if clean_existing:
            print("🧹 Limpiando usuarios existentes...")
            result = await users_collection.delete_many({})
            print(f"   Eliminados: {result.deleted_count} usuarios")
  {},
        "enrollments": [],
        "coursesCreated": []
    },
    {
        "firstName": "Elena",
        "lastName": "Ruiz",
        "email": "elena.ruiz@email.com",
        "password": "student123",
        "role": "student",
        "instructorProfile": {},
        "enrollments": [],
        "coursesCreated": []
    }
]

async def create_sample_users(clean_existing=False):
    """
    Crear usuarios de ejemplo en la base de datos.
    
    Args:
        clean_existing (bool): Si True, elimina usuarios": [],
        "coursesCreated": []
    },
    {
        "firstName": "Laura",
        "lastName": "Martínez",
        "email": "laura.martinez@email.com",
        "password": "student123",
        "role": "student",
        "instructorProfile": {},
        "enrollments": [],
        "coursesCreated": []
    },
    {
        "firstName": "David",
        "lastName": "Sánchez",
        "email": "david.sanchez@email.com",
        "password": "student123",
        "role": "student",
        "instructorProfile":in.com/in/ana-lopez-ux",
                "behance": "https://behance.net/ana-lopez-design"
            },
            "yearsExperience": 6,
            "totalStudents": 0,
            "averageRating": 0.0
        },
        "enrollments": [],
        "coursesCreated": []
    },
    
    # Estudiantes
    {
        "firstName": "Juan",
        "lastName": "Pérez",
        "email": "juan.perez@email.com",
        "password": "student123",
        "role": "student",
        "instructorProfile": {},
        "enrollmentsastName": "López",
        "email": "ana.lopez@elearning.com",
        "password": "instructor123",
        "role": "instructor",
        "instructorProfile": {
            "avatarUrl": "/assets/images/instructors/Inst_Ana_Lopez.webp",
            "bio": "Diseñadora UX/UI con pasión por crear experiencias digitales intuitivas y accesibles. Especializada en design systems y metodologías ágiles.",
            "expertise": "Diseño UX/UI",
            "socialLinks": {
                "linkedin": "https://linkedon experiencia en investigación y desarrollo de algoritmos avanzados.",
            "expertise": "Inteligencia Artificial",
            "socialLinks": {
                "linkedin": "https://linkedin.com/in/maria-garcia-ai",
                "github": "https://github.com/maria-garcia-ai"
            },
            "yearsExperience": 8,
            "totalStudents": 0,
            "averageRating": 0.0
        },
        "enrollments": [],
        "coursesCreated": []
    },
    {
        "firstName": "Ana",
        "lts": 0,
            "averageRating": 0.0
        },
        "enrollments": [],
        "coursesCreated": []
    },
    {
        "firstName": "María",
        "lastName": "García",
        "email": "maria.garcia@elearning.com",
        "password": "instructor123",
        "role": "instructor",
        "instructorProfile": {
            "avatarUrl": "/assets/images/instructors/Inst_Maria_Garcia.webp",
            "bio": "Experta en Inteligencia Artificial y Machine Learning. Doctora en Ciencias de la Computación c"bio": "Desarrollador Full Stack con más de 10 años de experiencia en tecnologías web modernas. Especializado en React, Node.js y arquitecturas escalables.",
            "expertise": "Desarrollo Web Full Stack",
            "socialLinks": {
                "linkedin": "https://linkedin.com/in/carlos-rodriguez-dev",
                "github": "https://github.com/carlos-rodriguez",
                "twitter": "https://twitter.com/carlosdev"
            },
            "yearsExperience": 10,
            "totalStuden "admin@elearning.com",
        "password": "admin123",
        "role": "admin",
        "instructorProfile": {},
        "enrollments": [],
        "coursesCreated": []
    },
    
    # Instructores
    {
        "firstName": "Carlos",
        "lastName": "Rodríguez",
        "email": "carlos.rodriguez@elearning.com",
        "password": "instructor123",
        "role": "instructor",
        "instructorProfile": {
            "avatarUrl": "/assets/images/instructors/Inst_Carlos_Rodriguez.webp",
            oles (student, instructor, admin)
- Contraseñas hasheadas con bcrypt
- Datos realistas y variados
- Perfiles de instructor completos
- Validación de duplicados
- Opción de limpieza previa
"""

import asyncio
from datetime import datetime
from E_Learning_JCB_Reflex.database.mongodb import MongoDB
from E_Learning_JCB_Reflex.utils.password import hash_password

# Datos de usuarios de ejemplo
SAMPLE_USERS = [
    # Administradores
    {
        "firstName": "Admin",
        "lastName": "Principal",
        "email":rses.instructor.userId_1
   ✅ courses.category_1
   ✅ contacts.email_1
   ✅ contacts.status_1

🔌 Conexión cerrada correctamente
✅ Todas las pruebas de conexión pasaron exitosamente
```

---

## 👥 Script de Creación de Usuarios de Ejemplo

### `scripts/create_sample_users.py`

**Propósito**: Crear usuarios de ejemplo para desarrollo y testing con datos realistas.

#### Funcionalidades Principales
```python
"""
Script para crear usuarios de ejemplo en la base de datos.

Características:
- Crea usuarios de los 3 r logging detallado
PYTHONPATH=. python scripts/test_connection.py

# Verificar desde directorio raíz
python -m scripts.test_connection
```

#### Salida Esperada
```
🚀 Iniciando prueba de conexión a MongoDB Atlas...
🔄 Conectando a MongoDB Atlas...
✅ Conexión exitosa a MongoDB Atlas
📊 Base de datos: elearning_jcb
📁 Colecciones encontradas: 4
   - users: 15 documentos
   - courses: 8 documentos
   - contacts: 3 documentos
   - lessons: 45 documentos

🔍 Verificando índices críticos...
   ✅ users.email_1
   ✅ cou except Exception as e:
        print(f"   ❌ Error en operaciones básicas: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando prueba de conexión a MongoDB Atlas...")
    success = asyncio.run(test_mongodb_connection())
    
    if success:
        print("\n✅ Todas las pruebas de conexión pasaron exitosamente")
        exit(0)
    else:
        print("\n❌ Falló la prueba de conexión")
        exit(1)
```

#### Uso del Script
```bash
# Ejecutar verificación básica
python scripts/test_connection.py

# Conecuperado correctamente")
        
        # Test de actualización
        await test_collection.update_one(
            {"_id": result.inserted_id},
            {"$set": {"updated": True}}
        )
        print("   ✅ Actualización: Documento modificado")
        
        # Test de eliminación
        await test_collection.delete_one({"_id": result.inserted_id})
        print("   ✅ Eliminación: Documento eliminado")
        
        # Limpiar colección de prueba
        await test_collection.drop()
        
   est_collection = db.test_connection
        test_doc = {
            "test": True,
            "timestamp": datetime.now(),
            "message": "Test de conexión exitoso"
        }
        
        result = await test_collection.insert_one(test_doc)
        print(f"   ✅ Escritura: Documento insertado con ID {result.inserted_id}")
        
        # Test de lectura
        found_doc = await test_collection.find_one({"_id": result.inserted_id})
        if found_doc:
            print("   ✅ Lectura: Documento red_indexes:
                if expected_index in indexes:
                    print(f"   ✅ {collection_name}.{expected_index}")
                else:
                    print(f"   ⚠️  {collection_name}.{expected_index} - FALTANTE")

async def test_basic_operations(db):
    """
    Probar operaciones básicas CRUD.
    
    Args:
        db: Instancia de la base de datos
    """
    print("\n🧪 Probando operaciones básicas...")
    
    try:
        # Test de escritura (insertar documento temporal)
        t  print("\n🔍 Verificando índices críticos...")
    
    critical_indexes = {
        "users": ["email_1"],
        "courses": ["instructor.userId_1", "category_1"],
        "contacts": ["email_1", "status_1"]
    }
    
    for collection_name, expected_indexes in critical_indexes.items():
        if collection_name in await db.list_collection_names():
            collection = db[collection_name]
            indexes = await collection.index_information()
            
            for expected_index in expecttion_name}: {count} documentos")
        
        # Verificar índices críticos
        await verify_indexes(db)
        
        # Cerrar conexión
        client.close()
        print("🔌 Conexión cerrada correctamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

async def verify_indexes(db):
    """
    Verificar que los índices críticos estén presentes.
    
    Args:
        db: Instancia de la base de datos
    """
  ener base de datos
        db = client.get_default_database()
        db_name = db.name
        print(f"📊 Base de datos: {db_name}")
        
        # Listar colecciones
        collections = await db.list_collection_names()
        print(f"📁 Colecciones encontradas: {len(collections)}")
        
        # Estadísticas por colección
        for collection_name in collections:
            collection = db[collection_name]
            count = await collection.count_documents({})
            print(f"   - {collecGODB_URI no encontrada en variables de entorno")
        return False
    
    try:
        print("🔄 Conectando a MongoDB Atlas...")
        
        # Crear cliente con timeout corto para prueba rápida
        client = AsyncIOMotorClient(
            mongodb_uri,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000
        )
        
        # Verificar conexión con ping
        await client.admin.command('ping')
        print("✅ Conexión exitosa a MongoDB Atlas")
        
        # ObtClient
from dotenv import load_dotenv

async def test_mongodb_connection():
    """
    Probar conexión completa a MongoDB Atlas.
    
    Verificaciones:
    1. Conectividad de red
    2. Autenticación de credenciales
    3. Acceso a la base de datos
    4. Listado de colecciones
    5. Conteo de documentos por colección
    6. Verificación de índices
    """
    
    # Cargar variables de entorno
    load_dotenv()
    mongodb_uri = os.getenv("MONGODB_URI")
    
    if not mongodb_uri:
        print("❌ Error: MONión

### `scripts/test_connection.py`

**Propósito**: Verificar la conectividad con MongoDB Atlas y validar la configuración de la base de datos.

#### Funcionalidades Principales
```python
"""
Script para verificar la conexión a MongoDB Atlas.

Características:
- Prueba de conectividad básica
- Verificación de autenticación
- Listado de colecciones disponibles
- Estadísticas básicas de la base de datos
- Validación de índices críticos
"""

import asyncio
import os
from motor.motor_asyncio import AsyncIOMotoro `scripts/`

El proyecto incluye **3 scripts principales** para configuración, testing y mantenimiento de la base de datos:

| Script | Propósito | Uso | Estado |
|--------|-----------|-----|--------|
| `test_connection.py` | Verificar conexión a MongoDB | Diagnóstico | ✅ Funcional |
| `create_sample_users.py` | Crear usuarios de ejemplo | Desarrollo/Testing | ✅ Funcional |
| `add_video_urls_to_lessons.py` | Añadir URLs de video a lecciones | Mantenimiento | ✅ Funcional |

---

## 🔍 Script de Verificación de Conex# Scripts y Utilidades - E-Learning JCB Reflex

## 🛠️ Scripts de Configuración y Mantenimiento

### Directori