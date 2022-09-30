import os
from datetime import time

from Python_selenium1 import my_logger


def take_screenshot(self):
    file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
    rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screen_name = file_path + rq + '.png'
    try:
        self.driver.get_screenshot_as_file(screen_name)
        my_logger.info("开始截图并保存")

    except Exception as e:
        my_logger.error("出现异常", format(e))