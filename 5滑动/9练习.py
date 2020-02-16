from util import get_driver

driver = get_driver()

size = driver.get_window_size()
width = size.get('width')
height = size.get('height')
driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)

driver.find_element_by_xpath('//*[contains(@text,"位置信息")]').click()
driver.find_element_by_xpath('//*[contains(@text, "模式")]').click()
driver.find_element_by_xpath('//*[contains(@text, "使用WLAN")]').click()
driver.find_element_by_class_name('android.widget.ImageButton').click()
result = driver.find_elements_by_id('android:id/summary')

if '耗电量低' in [i.text for i in result]:
    print('成功')
else:
    print('失败')
