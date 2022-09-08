import allure
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import SearchPageLocators, MainPageLocators


class SearchPage(BasePage):
    """
    Класс для проверки сценариев на странице поиска Яндекса
    """

    @allure.step("Проверяем появление таблицы результатов поиска после нажатия Enter")
    def should_be_see_result_search_after_press_enter(self):
        """
        Нажимаем кнопку Enter
        Проверяем появление таблицы результатов поиска после нажатия Enter
        """
        link = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        link.send_keys(Keys.ENTER)
        assert self.browser.find_element(*SearchPageLocators.SEARCH_CONTENT), "Таблица результатов поиска не появилась"

    @allure.step("Проверяем, что первая ссылка ведет на {url}")
    def should_be_first_link_tensor(self, url):
        """
        Проверяем, что первая ссылка ведет на url
        :params: url
        """
        link = self.browser.find_element(*SearchPageLocators.TENSOR_LINK)
        assert url in link.get_attribute('href'), "Первая ссылка не ведет на сайт {url}"