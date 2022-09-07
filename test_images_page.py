"""
Реализация тестового сценария <<Картинки на яндексе>>
"""
import allure
from .pages.images_page import ImagesPage
from .pages.main_page import MainPage


@allure.description("Тестовый сценарий <<Картинки на яндексе>>")
def test_guest_should_be_see_yandex_images(browser):
    # Создаем экземпляр класса, заходим на yandex.ru
    page = MainPage(browser)
    page.open()

    # Проверяем, что ссылка Картинки присутствует
    page.should_be_link_images()

    # Кликаем на ссылку Картинки, создаем экземпляр класса ImagesPage
    page.go_to_images_page()
    image_page = ImagesPage(browser, url = browser.current_url)

    # Проверяем, что перешли на url
    image_page.should_be_images_in_url('https://yandex.ru/images/')

    # Открываем первую популярную категорию картинок
    image_page.open_first_popular_category()

    # Проверяем, что название категории отображается в поле поиска
    image_page.should_be_see_name_category_in_search_box()

    # Открываем первую картинку
    image_page.open_first_small_image()

    # Проверяем что первая картинка открылась
    image_page.should_be_open_first_image()

    # Нажимаем кнопку вперед
    image_page.press_button_next()

    # Проверяем, что картинка сменилась
    image_page.should_be_open_second_image()

    # Нажимаем кнопку назад
    image_page.press_button_forward()

    # Проверяем, что открылась первая картинка
    image_page.should_be_image_from_step_eaght()