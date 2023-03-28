import pytest

from utils.allure_attach import AllureAttach
from utils.driver import Driver
from utils.settings import Settings


def pytest_addoption(parser):
    parser.addoption("--env", default="test")
    parser.addoption("--driver", default="emulator")
    parser.addoption("--attachments", default=True)


@pytest.fixture(scope='session')
def settings(request) -> Settings:
    setting = Settings(
        request.config.getoption("--env"),
        request.config.getoption("--driver")
    )

    return setting


@pytest.fixture(scope='function')
def window(settings):
    driver = Driver(settings)
    yield driver
    allureAttach = AllureAttach(settings)
    allureAttach.add(driver.driver())
    driver.quit()
