import allure


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
        with allure.step("Открываем главную страницу"):
            self.browser.get(self.url)