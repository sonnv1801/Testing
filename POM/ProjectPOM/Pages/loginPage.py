from selenium.webdriver.common.by import By

from POM.ProjectPOM.Locators.location import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.invali = Locators.invali

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

    def invali_password(self):
        msg = self.driver.find_element(By.XPATH, self.invali).text
        return msg



