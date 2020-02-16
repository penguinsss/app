from time import sleep

from util import get_driver

driver = get_driver()
sleep(1)

# 模拟热启动
# 将设置app放置后台5s，在此期间，点击桌面应用无效，因为它并没有运行结束，而是在后台运行
driver.background_app(5)

# 点击桌面图库 -不会点击 因为防止后台代码没有运行完成
# driver.find_element_by_xpath("//*[contains(@text,'图库')]").click()

driver.quit()
