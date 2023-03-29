from appium import webdriver


class BottomMenu:
    __driver: webdriver

    def __init__(self, driver: webdriver):
        self.__driver = driver
        self.__driver.implicitly_wait(5)
