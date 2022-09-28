from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.config.driver import timeout
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)).click()

    def click_on_nth_child(self, by_locator, position):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)).click()
        self.driver.find_elements(*by_locator)[position].click()

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def hover(self, by_locator):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
        el = self.driver.find_element(*by_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(el)
        return actions.perform()

    def return_text(self, by_locator):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)).text

    def return_if_exists(self, by_locator):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return len(self.driver.find_elements(*by_locator)) > 0
        except TimeoutException:
            return False

    def return_element_size(self, by_locator):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return self.driver.find_element(*by_locator).size
        except TimeoutException:
            return False

    def return_element_css_property(self, by_locator, css_property):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return self.driver.find_element(*by_locator).value_of_css_property(css_property)
        except TimeoutException:
            return False

    def return_elements_text(self, by_locator):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            elements = self.driver.find_elements(*by_locator)
            texts = []
            for el in elements:
                texts.append(el.text)
            return texts
        except TimeoutException:
            return False

