from selenium.webdriver.common.by import By


class LoginPageAround:
    # El localizador del campo Correo electrónico
    email_field = (By.ID, 'email')
    # El localizador del campo Contraseña
    password_field = (By.ID, 'password')
    # El localizador del botón Iniciar sesión
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')
    # Agrega aquí un localizador para el botón Registrarse
    ...

    # El constructor de clase
    def __init__(self, driver):
        self.driver = driver

    # El método comprueba si se puede hacer clic en el botón Iniciar sesión
    def check_sign_in_is_enabled(self):
        return self.driver.find_element(*self.sign_in_button).is_enabled()

    # El método hace clic en el botón Iniciar sesión
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    # El método hace clic en el botón Registrarse
    def click_registration_button(self):
        ...

    # El método valida el texto en el botón Registrarse
    def check_text_registration_button(self):
        registration_button_text = ...
        assert ...
