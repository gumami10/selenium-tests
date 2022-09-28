import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

timeout = 8


class TestCase(unittest.TestCase):

    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()),
                                       options=options)
        self.driver.implicitly_wait(timeout)
        self.driver.maximize_window()

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

