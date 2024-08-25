import time

import allure




def test_super_puper_mega_test(main_page, webinar_page, browser_page):
    with allure.step("Открыть главную страницу сайта Иннополис"):
        browser_page.goto(main_page.URL)
        time.sleep(2)
    with allure.step('Проверка URL-страницы "Вебинары"'):
        with browser_page.expect_popup() as page1_info:
            browser_page.get_by_role("link", name=main_page.WEBINAR, exact=True).click()
        page1 =  page1_info.value
        print(page1)
        assert page1.url == webinar_page.URL, 'Неправильный URL-адрес'
        time.sleep(2)
    with allure.step('Проверить заголовок на странице "Вебинары"'):
        heading_webinar = page1.locator("h1").text_content()
        print(heading_webinar)
        assert heading_webinar == webinar_page.HEADING, 'Неправильный заголовок на странице "Вебинары"'


    print('Супер-пупер-мега-тест выполнен')



