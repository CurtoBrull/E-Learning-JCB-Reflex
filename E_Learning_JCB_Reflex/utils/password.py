"""
Utilidades para el manejo seguro de contraseñas con bcrypt.

Este módulo proporciona funciones para hashear y verificar contraseñas
de forma segura utilizando el algoritmo bcrypt. Todas las contraseñas
se almacenan hasheadas en la base de datos para proteger la información
de los usuarios.

Funciones:
- hash_password: Hashea una contraseña con bcrypt
- verify_password: Verifica una contraseña contra su hash
- is_password_strong: Valida requisitos de seguridad de contraseña
"""

import bcrypt


def hash_password(password: str) -> str:
    """
    Hashea una contraseña usando el algoritmo bcrypt.

    Bcrypt genera automáticamente un salt único para cada contraseña,
    lo que hace que dos contraseñas iguales produzcan hashes diferentes.
    Esto protege contra ataques de rainbow tables.

    Args:
        password: Contraseña en texto plano a hashear

    Returns:
        str: Contraseña hasheada en formato string (listo para guardar en MongoDB)

    Ejemplo:
        >>> hashed = hash_password("micontraseña123")
        >>> # Resultado: "$2b$12$..." (60 caracteres)

    Nota:
        El hash generado incluye el salt y puede almacenarse directamente
        como string en MongoDB. No es necesario almacenar el salt por separado.
    """
    # Convertir la contraseña a bytes (requerido por bcrypt)
    password_bytes = password.encode('utf-8')

    # Generar salt automático y hashear la contraseña
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)

    # Retornar como string para almacenar en MongoDB
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con su hash bcrypt.

    Utiliza bcrypt.checkpw() para verificar de forma segura si la contraseña
    proporcionada coincide con el hash almacenado. Bcrypt se encarga de
    extraer el salt del hash y realizar la comparación.

    Args:
        plain_password: Contraseña en texto plano a verificar (proporcionada por el usuario)
        hashed_password: Hash bcrypt almacenado en la base de datos

    Returns:
        bool: True si la contraseña es correcta, False si es incorrecta o hay error

    Ejemplo:
        >>> hashed = hash_password("micontraseña123")
        >>> verify_password("micontraseña123", hashed)
        True
        >>> verify_password("contraseñaincorrecta", hashed)
        False

    Nota:
        La función maneja excepciones internamente y retorna False si hay
        algún error (por ejemplo, si el hash está corrupto).
    """
    try:
        # Convertir ambas strings a bytes (requerido por bcrypt)
        password_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')

        # Verificar la contraseña contra el hash usando bcrypt
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    except Exception as e:
        print(f"Error verifying password: {e}")
        return False


def is_password_strong(password: str) -> tuple[bool, str]:
    """
    Valida si una contraseña cumple con los requisitos mínimos de seguridad.

    Actualmente valida solo la longitud de la contraseña (6-128 caracteres).
    Se pueden agregar más validaciones como mayúsculas, números, caracteres
    especiales, etc.

    Args:
        password: Contraseña a validar

    Returns:
        tuple: (es_válida, mensaje_error)
            - es_válida (bool): True si cumple los requisitos, False si no
            - mensaje_error (str): Descripción del error si no es válida, "" si es válida

    Ejemplo:
        >>> is_password_strong("abc")
        (False, "La contraseña debe tener al menos 6 caracteres")
        >>> is_password_strong("micontraseña123")
        (True, "")

    Nota:
        Se pueden descomentar las validaciones adicionales en el código para
        requerir mayúsculas, minúsculas y números en la contraseña.
    """
    # Validar longitud mínima
    if len(password) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres"

    # Validar longitud máxima (bcrypt tiene límite de 72 bytes, pero 128 chars es razonable)
    if len(password) > 128:
        return False, "La contraseña es demasiado larga (máximo 128 caracteres)"

    # Opcional: Validaciones adicionales de complejidad
    # Descomentar para requerir mayúsculas, minúsculas y números
    # has_upper = any(c.isupper() for c in password)
    # has_lower = any(c.islower() for c in password)
    # has_digit = any(c.isdigit() for c in password)

    # if not (has_upper and has_lower and has_digit):
    #     return False, "La contraseña debe contener mayúsculas, minúsculas y números"

    return True, ""
