import allure
from .base_page import BasePage
from ..locators import MainPageLocators

class ProfilePage(BasePage):
    
    @allure.step("Переход в историю заказов")
    def go_to_order_history(self):
        self.click_element(MainPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click_element(MainPageLocators.LOGOUT_BUTTON)