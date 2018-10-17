from selenium.webdriver.common.by import By


class SearchMainPageLocators(object):
    search_input = (By.ID, "text")
    search_button = (By.XPATH, '//div[contains(@class,"search2__button")]/button')
    to_mail_button = (By.LINK_TEXT, "Войти в почту")
    set_homepage_button = (By.LINK_TEXT, "Сделать стартовой")
    yandex_link = (By.XPATH, '//tr[contains(@class, "footer")]//a')
