from tests.config.driver import TestCase
from tests.mystore.pages.MyStore import MyStore


class CartTest(TestCase):

    def test_add_product_to_cart(self):
        mystore = MyStore(self.driver)
        mystore.search_product_on_top_bar('dress')
        mystore.add_first_item_to_card()
        mystore.continue_shopping()
        self.assertTrue(mystore.verify_n_items_in_cart(1))

    def test_redirect_to_checkout(self):
        mystore = MyStore(self.driver)
        mystore.search_product_on_top_bar('dress')
        mystore.add_first_item_to_card()
        mystore.continue_shopping()
        mystore.go_to_checkout_by_cart_header()

        self.assertTrue(mystore.verify_is_in_checkout())

    def test_exclude_item_from_cart(self):
        mystore = MyStore(self.driver)
        mystore.search_product_on_top_bar('dress')
        mystore.add_first_item_to_card()
        mystore.continue_shopping()
        mystore.exclude_cart_item()

        self.assertTrue(mystore.verify_cart_is_empty())