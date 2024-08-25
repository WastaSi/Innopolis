
import pytest
from playwright.sync_api import Playwright

from pages.main_page import MainPage
from pages.webinar import WebinarPage


@pytest.fixture(scope='module')
def main_page():
    return MainPage()


@pytest.fixture(scope='module')
def webinar_page():
    return WebinarPage()


@pytest.fixture(scope='module')
def browser_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context.new_page()
    context.close()
    browser.close()