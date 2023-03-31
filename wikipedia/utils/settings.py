import json

from _pytest.fixtures import SubRequest

from wikipedia.utils.file import abs_path_from_project
from wikipedia.utils.setting import browserstack, emulator
from wikipedia.utils.setting import real


class Settings:
    __attachments: bool = True

    __emulator: emulator.Emulator
    __isEmulator: bool = False

    __browserstack: browserstack.Browserstack
    __isBrowserstack: bool = False

    __real: real.Real
    __IsReal: bool = False

    __config: {}

    def __init__(self, env: str, driver: str, subRequest: SubRequest):

        fp = open(abs_path_from_project(f'../config.{env}.json'))
        config = json.loads(fp.read())
        self.__config = config

        if 'emulator' in config:
            if driver == 'emulator':
                self.__isEmulator = True
                self.__emulator = emulator.Emulator(config['emulator'])

                udid = self.__getoption('--udid', subRequest)
                if udid is not None:
                    self.__emulator.setUdid(udid)

                app = self.__getoption('--app', subRequest)
                if app is not None:
                    self.__emulator.setApp(app)

        if 'browserstack' in config:
            if driver == 'browserstack':
                self.__isBrowserstack = True
                self.__browserstack = browserstack.Browserstack(config['browserstack'])

                platformVersion = self.__getoption('--platformVersion', subRequest)
                if platformVersion is not None:
                    self.__browserstack.setPlatformVersion(platformVersion)

                sessionName = self.__getoption('--sessionName', subRequest)
                if sessionName is not None:
                    self.__browserstack.setSessionName(sessionName)

                app = self.__getoption('--app', subRequest)
                if app is not None:
                    self.__browserstack.setApp(app)

                deviceName = self.__getoption('--deviceName', subRequest)
                if deviceName is not None:
                    self.__browserstack.setDeviceName(deviceName)
        if 'real' in config:
            if driver == 'real':
                self.__IsReal = True
                self.__real = real.Real(config['real'])

                udid = self.__getoption('--udid', subRequest)
                if udid is not None:
                    self.__real.setUdid(udid)

                app = self.__getoption('--app', subRequest)
                if app is not None:
                    self.__real.setApp(app)
        else:
            raise Exception("Driver not found")

    def isEmulator(self) -> bool:
        return self.__isEmulator

    def isBrowserstack(self) -> bool:
        return self.__isBrowserstack

    def isReal(self) -> bool:
        return self.__IsReal

    def emulator(self) -> emulator.Emulator:
        return self.__emulator

    def browserstack(self) -> browserstack.Browserstack:
        return self.__browserstack

    def real(self) -> real.Real:
        return self.__real

    def setAttachments(self, attachments: bool = False):
        self.__attachments = attachments

    def attachments(self) -> bool:
        return self.__attachments

    def __getoption(self, option: str, subRequest: SubRequest):
        try:
            return subRequest.config.getoption(option)
        except:
            return None
