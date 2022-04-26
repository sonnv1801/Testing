from selenium import webdriver
import time
import unittest
import sys
import os
from POM.ProjectPOM.Pages.todolist import Todolist

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class AddToDoList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/ST19A1A/KiemThuPhanMem/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_add_task(self):
        driver = self.driver
        driver.get("http://localhost:5000/todolist")
        todolist = Todolist(driver)
        todolist.click_btn_add()
        todolist.enter_title("Kiểm Thử Phần Mềm")
        todolist.enter_date("04-10-2022")
        todolist.enter_deadline("04-29-2022")
        todolist.enter_status('Hoàn Thành')
        todolist.enter_progress("100%")
        todolist.enter_size("Lớn")
        todolist.click_add_task()
        time.sleep(2)
        print("-------------------------------")
        print("Đã Thêm Thành Công 1 Công Việc!")
        print("-------------------------------")

    def test_cancel_task(self):
        driver = self.driver
        driver.get("http://localhost:5000/todolist")
        todolist = Todolist(driver)
        todolist.click_btn_add()
        todolist.enter_title("Nodejs10")
        todolist.enter_date("10-10-2022")
        todolist.enter_status('Sắp Hoàn Thành')
        todolist.enter_progress("90%")
        todolist.enter_size("Lớn")
        todolist.click_cancel_task()
        time.sleep(2)
        print("---------------------------------")
        print("Đã Hủy Thêm Công Việc Thành Công!")
        print("---------------------------------")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("----------------------")
        print('Hoàn Thành Bài Test')
        print("----------------------")


if __name__ == '__main__':
    unittest.main()
