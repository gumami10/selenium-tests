
from tests.config.driver import TestCase
from tests.zerobank.pages.ZeroBank import ZeroBank


class MobileResponsiveness(TestCase):

    def test_send_without_any_fields(self):
        zerobank = ZeroBank(self.driver)
        zerobank.adjust_screen_size_mobile()
        self.assertTrue(zerobank.verify_image_does_not_have_fixed_size())

