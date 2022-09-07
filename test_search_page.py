"""
Реализация тестового сценария <<Поиск в яндексе>>
"""
import allure
from .pages.main_page import MainPage 
from .pages.search_page import SearchPage


@allure.description("Тестовый сценарий <<Поиск в яндексе>>")
def test_guest_should_be_search_in_yandex(browser):
    # Создаем экземпляр класса, заходим на yandex.ru
    page = MainPage(browser)
    page.open()

    # Проверяем наличие поля поиска
    page.should_be_search_box()

    # Вводим в поле поиска Тензор
    page.input_search_tensor()

    # Проверяем появление таблицы с подсказками
    page.should_be_see_suggest()

    # Создаем экземпляр класса SearchPage
    search_page = SearchPage(browser)

    # Проверяем появление таблицы результатов после нажатия Enter
    search_page.should_be_see_result_search_after_press_enter()

    # Проверяем что первая ссылка ведет на tensor.ru
    search_page.should_be_first_link_tensor('tensor.ru')