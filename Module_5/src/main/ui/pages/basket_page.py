from playwright.sync_api import Page, expect

from Module_5.src.main.ui.pages.base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart = page.locator('#shopping_cart_container')
        self.cart_items = page.locator('.cart_item')
        self.checkout_button = page.get_by_role('button', name='Checkout')

    def open_cart(self):
        self.cart.click()

    def checkout(self):
        self.checkout_button.click()

    def get_item_names(self) -> list[str]:
        return self.cart_items.locator('.inventory_item_name').all_text_contents()

    def expect_item_in_cart(self, item_name: str):
        item = self.cart_items.locator('.inventory_item_name').filter(has_text=item_name)
        expect(item).to_be_visible()

    def expect_item_not_in_cart(self, item_name: str):
        item = self.cart_items.locator('.inventory_item_name').filter(has_text=item_name)
        expect(item).not_to_be_visible()

    def remove_item(self, item_name: str):
        item = self.cart_items.filter(has_text=item_name)
        item.get_by_role('button').click()

    def get_item_prices(self):
        prices = self.cart_items.locator('.inventory_item_price').all_text_contents()
        return [float(p.replace('$', '')) for p in prices]

    def get_items_total_price(self) -> float:
        return sum(self.get_item_prices())