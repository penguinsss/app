from appium import webdriver
import time

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

from util import get_driver

driver = get_driver()

# 截图
driver.get_screenshot_as_file("{}.png".format(int(time.time())))

time.sleep(2)
driver.quit()
