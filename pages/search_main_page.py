from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage
from pages.set_homepage_page import SetHomePPage
from pages.yandex_mail_page import YandexMailPage
from pages.yandex_main_page import YandexRuPage
from selenium.webdriver.support.ui import WebDriverWait
from locators.search_main_page_locators import SearchMainPageLocators
from selenium.webdriver.support import expected_conditions as ec


class SearchMainPage(BasePage):

    def __init__(self, driver):
        super(SearchMainPage, self).__init__(driver=driver, url="https://ya.ru")
        self.locator = SearchMainPageLocators()

    def open(self):
        self.driver.get(self.url)

    def fill_query(self, query):
        search_input = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((self.locator.search_input)))
        search_input.send_keys(query)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator.search_button))
        search_button.click()
        return SearchResultsPage(self.driver)

    def to_mail(self):
        to_mail_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator.to_mail_button))
        to_mail_button.click()
        return YandexMailPage(self.driver)

    def set_homepage(self):
        set_homepage_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator.set_homepage_button))
        set_homepage_button.click()
        return SetHomePPage(self.driver)

    def to_yandex_ru(self):
        to_yandex_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator.yandex_link))
        to_yandex_button.click()
        return YandexRuPage(self.driver)
