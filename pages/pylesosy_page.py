from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass

class PylesosyPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.execute_script("document.getElementById('cookies-container').remove();")

    # Locators
    pylesosy_page_name = "//h1[@class='catalog-section__title']"
    price_from_field = "//input[@name='pfrom']"
    price_to_field = "//input[@name='pto']"
    brand_dyson_check_box = "(//span[contains(text(), 'Dyson')])[1]"
    available_to_order_check_box = "//label[@class='i-radio__label']"
    dyson_v12s = "//a[contains(text(), 'Dyson V12S Detect Slim Submarine Complete')]"

    # Getters
    def get_pylesosy_page_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.pylesosy_page_name)))
    def get_price_from_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_from_field)))
    def get_price_to_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_to_field)))
    def get_brand_dyson_check_box(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_dyson_check_box)))
    def get_available_to_order_check_box(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.available_to_order_check_box)))
    def get_product_button(self, product_xpath):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, product_xpath)))

    # Actions
    def input_price_from(self, amount):
        self.get_price_from_field().send_keys(amount)
        print(f'Поле Цена от заполнена значением {amount}')
    def input_price_to(self, amount):
        self.get_price_to_field().send_keys(amount)
        print(f'Поле Цена от заполнена значением {amount}')
    def select_brand_dyson(self):
        self.get_brand_dyson_check_box().click()
        print('Клик по чек-боксу Dyson')
    def select_available_to_order(self):
        self.move_to_element(self.get_available_to_order_check_box())
        self.get_available_to_order_check_box().click()
        print('Клик по чек-боксу Доступные к заказу')
    def click_product_button(self, product):
        self.move_to_element(self.get_product_button(product))
        self.get_product_button(product).click()
        print('Клик по кнопке товара')

    # Methods
    def initial_check(self):
        self.get_current_url()
        self.assert_text(self.get_pylesosy_page_name(), 'Пылесосы')
    def add_filters_for_smoke_test(self):
        self.input_price_from(500)
        self.input_price_to(50000)
        self.select_brand_dyson()
        self.select_available_to_order()
    def go_to_product(self, product):
        self.click_product_button(product)