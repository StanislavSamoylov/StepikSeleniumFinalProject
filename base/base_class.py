import datetime
from selenium.webdriver import ActionChains


class BaseClass():
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод для получения CURRENT URL"""
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')

    def move_to_element(self, element):
        """Метод перехода к элементу на странице"""
        ActionChains(self.driver).move_to_element(element).perform()

    def assert_text(self, parsed_text, expected_result):
        """Метод для проверки значения текста"""
        value_parsed_text = parsed_text.text
        assert value_parsed_text == expected_result, f'ОШИБКА, Полученный текст {value_parsed_text} не соответствует ожидаемому тексту {expected_result}'
        print(f'Полученный текст {value_parsed_text} соответствует ожидаемому')

    def assert_url(self, expected_result):
        """Метод для проверки значения URL"""
        get_url = self.driver.current_url
        assert get_url == expected_result, f'ОШИБКА, Полученный URL {get_url} не соответствует ожидаемому URL {expected_result}'
        print(f'Полученный URL {get_url} соответствует ожидаемому')

    def convert_price_to_number(self, price_str):
        """Метод для перевода цены в формат числа"""
        return int(price_str.strip('₽').replace(' ', ''))

    def assert_price(self, price, expected_result):
        """Метод для проверки значения текста"""
        assert price == expected_result, f'ОШИБКА, Полученная цена {price} не соответствует ожидаемой {expected_result}'
        print(f'Полученная цена {price} соответствует ожидаемой')

    def take_screenshot(self):
        """Метод для создания скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f'{now_date}.png'
        self.driver.save_screenshot(f'./screen/{name_screenshot}')
        print(f'Скриншот сохранен как: {name_screenshot}')
