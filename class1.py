import unittest
#Import other modules that are required for testing

class SearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.FireFox()
    
        self.driver.get("http://www.lambdatest.com")
    
    def tearDown(self):
        self.driver.quit()