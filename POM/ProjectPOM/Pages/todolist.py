from selenium.webdriver.common.by import By
from POM.ProjectPOM.Locators.location import Locators


class Todolist():

    def __init__(self, driver):
        self.driver = driver

        self.btn_add_id = Locators.btn_add_id
        self.title_textbox_id = Locators.title_textbox_id
        self.date_textbox_id = Locators.date_textbox_id
        self.deadline_textbox_id = Locators.deadline_textbox_id
        self.status_textbox_id = Locators.status_textbox_id
        self.progress_textbox_id = Locators.progress_textbox_id
        self.size_textbox_id = Locators.size_textbox_id
        self.add_task = Locators.add_task
        self.cancel_task = Locators.cancel_task

    def click_btn_add(self):
        self.driver.find_element(By.ID, self.btn_add_id).click()

    def enter_title(self, title):
        self.driver.find_element(By.ID, self.title_textbox_id).clear()
        self.driver.find_element(By.ID, self.title_textbox_id).send_keys(title)

    def enter_date(self, date):
        self.driver.find_element(By.ID, self.date_textbox_id).clear()
        self.driver.find_element(By.ID, self.date_textbox_id).send_keys(date)

    def enter_deadline(self, date):
        self.driver.find_element(By.ID, self.deadline_textbox_id).clear()
        self.driver.find_element(By.ID, self.deadline_textbox_id).send_keys(date)

    def enter_status(self, status):
        self.driver.find_element(By.ID, self.status_textbox_id).clear()
        self.driver.find_element(By.ID, self.status_textbox_id).send_keys(status)

    def enter_progress(self, progress):
        self.driver.find_element(By.ID, self.progress_textbox_id).clear()
        self.driver.find_element(By.ID, self.progress_textbox_id).send_keys(progress)

    def enter_size(self, size):
        self.driver.find_element(By.ID, self.size_textbox_id).clear()
        self.driver.find_element(By.ID, self.size_textbox_id).send_keys(size)

    def click_add_task(self):
        self.driver.find_element(By.ID, self.add_task).click()

    def click_cancel_task(self):
        self.driver.find_element(By.ID, self.cancel_task).click()



