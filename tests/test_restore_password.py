import allure
from ..data import get_user_data
from ..pages.login_page import LoginPage
from ..pages.restore_password_page import RestorePasswordPage
from ..locators import RestorePageLocators
from ..urls import Urls

@allure.feature("Восстановление пароля")
class TestPasswordRestore:
      
    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_recover_password(self, driver):
        login_page = LoginPage(driver)
        driver.get(Urls.LOGIN_URL)
        login_page.go_to_restore_password()
        assert Urls.RECOVER_PASSWORD in driver.current_url

    @allure.title("Ввод email и клик по кнопке 'Восстановить'")
    def test_recover_password(self, driver):
        email, _ = get_user_data()
        restore_page = RestorePasswordPage(driver)
        driver.get(Urls.RECOVER_PASSWORD)
        restore_page.enter_email(email)
        restore_page.click_recover()
        restore_page.wait_for_click_element(RestorePageLocators.NEW_PASSWORD_FIELD)
        assert "reset-password" in driver.current_url

    @allure.title("Проверка активации поля пароля")
    def test_show_hide_password(self, driver):
        email, password = get_user_data()
        restore_page = RestorePasswordPage(driver)
        driver.get(Urls.RECOVER_PASSWORD)
        restore_page.enter_email(email)
        restore_page.click_recover()
        restore_page.wait_for_click_element(RestorePageLocators.NEW_PASSWORD_FIELD)
        restore_page.input_text(RestorePageLocators.NEW_PASSWORD_FIELD, password)
        restore_page.click_show_hide_password()
        element = restore_page.wait_for_element(RestorePageLocators.NEW_PASSWORD_FIELD)
        element_border = driver.find_element(*RestorePageLocators.NEW_PASSWORD)
        assert element.get_attribute("value") == password
        assert element_border.value_of_css_property("border") != "2px solid rgb(47, 47, 55)"
        assert "input_status_active" in element_border.get_attribute("class").split()