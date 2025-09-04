import allure
from .base_page import BasePage
from ..locators import MainPageLocators

class OrderFeedPage(BasePage):

    @allure.step("Клик по заказу")
    def click_order(self):
        self.click_element(MainPageLocators.ORDER_ITEM)

    @allure.step("Получение значения счетчика 'Выполнено за всё время'")
    def get_total_completed(self):
        return int(self.get_element_text(MainPageLocators.TOTAL_COMPLETED))
    
    @allure.step("Проверка открытия модального окна с деталями")
    def is_modal_open(self, locator):
        return self.wait_for_element(locator).is_displayed()

    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_completed(self):
        return int(self.get_element_text(MainPageLocators.TODAY_COMPLETED))

    @allure.step("Получение номера заказа в разделе 'В работе'")
    def get_in_progress_order_number(self, locator):
        return self.get_element_text(locator)