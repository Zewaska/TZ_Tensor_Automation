from selenium.webdriver.common.by import By


class BasePageLocators():
    SEARCH_BOX = (By.ID, "text")
    IMAGES_LINK = (By.CSS_SELECTOR, "a[data-id='images']")
    SUGGEST_LIST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    

class SearchPageLocators():
    SEARCH_CONTENT = (By.ID, "search-result")
    TENSOR_LINK = (By.CSS_SELECTOR, "a[accesskey='1']")

class ImagesPageLocators():
    FRIST_CATEGORY = (By.CSS_SELECTOR, "div[class='PopularRequestList-SearchText']")
    SEARCH_BOX = (By.CLASS_NAME, "input__control")
    FRIST_IMAGE = (By.CSS_SELECTOR, "img.serp-item__thumb")
    FRIST_IMAGE_ORIGIN = (By.CSS_SELECTOR, "div[class='MMThumbImage-Image']")
    IMAGE_ORIGIN = (By.CLASS_NAME, "MMImage-Origin") 
    BUTTON_NEXT = (By.CLASS_NAME,"MediaViewer-ButtonNext")
    BUTTON_FORWARD = (By.CLASS_NAME,"MediaViewer-ButtonPrev")

    