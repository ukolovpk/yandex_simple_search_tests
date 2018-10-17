import pytest
from selenium.webdriver import Firefox


@pytest.fixture
def webdriver(request):
     request.instance.driver = Firefox()
     request.addfinalizer(request.instance.driver.quit)
