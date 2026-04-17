from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass

class MainPage(BaseClass):

    base_url = 'https://biggeek.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    # Locators
    cookies_button = "//button[@id='cookies-button']"
    dlya_doma_button = "(//a[@class='static-header-bottom__link'])[7]"

    # Getters
    def get_cookies_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cookies_button)))
    def get_dlya_doma_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dlya_doma_button)))

    # Actions
    def click_cookies_button(self):
        self.get_cookies_button().click()
        print('Клик по кнопке Сайт использует cookies -> Понятно')
    def click_dlya_doma_button(self):
        self.get_dlya_doma_button().click()
        print('Клик по кнопке Для дома')

    # Methods
    def initial_check(self):
        self.get_current_url()
    def accept_cookies(self):
        self.click_cookies_button()
    def go_to_dlya_doma_section(self):
        self.click_dlya_doma_button()