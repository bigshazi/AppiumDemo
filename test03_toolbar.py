# coding:utf-8
'''
description:用户>工具栏
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
        """保证金&预缴款"""
        self.dr.clickBy('xpath', "//*[@text='保证金/预缴款']")
        ret = self.dr.getText('xpath', "//*[@text='保证金/变卖预缴款']")
        self.assertEqual(ret, "保证金/变卖预缴款")

    def test_02(self):
        """房产估价"""
        self.dr.clickBy('xpath', "//*[@text='房产估价']")
        ret = self.dr.getText('xpath', "//*[@text='一键估价']")
        self.assertEqual(ret, "一键估价")

    def test_03(self):
        """我的小蜜"""
        self.dr.clickBy('xpath', "//*[@text='我的小蜜']")
        ret = self.dr.getText('xpath', "//*[@text='拍小秘']")
        self.assertEqual(ret, "拍小秘")

    def test_04(self):
        """爱车估价"""
        self.dr.clickBy('xpath', "//*[@text='爱车估价']")
        ret = self.dr.getText('xpath', "//*[@text='车型']")
        self.assertEqual(ret, "车型")

    def test_05(self):
        """大额支付"""
        self.dr.clickBy('xpath', "//*[@text='大额支付']")
        ret = self.dr.getText('xpath', "//*[@text='使用银行专用款项交保证金说明']")
        self.assertEqual(ret, "使用银行专用款项交保证金说明")

    def test_06(self):
        """地图找房"""
        self.dr.clickBy('xpath', "//*[@text='地图找房']")
        ret = self.dr.getText('xpath', "//*[@text='地图找房']")
        self.assertEqual(ret, "地图找房")

    def test_07(self):
        """买家帮助"""
        self.dr.clickBy('xpath', "//*[@text='买家帮助']")
        ret = self.dr.getText('xpath', "//*[@text='帮助中心']")
        self.assertEqual(ret, "帮助中心")

    def test_08(self):
        """卖家帮助"""
        self.dr.clickBy('xpath', "//*[@text='卖家帮助']")
        ret = self.dr.getText('xpath', "//*[@text='帮助中心']")
        self.assertEqual(ret, "帮助中心")

    def test_09(self):
        """我的配资"""
        self.dr.clickBy('xpath', "//*[@text='我的配资']")
        ret = self.dr.getText('xpath', "//*[@text='我的配资']")
        self.assertEqual(ret, "我的配资")

    def test_10(self):
        """我的服务单"""
        self.dr.clickBy('xpath', "//*[@text='我的服务单']")
        ret = self.dr.getText('xpath', "//*[@text='您当前暂无任何服务单']")
        self.assertEqual(ret, "您当前暂无任何服务单")

if __name__=='__main__':
    unittest.main()