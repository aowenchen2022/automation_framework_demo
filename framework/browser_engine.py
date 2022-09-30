import configparser
import os.path
from selenium import webdriver

from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")#获取浏览器类型、名字
        logger.info("You had select %s browser." % browser)  #日志打印你选择的浏览器
        url = config.get("testServer", "URL") #获取测试的URL地址
        logger.info("The test server url is: %s" % url) #日志打印测试的URL地址

        #判断你所选择的浏览器
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)#初始化一个实例
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)#访问URL
        logger.info("Open url: %s" % url)
        driver.maximize_window()  #将窗口放大
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        print(driver)
        return driver

    #关闭浏览器
    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()