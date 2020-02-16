import base64

from appium import webdriver


# 输⼊⽂本内容到⼿机，中文输入支持：
#   1 使用Unicode键盘：'unicodeKeyboard': True
#   2 重置键盘：'resetKeyboard': True

def get_driver():
    # 启动参数
    desired_caps = {'platformName': 'android',    # 测试平台
                    'platformVersionName': '5.1',    # 测试版本，不写自动会去获取手机版本
                    'deviceName': 'sanxing',   # 设备名字，可以随便去写，但是不能为空
                    'appPackage': 'com.android.settings',
                    'appActivity': '.Settings',
                    'unicodeKeyboard': True}
    # 接口地址：wd是webdriver的简写，hub代表一个中心节点
    # 声明手机驱动对象  结果：启动启动参数指定app，创建session，session相当于服务端的driver（脚本中叫driver），即一个session就是一个driver，一个session就是某一个app
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


# base64编码
def encode_data(value_arg):
    return str(base64.b64encode(value_arg.encode('utf-8')), 'utf-8')


# base64解码
def decode_data(data):
    return str(base64.b64decode(data), 'utf-8')
