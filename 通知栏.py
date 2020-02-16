from appium import webdriver
import time

from util import get_driver

driver = get_driver()

# 打开通知栏
driver.open_notifications()
time.sleep(5)
# 点击横幅 id
driver.find_element_by_id("com.android.systemui:id/header").click()

# 点击设置按钮 id
time.sleep(1) # 防止设置按钮没有展示出来
driver.find_element_by_id("com.android.systemui:id/settings_button").click()

time.sleep(2) # 防止app还没有启动成功
# 获取app包名 启动名
print("包名:", driver.current_package)
print("启动名:", driver.current_activity)

time.sleep(2)
driver.quit()
