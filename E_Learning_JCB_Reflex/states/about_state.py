"""
Estado para la página Sobre Nosotros.

Carga estadísticas reales de la plataforma desde MongoDB.
"""

import reflex as rx
from E_Learning_JCB_Reflex.database.mongodb import MongoDB


class AboutState(rx.State):
    """Estadísticas reales de la plataforma cargadas desde la BD."""

    total_courses: int = 0
    total_instructors: int = 0
    total_students: int = 0
    total_lessons: int = 0
    total_enrollments: int = 0
    categories: list[str] = []
    loading: bool = False

    async def load_stats(self):
        self.loading = True
        try:
            await MongoDB.connect()
            db = MongoDB.get_db()

            # Cursos
            courses = await db["courses"].find({}).to_list(length=None)
            self.total_courses = len(courses)
            self.total_lessons = sum(len(c.get("lessons", [])) for c in courses)
            self.total_enrollments = sum(len(c.get("students", [])) for c in courses)

            # Categorías únicas
            cats = set()
            for c in courses:
                for cat in c.get("categories", []):
                    if cat:
                        cats.add(cat)
            self.categories = sorted(cats)

            # Usuarios
            users = await db["users"].find({}, {"role": 1}).to_list(length=None)
            self.total_instructors = sum(1 for u in users if u.get("role") == "instructor")
            self.total_students = sum(1 for u in users if u.get("role") == "student")

        except Exception as e:
            print(f"[AboutState] Error cargando stats: {e}")
        finally:
            self.loading = False
