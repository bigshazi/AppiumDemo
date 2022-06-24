# encoding=utf-8

from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'driverName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '10',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
driver.find_element("com.android.settings:id/title").click()  # 点击wlan
#time.sleep(2)
driver.find_element("android.widget.ImageButton").click()  # 点击返回
#time.sleep(2)
driver.find_element("//*[contains(@text, '更多')]").click()  # 点击更多
#time.sleep(2)
driver.find_element("//*[contains(@content-desc, '向上')]").click()  # 点击返回
#time.sleep(2)
driver.quit()