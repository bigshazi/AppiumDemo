# encoding=utf-8

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

#server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
# desired_capabilities = {
#     'platformName': 'Android',
#     'driverName': '127.0.0.1:62001',          # 需替换成你的driverName
#     'platformVersion': '5.1.1',
#     'appPackage': 'com.android.settings',
#     'appActivity': '.Settings'
# }

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.taobao.aliAuction', # 启动APP Package名称
  'appActivity': 'com.taobao.aliauction.appmodule.activity.MainActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}
driver = webdriver.Remote(server, desired_caps)
wdw = WebDriverWait(driver, 10, 1)
# 点击搜索
serach = wdw.until(lambda x:x.find_element_by_xpath("//*[contains(@content-desc, '搜索')]"))
serach.click()
# 输入搜索内容
serach_text = wdw.until(lambda x : x.find_element_by_id("android:id/search_src_text"))
serach_text.send_keys("设置")

# 清空搜索内容
serach_text.clear()
time.sleep(3)

driver.quit()