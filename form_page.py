import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Этот класс описывает страницу заполнения формы"""

class FormPage:
    @allure.step("Настройка драйвера")
    def __init__(self, driver: str):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнение полей формы")
    def fill_parameters(self, parameter, value: {}):
        self.driver.find_element(By.NAME, parameter).send_keys(value)

    @allure.step("Нажать на кнопку отправки формы")
    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    
    @allure.step("Получить результат подсветки поля Zip-code и других полей")
    def return_result(self, field_name: {}): 
        return self.driver.find_element(By.CSS_SELECTOR, f"[id='{field_name}']").value_of_css_property("background-color")
