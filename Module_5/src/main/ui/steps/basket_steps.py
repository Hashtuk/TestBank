import allure
from playwright.sync_api import Page

from Module_5.src.main.ui.pages.basket_page import BasketPage


class BasketSteps:
    def __init__(self, page: Page):
        self.page = page
        self.basket_page = BasketPage(page)

    @allure.step('Open the cart')
    def open_cart(self):
        self.basket_page.open_cart()
        return self

    @allure.step('Check if the item in the cart')
    def expect_item_in_cart(self, product_name: str):
        self.basket_page.expect_item_in_cart(product_name)
        return self

    @allure.step('Check if the item not in the cart')
    def expect_item_not_in_cart(self, product_name: str):
        self.basket_page.expect_item_not_in_cart(product_name)
        return self

    @allure.step('Remove the item from the cart')
    def remove_item(self, product_name: str):
        self.basket_page.remove_item(product_name)
        return self

    @allure.step('Count the total price from the cart')
    def get_items_total_price(self) -> float:
        price = self.basket_page.get_items_total_price()
        return price

    @allure.step('Start checkout process')
    def checkout(self):
        self.basket_page.checkout()