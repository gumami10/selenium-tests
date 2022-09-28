from tests.config.driver import TestCase
from tests.mystore.pages.MyStore import MyStore


class SearchTest(TestCase):

    def test_verify_keyword_on_searched_products(self):
        mystore = MyStore(self.driver)
        mystore.search_product_on_top_bar('dress')
        self.assertTrue(mystore.verify_all_products_contain_keyword('dress'))