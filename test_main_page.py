from .pages.base_page import BasePage
import time

def test_guest_should_see_search_box(browser):
    page = BasePage(browser)
    page.open()
    page.should_be_search()
    page.input_search_tensor()
    page.should_be_see_suggest()
    page.should_be_see_result_search_after_press_enter()

    time.sleep(5)

