from selenium.webdriver.common.by import By


class LoginPageAround:
    # The Email field locator
    email_field = (By.ID, 'email')
    # The Password field locator
    password_field = (By.ID, 'password')
    # The Login button locator
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')
    # Add a locator for the Sign-up button here
    ...

    # The class constructor
    def __init__(self, driver):
        self.driver = driver

    # The method checks if the Login button is clickable
    def check_sign_in_is_enabled(self):
        return self.driver.find_element(*self.sign_in_button).is_enabled()

    # The method clicks on the Login button
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    # The method clicks on the Sign-up button
    def click_registration_button(self):
        ...

    # The method validates the text on the Sign-up button
    def check_text_registration_button(self):
        registration_button_text = ...
        assert ...
