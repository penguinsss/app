import time

from util import get_driver

# swipe(start_x, start_y, end_x, end_y, duration=None)，duration单位ms
# 作用：
#   1 滑动没有持续时间，滑动相对随机，随机距离不远
#   2 滑动持续在2s左右时，滑动相对准确  --最常用
#   3 滑动持续为几十毫秒时，会产生点击起点位置操作
# 实际开发中，由于scoll和drag_and_drop兼容性差，所以百分之九十以上都会采用swipe滑动

driver = get_driver()

save = driver.find_element_by_xpath("//*[contains(@text,'存储')]").location
wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").location

# driver.swipe(save.get("x"), save.get("y"), wlan.get("x"), wlan.get("y"))

# 有滑动时间，滑动相对准确 最少2s
driver.swipe(save.get("x"), save.get("y"), wlan.get("x"), wlan.get("y"), 2000)

# 有滑动时间，滑动相对较长 最少200ms  但如果时几十毫秒，会产生点击起点位置操作
# driver.swipe(save.get("x"), save.get("y"), wlan.get("x"), wlan.get("y"), 200)

# 关闭
time.sleep(2)
driver.quit()
