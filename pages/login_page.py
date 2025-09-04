import allure
from .base_page import BasePage
from ..locators import LoginPageLocators, RestorePageLocators

class LoginPage(BasePage):

    @allure.step("Ввод учетных данных")
    def login(self, email, password):
        self.input_text(LoginPageLocators.LOGIN_EMAIL_FIELD, email)
        self.input_text(LoginPageLocators.LOGIN_PASSWORD_FIELD, password)
        self.click_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_restore_password(self):
        self.click_element(RestorePageLocators.PASSWORD_RESTORE_LINK)