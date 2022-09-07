from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import SearchPageLocators, MainPageLocators


class SearchPage(BasePage):
    """
    Класс для проверки сценариев на странице поиска Яндекса
    """

    def should_be_see_result_search_after_press_enter(self):
        """
        Нажимаем кнопку Enter
        Проверяем появление таблицы результатов поиска после нажатия Enter
        """
        search = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        search.send_keys(Keys.ENTER)
        assert self.browser.find_element(*SearchPageLocators.SEARCH_CONTENT), "Таблица результатов поиска не появилась"

    def should_be_first_link_tensor(self):
        """
        Проверяем, что первая ссылка ведет на сайт tensor.ru
        """
        link = self.browser.find_element(*SearchPageLocators.TENSOR_LINK)
        assert 'tensor.ru/' in link.get_attribute('href'), "Первая ссылка не ведет на сайт tensor.ru"