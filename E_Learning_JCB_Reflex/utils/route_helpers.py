"""
Utilidades para manejo de rutas dinámicas en Reflex.

Este módulo proporciona funciones auxiliares para trabajar con rutas dinámicas
en la aplicación Reflex, especialmente para extraer IDs y parámetros de las URLs.
"""


def get_dynamic_id(path: str, index: int = -1) -> str:
    """
    Extrae un ID dinámico de una ruta URL.

    Esta función es útil para obtener IDs de rutas dinámicas como
    "/courses/507f1f77bcf86cd799439011" o "/users/123/edit".

    Args:
        path: La ruta URL completa de la cual extraer el ID
        index: Índice del segmento de la ruta a obtener. Por defecto -1 (último segmento)
              - -1: último segmento (más común para IDs)
              - 0: primer segmento
              - 1: segundo segmento, etc.

    Returns:
        str: El ID extraído de la ruta, o "" si la ruta está vacía

    Ejemplos:
        >>> get_dynamic_id("/courses/507f1f77bcf86cd799439011")
        '507f1f77bcf86cd799439011'

        >>> get_dynamic_id("/courses/507f1f77bcf86cd799439011", index=-1)
        '507f1f77bcf86cd799439011'

        >>> get_dynamic_id("/courses/507f1f77bcf86cd799439011", index=0)
        'courses'

        >>> get_dynamic_id("/users/123/edit", index=-2)
        '123'

    Nota:
        La función elimina barras diagonales al inicio y final antes de dividir
        la ruta en segmentos.
    """
    # Eliminar barras al inicio/final y dividir por "/"
    segments = path.strip("/").split("/")

    # Retornar cadena vacía si no hay segmentos
    if len(segments) == 0:
        return ""

    # Retornar el segmento en el índice especificado
    return segments[index]
