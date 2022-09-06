from selenium.webdriver.common.by import By


class BasePageLocators():
    SEARCH_BOX = (By.ID, "text")
    IMAGES_LINK = (By.CSS_SELECTOR, "a[data-id='images']")
    SUGGEST_LIST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    SEARCH_CONTENT = (By.ID, "search-result")
    TENSOR_LINK = (By.CSS_SELECTOR, "a[accesskey='1']")

class ImagesPageLocators():
    FRIST_CATEGORY = (By.CSS_SELECTOR, "div[class='PopularRequestList-Shadow']")
    SEARCH_BOX = (By.CLASS_NAME, "input__control")
    