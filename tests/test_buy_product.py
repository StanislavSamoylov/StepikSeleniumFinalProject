from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.main_page import MainPage
from pages.dlya_doma_page import DlyaDomaPage
from pages.pylesosy_page import PylesosyPage
from pages.dyson_v12s_page import DysonV12SPage
from pages.cart_page import CartPage

def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    # или options.add_argument("--incognito")
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Начало тестового сценария')

    main_page = MainPage(driver)
    main_page.initial_check()
    main_page.accept_cookies()
    main_page.go_to_dlya_doma_section()

    dlya_doma_page = DlyaDomaPage(driver)
    dlya_doma_page.initial_check()
    dlya_doma_page.go_to_pylesosy_section()

    pylesosy_page = PylesosyPage(driver)
    pylesosy_page.initial_check()
    pylesosy_page.add_filters_for_smoke_test()
    pylesosy_page.go_to_product(pylesosy_page.dyson_v12s)

    dyson_v12s_page = DysonV12SPage(driver)
    dyson_v12s_page.initial_check()
    dyson_v12s_page.check_price()
    dyson_v12s_page.product_add_and_go_to_cart()

    cart_page = CartPage(driver)
    cart_page.initial_check()
    cart_page.check_product_name()
    cart_page.check_price()
    cart_page.final_step()

    """Закрытие браузера"""
    time.sleep(5)
    driver.close()
    print(f'Позитивный тест для товара завершен. Браузер закрыт')