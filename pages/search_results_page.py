from pages.base_page import BasePage
from locators.search_results_page_locators import SearchResultsPageLocators


class SearchResultsPage(BasePage):

    def __init__(self, driver):
        super(SearchResultsPage, self).__init__(driver=driver, url="https://yandex.ru/search/?text={query}")
        self.locator = SearchResultsPageLocators()

    def open(self, query_text):
        self.driver.get(self.url.format(query=query_text))

    def get_title(self):
        print(self.driver.title)
