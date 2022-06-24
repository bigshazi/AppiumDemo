# coding:utf-8
'''
description:测试登陆功能
'''
import unittest
from element.driver import Driver

class test_appium(unittest.TestCase):
    def setUp(self):
        self.dr = Driver()
        self.dr.get_driver()

    def tearDown(self):
        self.dr.driver.quit()

    def test_01(self):
        '''手淘一键登陆'''
        self.dr.login_tb()

    def test_02(self):
        """用户登出"""
        self.dr.logout()
        ret = self.dr.getText('id','com.taobao.aliAuction:id/tv_asset')
        self.assertEqual(ret, "资产")

    def test_03(self):
        '''退出用户之后再次使用手淘一键登陆'''
        self.dr.login_tb()

if __name__=='__main__':
    unittest.main()