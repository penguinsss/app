"""短信发送和删除：
 1.新建短信
 2.输⼊⼿机号码
 3.发送三个内容
 123
 hello
 appium
 4.⻓按hello
 5.点击删除
 6.点击确认删除
 7.判断hello删除成功"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {'platformName': 'android',    # 测试平台
                'platformVersionName': '5.1',    # 测试版本，不写自动会去获取手机版本
                'deviceName': 'sanxing',   # 设备名字，可以随便去写，但是不能为空
                'appPackage': 'com.android.mms',
                'appActivity': '.ui.ConversationList',
                'unicodeKeyboard': True}
# 接口地址：wd是webdriver的简写，hub代表一个中心节点
# 声明手机驱动对象  结果：启动启动参数指定app，创建session，session相当于服务端的driver（脚本中叫driver），即一个session就是一个driver，一个session就是某一个app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 新建短信
driver.find_element_by_id("com.android.mms:id/action_compose_new").click()
# 输入手机号码
driver.find_element_by_id("com.android.mms:id/recipients_editor").send_keys('1')

msg_edit = driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
send = driver.find_element_by_id("com.android.mms:id/send_button_sms")
for i in ['a', 's', 'd']:
    msg_edit.send_keys(i)
    send.click()

del_msg = driver.find_element_by_xpath('//*[contains(@text, "s")]')
TouchAction(driver).long_press(del_msg).release().perform()

driver.find_element_by_xpath('//*[contains(@text, "删除")]').click()
driver.find_element_by_id("android:id/button1").click()

# 判断s删除成功
results = driver.find_elements_by_id("com.android.mms:id/text_view")
list_res = [i.text for i in results]
print(list_res)
if "hello" not in list_res:
    print("删除成功")
else:
    print("删除失败")