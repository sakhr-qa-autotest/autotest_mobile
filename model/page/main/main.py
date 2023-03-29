from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement


class Main:
    __driver: webdriver

    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__driver.implicitly_wait(5)

    def logo(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar')

    def search(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')
