from tests.config.driver import TestCase
from tests.zerobank.pages.ZeroBank import ZeroBank


class NavigationTest(TestCase):

    def test_verify_navigation_on_home(self):
        zerobank = ZeroBank(self.driver)
        self.assertTrue(zerobank.verify_navigation())

    def test_verify_navigation_on_online_banking(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_online_banking()
        self.assertTrue(zerobank.verify_navigation())

    def test_verify_navigation_on_feedback(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        self.assertTrue(zerobank.verify_navigation())

    def test_verify_navigation_on_FAQ(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        zerobank.navigate_to_faq()
        self.assertTrue(zerobank.verify_navigation())

    def test_verify_navigation_on_Login(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_signin()
        self.assertTrue(zerobank.verify_navigation())

