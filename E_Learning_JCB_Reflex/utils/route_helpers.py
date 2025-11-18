'''
Docstring para E_Learning_JCB_Reflex.utils.route_helpers
'''

def get_dynamic_id(path: str, index: int = -1) -> str:
    """
    Obtiene el ID dinámico de una ruta dada.

    Args:
        path (str): La ruta de la cual extraer el ID.
        index (int, optional): El índice del segmento de la ruta que se desea obtener. Por defecto es -1 (último segmento).

    Returns:
        str: El ID dinámico extraído de la ruta.
    """      
    segments = path.strip("/").split("/")
    if len(segments) == 0:
        return ""
    return segments[index]