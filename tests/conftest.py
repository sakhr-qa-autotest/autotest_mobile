from distutils.util import strtobool

import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest

from wikipedia.utils.allure_attach import AllureAttach
from wikipedia.utils.driver import Driver
from wikipedia.utils.settings import Settings


def pytest_addoption(parser: Parser):
    parser.addoption("--env", default="test")
    parser.addoption("--driver", default="emulator")
    parser.addoption("--attachments", default=True)
    parser.addoption("--platformName", default=None)
    parser.addoption("--udid", default=None)
    parser.addoption("--platformVersion", default=None)
    parser.addoption("--deviceName", default="Google Pixel 3")
    parser.addoption("--sessionName", default=None)
    parser.addoption("--app", default=None)


@pytest.fixture(scope='session')
def settings(request: SubRequest) -> Settings:
    setting = Settings(
        request.config.getoption("--env"),
        request.config.getoption("--driver"),
        request
    )

    if type(request.config.getoption("--attachments")) != type(True):
        setting.set_attachments(bool(strtobool(request.config.getoption("--attachments"))))
    else:
        setting.set_attachments(request.config.getoption("--attachments"))

    return setting


@pytest.fixture(scope='function')
def window(settings):
    driver = Driver(settings)
    yield driver
    allureAttach = AllureAttach(settings)
    allureAttach.add(driver.driver())
    driver.quit()
