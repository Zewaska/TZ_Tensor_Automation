import allure
from .base_page import BasePage
from .locators import ImagesPageLocators


class ImagesPage(BasePage):
    """
    Класс для проверки сценариев на странице <<Картинки>> Яндекса
    """   
    def __init__(self, browser, url, timeout=10):
        """
        Конструктор класса
        """
        self.browser = browser
        self.url = url
        self.__name_category = None
        self.__first_image_small = None
        self.__first_image_src = None
        self.browser.implicitly_wait(timeout)
    
    @allure.step("Проверяем, что перешли на {url}")
    def should_be_images_in_url(self, url):
        """
        Переходим в открывшуюся вкладку браузера
        Проверяем, что перешли на url
        :params: url
        """
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert url in self.browser.current_url,\
        "В строке адреса страницы отсутствует {url}"

    @allure.step("Открываем первую популярную категорию")
    def open_first_popular_category(self):
        """
        Находим и нажимаем на первую популярную категорию
        """
        link = self.browser.find_element(*ImagesPageLocators.FRIST_CATEGORY)
        self.name_category = link.text
        link.click()
    
    @allure.step("Проверяем название категории в поле поиска")
    def should_be_see_name_category_in_search_box(self):
        """
        Проверяем, что название категории отображается в поле поиска
        """
        name_in_box = self.browser.find_element(*ImagesPageLocators.SEARCH_BOX)
        assert name_in_box.get_attribute("value") == self.name_category,\
            "Название категории в строке поиска не совпадает с названием первой популярной категории"
        
    @allure.step("Открываем первую картинку")
    def open_first_small_image(self):
        """
        Находим и нажимаем первую картинку
        """
        link = self.browser.find_element(*ImagesPageLocators.FRIST_IMAGE)
        self.first_image_small = link.get_attribute("src")
        link.click()

    @allure.step("Проверяем, что открыли первую картинку")
    def should_be_open_first_image(self):
        """
        Проверяем, что открыли первую картинку
        """
        link = self.browser.find_element(*ImagesPageLocators.FRIST_IMAGE_ORIGIN)

        # Сохраняем значение 'src' первой картинки
        self.first_image_src = self.get_src_image()
        assert self.first_image_small.replace("https:", '') in link.get_attribute("style"),\
            "Открылась не первая картинка из популярной категории"

    def get_src_image(self):
        """
        Получаем значение 'src' картинки
        Возвращаем значение 'src' картинки
        """
        image = self.browser.find_element(*ImagesPageLocators.IMAGE_ORIGIN)
        return image.get_attribute('src')

    @allure.step("Нажимаем кнопку вперед")
    def press_button_next(self):
        """
        Находим и нажимаем кнопку вперед
        """
        self.browser.find_element(*ImagesPageLocators.BUTTON_NEXT).click()

    @allure.step("Проверем, что картинка сменилась")
    def should_be_open_second_image(self):
        """
        Проверем, что картинка сменилась
        """
        second_image_src = self.get_src_image()
        assert self.first_image_src != second_image_src, "Картинка не сменилась"

    @allure.step("Нажимаем кнопку назад")
    def press_button_forward(self):
        """
        Находим и нажимаем кнопку назад
        """
        self.browser.find_element(*ImagesPageLocators.BUTTON_FORWARD).click()

    @allure.step("Проверяем, что открылась первая картинка")
    def should_be_image_from_step_eaght(self):
        """
        Проверяем, что открылась первая картинка 
        """    
        current_src_image = self.get_src_image()
        assert self.first_image_src == current_src_image, "Изображение отличается от картинки из шага 8"