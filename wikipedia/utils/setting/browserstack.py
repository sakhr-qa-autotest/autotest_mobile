from appium.options.android import UiAutomator2Options


class Browserstack:
    __automationName: str = None
    __platformName: str = None
    __platformVersion: str = None
    __deviceName: str = None
    __app: str = None
    __hubUrl: str = None
    __userLogin: str = None
    __accessKey: str = None
    __projectName: str = None
    __buildName: str = None
    __sessionName: str = None

    def __init__(self, config: {}):
        if 'automationName' in config:
            self.__automationName = config['automationName']
        if 'platformName' in config:
            self.__platformName = config['platformName']
        if 'platformVersion' in config:
            self.__platformVersion = config['platformVersion']
        if 'deviceName' in config:
            self.__deviceName = config['deviceName']
        if 'app' in config:
            self.__app = config['app']
        if 'hubUrl' in config:
            self.__hubUrl = config['hubUrl']
        if 'userLogin' in config:
            self.__userLogin = config['userLogin']
        if 'accessKey' in config:
            self.__accessKey = config['accessKey']
        if 'projectName' in config:
            self.__projectName = config['projectName']
        if 'buildName' in config:
            self.__buildName = config['buildName']
        if 'sessionName' in config:
            self.__sessionName = config['sessionName']

    def platformName(self) -> str:
        return self.__platformName

    def automationName(self) -> str:
        return self.__automationName

    def setPlatformVersion(self, platformVersion: str):
        self.__platformVersion = platformVersion

    def setApp(self, app: str):
        self.__app = app

    def platformVersion(self) -> str:
        return self.__platformVersion

    def setDeviceName(self, value: str):
        self.__deviceName = value

    def deviceName(self) -> str:
        return self.__deviceName

    def app(self) -> str:
        return self.__app

    def hubUrl(self) -> str:
        return self.__hubUrl

    def userLogin(self) -> str:
        return self.__userLogin

    def accessKey(self) -> str:
        return self.__accessKey

    def projectName(self) -> str:
        return self.__projectName

    def buildName(self) -> str:
        return self.__buildName

    def setSessionName(self, sessionName: str):
        self.__sessionName = sessionName

    def sessionName(self) -> str:
        return self.__sessionName

    def options(self) -> UiAutomator2Options:
        options = UiAutomator2Options()

        options.load_capabilities(
            {
                'platformVersion': self.platformVersion(),
                'bstack:options': {
                    'projectName': self.projectName(),
                    'buildName': self.buildName(),
                    'sessionName': self.sessionName(),
                    'userName': self.userLogin(),
                    'accessKey': self.accessKey(),
                },
            }
        )

        # self.__hubUrl = "http://" + self.userLogin() + ":" + self.accessKey() + "@hub-cloud.browserstack.com/wd/hub"

        if self.app() is not None:
            options.app = self.app()

        if self.deviceName() is not None:
            options.device_name = self.deviceName()

        return options
