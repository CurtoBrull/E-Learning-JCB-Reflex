"""
Script para agregar URLs de videos de YouTube a las lecciones existentes.

Este script actualiza todas las lecciones en la base de datos para agregar
el campo video_url con videos de ejemplo de YouTube.
"""
import asyncio
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

# Videos de ejemplo de YouTube para desarrollo web
EXAMPLE_VIDEOS = [
    "https://www.youtube.com/watch?v=qz0aGYrrlhU",  # HTML Tutorial
    "https://www.youtube.com/watch?v=yfoY53QXEnI",  # CSS Tutorial
    "https://www.youtube.com/watch?v=W6NZfCO5SIk",  # JavaScript Tutorial
    "https://www.youtube.com/watch?v=SBmSRK3feww",  # JavaScript ES6
    "https://www.youtube.com/watch?v=Oe421EPjeBE",  # React Tutorial
    "https://www.youtube.com/watch?v=f2EqECiTBL8",  # Node.js Tutorial
    "https://www.youtube.com/watch?v=rRgD1yVwIvE",  # Express.js Tutorial
    "https://www.youtube.com/watch?v=ExsyufNRoMw",  # MongoDB Tutorial
    "https://www.youtube.com/watch?v=0W5Z4Jq2M8c",  # API REST Tutorial
    "https://www.youtube.com/watch?v=72iEz5iopqQ",  # Full Stack Tutorial
    "https://www.youtube.com/watch?v=JnEH9tYLxLk",  # Deployment Tutorial
]


async def update_lessons_with_videos():
    """Actualiza todas las lecciones agregando video_url."""

    client = AsyncIOMotorClient(MONGODB_URI)
    db = client.get_default_database()
    courses_collection = db["courses"]

    print("🔍 Buscando cursos en la base de datos...")

    # Obtener todos los cursos
    courses = await courses_collection.find({}).to_list(length=None)

    print(f"✓ Encontrados {len(courses)} cursos")

    for course in courses:
        course_id = course["_id"]
        course_title = course.get("title", "Sin título")
        lessons = course.get("lessons", [])

        if not lessons:
            print(f"  ⚠ Curso '{course_title}' no tiene lecciones")
            continue

        print(f"\n📚 Procesando curso: {course_title}")
        print(f"  Lecciones encontradas: {len(lessons)}")

        # Actualizar cada lección con una URL de video
        updated_lessons = []
        for i, lesson in enumerate(lessons):
            # Asignar un video de ejemplo (cíclico si hay más lecciones que videos)
            video_url = EXAMPLE_VIDEOS[i % len(EXAMPLE_VIDEOS)]

            # Agregar video_url a la lección (forzar actualización)
            current_url = lesson.get("video_url", "")
            if not current_url or current_url.strip() == "":
                lesson["video_url"] = video_url
                print(f"  ✓ Lección {i+1}: '{lesson.get('title', 'Sin título')}' -> Video agregado: {video_url}")
            else:
                print(f"  ⚠ Lección {i+1}: '{lesson.get('title', 'Sin título')}' -> Ya tiene video: {current_url}")

            updated_lessons.append(lesson)

        # Actualizar el curso en la base de datos
        result = await courses_collection.update_one(
            {"_id": course_id},
            {"$set": {"lessons": updated_lessons}}
        )

        if result.modified_count > 0:
            print(f"  ✅ Curso actualizado exitosamente")
        else:
            print(f"  ℹ️  Curso no requería actualizaciones")

    print("\n✅ Proceso completado!")
    client.close()


if __name__ == "__main__":
    print("=" * 60)
    print("ACTUALIZACIÓN DE VIDEOS EN LECCIONES")
    print("=" * 60)
    asyncio.run(update_lessons_with_videos())
