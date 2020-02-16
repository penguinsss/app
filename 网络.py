from appium import webdriver
import time

from util import get_driver

driver = get_driver()

# 打印手机网络状态
# driver.network_connection返回值：
#  0：没有⼿机卡
#  1: ⻜⾏模式
#  2: Wi-Fi模式
#  4: 数据⽹络 2g 3g 4g 5g
#  6: wifi+数据
print("当前网络为:", driver.network_connection)

# 修改手机网络 data
driver.set_network_connection(4)
# 打印手机网络状态
print("当前网络为:", driver.network_connection)

# 修改手机网络
driver.set_network_connection(2)
# 打印手机网络状态
print("当前网络为:", driver.network_connection)

# 修改手机网络
driver.set_network_connection(1)
# 打印手机网络状态
print("当前网络为:", driver.network_connection)


time.sleep(2)
driver.quit()
