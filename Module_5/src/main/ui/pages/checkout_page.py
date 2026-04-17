from playwright.sync_api    import Page, expect

from Module_5.src.main.ui.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = page.get_by_role('textbox', name='First Name')
        self.last_name = page.get_by_role('textbox', name='Last Name')
        self.postal_code = page.get_by_role('textbox', name='Zip/Postal Code')
        self.continue_button = page.get_by_role('button', name='Continue')
        self.finish_button = page.get_by_role('button', name='Finish')
        self.item_total = page.locator('.summary_subtotal_label')
        self.success_message = page.locator('.complete-header')
        self.error_message = page.locator('.error-message-container')

    def step_one_checkout(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def step_two_checkout(self):
        self.finish_button.click()

    def get_items_total_price(self) -> float:
        expect(self.item_total).to_be_visible()
        total = self.item_total.inner_text()
        return float(total.replace('Item total: $', ''))

    def get_success_text(self) -> str:
        return self.success_message.inner_text()

    def get_error_text(self) -> str:
        return self.error_message.inner_text()