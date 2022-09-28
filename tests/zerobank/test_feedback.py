from tests.config.driver import TestCase
from tests.zerobank.pages.ZeroBank import ZeroBank


class FeedbackTest(TestCase):

    def test_send_without_any_fields(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        zerobank.send_feedback()
        self.assertFalse(zerobank.verify_feedback_send())

    def test_send_with_invalid_email(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        zerobank.type_feedback_name("eric groppe")
        zerobank.type_feedback_email("eric")
        zerobank.type_feedback_subject("subject")
        zerobank.type_feedback_questions("questions")

        zerobank.send_feedback()
        self.assertFalse(zerobank.verify_feedback_send())

    def test_send_without_email(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        zerobank.type_feedback_name("eric groppe")
        zerobank.type_feedback_subject("subject")
        zerobank.type_feedback_questions("questions")

        zerobank.send_feedback()
        self.assertFalse(zerobank.verify_feedback_send())


    def test_send_without_name(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        zerobank.type_feedback_email("eric@eric.com")
        zerobank.type_feedback_subject("subject")
        zerobank.type_feedback_questions("questions")

        zerobank.send_feedback()
        self.assertFalse(zerobank.verify_feedback_send())

    def test_send_without_subject(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        zerobank.type_feedback_name("eric groppe")
        zerobank.type_feedback_email("eric@eric.com")
        zerobank.type_feedback_questions("questions")

        zerobank.send_feedback()
        self.assertFalse(zerobank.verify_feedback_send())

    def test_send_without_questions(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        zerobank.type_feedback_name("eric groppe")
        zerobank.type_feedback_email("eric@eric.com")
        zerobank.type_feedback_subject("subject")

        zerobank.send_feedback()
        self.assertFalse(zerobank.verify_feedback_send())

    def test_send_successfully(self):
        zerobank = ZeroBank(self.driver)
        zerobank.navigate_to_feedback()
        zerobank.type_feedback_name("eric groppe")
        zerobank.type_feedback_email("eric@eric.com")
        zerobank.type_feedback_subject("subject")
        zerobank.type_feedback_questions("questions")

        zerobank.send_feedback()
        self.assertTrue(zerobank.verify_feedback_send())