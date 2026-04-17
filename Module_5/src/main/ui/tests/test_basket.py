from playwright.sync_api import Page, expect

from Module_5.src.main.ui.steps.basket_steps import BasketSteps
from Module_5.src.main.ui.steps.catalog_steps import CatalogSteps
from Module_5.src.main.ui.steps.checkout_steps import CheckoutSteps


def test_add_item_and_check_in_cart(page: Page):
    catalog_step = CatalogSteps(page)
    basket_step = BasketSteps(page)

    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.add_to_cart('Sauce Labs Backpack')

    basket_step.open_cart()
    basket_step.expect_item_in_cart('Sauce Labs Backpack')


def test_add_few_items_and_check_in_cart(page: Page):
    catalog_step = CatalogSteps(page)
    basket_step = BasketSteps(page)

    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.add_to_cart('Sauce Labs Bolt T-Shirt')
    catalog_step.add_to_cart('Sauce Labs Fleece Jacket')

    basket_step.open_cart()
    basket_step.expect_item_in_cart('Sauce Labs Bolt T-Shirt')
    basket_step.expect_item_in_cart('Sauce Labs Fleece Jacket')


def test_remove_few_items_from_cart(page: Page):
    catalog_step = CatalogSteps(page)
    basket_step = BasketSteps(page)

    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.add_to_cart('Sauce Labs Bolt T-Shirt')
    catalog_step.add_to_cart('Sauce Labs Fleece Jacket')

    basket_step.open_cart()
    basket_step.expect_item_in_cart('Sauce Labs Bolt T-Shirt')
    basket_step.expect_item_in_cart('Sauce Labs Fleece Jacket')

    basket_step.remove_item('Sauce Labs Bolt T-Shirt')
    basket_step.expect_item_not_in_cart('Sauce Labs Bolt T-Shirt')
    basket_step.remove_item('Sauce Labs Fleece Jacket')
    basket_step.expect_item_not_in_cart('Sauce Labs Fleece Jacket')


def test_checkout_multiple_items(page: Page):
    catalog_step = CatalogSteps(page)
    basket_step = BasketSteps(page)
    checkout_step = CheckoutSteps(page)

    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.add_to_cart('Sauce Labs Bolt T-Shirt')
    catalog_step.add_to_cart('Sauce Labs Fleece Jacket')

    basket_step.open_cart()
    basket_step.expect_item_in_cart('Sauce Labs Bolt T-Shirt')
    basket_step.expect_item_in_cart('Sauce Labs Fleece Jacket')
    basket_total = basket_step.get_items_total_price()
    basket_step.checkout()

    checkout_step.step_one_checkout('qwe', 'asd', '123')
    checkout_total = checkout_step.get_items_total_price()
    assert basket_total == checkout_total
    checkout_step.step_two_checkout()
    assert 'Thank you for your order!' in checkout_step.get_success_text()


def test_checkout_with_missing_information(page: Page):
    catalog_step = CatalogSteps(page)
    basket_step = BasketSteps(page)
    checkout_step = CheckoutSteps(page)

    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.add_to_cart('Sauce Labs Bolt T-Shirt')
    catalog_step.add_to_cart('Sauce Labs Fleece Jacket')

    basket_step.open_cart()
    basket_step.expect_item_in_cart('Sauce Labs Bolt T-Shirt')
    basket_step.expect_item_in_cart('Sauce Labs Fleece Jacket')
    basket_step.checkout()

    checkout_step.step_one_checkout('qwe', 'asd', '')
    assert 'Error' in checkout_step.get_error_text()