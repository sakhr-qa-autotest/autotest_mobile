import allure
from allure import step

from wikipedia.model.page.main.main import Main
from wikipedia.model.page.setting import Setting
from wikipedia.model.page.welcome.screen import Screen


@allure.title("Добавляем дополнительный язык")
def test_add_language(window):
    screen = Screen(window.driver())
    screen.skip().click()
    main = Main(window.driver())

    main.bottomMore().click()
    main.bottomSetting().click()
    setting = Setting(window.driver())
    setting.findElementByText('Wikipedia languages').click()
    setting.findElementByText('ADD LANGUAGE').click()

    with step('Добавляем Русский язык'):
        setting.findElementByText('Русский').click()
        setting.back()

        assert setting.findElementByText('English, русский').text == "English, русский"


@allure.title("Меняем шрифт")
def test_change_font(window):
    screen = Screen(window.driver())
    screen.skip().click()
    main = Main(window.driver())

    main.bottomMore().click()
    main.bottomSetting().click()
    setting = Setting(window.driver())
    setting.findElementByText('App theme').click()
    with step('Смена шрифта на SERIF'):
        setting.findElementByText('SERIF', 'android.widget.Button').click()
        setting.back()
        assert True
