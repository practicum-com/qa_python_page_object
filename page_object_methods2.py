from selenium.webdriver.common.by import By


class RegistrationPageAround:
    # The Email field locator
    email_field = ...
    # The Password field locator
    password_field = ...
    # The Sign-up button locator
    registration_button = ...

    # The class constructor
    def __init__(self, driver):
        ...

    # The method fills in the Email field
    def set_email(self, email):
        ...

    # The method fills in the Password field
    def set_password(self, password):
        ...

    # The method clicks on the Sign-up button
    def click_registration_button(self):
        ...

    # The sign-up method — it combines the email, the password, and the click
    def register(self, ...):
        ...
