from .pages.base_page import BasePage


def test_guest_should_be_search_in_yandex(browser):
    page = BasePage(browser)
    page.open()
    page.should_be_search_box()
    page.input_search_tensor()
    page.should_be_see_suggest()
    page.should_be_see_result_search_after_press_enter()
    page.should_be_first_link_tensor()

