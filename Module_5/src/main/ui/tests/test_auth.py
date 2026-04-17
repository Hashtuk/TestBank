from playwright.sync_api    import expect, Page

from Module_5.src.main.ui.pages.login_page import LoginPage
from Module_5.src.main.ui.steps.catalog_steps import CatalogSteps
from Module_5.src.main.ui.steps.login_steps import LoginSteps
from Module_5.src.main.ui.utils.constants import Urls


def test_auth(page: Page):
    login_steps = LoginSteps(page)
    login_steps.open_login_page().login('standard_user', 'secret_sauce')
    expect(page, 'Failed to redirect to inventory').to_have_url('https://www.saucedemo.com/inventory.html')


def test_auth_invalid(page: Page):
    login_steps = LoginSteps(page)
    login_steps.open_login_page().login('locked_out_user', 'secret_sauce')
    expect(page).to_have_url(login_steps.LOGIN_URL)
    assert 'locked out' in login_steps.get_error_text()


def test_logout_standard_user(page: Page):
    catalog_step = CatalogSteps(page)
    login_steps = LoginSteps(page)
    login_steps.open_login_page().login('standard_user', 'secret_sauce')
    catalog_step.logout()
    expect(page).to_have_url(Urls.BASE)


def test_logout_visual_user(page: Page):
    catalog_step = CatalogSteps(page)
    login_steps = LoginSteps(page)
    login_steps.open_login_page().login('visual_user', 'secret_sauce')
    catalog_step.logout()
    expect(page).to_have_url(Urls.BASE)