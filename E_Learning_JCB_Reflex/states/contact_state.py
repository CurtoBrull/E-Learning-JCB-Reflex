"""Estado para la gestión del formulario de contacto."""

import reflex as rx
from E_Learning_JCB_Reflex.services import contact_service


class ContactState(rx.State):
    """Estado del formulario de contacto."""

    # Campos del formulario
    name: str = ""
    email: str = ""
    message: str = ""

    # Estados de la UI
    loading: bool = False
    error: str = ""
    success: bool = False

    def set_name(self, value: str):
        """Actualizar el nombre."""
        self.name = value

    def set_email(self, value: str):
        """Actualizar el email."""
        self.email = value

    def set_message(self, value: str):
        """Actualizar el mensaje."""
        self.message = value

    def reset_form(self):
        """Resetear el formulario."""
        self.name = ""
        self.email = ""
        self.message = ""
        self.error = ""
        self.success = False

    async def submit_contact(self):
        """Enviar el formulario de contacto."""
        # Validación
        if not self.name or not self.email or not self.message:
            self.error = "Todos los campos son obligatorios"
            return

        # Validación básica de email
        if "@" not in self.email or "." not in self.email:
            self.error = "Por favor, introduce un email válido"
            return

        if len(self.message) < 10:
            self.error = "El mensaje debe tener al menos 10 caracteres"
            return

        # Resetear estados
        self.loading = True
        self.error = ""
        self.success = False

        try:
            # Enviar a la base de datos
            result = await contact_service.create_contact(
                name=self.name,
                email=self.email,
                message=self.message
            )

            if result:
                self.success = True
                # Resetear el formulario después del éxito
                self.name = ""
                self.email = ""
                self.message = ""
            else:
                self.error = "Error al enviar el mensaje. Por favor, inténtalo de nuevo."

        except Exception as e:
            print(f"Error submitting contact: {e}")
            self.error = "Error al enviar el mensaje. Por favor, inténtalo de nuevo."

        finally:
            self.loading = False
