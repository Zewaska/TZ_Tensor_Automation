import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()