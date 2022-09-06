from .pages.base_page import BasePage
from .pages.images_page import ImagesPage


def test_guest_should_be_see_yandex_images(browser):
    page = BasePage(browser)
    page.open()
    page.should_be_link_images()
    page.go_to_images_page()
    image_page = ImagesPage(browser, url = browser.current_url)
    image_page.open_first_popular_category()
    image_page.should_be_see_name_category_in_search_box()
    image_page.open_first_small_image()
    image_page.should_be_open_first_image()
    image_page.press_button_next()
    image_page.should_be_open_second_image()
    image_page.press_button_forward()
    image_page.should_be_image_from_step_eaght()
