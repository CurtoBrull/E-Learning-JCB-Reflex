"""User service for database operations."""

from typing import List, Dict
from bson import ObjectId
from E_Learning_JCB_Reflex.models.user import User
from E_Learning_JCB_Reflex.database import MongoDB
from E_Learning_JCB_Reflex.utils.password import hash_password


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


async def create_user(
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    role: str = "student"
) -> bool:
    """Crear un nuevo usuario en la base de datos con password hasheado."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        # Hashear la contraseña con bcrypt
        hashed_password = hash_password(password)

        # Crear el objeto de usuario con password hasheado
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password,
            role=role
        )

        # Convertir a diccionario para MongoDB
        user_dict = user.to_dict()

        # Remover el id si está presente (MongoDB lo generará)
        if "id" in user_dict:
            del user_dict["id"]

        # Insertar en la base de datos
        result = await users_collection.insert_one(user_dict)

        return result.acknowledged

    except Exception as e:
        print(f"Error creating user: {e}")
        return False


async def update_user(user_id: str, update_data: dict) -> bool:
    """Actualizar un usuario existente."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        result = await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )

        return result.modified_count > 0

    except Exception as e:
        print(f"Error updating user: {e}")
        return False
