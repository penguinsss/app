from util import get_driver

driver = get_driver()

# search = driver.find_element_by_id('com.android.settings:id/search')
# search.click()
# search_input = driver.find_element_by_id('android:id/search_src_text')
# # 输入中文时，需要添加启动参数支持
# search_input.send_keys('文')
# search_input.clear()
# search_input.send_keys('星魂')

# 获取元素id class text content-desc的属性值:
# get_attribute(value):
#     value = name -> 返回content-desc或text
#     value = text -> 返回text
#     value = className -> 返回class，只有API>=18（Android4.3）才能支持
#     value = resourceId -> 返回resource_id，只有API>=18才能支持

# print('resource_id:', search.get_attribute('resourceId'))
# print('class:', search.get_attribute('className'))
# print('content_desc:', search.get_attribute('name'))

# 应用场景：只是想滑动轮播图，并不想整个页面滑动
more_btn = '//*[contains(@text, "更")]'
more = driver.find_element_by_xpath(more_btn)
# 1 获取元素屏幕坐标
print('坐标：', more.location)
# 2 获取元素大小
print('宽和高：', more.size)


# 获取包命和启动名
print('包命：', driver.current_package)
print('启动名：', driver.current_activity)

driver.quit()
