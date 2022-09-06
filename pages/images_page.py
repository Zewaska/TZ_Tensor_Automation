from .locators import ImagesPageLocators
from .base_page import BasePage


class ImagesPage(BasePage):
    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = self.browser.current_url
        self.browser.implicitly_wait(timeout)
        #self.name_category = list()
        
        
    def open_first_popular_category(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        link = self.browser.find_element(*ImagesPageLocators.FRIST_CATEGORY)
        #global name_category
        #name_category = link.text
        #print(name_category)
        link.click()
        

    def should_be_see_name_category_in_search_box(self):
        assert self.browser.find_element(*ImagesPageLocators.SEARCH_BOX)
        #print(name_in_box.text)
        #name_in_box == True, "Название категории в строке поиска не совпадает с названием первой популярной категории"
        #pass