import pytest
from pages.search_main_page import SearchMainPage


@pytest.mark.usefixtures("webdriver")
class TestYandexSearch(object):

    def test_ya_search_main_page(self):

        # Проверка работоспособности "Войти в почту"
        main_page = SearchMainPage(driver=self.driver)
        main_page.open()
        mail_page = main_page.to_mail()
        assert mail_page.get_current_url() == mail_page.url

        # Проверка работоспособности "Сделать стартовой"
        main_page.open()
        set_homepage_page = main_page.set_homepage()
        assert set_homepage_page.get_current_url() == set_homepage_page.url

        # Проверка работоспособности ссылки "Яндекс"
        main_page.open()
        yandex_ru_page = main_page.to_yandex_ru()
        assert yandex_ru_page.get_current_url() == yandex_ru_page.url

    def test_ya_search(self):

        # Проверка работоспособности поиска. Проверка, что среди результатов поиска - наш запрос
        main_page = SearchMainPage(driver=self.driver)
        main_page.open()
        query = "playrix"
        main_page.fill_query(query)
        results_page = main_page.click_search_button()
        assert query in results_page.get_title()
        assert results_page.check_results([query, "плейрикс"])


if __name__ == "__main__":
    pytest.main()
