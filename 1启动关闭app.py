from time import sleep

from util import get_driver

driver = get_driver()

sleep(2)

# 1、关闭app，但不关闭驱动对象
# driver.close_app()
# 2、关闭app 同时关闭手机驱动对象
# driver.quit()

# 方式一关闭，短信可以启动
# 方式二关闭，报错
driver.start_activity('com.android.mms', '.ui.ConversationList')

# 当有多个app，close_app()关闭的是driver启动参数中的那个app，即设置
driver.close_app()
