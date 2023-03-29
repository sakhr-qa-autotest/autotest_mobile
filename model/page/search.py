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

    def results(self) -> [WebElement]:
        return self.__driver.find_elements(AppiumBy.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')

    def resultText(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/results_text')

    def closeSearch(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/search_close_btn')

    def backToMain(self) -> WebElement:
        return self.__driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
