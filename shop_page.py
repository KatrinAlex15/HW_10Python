import allure
from selenium.webdriver.common.by import By

"""Этот класс описывает страницу онлайн-магазина"""

class ShopPage:
    @allure.step("Открыть страницу онлайн-магазина")
    def __init__(self, driver: str):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизоваться на сайте")
    def fill_form(self, user_name: str, password: str):
        self.driver.find_element(By.NAME, "user-name").send_keys(user_name)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавить товары в корзину")
    def add_products(self):
        self.driver.find_element(By.ID, "add-to-card-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-card-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-card-sauce-labs-onesie").click()

    @allure.step("Перейти в корзину")
    def shopping_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step("Нажать на кнопку checkout")
    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step("Заполнить форму данными, нажать на кнопку continue")
    def your_information(self, first_name: str, last_name: str, postal_code: int):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую стоимость")
    def total(self) -> int:
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text
