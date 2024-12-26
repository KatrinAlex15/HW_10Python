import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManage
from shop_page import ShopPage

#@pytest.fixture
@allure.title("Тест на проверку Онлайн-магазина")
@allure.feature("Shop")
@allure.description("Проверка работы онлайн-магазина на авторизацию, добавление товара в корзину, оформление заказа и итоговую стоимость заказа")
@allure.severity("critical")


def test_03_shop(driver):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Открыть сайт онлайн-магазина"):
        shop_page = ShopPage(driver)
    with allure.step("Авторизоваться на сайте"):
        shop_page.fill_form("standard_user", "secret_sauce")
    with allure.step("Добавить товары в корзину"):
        shop_page.add_products()
    with allure.step("Перейти в корзину"):
        shop_page.shopping_cart()
    with allure.step("Нажать кнопку checkout"):
        shop_page.checkout()
    with allure.step("Заполнить данными страницу оформления заказа"):
        shop_page.your_information("Kate","Alekseeva","123456")
    with allure.step("Получить итоговую стоимость"):
        total_value = shop_page.total()
    with allure.step("Проверить итоговую стоимость"):
        assert total_value == "Total: $58.29"

    """Закрытие браузера"""
    driver.quit()
