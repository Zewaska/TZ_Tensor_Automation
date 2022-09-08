import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def find_element(self, locator, time=10):
        """
        Поиск элемента по локатору в течение заданного времени
        Возвращает элемент или генерирует ошибку
        :param: локатор
        :param: промежуток времени
        """
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                message=f'Не найден элемент по локатору {locator}')

    @allure.step("Открываем главную страницу")
    def open(self):
        """
        Открываем главную страницу
        """
        self.browser.get(self.url)