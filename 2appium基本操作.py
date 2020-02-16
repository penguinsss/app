import os

from util import get_driver, encode_data, decode_data

driver = get_driver()

"3、app是否已安装"
# is_installed = driver.is_app_installed('com.example.corel.calc')
# # 没安装安装，安装了就卸载
# if is_installed:
#     "2、卸载手机自己安装的app，不能卸载系统的app"
#     driver.remove_app('com.example.corel.calc')
# else:
#     "1、安装apk到手机，支持重复安装进行覆盖，绝对路径"
#     driver.install_app(os.getcwd() + os.sep + 'apk' + os.sep + 'com.example.corel.calc_2.1.1023_11.apk')


"4、将hello写入到手机"
# data = encode_data('文文')
# driver.push_file('/sdcard/abc.txt', data)  # 不指定abc.txt，会生成一个.tmp结尾的临时文件，不便于后续的维护

"5、从手机拉取文件，返回的是base64编码数据"
data = driver.pull_file('/sdcard/abc.txt')
re_data = decode_data(data)
print(re_data)
#
# "6、driver.page_source：获取 当前屏幕 元素结构，返回xml字符串,只是当前屏幕（activity页面内容是xml承载的）"
# with open('./result/page.xml', 'w') as f:
#     f.write(driver.page_source)

driver.quit()


































