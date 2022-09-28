from tests.config.driver import TestCase
from tests.mystore.locators.locators import MyStoreLocators
from tests.mystore.pages.MyStore import MyStore


class ContactFormTest(TestCase):

    def test_success_sending_form(self):
        mystore = MyStore(self.driver)
        mystore.navigate_to_contact()
        mystore.choose_subject(MyStoreLocators.contact_form_id_contact_value_webmaster)
        mystore.fill_email('eric@gmail.com')
        mystore.fill_order_reference('1234567')
        mystore.fill_message('Hello World')
        mystore.upload_attach_file()
        mystore.send_contact_form()
        self.assertTrue(mystore.verify_send_successfully)

    def test_failed_missing_email(self):
        mystore = MyStore(self.driver)
        mystore.navigate_to_contact()
        mystore.choose_subject(MyStoreLocators.contact_form_id_contact_value_webmaster)
        mystore.fill_order_reference('1234567')
        mystore.fill_message('Hello World')
        mystore.send_contact_form()
        self.assertTrue(mystore.verify_not_send())

    def test_failed_missing_order(self):
        mystore = MyStore(self.driver)
        mystore.navigate_to_contact()
        mystore.choose_subject(MyStoreLocators.contact_form_id_contact_value_webmaster)
        mystore.fill_email('eric@gmail.com')
        mystore.fill_message('Hello World')
        mystore.send_contact_form()
        self.assertTrue(mystore.verify_not_send())

    def test_failed_missing_subject(self):
        mystore = MyStore(self.driver)
        mystore.navigate_to_contact()
        mystore.fill_email('eric@gmail.com')
        mystore.fill_message('Hello World')
        mystore.fill_order_reference('1234567')
        mystore.send_contact_form()
        self.assertTrue(mystore.verify_not_send())

    def test_failed_missing_message(self):
        mystore = MyStore(self.driver)
        mystore.navigate_to_contact()
        mystore.fill_email('eric@gmail.com')
        mystore.choose_subject(MyStoreLocators.contact_form_id_contact_value_webmaster)
        mystore.fill_order_reference('1234567')
        mystore.send_contact_form()
        self.assertTrue(mystore.verify_not_send())

    def test_failed_invalid_email(self):
        mystore = MyStore(self.driver)
        mystore.navigate_to_contact()
        mystore.choose_subject(MyStoreLocators.contact_form_id_contact_value_webmaster)
        mystore.fill_email('invalid')
        mystore.fill_message('Hello World')
        mystore.fill_order_reference('1234567')
        mystore.send_contact_form()
        self.assertTrue(mystore.verify_not_send())