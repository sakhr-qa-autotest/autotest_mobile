import allure
from allure import step

from wikipedia.model.page.main.main import Main
from wikipedia.model.page.welcome.screen import Screen


@allure.title("Проверка экрана приветствие")
def test_continue(window):
    with step('Проверяем и читаем сообщения при первом запуске'):
        screen = Screen(window.driver())

        title0 = screen.title().text
        assert 'The Free Encyclopedia…in over 300 languages'.replace('\n', '') == title0.replace('\n', '')
        screen.forward().click()

        title2 = screen.title().text
        assert "New ways to explore".replace('\n', '') == title2.replace('\n', '')
        screen.forward().click()

        title3 = screen.title().text
        assert "Reading lists with sync".replace('\n', '') == title3.replace('\n', '')
        screen.forward().click()

        title4 = screen.title().text
        assert "Send anonymous data".replace('\n', '') == title4.replace('\n', '')


@allure.title("Проверка кнопку skip")
def test_skip(window):
    with step('Нажимаем на skip и проверяем переход'):
        screen = Screen(window.driver())
        screen.skip().click()

        main = Main(window.driver())
        assert main.logo().text == ""
