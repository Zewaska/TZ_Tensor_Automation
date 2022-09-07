import allure
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """
    Класс для проверки шагов на главной странице Яндекса
    """
    
    def go_to_images_page(self):
        """
        Находим и открываем страницу <<Картинки>>
        """
        with allure.step("Открываем страницу <<Картинки>>"):
            self.browser.find_element(*MainPageLocators.IMAGES_LINK).click()
        
    def should_be_search_box(self):
        """
        Проверяем наличие поля поиск
        """
        with allure.step("Проверяем наличие поля поиск"):
            assert self.browser.find_element(*MainPageLocators.SEARCH_BOX), "Поле поиска нет на главной странице"

    def input_search_tensor(self):
        """
        Находим и передаем в поиск Тензор
        """
        with allure.step("Вводим в поиск Тензор"):
            self.browser.find_element(*MainPageLocators.SEARCH_BOX).send_keys("Тензор")

    def should_be_see_suggest(self):
        """
        Проверяем, что появилась таблица с подсказками
        """
        with allure.step("Проверяем наличие таблицы с подсказками"):
            assert self.browser.find_element(*MainPageLocators.SUGGEST_LIST), "Таблица с подсказками не появилась"
        
    def should_be_link_images(self):
        """
        Проверяем наличие ссылки «Картинки»
        """
        with allure.step("Проверяем наличие ссылки «Картинки»"):
            assert self.browser.find_element(*MainPageLocators.IMAGES_LINK), "Ссылка <<Картинки>> не присутствует на странице"