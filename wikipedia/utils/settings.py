import json

from _pytest.fixtures import SubRequest

from wikipedia.utils.file import abs_path_from_project
from wikipedia.utils.setting import browserstack, emulator
from wikipedia.utils.setting import real


class Settings:
    __attachments: bool = True

    __emulator: emulator.Emulator
    __is_emulator: bool = False

    __browserstack: browserstack.Browserstack
    __is_browserstack: bool = False

    __real: real.Real
    __is_real: bool = False

    __config: {}

    def __init__(self, env: str, driver: str, subRequest: SubRequest):

        fp = open(abs_path_from_project(f'../config.{env}.json'))
        config = json.loads(fp.read())
        self.__config = config

        if 'emulator' in config:
            if driver == 'emulator':
                self.__is_emulator = True
                self.__emulator = emulator.Emulator(config['emulator'])

                udid = self.__getoption('--udid', subRequest)
                if udid is not None:
                    self.__emulator.setUdid(udid)

                app = self.__getoption('--app', subRequest)
                if app is not None:
                    self.__emulator.setApp(app)

        if 'browserstack' in config:
            if driver == 'browserstack':
                self.__is_browserstack = True
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
                self.__is_real = True
                self.__real = real.Real(config['real'])

                udid = self.__getoption('--udid', subRequest)
                if udid is not None:
                    self.__real.setUdid(udid)

                app = self.__getoption('--app', subRequest)
                if app is not None:
                    self.__real.setApp(app)
        else:
            raise Exception("Driver not found")

    def is_emulator(self) -> bool:
        return self.__is_emulator

    def is_browserstack(self) -> bool:
        return self.__is_browserstack

    def is_real(self) -> bool:
        return self.__is_real

    def emulator(self) -> emulator.Emulator:
        return self.__emulator

    def browserstack(self) -> browserstack.Browserstack:
        return self.__browserstack

    def real(self) -> real.Real:
        return self.__real

    def set_attachments(self, attachments: bool = False):
        self.__attachments = attachments

    def attachments(self) -> bool:
        return self.__attachments

    def __getoption(self, option: str, subRequest: SubRequest):
        try:
            return subRequest.config.getoption(option)
        except:
            return None
