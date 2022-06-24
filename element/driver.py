# coding:utf-8
'''
description:driver配置
'''
from appium import webdriver
from time import sleep
class Driver():
    def get_driver(self):
        '''获取driver'''
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'  # 平台
            self.desired_caps['platformVersion'] = '10'  # 系统版本
            # self.desired_caps['platformVersion'] = '8.1.0'  # 系统版本
            # self.desired_caps['app'] = 'E:/autotestingPro/app/UCliulanqi_701.apk'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            self.desired_caps['appPackage'] = 'com.taobao.aliAuction'     # APK包名
            # self.desired_caps['appActivity'] = '.app.activity.SplashActivity'     # 被测程序启动时的Activity
            self.desired_caps['appActivity'] = 'com.taobao.aliAuction.app.activity.MainActivity'  # 被测程序启动时的Activity
            self.desired_caps['unicodeKeyboard'] = 'true'   # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            self.desired_caps['resetKeyboard'] = 'true' # 是否在测试结束后将键盘重轩为系统默认的输入法。
            self.desired_caps['newCommandTimeout'] = '120' # Appium服务器待appium客户端发送新消息的时间。默认为60秒
            # self.desired_caps['deviceName'] = '0a3880440210'     # 手机ID
            self.desired_caps['deviceName'] = '7HX0219920018573'  # 手机ID
            self.desired_caps['noReset'] = True # true:不重新安装APP，false:重新安装app
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)
            self.driver.implicitly_wait(8)
            return self.driver
        except Exception as e:
            raise e

    def findBy(self, type, element):
        """根据类型查找元素"""
        if type == 'id':
            dr = self.driver.find_element_by_id(element)
        if type == 'name':
            dr = self.driver.find_element_by_name(element)
        if type == 'xpath':
            dr = self.driver.find_element_by_xpath(element)
        if type == 'link_text':
            dr = self.driver.find_element_by_link_text(element)
        if type == 'text':
            dr = self.driver.find_element_by_accessibility_id(element)
        return dr

    def clickBy(self, type, element):
        self.findBy(type, element).click()

    def getText(self, type, element):
        dr = self.findBy(type, element).text
        return dr

    def guide(self):
        """首次登陆引导"""
        #同意隐私协议
        self.driver.find_element_by_id('com.taobao.aliAuction:id/tv_agree').click()
        #进入阿里拍卖
        self.driver.find_element_by_id('com.taobao.aliAuction:id/launch_button').click()
        #立即登陆
        self.driver.find_element_by_id('com.taobao.aliAuction:id/tv_login_button').click()
        #同意隐私协议
        self.driver.find_element_by_id('com.taobao.aliAuction:id/rbt_agree').click()
        # 手淘免登
        self.driver.find_element_by_id('com.taobao.aliAuction:id/pm_fastLogin').click()
        # 确认授权
        res = self.is_element_exist('确认授权')
        print('确认授权',res)
        if res == True:
            self.driver.find_element_by_accessibility_id('确认授权').click()
        sleep(1)
        # 打开关注&提醒 页允许定位权限
        self.driver.find_element_by_id('com.taobao.aliAuction:id/page_follow').click()
        ret = self.is_element_exist('com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        print('定位权限', ret)
        if ret == True:
            self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
        # self.driver.find_element_by_xpath("//*[@text='确认授权']").click()



    def touch_tap(self,x,y,duration=100):   #点击坐标  ,x1,x2,y1,y2,duration
        """点击相对坐标"""
        screen_width = self.driver.get_window_size()['width']  #获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']   #获取当前屏幕的高
        a =(float(x)/screen_width)*screen_width
        x1 = int(a)
        b = (float(y)/screen_height)*screen_height
        y1 = int(b)
        self.driver.tap([(x1,y1),(x1,y1)],duration)

    def login_tb(self):
        """手淘免登陆（已登陆手淘）"""
        # 手淘免登
        self.driver.find_element_by_id('com.taobao.aliAuction:id/pm_fastLogin').click()
        # 确认授权
        self.driver.find_element_by_xpath("/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageButton/android.widget.TextView/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView/android.widget.TextView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout").click()


    def logout(self):
        """用户登出"""
        self.clickBy('xpath','//android.widget.FrameLayout[@content-desc="我的"]/android.widget.ImageView')
        self.clickBy('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView[2]')
        self.clickBy('id','com.taobao.aliAuction:id/tv_logout')
        self.clickBy('id','android:id/button1')

    def to_userPage(self):
        self.clickBy('xpath', '//android.widget.FrameLayout[@content-desc="我的"]/android.widget.ImageView')

    def to_setting(self):
        self.clickBy('xpath', '//android.widget.FrameLayout[@content-desc="我的"]/android.widget.ImageView')
        self.clickBy('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView[2]')

    def is_element_exist(self, element, timeout=3):
        count = 0
        while count < timeout:
            souce = self.driver.page_source
            if element in souce:
                return True
            else:
                count += 1
                sleep(1)
        return False

if __name__=='__main__':
    aa = Driver()
    aa.get_driver()
