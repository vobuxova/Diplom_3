from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure
from .base_page import BasePage
from ..locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Переход в личный кабинет")
    def go_to_personal_account(self):
        self.click_element(MainPageLocators.ACCOUNT_LINK)

    @allure.step("Переход в ленту заказов")
    def go_to_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Переход в конструктор")
    def go_to_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_ITEM)

    @allure.step("Проверка открытия модального окна с деталями")
    def is_modal_open(self, locator):
        return self.wait_for_element(locator).is_displayed()

    @allure.step("Закрытие модального окна")
    def close_modal(self, locator):
        self.click_element(locator)

    @allure.step("Проверка закрытия модального окна")
    def is_modal_closed(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетаскивание ингредиента в конструктор")
    def drag_ingredient_to_burger(self):
        
        source = self.wait_for_element(MainPageLocators.INGREDIENT_ITEM)
        target = self.wait_for_element(MainPageLocators.BURGER_CONSTRUCTOR_AREA)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        
    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.drag_ingredient_to_burger()

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self):
        count = self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)
        return int(count)

    @allure.step("Оформление заказа")
    def place_order(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)