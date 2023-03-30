from appium.options.android import UiAutomator2Options

from wikipedia.utils.file import abs_path_from_project


class Real:
    __automationName: str = None
    __platformName: str = None
    __app: str = None
    __appWaitActivity: str = None
    __newCommandTimeout: str = None
    __udid: str = None
    __hubUrl: str = None

    def __init__(self, config: {}):
        if 'automationName' in config:
            self.__automationName = config['automationName']
        if 'platformName' in config:
            self.__platformName = config['platformName']
        if 'app' in config:
            self.__app = config['app']
        if 'appWaitActivity' in config:
            self.__appWaitActivity = config['appWaitActivity']
        if 'newCommandTimeout' in config:
            self.__newCommandTimeout = config['newCommandTimeout']
        if 'udid' in config:
            self.__udid = config['udid']
        if 'hubUrl' in config:
            self.__hubUrl = config['hubUrl']

    def hubUrl(self) -> str:
        return self.__hubUrl

    def automationName(self) -> str:
        return self.__automationName

    def setPlatformName(self, platformName: str):
        self.__platformName = platformName

    def platformName(self) -> str:
        return self.__platformName

    def setUdid(self, udid: str):
        self.__udid = udid

    def app(self) -> str:
        return self.__app

    def appWaitActivity(self) -> str:
        return self.__appWaitActivity

    def newCommandTimeout(self) -> str:
        return self.__newCommandTimeout

    def udid(self) -> str:
        return self.__udid

    def options(self) -> UiAutomator2Options:
        options = UiAutomator2Options()

        if self.app() is not None:
            options.app = (
                abs_path_from_project('../' + self.app())
                if self.app() and (
                        self.app().startswith('./') or self.app().startswith('../'))
                else self.app()
            )
        if self.udid() is not None:
            options.udid = self.udid()
            options.ignore_hidden_api_policy_error = True

        if self.platformName() is not None:
            options.platform_name = self.platformName()

        if self.appWaitActivity() is not None:
            options.app_wait_activity = self.appWaitActivity()

        options.new_command_timeout = 60

        return options
