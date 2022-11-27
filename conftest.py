import pytest
from selene.support.shared import browser


@pytest.fixture()
def set_browser_size():
    browser.config.window_width = 800
    browser.config.window_height = 600


@pytest.fixture()
def open_browser(set_browser_size):
    browser.open('https://google.com')