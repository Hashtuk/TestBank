import allure
from playwright.sync_api import Page, expect

from Module_5.src.main.ui.pages.catalog_page import CatalogPage


class CatalogSteps:
    def __init__(self, page: Page):
        self.page = page
        self.catalog_page = CatalogPage(page)

    @allure.step('Login as {username}')
    def login(self, username: str, password: str):
        self.catalog_page.login(username, password)
        return self

    @allure.step('Add {product_name} to cart')
    def add_to_cart(self, product_name: str):
        button = self.catalog_page.add_to_cart(item_name=product_name)
        expect(button).to_have_text('Remove')
        return self

    @allure.step('Remove {product_name} from cart')
    def remove_from_cart(self, product_name: str):
        button = self.catalog_page.remove_from_cart(item_name=product_name)
        expect(button).to_have_text('Add to cart')
        return self

    @allure.step('Sort items on: {option}')
    def sort_items(self, option: str):
        self.catalog_page.sort_items(option)
        return self

    @allure.step('Count the amount of products on the page')
    def get_products_count(self) -> int:
        return self.catalog_page.get_items_count()

    @allure.step('Getting all product names')
    def get_product_names(self) -> list[str]:
        return self.catalog_page.get_items_name()

    @allure.step('Getting all product prices')
    def get_product_prices(self) -> list[float]:
        return self.catalog_page.get_items_price()

    @allure.step('Count the amount of products in the cart')
    def count_products_in_cart(self) -> int:
        return self.catalog_page.get_cart_count()

    @allure.step('Open product details')
    def open_product_details(self, product_name: str) -> tuple:
        return self.catalog_page.get_product_details(product_name)

    @allure.step('Logout from account')
    def logout(self):
        self.catalog_page.logout()
        return self
