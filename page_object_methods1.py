from selenium.webdriver.common.by import By


class HomePageAround:
    # The Add button locator1
    add_new_place_button = (By.CLASS_NAME, 'profile__add-button')
    # The Name field locator
    name_field = (By.NAME, 'name')
    # The Link-to-the-image field locator
    link_to_picture_field = (By.NAME, 'link')
    # The Save button locator
    save_button = (By.XPATH, ".//form[@name='new-card']/button[text()='Save']")

    def __init__(self, driver):
        self.driver = driver

    # The method clicks on the Add button
    def click_add_new_place_button(self):
        self.driver.find_element(*self.add_new_place_button).click()

    # The method enters the name of the new place
    def set_name(self):
        new_title = "Новое место"
        self.driver.find_element(*self.name_field).send_keys(new_title)

    # The method enters a link to the image
    def set_link_to_picture_field(self):
        self.driver.find_element(*self.link_to_picture_field).send_keys("Link to the image")

    # The method clicks on the Save button
    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()

    # The step to add a new place
