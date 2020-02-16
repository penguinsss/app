from time import sleep

from util import get_driver

driver = get_driver()

# 1 获取手机分辨率，通常用于swipe方法完成滑动操作
size = driver.get_window_size()
print('分辨率：', size)

width = size.get('width')
height = size.get('height')

# 向下滑动
driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)

sleep(3)
driver.close_app()
# 向右滑动
driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)

sleep(3)
driver.quit()
