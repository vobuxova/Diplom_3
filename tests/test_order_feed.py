import allure
from ..pages.main_page import MainPage
from ..pages.login_page import LoginPage
from ..pages.order_page import OrderFeedPage
from ..pages.profile_page import ProfilePage
from ..urls import Urls
from ..data import get_existing_user
from ..locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Открытие деталей заказа")
    def test_order_details(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        login_page.login(email, password)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        driver.get(Urls.ORDER_FEED)
        order_feed_page.click_order()
        assert order_feed_page.is_modal_open(MainPageLocators.ORDER_WINDOW)

    @allure.title("Заказы из истории отображаются в ленте заказов")
    def test_orders_in_feed(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        profile_page = ProfilePage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        login_page.login(email, password)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        button = main_page.find_element(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 40).until(
            EC.invisibility_of_element_located((MainPageLocators.MODAL_OVERLAY)))
        main_page.go_to_personal_account()
        profile_page.click_element(MainPageLocators.ORDER_HISTORY_BUTTON)  
        history_order = profile_page.get_element_text(MainPageLocators.ORDER_ITEM_IN_HISTORY)        
        main_page.go_to_order_feed()
        in_progress_orders = order_feed_page.get_in_progress_order_number(MainPageLocators.ORDER_ITEM)
        assert history_order == in_progress_orders, f"Номер заказа {history_order} не найден в ленте заказов"
        
    @allure.title("Увеличение счетчика 'Выполнено за всё время'")
    def test_total_completed_counter(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        login_page.login(email, password)
        main_page.go_to_order_feed()
        initial_total = order_feed_page.get_total_completed()
        driver.get(Urls.BASE_URL)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        button = main_page.find_element(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        driver.execute_script("arguments[0].click();", button)   
        WebDriverWait(driver, 60).until(
            EC.invisibility_of_element_located((MainPageLocators.MODAL_OVERLAY)))
        orders = main_page.find_element(MainPageLocators.ORDER_FEED_LINK)
        driver.execute_script("arguments[0].click();", orders) 
        assert order_feed_page.get_total_completed() > initial_total
                
    @allure.title("Увеличение счетчика 'Выполнено за сегодня'")
    def test_today_completed_counter(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        login_page.login(email, password)
        main_page.go_to_order_feed()
        initial_today = order_feed_page.get_today_completed()
        driver.get(Urls.BASE_URL)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        button = main_page.find_element(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        driver.execute_script("arguments[0].click();", button) 
        WebDriverWait(driver, 40).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY))      
        orders = main_page.find_element(MainPageLocators.ORDER_FEED_LINK)
        driver.execute_script("arguments[0].click();", orders) 
        assert order_feed_page.get_today_completed() > initial_today
        
    @allure.title("Номер заказа в разделе 'В работе'")
    def test_order_in_progress(self, driver):
        email, password = get_existing_user()
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.go_to_personal_account()
        login_page.login(email, password)
        main_page.add_ingredient_to_order()
        main_page.place_order()
        button = main_page.find_element(MainPageLocators.ORDER_WINDOW_CLOSE_BUTTON)
        WebDriverWait(driver, 40).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY))    
        order_number = main_page.get_element_text(MainPageLocators.ORDER_NUMBER)
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 40).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY))    
        orders = main_page.find_element(MainPageLocators.ORDER_FEED_LINK)
        driver.execute_script("arguments[0].click();", orders) 
        time.sleep(3)
        assert order_feed_page.get_in_progress_order_number(MainPageLocators.ORDER_NUMBER_IN_PROCCESS) ==  f"0{order_number}"  