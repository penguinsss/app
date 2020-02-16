import time

from util import get_driver

driver = get_driver()

time.sleep(2)
# 模拟点击手机返回按钮
driver.keyevent(4)


# # 模拟音量键 3次 +
# for i in range(3):
#     driver.keyevent(24)
#
# # 模拟音量键 3次 -
# for i in range(3):
#     driver.keyevent(25)

time.sleep(2)
driver.quit()
