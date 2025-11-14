"""User service for database operations."""

from typing import List, Dict
from bson import ObjectId
from E_Learning_JCB_Reflex.models.user import User
from E_Learning_JCB_Reflex.database import MongoDB


async def get_user_by_id(user_id: str) -> User | None:
    """Obtener un usuario por ID."""
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
    Obtener múltiples usuarios por IDs.

    Retorna un diccionario con ID como clave y User como valor.
    Útil para poblar múltiples referencias de usuarios eficientemente.
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        # Convertir strings a ObjectIds
        object_ids = [ObjectId(uid) for uid in user_ids if uid]

        # Obtener todos los usuarios en una sola consulta
        cursor = users_collection.find({"_id": {"$in": object_ids}})
        users_data = await cursor.to_list(length=None)

        # Crear diccionario con ID (string) como clave
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
