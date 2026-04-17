from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseClass

class DlyaDomaPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    dlya_doma_page_name = "//h1[@class='catalog-section__title']"
    pylesosy_button = "//a[@class='catalog-filter-links__item '][1]"

    # Getters
    def get_dlya_doma_page_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.dlya_doma_page_name)))
    def get_pylesosy_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pylesosy_button)))

    # Actions
    def click_pylesosy_button(self):
        self.get_pylesosy_button().click()
        print('Клик по кнопке Пылесосы')

    # Methods
    def initial_check(self):
        self.get_current_url()
        self.assert_text(self.get_dlya_doma_page_name(), 'Для дома')
    def go_to_pylesosy_section(self):
        self.click_pylesosy_button()