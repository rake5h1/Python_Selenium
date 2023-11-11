from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.user_input_locator =(By.NAME,'username')
        self.password_locator=(By.NAME,'password')
        self.button_locator=(By.CLASS_NAME,'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button')
    def enter_details(self):
        user_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.user_input_locator)
        )
        user_input.send_keys('admin')
        # self.driver.find_element(By.CLASS_NAME,'oxd-input oxd-input--active').send_keys('admin')
        sleep(10)
        password_input=WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_locator)
        )
        password_input.send_keys('admin123')
        sleep(10)

    # def click_login(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(self.button_locator)
    #     ).click()
    #     sleep(10)
