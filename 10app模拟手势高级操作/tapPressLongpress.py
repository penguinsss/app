from time import sleep

from appium.webdriver.common.touch_action import TouchAction

from util import get_driver

driver = get_driver()

wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
touch_action = TouchAction(driver)

"""1 手指轻敲操作：模拟⼿指轻敲⼀下屏幕操作"""
# TouchAction(driver).tap(wlan).perform()  # 元素方式
# touch_action.tap(x=wlan.location.get('x'), y=wlan.location.get('y')).perform() # 坐标方式

"""2 ⼿指按操作：: 模拟⼿指按下屏幕，然后松开"""
# touch_action.press(wlan).release().perform()  # 元素方式
# touch_action.press(x=wlan.location.get('x'), y=wlan.location.get('y')).perform() # 坐标方式
#
# """3 等待操作：wait(ms=0)"""
# # 方式一：press + wait
wlan.click()
sleep(3)
ssid = driver.find_element_by_xpath("//*[contains(@text,'SSID')]")
# # 添加等待(有⻓按)／不添加等待(⽆⻓按效果)
touch_action.press(ssid).wait(2000).release().perform()
#
# # 方式二：long_press
# touch_action.long_press(ssid).release().perform()  # 元素方式
# touch_action.long_press(x=ssid.location.get('x'), y=wlan.location.get('y')).release().perform()  # 坐标方式


sleep(2)
driver.quit()