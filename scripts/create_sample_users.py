"""Script para crear usuarios de ejemplo en la base de datos."""

import asyncio
import sys
from pathlib import Path

# Añadir el directorio raíz al path
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from E_Learning_JCB_Reflex.services import user_service


async def create_sample_users():
    """Crear usuarios de ejemplo para cada rol."""
    print("🔧 Creando usuarios de ejemplo...\n")

    users_to_create = [
        {
            "first_name": "María",
            "last_name": "García",
            "email": "maria.garcia@elearningjcb.com",
            "password": "student123",
            "role": "student"
        },
        {
            "first_name": "Carlos",
            "last_name": "Rodríguez",
            "email": "carlos.rodriguez@elearningjcb.com",
            "password": "instructor123",
            "role": "instructor"
        },
        {
            "first_name": "Ana",
            "last_name": "Martínez",
            "email": "ana.martinez@elearningjcb.com",
            "password": "admin123",
            "role": "admin"
        }
    ]

    for user_data in users_to_create:
        # Verificar si el usuario ya existe
        existing_user = await user_service.get_user_by_email(user_data["email"])

        if existing_user:
            print(f"⚠️  Usuario {user_data['email']} ya existe, saltando...")
            continue

        # Crear el usuario
        result = await user_service.create_user(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            password=user_data["password"],
            role=user_data["role"]
        )

        if result:
            print(f"✅ Usuario creado: {user_data['first_name']} {user_data['last_name']} ({user_data['role']})")
            print(f"   Email: {user_data['email']}")
            print(f"   Password: {user_data['password']}\n")
        else:
            print(f"❌ Error al crear usuario: {user_data['email']}\n")

    print("✨ Proceso completado!")


if __name__ == "__main__":
    asyncio.run(create_sample_users())
