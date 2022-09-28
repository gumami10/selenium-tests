from tests.config.BasePage import BasePage
from tests.zerobank.locators.locators import ZeroBankLocators


class ZeroBank(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://zero.webappsecurity.com/')

    def adjust_screen_size_mobile(self):
        self.driver.set_window_size(375, 667)

    def verify_navigation(self):
        return self.return_if_exists(ZeroBankLocators.navigation)

    def verify_feedback_send(self):
        flag = self.return_if_exists(ZeroBankLocators.feedback_send)
        return not flag

    def verify_image_does_not_have_fixed_size(self):
        if self.return_element_css_property(ZeroBankLocators.home_img, 'width') or self.return_element_css_property(ZeroBankLocators.home_img, 'height'):
            return False
        return True

    def navigate_to_online_banking(self):
        return self.click(ZeroBankLocators.onlineBankingMenu)

    def navigate_to_feedback(self):
        return self.click(ZeroBankLocators.feedback)

    def navigate_to_faq(self):
        return self.click(ZeroBankLocators.FAQ)

    def navigate_to_signin(self):
        return self.click(ZeroBankLocators.signin)

    def send_feedback(self):
        return self.click(ZeroBankLocators.feedback_send)

    def type_feedback_email(self, email):
        return self.enter_text(ZeroBankLocators.feedback_email, email)

    def type_feedback_name(self, name):
        return self.enter_text(ZeroBankLocators.feedback_name, name)

    def type_feedback_subject(self, subject):
        return self.enter_text(ZeroBankLocators.feedback_subject, subject)

    def type_feedback_questions(self, questions):
        return self.enter_text(ZeroBankLocators.feedback_questions, questions)