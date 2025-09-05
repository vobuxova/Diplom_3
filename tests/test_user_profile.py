import allure
from ..pages.main_page import MainPage
from ..pages.login_page import LoginPage
from ..pages.profile_page import ProfilePage
from ..urls import Urls
from ..data import get_existing_user
from ..locators import LoginPageLocators

@allure.feature("Личный кабинет")
class TestUserProfile:
    
    @allure.title("Переход в личный кабинет неавторизованным пользователем")
    def test_go_to_profile(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        assert Urls.LOGIN_URL == driver.current_url

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        login_page.login(email, password)
        main_page.go_to_personal_account()
        profile_page.go_to_order_history()
        assert Urls.ORDER_HISTORY == driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        login_page.login(email, password)
        main_page.go_to_personal_account()
        profile_page.logout()
        login_page.wait_for_element(LoginPageLocators.ENTER_BUTTON)
        assert Urls.LOGIN_URL == driver.current_url
        
        