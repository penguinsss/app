from util import get_driver, encode_data, decode_data

driver = get_driver()
with open('./hello.txt') as f:
    msg = f.read()
data = encode_data(msg)
driver.push_file('/sdcard/data.txt', data)

data = driver.pull_file('/sdcard/data.txt')
re_data = decode_data(data)
with open('./app.txt', 'w') as f:
    f.write(re_data)

driver.quit()
