import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement


class Search:
    __driver: webdriver

    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__driver.implicitly_wait(5)

    def search(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')

    def resultText(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/results_text')

    def closeSearch(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/search_close_btn')

    def backToMain(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')

    def findElementByText(self, text: str, className: str = 'android.widget.TextView') -> WebElement:
        time.sleep(0.3)
        elements = self.__driver.find_elements(AppiumBy.CLASS_NAME, className)

        for element in elements:
            if element.text == text:
                return element
