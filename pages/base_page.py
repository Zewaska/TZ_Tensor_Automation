from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    Базовый класс
    """   
    def __init__(self, browser, timeout=5):
        """
        Конструктор класса
        """
        self.browser = browser
        self.url = 'https://yandex.ru/'
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Открываем главную страницу
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Проверяем присутствие элемента на странице

        :how: способ поиска элемента
        :what: селектор поиска элемента
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

