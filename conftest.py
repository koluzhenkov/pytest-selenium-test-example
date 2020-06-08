import allure
import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app():
    # with allure.step('Running browser'):
    fixture = Application()
    yield fixture
    # with allure.step('Stopping browser'):
    fixture.destroy()
