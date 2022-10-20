import time
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import os.path

# create a logger instance
from selenium.webdriver.support.wait import WebDriverWait

from framework.logger import Logger

logger = Logger(logger="BasePage").getlog()





class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def is_displayed(element):
        value = element.is_displayed()
        return value

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info('Sleep for %d seconds' % seconds)

    def quit_browser(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    def find_element(self, selector):
        by = selector[0]
        value = selector[1]
        element = None
        if by in ['id', 'name', 'class', 'xpath', 'link']:
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link(value)
                else:
                    logger.error('No find the element')
                logger.info("Had find the element! , by %s via value: %s" % (by, value))
                return element
            except NoSuchElementException as e:
                logger.error("NoSuchElementException %s" % e)
                self.get_windows_img()
        else:
            logger.error("please enter a valid type of element")

    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type: %s" % text)
        except BaseException as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
