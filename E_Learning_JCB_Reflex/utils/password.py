"""Utilidades para el manejo seguro de contraseñas con bcrypt."""

import bcrypt


def hash_password(password: str) -> str:
    """
    Hashea una contraseña usando bcrypt.

    Args:
        password: Contraseña en texto plano

    Returns:
        str: Contraseña hasheada en formato string
    """
    # Convertir la contraseña a bytes
    password_bytes = password.encode('utf-8')

    # Generar salt y hashear
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)

    # Retornar como string para almacenar en MongoDB
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con su hash.

    Args:
        plain_password: Contraseña en texto plano a verificar
        hashed_password: Hash almacenado en la base de datos

    Returns:
        bool: True si la contraseña es correcta, False en caso contrario
    """
    try:
        # Convertir ambas a bytes
        password_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')

        # Verificar
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    except Exception as e:
        print(f"Error verifying password: {e}")
        return False


def is_password_strong(password: str) -> tuple[bool, str]:
    """
    Verifica si una contraseña cumple con los requisitos de seguridad.

    Args:
        password: Contraseña a validar

    Returns:
        tuple: (es_válida: bool, mensaje_error: str)
    """
    if len(password) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres"

    if len(password) > 128:
        return False, "La contraseña es demasiado larga (máximo 128 caracteres)"

    # Opcional: Puedes agregar más validaciones
    # has_upper = any(c.isupper() for c in password)
    # has_lower = any(c.islower() for c in password)
    # has_digit = any(c.isdigit() for c in password)

    # if not (has_upper and has_lower and has_digit):
    #     return False, "La contraseña debe contener mayúsculas, minúsculas y números"

    return True, ""
