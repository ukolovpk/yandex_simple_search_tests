class BasePage(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
