from playwright.sync_api import Page, expect

from Module_5.src.main.ui.steps.catalog_steps import CatalogSteps


def test_count_catalog(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')
    assert catalog_step.get_products_count() == 6


def test_sorted_by_name(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.sort_items('az')
    assert catalog_step.get_product_names() == sorted(catalog_step.get_product_names())


def test_sorted_by_name_reversed(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.sort_items('za')
    assert catalog_step.get_product_names() == sorted(catalog_step.get_product_names(), reverse=True)


def test_sorted_by_price(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.sort_items('lohi')
    assert catalog_step.get_product_prices() == sorted(catalog_step.get_product_prices())

    catalog_step.sort_items('hilo')
    assert catalog_step.get_product_prices() == sorted(catalog_step.get_product_prices(), reverse=True)

def test_add_to_cart(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.add_to_cart('Sauce Labs Bike Light')
    assert catalog_step.count_products_in_cart() == 1


def test_add_and_remove_from_cart(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.add_to_cart('Sauce Labs Onesie')
    assert catalog_step.count_products_in_cart() == 1

    catalog_step.remove_from_cart('Sauce Labs Onesie')
    assert catalog_step.count_products_in_cart() == 0


def test_product_details_onesie(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')

    name, price, details_name, details_price = catalog_step.open_product_details('Sauce Labs Onesie')
    assert name == details_name
    assert price == details_price


def test_product_details_jacket(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')

    name, price, details_name, details_price = catalog_step.open_product_details('Sauce Labs Fleece Jacket')
    assert name == details_name
    assert price == details_price


def test_remove_shirt_from_catalog(page: Page):
    catalog_step = CatalogSteps(page)
    catalog_step.login('standard_user', 'secret_sauce')
    catalog_step.add_to_cart('Test.allTheThings() T-Shirt (Red)')

    catalog_step.remove_from_cart('Test.allTheThings() T-Shirt (Red)')