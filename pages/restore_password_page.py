import allure
from .base_page import BasePage
from ..locators import RestorePageLocators

class RestorePasswordPage(BasePage):

    @allure.step("Ввод email для восстановления")
    def enter_email(self, email):
        self.input_text(RestorePageLocators.EMAIL_FIELD, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_recover(self):
        self.click_element(RestorePageLocators.RESTORE_BUTTON)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_hide_password(self):
        self.click_element(RestorePageLocators.VISIBILITY_PASSWORD_BUTTON)
