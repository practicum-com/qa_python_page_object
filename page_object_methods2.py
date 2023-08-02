from selenium.webdriver.common.by import By


class RegistrationPageAround:
    # El localizador del campo Correo electrónico
    email_field = ...
    # El localizador del campo Contraseña
    password_field = ...
    # El localizador del botón Registrarse
    registration_button = ...

    # El constructor de clase
    def __init__(self, driver):
        ...

    # El método rellena el campo Correo electrónico
    def set_email(self, email):
        ...

    # El método rellena el campo Contraseña
    def set_password(self, password):
        ...

    # El método hace clic en el botón Registrarse
    def click_registration_button(self):
        ...

    # El método de registro: combina el correo electrónico, la contraseña y el clic
    def register(self, ...):
        ...
