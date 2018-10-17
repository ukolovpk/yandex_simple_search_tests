from selenium.webdriver.common.by import By


class SearchResultsPageLocators(object):
    results_list = (By.XPATH, '//div[@class="content__left"]//li[contains(@class, "serp-item")]//div[@class="organic__url-text"]')
