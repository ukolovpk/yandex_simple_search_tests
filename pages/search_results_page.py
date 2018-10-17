from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.search_results_page_locators import SearchResultsPageLocators


class SearchResultsPage(BasePage):

    def __init__(self, driver):
        super(SearchResultsPage, self).__init__(driver=driver, url="https://yandex.ru/search/?text={query}")
        self.locator = SearchResultsPageLocators()

    def open(self, query_text):
        self.driver.get(self.url.format(query=query_text))

    def get_title(self):  # del
        print(self.driver.title)

    def check_results(self, query_values):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator.results_list))
        results_list = self.driver.find_elements(*self.locator.results_list)
        headers = [i.text.lower() for i in results_list]
        for i in headers:
            if not any(s in i for s in query_values):
                raise Exception("At least one of expected values is not in '{act}'".format(act=i))
