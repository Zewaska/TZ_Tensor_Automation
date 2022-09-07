from .locators import SearchPageLocators, BasePageLocators
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def should_be_see_result_search_after_press_enter(self):
        search = self.browser.find_element(*BasePageLocators.SEARCH_BOX)
        search.send_keys(Keys.ENTER)
        assert self.browser.find_element(*SearchPageLocators.SEARCH_CONTENT), "Таблица результатов поиска не появилась"

    def should_be_first_link_tensor(self):
        link = self.browser.find_element(*SearchPageLocators.TENSOR_LINK)
        assert 'tensor.ru/' in link.get_attribute('href'), "Первая ссылка не ведет на сайт tensor.ru" 