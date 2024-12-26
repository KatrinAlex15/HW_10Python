import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage

@allure.title("Тест на проверку заполнения формы")
@allure.feature("FORM")
@allure.description("Проверка заполнения всех полей формы, если не заполнены- подсвечивает красным")
@allure.severity("critical")

def test_form_submission():
    with allure.step("Открыть страницу форму по ссылке"):
        driver = webdriver.chrome(service=ChromeService(ChromeDriverManager().install))
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    """Создание обьекта страницы формы"""

    form_page = FormPage(driver)
    with allure.step("Ввести данные в поля, поле zip оставить пустым"):
        parameters = {("first-name","Иван"),
                      ("last-name","Петров"),
                      ("address","Ленина, 55-3"),
                      ("e-mail","test@skypro.com"),
                      ("phone","+7985899998787"),
                      ("city","Москва"),
                      ("country","Россия"),
                      ("job-position","QA"),
                      ("company","SkyPro")
        }


"""Заполнение формы"""
form_page.fill_parameters(parameter, value)
with allure.step("Нажать на кнопку отправки формы Submit"):
    form_page.submit_form()


"""Подсветка поля Zip-code и других полей"""
with allure.step("Проверка подсветки поля Zipcode и остальных полей"):
    form_page.submit_form()
    alert_success_color = "rgba(209, 231, 221, 1)"
    alert_danger_color = "rgba(248, 215, 218, 1)"
    assert page.return_result("first-name")== alert_success_color
    assert page.return_result("last-name") == alert_success_color
    assert page.return_result("address") == alert_success_color
    assert page.return_result("e-mail") == alert_success_color
    assert page.return_result("phone") == alert_success_color
    assert page.return_result("city") == alert_success_color
    assert page.return_result("country") == alert_success_color
    assert page.return_result("job-position") == alert_success_color
    assert page.return_result("company") == alert_success_color
    assert page.return_result("zip-code") == alert_danger_color

"""Закрытие браузера"""




#@pytest.fixture

