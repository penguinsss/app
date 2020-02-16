import time

from util import get_driver

# drag_and_drop(origin_el, destination_el):从⼀个元素滑动到另⼀个元素,起点元素最终会替代终点元素原本屏幕上的位置

driver = get_driver()

save = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")

driver.drag_and_drop(save, wlan)

# 关闭
time.sleep(2)
driver.quit()
