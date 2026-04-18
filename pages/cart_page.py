from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass

class CartPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    cart_page_name = "//h1[@class='cart-order__title title']"
    product_name = "//h2[@class='product-cart__title']"
    product_price = "//p[@class='order-purchases-bottom__count']"

    # Getters
    def get_cart_page_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.cart_page_name)))
    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.product_name)))
    def get_products_price(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.product_price)))

    # Actions

    # Methods
    def initial_check(self):
        self.get_current_url()
        self.assert_text(self.get_cart_page_name(), 'Корзина')
    def check_product_name(self):
        self.assert_text(self.get_product_name(),'Беспроводной вертикальный пылесос Dyson V12S Detect Slim Submarine Complete (SV46) (Gold/Gold) (2022)\nМалайзия/Сингапур\nКрупногабаритный товар')
    def check_price(self):
        cp_price_str = self.get_products_price().text.split('\n')[1]
        cp_price_num = self.convert_price_to_number(cp_price_str) # попробовать по индексу передать нужную часть внутрь функции или сделать более универсальной базовую
        self.assert_price(cp_price_num, 47990)
    def final_step(self):
        self.take_screenshot()
