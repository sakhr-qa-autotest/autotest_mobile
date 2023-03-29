import json

import utils.file
from utils.setting import browserstack, emulator, real


class Settings:
    __attachments: bool = True

    __emulator: emulator.Emulator
    __isEmulator: bool = False

    __browserstack: browserstack.Browserstack
    __isBrowserstack: bool = False

    __real: real.Real
    __IsReal: bool = False

    __config: {}

    def __init__(self, env: str, driver: str):

        fp = open(utils.file.abs_path_from_project(f'config.{env}.json'))
        config = json.loads(fp.read())
        self.__config = config

        if 'emulator' in config:
            if driver == 'emulator':
                self.__isEmulator = True
                self.__emulator = emulator.Emulator(config['emulator'])
        if 'browserstack' in config:
            if driver == 'browserstack':
                self.__isBrowserstack = True
                self.__browserstack = browserstack.Browserstack(config['browserstack'])
        if 'real' in config:
            if driver == 'real':
                self.__IsReal = True
                self.__real = real.Real(config['real'])
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
