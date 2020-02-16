from time import sleep

from appium.webdriver.common.touch_action import TouchAction


# appium版本 1.12
#   move_to：绝对坐标
# appium版本 1.7之前
#   move_to：相对坐标
from util import get_driver

driver = get_driver()
bat = driver.find_element_by_xpath("//*[contains(@text,'电池')]")
wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")

driver.drag_and_drop(bat, wlan)
driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
sleep(2)
driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()

sleep(2)

TouchAction(driver).press(x=234, y=850).wait(100).move_to(x=723, y=850).wait(100) \
    .move_to(x=723, y=1326).wait(100).move_to(x=234, y=1808).release().perform()

sleep(2)
driver.quit()