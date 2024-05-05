import pytest
from selene import browser, be, have


@pytest.fixture()
def browser_params():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    print("Открыли браузер")

    yield
    browser.quit()
    print("Закрыли браузер")
