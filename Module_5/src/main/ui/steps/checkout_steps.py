import allure
from playwright.sync_api import Page

from Module_5.src.main.ui.pages.checkout_page import CheckoutPage


class CheckoutSteps:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_page = CheckoutPage(page)

    @allure.step('Fill the required fields and continue process')
    def step_one_checkout(self, first_name, lst_name, postal_code):
        self.checkout_page.step_one_checkout(first_name, lst_name, postal_code)
        return self

    @allure.step('Count the total price from checkout')
    def get_items_total_price(self) -> float:
        price = self.checkout_page.get_items_total_price()
        return price

    @allure.step('Finish the checkout process')
    def step_two_checkout(self):
        self.checkout_page.step_two_checkout()

    @allure.step('Get the text after successful checkout')
    def get_success_text(self) -> str:
        return self.checkout_page.get_success_text()

    @allure.step('Get the text after unsuccessful checkout')
    def get_error_text(self) -> str:
        return self.checkout_page.get_error_text()