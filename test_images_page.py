from .pages.base_page import BasePage
from .pages.images_page import ImagesPage
import time


def test_guest_should_be_see_yandex_images(browser):
    page = BasePage(browser)
    page.open()
    page.should_be_images_page()
    page.go_to_images_page()
    image_page = ImagesPage(browser, url = browser.current_url)
    image_page.open_first_popular_category()
    image_page.should_be_see_name_category_in_search_box()

    time.sleep(5)