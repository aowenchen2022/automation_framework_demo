import time
from selenium import webdriver
from framework.logger import Logger
my_logger = Logger(logger='test_log').getlog()

class TestMyLog(object):

    def print_log(self):
        driver = webdriver.Chrome()
        my_logger.info("打开浏览器")
        driver.maximize_window()
        my_logger.info("最大化浏览器窗口。")
        driver.implicitly_wait(8)

        dr = webdriver.Chrome()
        dr.get("https://www.baidu.com")
        my_logger.info("打开百度首页。")
        time.sleep(1)
        my_logger.info("暂停一秒。")
        driver.quit()
        my_logger.info("关闭并退出浏览器。")


test_log = TestMyLog()
test_log.print_log()
