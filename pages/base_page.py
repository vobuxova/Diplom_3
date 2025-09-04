from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        
    @allure.step("Нахождение объекта")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидание кликабельности элемента")
    def wait_for_click_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ввод текста в поле")
    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Получение значения атрибута элемента")
    def get_element_attribute(self, locator, attribute):
        element = self.wait_for_element(locator)
        return element.get_attribute(attribute)