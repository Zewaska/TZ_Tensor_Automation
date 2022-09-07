from selenium.common.exceptions import NoSuchElementException

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, timeout=4):
        self.browser = browser
        self.url = 'https://yandex.ru/'
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        
    def go_to_images_page(self):
        link = self.browser.find_element(*BasePageLocators.IMAGES_LINK)
        link.click()
        
    def should_be_search_box(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_BOX), "Поле поиска нет на главной странице"

    def input_search_tensor(self):
        search = self.browser.find_element(*BasePageLocators.SEARCH_BOX)
        search.send_keys("Тензор")

    def should_be_see_suggest(self):
        assert self.browser.find_element(*BasePageLocators.SUGGEST_LIST), "Таблица с подсказками не появилась"
        


    def should_be_link_images(self):
        assert self.is_element_present(*BasePageLocators.IMAGES_LINK), "Ссылка <<Картинки>> не присутствует на странице"


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

