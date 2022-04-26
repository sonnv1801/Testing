from selenium.webdriver.common.by import By

from POM.ProjectPOM.Locators.location import Locators

class HomePage():
    def __init__(self, driver):
        self.driver = driver

        # self.thongbao_hocphi = Locators.thongbao_hocphi
        self.img_id = Locators.image
        self.edit_id = Locators.edit
        self.edit_sdt_ba_id = Locators.edit_sdt_ba
        self.edit_sdt_me_id = Locators.edit_sdt_me
        self.save_profile_id = Locators.save_profile
        # self.hethong_button_id = Locators.hethong
        # self.logout_button_id = Locators.logout

    # def click_hocphi(self):
    #     self.driver.find_element(By.ID, self.thongbao_hocphi).click()

    def click_image(self):
        self.driver.find_element(By.ID, self.img_id).click()

    def click_edit_profile(self):
        self.driver.find_element(By.ID, self.edit_id).click()


    def enter_sdt_ba(self, sdt_ba):
        self.driver.find_element(By.ID, self.edit_sdt_ba_id).clear()
        self.driver.find_element(By.ID, self.edit_sdt_ba_id).send_keys(sdt_ba)

    def enter_sdt_me(self, sdt_me):
        self.driver.find_element(By.ID, self.edit_sdt_me_id).clear()
        self.driver.find_element(By.ID, self.edit_sdt_me_id).send_keys(sdt_me)

    def click_save_profile(self):
        self.driver.find_element(By.ID, self.save_profile_id).click()


    # def click_hethong(self):
    #     self.driver.find_element(By.LINK_TEXT, self.hethong_button_id).click()
    #
    # def click_logout(self):
    #     self.driver.find_element(By.LINK_TEXT, self.logout_button_id).click()

