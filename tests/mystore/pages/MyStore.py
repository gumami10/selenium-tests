from tests.config.BasePage import BasePage
from tests.mystore.locators.locators import MyStoreLocators
import time


class MyStore(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://automationpractice.com/')

    def search_product_on_top_bar(self, product):
        self.enter_text(MyStoreLocators.search_bar, product)
        self.click(MyStoreLocators.submit_search)

    def verify_all_products_contain_keyword(self, keyword):
        texts = self.return_elements_text(MyStoreLocators.products_result_search_title)
        for text in texts:
            if not text.lower().__contains__(keyword):
                return False
        return True

    def add_first_item_to_card(self):
        self.hover(MyStoreLocators.products_result_search_title)
        self.click_on_nth_child(MyStoreLocators.add_to_cart, 0)

    def continue_shopping(self):
        self.click(MyStoreLocators.continue_to_shopping)

    def go_to_checkout_by_cart_header(self):
        self.hover(MyStoreLocators.cart_header_quantity)
        self.click(MyStoreLocators.checkout_header_cart)

    def verify_n_items_in_cart(self, number):
        return number == int(self.return_text(MyStoreLocators.cart_header_quantity))

    def verify_is_in_checkout(self):
        return self.return_if_exists(MyStoreLocators.cart_summary)

    def exclude_cart_item(self):
        self.hover(MyStoreLocators.cart_header_quantity)
        self.click(MyStoreLocators.header_cart_remove_item)

    def verify_cart_is_empty(self):
        return self.return_if_exists(MyStoreLocators.header_cart_no_item)







