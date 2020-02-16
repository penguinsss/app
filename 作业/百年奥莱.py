"""百年奥莱
 完成百年奥莱app登录和退出操作
 ⾸⻚-我
 登录选择⻚⾯-已有账号，去登录
 登录⻚⾯-登录操作
 个⼈中⼼-判断登录成功
 个⼈中⼼-点击设置
 设置⻚⾯-向上滑动
 点击退出
 点击确认退出
 判断-退出成功
 点击我-判断⻚⾯"""
import time

from appium import webdriver
# server 启动参数
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.yunmall.lc'
desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def wait_ele(ty, value):
    """
    定位元素
    :param ty: 定位类型 id class xpath
    :param value: 定位类型属性值
    :return: 定位对象
    """
    if ty == "id":
        return WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_id(value))
    if ty == "xpath":
        return WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath(value))
    if ty == "class":
        return WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_class_name(value))


# 更新弹窗 id com.yunmall.lc:id/img_close
wait_ele("id", "com.yunmall.lc:id/img_close").click()
# 首页-我 id com.yunmall.lc:id/tab_me
wait_ele("id", "com.yunmall.lc:id/tab_me").click()
# 登录选择页面-已有账号，去登录 id com.yunmall.lc:id/textView1
wait_ele("id", "com.yunmall.lc:id/textView1").click()
# 登录页面-登录操作
# 用户名 id com.yunmall.lc:id/logon_account_textview
wait_ele("id", "com.yunmall.lc:id/logon_account_textview").send_keys("13488834010")
# 密码 ID com.yunmall.lc:id/logon_password_textview
wait_ele("id", "com.yunmall.lc:id/logon_password_textview").send_keys("159357li")
# 登录按钮 id com.yunmall.lc:id/logon_button
wait_ele("id", "com.yunmall.lc:id/logon_button").click()
# 个人中心-用户名 id  com.yunmall.lc:id/tv_user_nikename
name = wait_ele("id", "com.yunmall.lc:id/tv_user_nikename").text
if name == "mlili":
    print("登录成功")
# 个人中心-点击设置 ID com.yunmall.lc:id/ymtitlebar_left_btn_image
wait_ele("id", "com.yunmall.lc:id/ymtitlebar_left_btn_image").click()
# 设置页面-向上滑动
# 等待时间
time.sleep(2)
# 分辨率
size = driver.get_window_size()
# 宽
width = size.get("width")
# 高
height = size.get("height")
# 高*80%,宽*50% ->高*20%,宽*50%
driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2)

# 点击退出 ID com.yunmall.lc:id/setting_logout
wait_ele("id", "com.yunmall.lc:id/setting_logout").click()
# 点击确认退出 id com.yunmall.lc:id/ymdialog_right_button
wait_ele("id", "com.yunmall.lc:id/ymdialog_right_button").click()
# 判断-退出成功
#     点击我
wait_ele("id", "com.yunmall.lc:id/tab_me").click()
#     判断页面
#     获取手机号注册 id com.yunmall.lc:id/register_button
data = wait_ele("id", "com.yunmall.lc:id/register_button").text
if data == "手机号注册":
    print("退出成功")

# 退出
driver.quit()
