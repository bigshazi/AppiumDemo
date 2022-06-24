# coding:utf-8
'''
description:测试首页功能
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
        '''精选tab页'''
        self.dr.clickBy('id','com.taobao.aliAuction:id/tv_all')
        ret = self.dr.getText('id', 'com.taobao.aliAuction:id/tv_all')
        self.assertEqual(ret, "精选")

    def test_02(self):
        '''资产tab页'''
        self.dr.clickBy('id','com.taobao.aliAuction:id/tv_asset')
        ret = self.dr.getText('xpath',"//*[@text='土地']")
        self.assertEqual(ret, "土地")

    def test_03(self):
        '''珍品tab页'''
        self.dr.clickBy('id', 'com.taobao.aliAuction:id/tv_collect')
        ret = self.dr.getText('xpath', "//*[@text='拍卖行']")
        self.assertEqual(ret, "拍卖行")

    def test_04(self):
        '''首页点击'假一赔三'能正常打开服务保障页'''
        self.dr.clickBy('xpath', "//*[@text='假一赔三']")
        ret = self.dr.getText('xpath', "//*[@text='阿里拍卖服务保障']")
        self.assertEqual(ret, "阿里拍卖服务保障")
        self.dr.driver.keyevent(4)

    def test_05(self):
        '''首页点击'官方保障'能正常打开服务保障页'''
        self.dr.clickBy('xpath', "//*[@text='官方保障']")
        ret = self.dr.getText('xpath', "//*[@text='阿里拍卖服务保障']")
        self.assertEqual(ret, "阿里拍卖服务保障")
        self.dr.driver.keyevent(4)

    def test_06(self):
        '''首页点击'服务热线'能正常打开拨号盘'''
        self.dr.clickBy('xpath', "//*[@text='服务热线 400-822-2870']")
        # ret = self.dr.getText('id', "com.android.contacts:id/digits")
        ret = self.dr.getText('id', "com.huawei.contacts:id/digits")
        self.assertEqual(ret, "400 822 2870")
        self.dr.driver.keyevent(4)

    def test_07(self):
        '''关注提醒页面'''
        self.dr.clickBy('id', "com.taobao.aliAuction:id/page_follow")
        ret = self.dr.findBy('id', "com.taobao.aliAuction:id/mToolBar")
        self.assertIsNotNone(ret)
        self.dr.driver.keyevent(4)

    def test_08(self):
        '''消息页面'''
        self.dr.clickBy('id', "com.taobao.aliAuction:id/page_message")
        ret = self.dr.getText('id', "com.taobao.aliAuction:id/tv_title")
        self.assertEqual(ret, "消息")
        self.dr.driver.keyevent(4)

    @classmethod
    def setUpClass(self):
        self.dr = Driver()
        self.dr.get_driver()
        self.dr.guide()

    # @classmethod
    # def tearDownClass(self):
    #     self.dr.driver.quit()

if __name__=='__main__':
    unittest.main()