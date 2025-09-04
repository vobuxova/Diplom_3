import allure
from ..pages.main_page import MainPage
from ..pages.login_page import LoginPage
from ..urls import Urls
from ..data import get_existing_user
from ..locators import MainPageLocators

@allure.feature("Основной функционал")
class TestMainFunctionality:
    
    @allure.title("Переход в конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.ORDER_FEED)
        main_page.go_to_constructor()
        assert Urls.BASE_URL + "/" == driver.current_url

    @allure.title("Переход в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_order_feed()
        assert Urls.ORDER_FEED in driver.current_url

    @allure.title("Открытие деталей ингредиента")
    def test_ingredient_details(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.click_ingredient()
        assert main_page.is_modal_open(MainPageLocators.MODAL_INGREDIENT_DETAILS)

    @allure.title("Закрытие модального окна деталей")
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.click_ingredient()
        main_page.close_modal(MainPageLocators.MODAL_CLOSE_BUTTON)
        assert main_page.is_modal_closed(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.title("Увеличение счетчика ингредиента при перетаскивании")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        initial_counter = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order() 
        assert main_page.get_ingredient_counter() > initial_counter, f"Счетчик не увеличился: было {initial_counter}, стало {main_page.get_ingredient_counter()}"

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_place_order(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        login_page.login(email, password)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        assert main_page.is_modal_open(MainPageLocators.ORDER_MODAL_WINDOW)