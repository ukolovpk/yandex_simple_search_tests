from pages.base_page import BasePage


class YandexMailPage(BasePage):
    def __init__(self, driver):
        super(YandexMailPage, self).__init__(driver=driver, url="https://mail.yandex.ru/")
