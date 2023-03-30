import allure
from allure import step

from wikipedia.model.page.main.main import Main
from wikipedia.model.page.search import Search
from wikipedia.model.page.welcome.screen import Screen


@allure.title("Проверяем успешный поиск")
def test_successful_search(window):
    screen = Screen(window.driver())
    screen.skip().click()

    with step('Вводим в поиск строку которая вернет успешный результат'):
        main = Main(window.driver())
        main.search().click()
        search = Search(window.driver())
        search.search().set_text("appium")
        result = search.findElementByText('Automation for Apps')

        assert result.text == 'Automation for Apps'


@allure.title("Проверяем успешный поиск")
def test_unsuccessful_search(window):
    screen = Screen(window.driver())
    screen.skip().click()

    with step('Вводим в поиск строку которая вернет успешный результат'):
        main = Main(window.driver())
        main.search().click()
        search = Search(window.driver())
        search.search().set_text("appiumdddd")

        assert search.resultText().text == "No results"


@allure.title("Очистка инпута поиска")
def test_clear_search_input(window):
    screen = Screen(window.driver())
    screen.skip().click()
    main = Main(window.driver())
    main.search().click()
    search = Search(window.driver())
    search.search().set_text("appiumdddd")

    with step('Нажимаем иконку очистки поля поиска'):
        search.closeSearch().click()

    assert search.search().text == 'Search Wikipedia'


@allure.title("вернуться на главную")
def test_back_to_main(window):
    screen = Screen(window.driver())
    screen.skip().click()
    main = Main(window.driver())
    main.search().click()
    search = Search(window.driver())

    with step('Нажимаем вернуться назад'):
        search.backToMain().click()

    assert main.logo().text == ""
