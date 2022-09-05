from selenium.webdriver.common.by import By


class BasePageLocators():
    SEARCH_BOX = (By.ID, "text")
    IMAGES_LINK = (By.CLASS_NAME, "services-new__icon_images")
    SUGGEST_LIST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    SEARCH_CONTENT = (By.ID, "search-result")