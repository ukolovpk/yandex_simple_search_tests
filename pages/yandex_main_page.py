from pages.base_page import BasePage


class YandexRuPage(BasePage):
    def __init__(self, driver):
        super(YandexRuPage, self).__init__(driver=driver, url="https://yandex.ru/")
