# coding:utf-8
'''
description:用户功能
'''
import unittest
from element.driver import Driver

class test_appium(unittest.TestCase):
    def setUp(self):
        self.dr = Driver()
        self.dr.get_driver()
        self.dr.to_userPage()

    def tearDown(self):
        self.dr.driver.quit()


    def test_01(self):
        """从我的tab页跳提醒tab页"""
        self.dr.clickBy('xpath', "//*[@text='提醒']")
        ret = self.dr.getText('xpath', "//*[@text='拍品提醒']")
        self.assertEqual(ret, "拍品提醒")

    def test_02(self):
        """从我的tab页跳关注tab页"""
        self.dr.clickBy('xpath', "//*[@text='关注']")
        ret = self.dr.getText('xpath', "//*[@text='关注上新']")
        self.assertEqual(ret, "关注上新")

    def test_03(self):
        """从我的tab页跳待交保"""
        self.dr.clickBy('xpath', "//*[@text='待交保']")
        ret = self.dr.getText('xpath', "//*[@text='我的拍卖']")
        self.assertEqual(ret, "我的拍卖")

    def test_04(self):
        """从我的tab页跳待开拍"""
        self.dr.clickBy('xpath', "//*[@text='待开拍']")
        ret = self.dr.getText('xpath', "//*[@text='我的拍卖']")
        self.assertEqual(ret, "我的拍卖")
        # xx = self.dr.is_element_exist("//*[@text='待开拍']")
        # print(xx)
        # if xx == True:
        #     self.dr.clickBy('xpath', "//*[@text='待开拍']")
        #     ret = self.dr.getText('xpath', "//*[@text='我的拍卖']")
        #     self.assertEqual(ret, "我的拍卖")

    def test_05(self):
        """从我的tab页跳竞价中"""
        self.dr.clickBy('xpath', "//*[@text='竞价中']")
        ret = self.dr.getText('xpath', "//*[@text='我的拍卖']")
        self.assertEqual(ret, "我的拍卖")

    def test_06(self):
        """从我的tab页跳已结束"""
        self.dr.clickBy('xpath', "//*[@text='已结束']")
        ret = self.dr.getText('xpath', "//*[@text='我的拍卖']")
        self.assertEqual(ret, "我的拍卖")

    def test_07(self):
        """从我的tab页跳已拍下"""
        self.dr.clickBy('xpath', "//*[@text='已拍下']")
        ret = self.dr.getText('xpath', "//*[@text='我的订单']")
        self.assertEqual(ret, "我的订单")

    def test_08(self):
        """从我的tab页查看保证金/变卖预缴款"""
        self.dr.clickBy('xpath', "//*[@text='查看']")
        ret = self.dr.getText('xpath', "//*[@text='保证金/变卖预缴款']")
        self.assertEqual(ret, "保证金/变卖预缴款")

if __name__=='__main__':
    unittest.main()