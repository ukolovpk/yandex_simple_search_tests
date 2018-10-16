from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from locators.search_main_page_locators import SearchMainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class SearchMainPage(BasePage):

    def __init__(self, driver):
        super(SearchMainPage, self).__init__(driver=driver, url="https://ya.ru")
        self.locator = SearchMainPageLocators()

    def open(self):
        self.driver.get(self.url)

    def fill_query(self, query):
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.locator.search_input)))
        search_input.send_keys(query)

    def click_search_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.search_button)).click()
        return SearchResultsPage(self.driver)


if __name__ == '__main__':
    my_driver = Firefox()
    page = SearchMainPage(driver=my_driver)
    page.open()
    print('Page title: ' + my_driver.title)
    page.fill_query("vk")
    page2 = page.click_search_button()
    page2.get_title()
    my_driver.quit()
