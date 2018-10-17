from selenium.webdriver.common.by import By


class SearchResultsPageLocators(object):
    results_list = (By.XPATH, '//div[@class="organic__url-text"]')
