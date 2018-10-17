from pages.base_page import BasePage


class SetHomePPage(BasePage):
    def __init__(self, driver):
        super(SetHomePPage, self).__init__(driver=driver, url="https://home.yandex.ru/?from=prov_yaru")
