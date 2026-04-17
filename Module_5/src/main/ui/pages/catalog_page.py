from playwright.sync_api    import Page

from Module_5.src.main.ui.pages.base_page import BasePage
from Module_5.src.main.ui.utils.constants import Urls


class CatalogPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.menu_button = page.get_by_role('button', name='Open Menu')
        self.logout_button = page.get_by_role('link', name='Logout')
        self.login_button = page.get_by_role('button', name='Login')
        self.inventory_item = page.locator('.inventory_item')
        self.sort_select = page.locator('.product_sort_container')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.cart = page.locator('#shopping_cart_container')

    def open(self):
        self.page.goto(Urls.BASE)

    def login(self, username: str, password: str):
        self.open()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.menu_button.click()
        self.logout_button.click()

    def sort_items(self, option: str):
        self.sort_select.select_option(option)

    def add_to_cart(self, item_name: str):
        item = self.inventory_item.filter(has_text=item_name)
        button = item.get_by_role('button')
        if button.inner_text() == 'Add to cart':
            button.click()
        return button

    def remove_from_cart(self, item_name: str):
        item = self.inventory_item.filter(has_text=item_name)
        button = item.get_by_role('button')
        if button.inner_text() == 'Remove':
            button.click()
        return button

    def get_items_count(self) -> int:
        return self.inventory_item.count()

    def get_items_name(self) -> list[str]:
        return self.inventory_item.locator('.inventory_item_name').all_text_contents()

    def get_items_price(self) -> list[float]:
        prices = self.inventory_item.locator('.inventory_item_price').all_text_contents()
        return [float(p.replace('$', '')) for p in prices]

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def get_product_details(self, item_name: str):
        item = self.inventory_item.filter(has_text=item_name)
        name = item.locator('.inventory_item_name').inner_text()
        price_text = item.locator('.inventory_item_price').inner_text()
        price = float(price_text.replace('$', ''))

        item.locator('.inventory_item_name').click()
        details_name = self.page.locator('.inventory_details_name').inner_text()
        details_price_text = self.page.locator('.inventory_details_price').inner_text()
        details_price = float(details_price_text.replace('$', ''))

        self.page.go_back()

        return name, price, details_name, details_price

