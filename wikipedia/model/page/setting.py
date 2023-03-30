import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement


class Setting:
    __driver: webdriver

    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__driver.implicitly_wait(5)

    def findElementByText(self, text: str, className: str = 'android.widget.TextView') -> WebElement:
        time.sleep(0.3)
        elements = self.__driver.find_elements(AppiumBy.CLASS_NAME, className)

        for element in elements:
            if element.text == text:
                return element

    def back(self) -> WebElement:
        return self.__driver.back()
