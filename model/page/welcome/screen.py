from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement


class Screen:
    __driver: webdriver

    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__driver.implicitly_wait(5)

    def skip(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')

    def forward(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')

    def title(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
