import time
import unittest

from selenium.webdriver.common.by import By

from framework.browser_engine import BrowserEngine


class BaiduSearch(unittest.TestCase):


    def setUp(self):

        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)


    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element(by=By.ID, value='kw').send_keys('selenium')
        time.sleep(1)
        self.driver.find_element(by=By.ID, value='su').click()
        time.sleep(5)
        try:
            assert 'selenium' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

if __name__ == '__main__':
    unittest.main()