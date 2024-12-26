import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


""""Этот класс представляет страницу калькулятора"""

class CalculatorPage:
     @allure.step("Открыть страницу калькулятора в браузере")
     def __init__(self, driver: str):
         self.driver = driver
         self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

     @allure.step("Установить задержку по времени")
     def set_delay(self, delay: int):
         delay_input = self.driver.find_element(By.ID, "delay")
         delay_input.clear()
         delay_input.send_keys(delay)

     @allure.step("Нажать кнопки на калькуляторе")
     def click_button(self):
         self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

     @allure.step("Получить результат операции с ожиданием")
     def return_result(self, EC_result) -> int:
         wait = WebDriverWait(self.driver, 50)
         result = wait.until(
             EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), EC_result)
         )
         result = self.driver.find_element(By.CSS_SELECTOR, '.screen')
         return result.text