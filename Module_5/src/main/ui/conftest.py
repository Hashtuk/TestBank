import pytest
from playwright.sync_api import Page


@pytest.fixture(scope='session')
def browser_type_launch_args():
    return {
        'headless': False
    }

@pytest.fixture
def auth_page(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_role('button', name='Login').click()
    return page