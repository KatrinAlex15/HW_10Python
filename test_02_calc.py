import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


#@pytest.fixture
@allure.title("Тест на проверку работы калькулятора")
@allure.feature("Calculator")
@allure.description("Проверка корректной работы калькулятора, сравнение полученного результата с действительным значением")
@allure.severity("critical")


def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_02_calculator():
    with allure.step("открыть страницу калькулятора"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    """Создание объекта страницы калькулятора"""
    calculator_page = CalculatorPage(driver)
    with allure.step("Установить задержку в поле 45 секунд"):
        calculator_page.set_delay("45")
    with allure.step("Ввести 7 + 8 ="):
        calculator_page.click_button()
    
    """Проверка полученного результата"""
    result = calculator_page.return_result("15")
    assert result == "15"



"""Закрытие браузера"""

driver.quit()