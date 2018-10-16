from selenium.webdriver.common.by import By


class SearchMainPageLocators(object):
    search_input = (By.ID, "text")
    search_button = (By.XPATH, '//div[contains(@class, "search2__button")]/button')
    yandex_link = (By.LINK_TEXT, "")
