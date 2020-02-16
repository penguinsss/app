from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from util import get_driver

#   ❀ 借助sdk家⽬录下的tools⽬录中的uiautomatorviewer.bat进行定位，而该shell脚本和appium共用同一个adb，
# 如果自动化脚本中因异常没有关闭adb服务，那此时进行快照截图的话是会报错的，解决办法：adb kill-server
# 三种定位使用优先级：
#     优先使用：id class
#     其次使用：xpath，需借助text、class、resource-id才可完成

# xpath语句（只需掌握模糊匹配，//：任意节点路径）：
#  1."//*[contains(@text,'text属性值')]"
#  2."//*[contains(@class,'class属性值')]"
#  3."//*[contains(@resource-id,'resource-id属性值')]"

driver = get_driver()

# 1、点击搜索
# driver.find_element_by_id('com.android.settings:id/search').click()

# 3.1 xpath + id组合 点击搜索
search_btn = '//*[contains(@resource-id, "com.android.settings:id/search")]'
driver.find_element_by_xpath(search_btn).click()
sleep(2)

# 2、点击返回
# driver.find_element_by_class_name('android.widget.ImageButton').click()

# 3.2 xpath + class组合 点击返回
search_return_btn = '//*[contains(@class, "android.widget.ImageButton")]'
driver.find_element_by_xpath(search_return_btn).click()
sleep(2)

# 3. 点击更多
more_btn = '//*[contains(@text, "更")]'
driver.find_element_by_xpath(more_btn).click()
sleep(2)

# 定位一组元素id，class，xpath
ids_value = driver.find_elements_by_id('com.android.settings:id/title')
for i in ids_value:
    print(i.text)

print('❀______')

classes_value = driver.find_elements_by_class_name('android.widget.TextView')
for i in classes_value:
    print(i.text)

print('❀______')

xpath_value = '//*[contains(@text, "示")]'
xpaths_value = driver.find_elements_by_xpath(xpath_value)
for i in xpaths_value:
    print(i.text)

# 隐式等待：是等到整个页面加载结束才进行后续操作
# 显示等待：是等待某一个具体的元素成功获取
driver.find_element_by_xpath('//*[contains(@text, "更多")]').click()
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[contains(@text, "飞行模式")]')).click()

driver.quit()
