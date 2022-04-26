from selenium import webdriver
import time
import unittest

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from POM.ProjectPOM.Pages.loginPage import LoginPage
from POM.ProjectPOM.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/ST19A1A/KiemThuPhanMem/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_invalid_password(self):
        driver = self.driver

        driver.get("http://my.uda.edu.vn/sv/svlogin")
        login = LoginPage(driver)
        login.enter_username("47788")
        login.enter_password("LaBanKey@18011")
        login.click_login()

        print("----------------------------------")
        print("Mật Khẩu Sai!")
        print("----------------------------------")

        message = login.invali_password()
        self.assertEqual(message, "Kiểm tra lại tên hay password!")
        print("----------------------------------")
        print("Đã Phát Hiện Ra Nhập Sai Mật Khẩu")
        print("----------------------------------")

        time.sleep(2)

    def test_login_edit_profile(self):
        driver = self.driver

        driver.get("http://my.uda.edu.vn/sv/svlogin")
        login = LoginPage(driver)
        login.enter_username("47788")
        login.enter_password("LaBanKey@1801")
        login.click_login()
        print("----------------------------------")
        print("Đã Đăng Nhập Vào UDA Thành Công!")
        print("----------------------------------")

        homepage = HomePage(driver)
        # homepage.click_hethong()
        homepage.click_image()

        print("----------------------------------")
        print("Đã Vào Profile!")
        print("----------------------------------")

        homepage.click_edit_profile()

        print("----------------------------------")
        print("Đã Vào Edit Profile!")
        print("----------------------------------")

        homepage.enter_sdt_ba("0385130966")
        homepage.enter_sdt_me("0364527407")

        print("----------------------------------")
        print("Đã Edit Thành Công!")
        print("----------------------------------")

        homepage.click_save_profile()

        print("----------------------------------")
        print("Đã Lưu Thành Công!")
        print("----------------------------------")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Hoàn Thành Kiểm Tra!')


if __name__ == '__main__':
    unittest.main()

# python -m POM.ProjectPOM.Tests.login
