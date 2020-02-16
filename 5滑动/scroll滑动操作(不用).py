import time

from util import get_driver

# scroll(origin_el, destination_el, duration=None)
# 滑动相对随机，不用

driver = get_driver()

save = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")

# 无滑动时间
driver.scroll(save, wlan)
# 有滑动时间2s
# driver.scroll(save, wlan, 200)

# 关闭
time.sleep(2)
driver.quit()
