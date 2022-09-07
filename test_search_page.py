"""
Реализация тестового сценария <<Поиск в яндексе>>
"""
from .pages.main_page import MainPage 
from .pages.search_page import SearchPage


def test_guest_should_be_search_in_yandex(browser):
    page = MainPage(browser)
    page.open()
    page.should_be_search_box()
    page.input_search_tensor()
    page.should_be_see_suggest()
    search_page = SearchPage(browser)
    search_page.should_be_see_result_search_after_press_enter()
    search_page.should_be_first_link_tensor()

