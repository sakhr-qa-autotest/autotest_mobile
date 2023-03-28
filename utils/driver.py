from appium import webdriver

from utils.settings import Settings


class Driver:
    __driver: webdriver = None

    def __init__(self, settings: Settings):

        if settings.isBrowserstack() == True:
            options = settings.browserstack().options()
            hubUrl = settings.browserstack().hubUrl()
        elif settings.isEmulator() == True:
            options = settings.emulator().options()
            hubUrl = settings.emulator().hubUrl()
        elif settings.isReal() == True:
            options = settings.real().options()
            hubUrl = settings.real().hubUrl()
        else:
            raise Exception("")

        self.__driver = webdriver.Remote(
            command_executor=hubUrl, options=options
        )

    def driver(self) -> webdriver:
        return self.__driver

    def close(self):
        return self.__driver.close()

    def quit(self):
        return self.__driver.quit()
