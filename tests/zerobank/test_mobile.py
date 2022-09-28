
from tests.config.driver import TestCase
from tests.zerobank.pages.ZeroBank import ZeroBank


class MobileResponsiveness(TestCase):

    def test_home_image_doesnt_have_fixed_properties(self):
        zerobank = ZeroBank(self.driver)
        zerobank.adjust_screen_size_mobile()
        self.assertTrue(zerobank.verify_image_does_not_have_fixed_size())

