from .locators import ImagesPageLocators
from .base_page import BasePage


class ImagesPage(BasePage):
    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = self.browser.current_url
        self.__name_category = None
        self.__first_image_small = None
        self.__first_image_src = None
        self.browser.implicitly_wait(timeout)
        
        
    def open_first_popular_category(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        link = self.browser.find_element(*ImagesPageLocators.FRIST_CATEGORY)
        self.name_category = link.text
        link.click()
        

    def should_be_see_name_category_in_search_box(self):
        name_in_box = self.browser.find_element(*ImagesPageLocators.SEARCH_BOX)
        assert name_in_box.get_attribute("value") == self.name_category, "Название категории в строке поиска не совпадает с названием первой популярной категории"
        
    def open_first_small_image(self):
        link = self.browser.find_element(*ImagesPageLocators.FRIST_IMAGE)
        self.first_image_small = link.get_attribute("src")
        link.click()

    def should_be_open_first_image(self):
        link = self.browser.find_element(*ImagesPageLocators.FRIST_IMAGE_ORIGIN)
        self.first_image_src = self.get_src_image()
        assert self.first_image_small.replace("https:", '') in link.get_attribute("style"), "Открылась не первая картинка из популярной категории"

    def get_src_image(self):
        image = self.browser.find_element(*ImagesPageLocators.IMAGE_ORIGIN)
        return image.get_attribute('src')

    def press_button_next(self):
        link = self.browser.find_element(*ImagesPageLocators.BUTTON_NEXT)
        link.click()

    def should_be_open_second_image(self):
        second_image_src = self.get_src_image()
        assert self.first_image_src != second_image_src, "Картинка не сменилась"

    def press_button_forward(self):
        link = self.browser.find_element(*ImagesPageLocators.BUTTON_FORWARD)
        link.click()

    def should_be_image_from_step_eaght(self):
        current_src_image = self.get_src_image()
        assert self.first_image_src == current_src_image, "Изображение отличается от картинки из шага 8"