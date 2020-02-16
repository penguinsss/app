from time import sleep

from appium.webdriver.common.touch_action import TouchAction

from util import get_driver

driver = get_driver()

save = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
more = driver.find_element_by_xpath("//*[contains(@text,'更多')]")

touch_action = TouchAction(driver)  # 手势操作类

# 滑动方式一：press(元素).move_to(元素)  滑动距离很长
# touch_action.press(save).move_to(more).release().perform()
# 滑动方式二：press(坐标).move_to(坐标)  滑动距离很长
# touch_action.press(x=save.location.get('x'), y=save.location.get('y')).move_to(x=more.location.get('x'),
#                                                                                y=more.location.get(
#                                                                                    'y')).release().perform()
# 滑动方式三：long_press(元素).move_to(坐标)  精准滑动，drag_and_drop底层实现方式
touch_action.long_press(save).move_to(x=more.location.get("x"), y=more.location.get("y"))\
 .release().perform()

sleep(2)
driver.quit()

# appium版本1.12
#  move_to：绝对坐标
#  A(xa,ya) -> B(xb,yb)
#  案例：
#  press(xa,ya).move_to(xb,yb)
# appium1.7.2之前版本
#  move_to:相对坐标
#  A(xa,ya) -> B(xb,yb)
#  案例：
#  press(xa,ya).move_to(xb-xa,yb-ya)
