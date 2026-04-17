from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass

class DysonV12SPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    dyson_v12s_page_name = "//h1[@class='produt-section__title cart-modal-title']"
    dyson_v12s_price = "(//span[@class='total-prod-price'])[1]"
    add_to_cart_button = "//a[@class='prod-info-price__cart-btn button cart-modal-open']"
    go_to_cart_button = "//a[@class='button button--medium cart-modal__cart-link']"

    # Getters
    def get_dyson_v12s_page_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.dyson_v12s_page_name)))
    def get_dyson_v12s_price(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.dyson_v12s_price)))
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))
    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

    # Actions
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Клик по кнопке В корзину')
    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print('Клик по кнопке Перейти к корзине')

    # Methods
    def initial_check(self):
        self.get_current_url()
        self.assert_text(self.get_dyson_v12s_page_name(), 'Беспроводной вертикальный пылесос Dyson V12S Detect Slim Submarine Complete (SV46) (Gold/Gold) (2022)\nПылесос золотого цвета')
    def check_price(self):
        pp_price_str = self.get_dyson_v12s_price().text
        pp_price_num = self.convert_price_to_number(pp_price_str)
        self.assert_price(pp_price_num, 47990)
    def product_add_and_go_to_cart(self):
        self.click_add_to_cart_button()
        self.click_go_to_cart_button()