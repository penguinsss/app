from util import get_driver

driver = get_driver()
# 1 点击搜索
driver.find_element_by_id('com.android.settings:id/search').click()
# 数据
search_text = [{'key': '1', 'res': '休眠'}, {'key': 'm', 'res': 'MAC地址'}, {'key': 'w', 'res': 'WPS按钮'}]
# 2 定位输入框
search_input = driver.find_element_by_id('android:id/search_src_text')
for i in search_text:
    search_input.clear()
    search_input.send_keys(i.get('key'))
    ele_list = driver.find_elements_by_id('com.android.settings:id/title')
    res_list = []
    for j in ele_list:
        res_list.append(j.text)
    if i.get('res') in res_list:
        print('搜索成功')
    else:
        print('搜索失败')

driver.quit()














