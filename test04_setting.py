# coding:utf-8
'''
description:setting
'''
import unittest
from element.driver import Driver
from time import sleep

class test_appium(unittest.TestCase):
    def setUp(self):
        self.dr = Driver()
        self.dr.get_driver()
        self.dr.to_setting()

    def tearDown(self):
        self.dr.driver.quit()

    def test_01(self):
        """我的收获地址"""
        self.dr.clickBy('id', "com.taobao.aliAuction:id/tv_address")
        ret = self.dr.findBy('text', "我的收货地址")
        self.assertIsNotNone(ret)

    def test_02(self):
        """消息通知"""
        self.dr.clickBy('id', "com.taobao.aliAuction:id/tv_msg_receiver")
        ret = self.dr.getText('id', "com.taobao.aliAuction:id/tv_state")
        self.assertEqual(ret, "已开启")

    def test_03(self):
        """账号"""
        self.dr.clickBy('id', "com.taobao.aliAuction:id/tv_account")
        ret = self.dr.getText('id', "com.taobao.aliAuction:id/tv_account_delete")
        self.assertEqual(ret, "账号注销")

    def test_04(self):
        """支付"""
        self.dr.clickBy('id', "com.taobao.aliAuction:id/tv_pay_info")
        ret = self.dr.getText('id', "com.taobao.aliAuction:id/verify_tip")
        self.assertEqual(ret, "面容、指纹")

    def test_05(self):
        """清除缓存"""
        self.dr.clickBy('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]")
        ret = self.dr.getText('id', "android:id/message")
        self.assertEqual(ret, "你确定要清除所有缓存数据吗?")

    def test_06(self):
        """隐私"""
        self.dr.clickBy('id', "com.taobao.aliAuction:id/tv_pri_setting")
        ret = self.dr.getText('xpath', "//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]")
        self.assertEqual(ret, "系统权限管理")

    def test_07(self):
        """帮助与反馈"""
        self.dr.clickBy('id', "com.taobao.aliAuction:id/tv_report")
        ret = self.dr.getText('xpath', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView")
        self.assertEqual(ret, "用户反馈")

    def test_08(self):
        """版本更新"""
        self.dr.clickBy('id', "com.taobao.aliAuction:id/tv_updata")
        # ret = self.dr.getText('id', "submitBtn")
        # self.assertEqual(ret, "提交")

    def test_09(self):
        """关于阿里拍卖"""
        self.dr.clickBy('id', "com.taobao.aliAuction:id/tv_about")
        ret = self.dr.getText('id', "com.taobao.aliAuction:id/tv_version_info")
        self.assertEqual(ret, "版权信息")

if __name__=='__main__':
    unittest.main()