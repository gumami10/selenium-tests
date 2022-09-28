from selenium.webdriver.common.by import By


class ZeroBankLocators:
    navigation = By.ID, 'nav'
    onlineBankingMenu = By.ID, 'onlineBankingMenu'
    feedback = By.ID, 'feedback'
    FAQ = By.ID, 'faq-link'
    signin = By.ID, 'signin_button'
    home_img = By.CSS_SELECTOR, "div.item img"
    feedback_name = By.ID, 'name'
    feedback_email = By.ID, 'email'
    feedback_subject = By.ID, 'subject'
    feedback_questions = By.ID, 'comment'
    feedback_send = By.NAME, 'submit'
    feedback_successful_send_label = By.XPATH, "//div[contains(text(), 'Thank you for your comments')]"
