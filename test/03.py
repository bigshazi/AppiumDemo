# encoding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',          # 需替换成你的deviceName
    'platformVersion': '5.1.1',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}
driver = webdriver.Remote(server, desired_capabilities)

while True:
    try:
        about_button = driver.find_element_by_xpath("//*[contains(@text, '关于')]")
        about_button.click()
        time.sleep(2)
        break
    except Exception:
        # 向下翻页
        # 这里还要注意，翻完页之后，上一页的最下面的元素还应该在页面上，以免丢失元素
        driver.swipe(320,1081,320,500,3000)
        # 判断关于我们页面是否有5.1.1
        eles = driver.find_elements_by_id("android:id/summary")
        for i in eles:
            # if "5.1" in i.text:   # 判断只要包含5.1就可以
            if i.text == "5.1.1":  # 判断i.text必须等于5.1.1
                print("有5.1.1")
                break
        else:
            print("没有")

driver.quit()