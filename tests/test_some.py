import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy


@allure.title("Состояние корзины в заголовке")
def test_some(window):
    with step('Skip'):
        window.driver().find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button').click()
