from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction  # 导包

server = r'http://localhost:4723/wd/hub'  # Appium Server, 端口默认为4723

desired_capabilities = {

    'platformName': 'Android',

    'deviceName': '127.0.0.1:62001',  # 需替换成你的deviceName

    'platformVersion': '5.1.1',

    'appPackage': 'com.android.settings',

    'appActivity': '.Settings'

}

driver = webdriver.Remote(server, desired_capabilities)

tc = TouchAction(driver)  # 创建TouchAction类对象

# more_button = driver.find_element_by_xpath("//*[contains(@text, '更多')]")

# tc.tap(more_button).perform()  # 可以直接传入找到的元素

tc.tap(x=108, y=445).perform()  # 也可以不找元素，直接传入坐标


# 前面的代码都一样driver = webdriver.Remote(server, desired_capabilities)
more_button = driver.find_element_by_xpath("//*[contains(@text, '更多')]")
tc = TouchAction(driver)
tc.tap(more_button).perform()
# tc.press(x=24, y=478).perform()   # 按下某个点，不松开
tc.press(x=24, y=478).wait(5000).release().perform()   # 按下某个点，等待5秒钟后，松开。可以理解为长按