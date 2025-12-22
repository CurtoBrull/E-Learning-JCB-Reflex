"""
Servicio de usuarios para operaciones de base de datos.

Este módulo proporciona todas las funciones necesarias para gestionar usuarios
en la base de datos MongoDB. Incluye operaciones CRUD, autenticación, búsqueda
y gestión de contraseñas.

Funciones principales:
- get_user_by_id: Obtener usuario por ID
- get_user_by_email: Obtener usuario por email
- create_user: Crear nuevo usuario con contraseña hasheada
- update_user: Actualizar datos de usuario
- delete_user: Eliminar usuario
- change_password: Cambiar contraseña de usuario
- get_all_students/instructors/admins: Obtener usuarios por rol
"""

from typing import List, Dict
from bson import ObjectId
from E_Learning_JCB_Reflex.models.user import User
from E_Learning_JCB_Reflex.database import MongoDB
from E_Learning_JCB_Reflex.utils.password import hash_password, verify_password


async def get_user_by_id(user_id: str) -> User | None:
    """
    Obtener un usuario por su ID.

    Busca un usuario en la base de datos usando su ObjectId de MongoDB.

    Args:
        user_id: ID del usuario (string del ObjectId de MongoDB)

    Returns:
        User | None: Objeto User si se encuentra, None si no existe o hay error

    Ejemplo:
        >>> user = await get_user_by_id("507f1f77bcf86cd799439011")
        >>> if user:
        ...     print(user.get_full_name())
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]
        user_data = await users_collection.find_one({"_id": ObjectId(user_id)})

        if user_data:
            return User.from_dict(user_data)
        return None

    except Exception as e:
        print(f"Error fetching user by ID: {e}")
        return None


async def get_users_by_ids(user_ids: List[str]) -> Dict[str, User]:
    """
    Obtener múltiples usuarios por sus IDs en una sola consulta.

    Optimización para obtener varios usuarios de una vez, evitando múltiples
    consultas a la base de datos. Útil para poblar referencias de usuarios
    en listados o cuando se necesitan datos de múltiples usuarios.

    Args:
        user_ids: Lista de IDs de usuarios (strings de ObjectIds)

    Returns:
        Dict[str, User]: Diccionario con ID como clave y objeto User como valor.
                        Retorna diccionario vacío si hay error.

    Ejemplo:
        >>> user_ids = ["507f1f77bcf86cd799439011", "507f1f77bcf86cd799439012"]
        >>> users = await get_users_by_ids(user_ids)
        >>> for user_id, user in users.items():
        ...     print(f"{user_id}: {user.get_full_name()}")
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        # Convertir strings a ObjectIds (filtrar IDs vacíos)
        object_ids = [ObjectId(uid) for uid in user_ids if uid]

        # Obtener todos los usuarios en una sola consulta usando $in
        cursor = users_collection.find({"_id": {"$in": object_ids}})
        users_data = await cursor.to_list(length=None)

        # Crear diccionario con ID (string) como clave para fácil acceso
        users_dict = {}
        for user_data in users_data:
            user = User.from_dict(user_data)
            users_dict[user.id] = user

        return users_dict

    except Exception as e:
        print(f"Error fetching users by IDs: {e}")
        return {}


async def get_user_name(user_id: str) -> str:
    """
    Obtener nombre completo de un usuario por ID.

    Helper function que retorna el nombre completo directamente.
    Si no encuentra el usuario, retorna "Usuario Desconocido".
    """
    user = await get_user_by_id(user_id)
    if user:
        return user.get_full_name()
    return "Usuario Desconocido"


async def get_all_students() -> List[User]:
    """Obtener todos los usuarios con role='student'."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]
        cursor = users_collection.find({"role": "student"})
        users_data = await cursor.to_list(length=None)

        return [User.from_dict(user_data) for user_data in users_data]

    except Exception as e:
        print(f"Error fetching students: {e}")
        return []


async def get_all_instructors() -> List[User]:
    """Obtener todos los usuarios con role='instructor'."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]
        cursor = users_collection.find({"role": "instructor"})
        users_data = await cursor.to_list(length=None)

        return [User.from_dict(user_data) for user_data in users_data]

    except Exception as e:
        print(f"Error fetching instructors: {e}")
        return []


async def get_user_by_email(email: str) -> User | None:
    """Obtener un usuario por email."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]
        user_data = await users_collection.find_one({"email": email})

        if user_data:
            return User.from_dict(user_data)
        return None

    except Exception as e:
        print(f"Error fetching user by email: {e}")
        return None


async def get_all_admins() -> List[User]:
    """Obtener todos los usuarios con role='admin'."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]
        cursor = users_collection.find({"role": "admin"})
        users_data = await cursor.to_list(length=None)

        return [User.from_dict(user_data) for user_data in users_data]

    except Exception as e:
        print(f"Error fetching admins: {e}")
        return []


async def create_user(
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    role: str = "student"
) -> bool:
    """
    Crear un nuevo usuario en la base de datos.

    Crea un nuevo usuario con contraseña hasheada usando bcrypt. La contraseña
    se hashea automáticamente antes de almacenarla en la base de datos por
    seguridad. MongoDB genera automáticamente el _id del usuario.

    Args:
        first_name: Nombre del usuario
        last_name: Apellido del usuario
        email: Correo electrónico único del usuario
        password: Contraseña en texto plano (se hasheará automáticamente)
        role: Rol del usuario ("student", "instructor" o "admin"). Por defecto "student"

    Returns:
        bool: True si el usuario se creó exitosamente, False si hubo error

    Ejemplo:
        >>> success = await create_user(
        ...     first_name="Juan",
        ...     last_name="Pérez",
        ...     email="juan@email.com",
        ...     password="password123",
        ...     role="student"
        ... )
        >>> if success:
        ...     print("Usuario creado exitosamente")

    Nota:
        La función NO verifica si el email ya existe. Esa validación debe
        hacerse antes de llamar a esta función.
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        # Hashear la contraseña con bcrypt para seguridad
        hashed_password = hash_password(password)

        # Crear el objeto de usuario con password hasheado
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password,
            role=role
        )

        # Convertir a diccionario para MongoDB (formato camelCase)
        user_dict = user.to_dict()

        # Remover el id si está presente (MongoDB lo generará automáticamente)
        if "id" in user_dict:
            del user_dict["id"]

        # Insertar en la base de datos
        result = await users_collection.insert_one(user_dict)

        return result.acknowledged

    except Exception as e:
        print(f"Error creating user: {e}")
        return False


async def update_user(user_id: str, update_data: dict) -> bool:
    """
    Actualizar los datos de un usuario existente.

    Actualiza campos específicos de un usuario usando la operación $set de MongoDB.
    Solo actualiza los campos proporcionados en update_data.

    Args:
        user_id: ID del usuario a actualizar
        update_data: Diccionario con los campos a actualizar (en formato camelCase de MongoDB)

    Returns:
        bool: True si se encontró el usuario (aunque no se haya modificado),
              False si el usuario no existe o hay error

    Ejemplo:
        >>> update_data = {"firstName": "Juan Carlos", "role": "instructor"}
        >>> success = await update_user("507f1f77bcf86cd799439011", update_data)

    Nota:
        - La función retorna True si encuentra el usuario, aunque los valores
          sean iguales y no se modifique nada (matched_count > 0).
        - NO actualiza la contraseña. Usar change_password() para eso.
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        result = await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )

        # Retornar True si se encontró el usuario (matched_count > 0)
        # No importa si se modificó o no (modified_count puede ser 0 si los valores son iguales)
        return result.matched_count > 0

    except Exception as e:
        print(f"Error updating user: {e}")
        return False


async def change_password(user_id: str, current_password: str, new_password: str) -> bool:
    """
    Cambiar la contraseña de un usuario.

    Verifica la contraseña actual antes de cambiarla por seguridad.
    La nueva contraseña se hashea automáticamente con bcrypt.

    Args:
        user_id: ID del usuario
        current_password: Contraseña actual en texto plano (para verificación)
        new_password: Nueva contraseña en texto plano (se hasheará)

    Returns:
        bool: True si se cambió la contraseña exitosamente, False si:
              - El usuario no existe
              - La contraseña actual es incorrecta
              - Ocurrió un error

    Ejemplo:
        >>> success = await change_password(
        ...     user_id="507f1f77bcf86cd799439011",
        ...     current_password="password123",
        ...     new_password="newpassword456"
        ... )
        >>> if success:
        ...     print("Contraseña cambiada exitosamente")
        ... else:
        ...     print("Contraseña actual incorrecta")
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        # Obtener el usuario actual para verificar contraseña
        user_data = await users_collection.find_one({"_id": ObjectId(user_id)})

        if not user_data:
            return False

        # Verificar la contraseña actual con bcrypt
        if not verify_password(current_password, user_data.get("password", "")):
            return False

        # Hashear la nueva contraseña con bcrypt
        hashed_new_password = hash_password(new_password)

        # Actualizar la contraseña en la base de datos
        result = await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"password": hashed_new_password}}
        )

        return result.modified_count > 0

    except Exception as e:
        print(f"Error changing password: {e}")
        return False


async def admin_change_password(user_id: str, new_password: str) -> bool:
    """
    Cambiar la contraseña de un usuario sin verificar la contraseña actual.

    Esta función es exclusiva para administradores y permite cambiar la contraseña
    de cualquier usuario sin necesidad de conocer su contraseña actual. Se debe
    verificar que el usuario que llama a esta función sea admin antes de ejecutarla.

    Args:
        user_id: ID del usuario al que se le cambiará la contraseña
        new_password: Nueva contraseña en texto plano (se hasheará)

    Returns:
        bool: True si se encontró y actualizó el usuario, False si no existe o hay error

    Ejemplo:
        >>> # Solo llamar si el usuario autenticado es admin
        >>> if current_user.is_admin:
        ...     success = await admin_change_password("507f1f77bcf86cd799439011", "newpass123")

    Advertencia:
        Esta función NO verifica permisos de admin. Esa verificación debe
        hacerse en la capa de estado/controlador antes de llamar a esta función.
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        # Hashear la nueva contraseña con bcrypt
        hashed_new_password = hash_password(new_password)

        # Actualizar la contraseña sin verificar la actual
        result = await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"password": hashed_new_password}}
        )

        return result.matched_count > 0

    except Exception as e:
        print(f"Error changing password (admin): {e}")
        return False


async def delete_user(user_id: str) -> bool:
    """
    Eliminar un usuario del sistema permanentemente.

    Elimina completamente un usuario de la base de datos. Esta operación
    es irreversible.

    Args:
        user_id: ID del usuario a eliminar

    Returns:
        bool: True si se eliminó el usuario, False si no existe o hay error

    Ejemplo:
        >>> success = await delete_user("507f1f77bcf86cd799439011")
        >>> if success:
        ...     print("Usuario eliminado exitosamente")

    Advertencia:
        - Esta operación es IRREVERSIBLE
        - NO elimina automáticamente las referencias del usuario en otras colecciones
          (como inscripciones a cursos). Eso debe manejarse manualmente si es necesario.
        - Verificar permisos de admin antes de llamar a esta función
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        result = await users_collection.delete_one({"_id": ObjectId(user_id)})

        return result.deleted_count > 0

    except Exception as e:
        print(f"Error deleting user: {e}")
        return False


class UserService:
    """
    Clase de servicio para centralizar todas las operaciones de usuario.

    Esta clase proporciona una interfaz unificada para acceder a todas las
    funciones de gestión de usuarios. Todos los métodos son estáticos y
    simplemente delegan a las funciones correspondientes.

    La instancia global 'user_service' está disponible para usar en toda la aplicación.

    Ejemplo:
        >>> from E_Learning_JCB_Reflex.services.user_service import user_service
        >>> user = await user_service.get_user_by_email("juan@email.com")
    """

    @staticmethod
    async def get_user_by_id(user_id: str) -> User | None:
        return await get_user_by_id(user_id)

    @staticmethod
    async def get_users_by_ids(user_ids: List[str]) -> Dict[str, User]:
        return await get_users_by_ids(user_ids)

    @staticmethod
    async def get_user_name(user_id: str) -> str:
        return await get_user_name(user_id)

    @staticmethod
    async def get_all_students() -> List[User]:
        return await get_all_students()

    @staticmethod
    async def get_all_instructors() -> List[User]:
        return await get_all_instructors()

    @staticmethod
    async def get_user_by_email(email: str) -> User | None:
        return await get_user_by_email(email)

    @staticmethod
    async def create_user(first_name: str, last_name: str, email: str, password: str, role: str = "student") -> bool:
        return await create_user(first_name, last_name, email, password, role)

    @staticmethod
    async def update_user(user_id: str, update_data: dict) -> bool:
        return await update_user(user_id, update_data)

    @staticmethod
    async def change_password(user_id: str, current_password: str, new_password: str) -> bool:
        return await change_password(user_id, current_password, new_password)

    @staticmethod
    async def get_all_admins() -> List[User]:
        return await get_all_admins()

    @staticmethod
    async def admin_change_password(user_id: str, new_password: str) -> bool:
        return await admin_change_password(user_id, new_password)

    @staticmethod
    async def delete_user(user_id: str) -> bool:
        return await delete_user(user_id)


# Instancia global del servicio
user_service = UserService()
