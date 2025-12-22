"""
Estado para la gestión del formulario de contacto.

Este módulo maneja el estado del formulario de contacto que permite a los
usuarios enviar mensajes a la plataforma. Incluye validación de campos,
envío a la base de datos y gestión de estados de éxito/error.

Funcionalidades principales:
- Capturar nombre, email y mensaje del usuario
- Validar campos del formulario
- Enviar mensaje a la base de datos
- Mostrar mensajes de éxito o error
- Resetear formulario después del envío exitoso
"""

import reflex as rx
from E_Learning_JCB_Reflex.services import contact_service


class ContactState(rx.State):
    """
    Estado para el formulario de contacto.

    Maneja la captura, validación y envío de mensajes de contacto
    desde el formulario público de la plataforma.

    Atributos de estado:
        # Campos del formulario
        name (str): Nombre de la persona que envía el mensaje
        email (str): Email de contacto
        message (str): Contenido del mensaje

        # Estados de UI
        loading (bool): Indicador de envío en progreso
        error (str): Mensaje de error de validación o envío
        success (bool): Indica si el envío fue exitoso

    Validaciones implementadas:
        - Todos los campos son obligatorios
        - Email debe contener "@" y "."
        - Mensaje debe tener al menos 10 caracteres
    """

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
        """
        Enviar el formulario de contacto a la base de datos.

        Valida todos los campos del formulario y, si son válidos, guarda
        el mensaje en la colección "contacts" de MongoDB. Si el envío es
        exitoso, resetea el formulario automáticamente.

        Validaciones realizadas:
            1. Campos obligatorios: name, email, message deben estar completos
            2. Email válido: debe contener "@" y "."
            3. Mensaje mínimo: debe tener al menos 10 caracteres

        Actualiza el estado:
            - loading: True durante el envío
            - error: Mensaje de error si falla la validación o el envío
            - success: True si se envió exitosamente
            - Campos del formulario: Se resetean a "" si es exitoso

        Returns:
            None: Los mensajes de error se establecen en self.error

        Ejemplo de flujo:
            1. Usuario completa formulario
            2. Click en "Enviar"
            3. submit_contact() valida campos
            4. Si es válido, llama a contact_service.create_contact()
            5. Si es exitoso, muestra success=True y limpia formulario
        """
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
