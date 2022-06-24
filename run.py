import unittest
from tools.HTMLTestReportCN import HTMLTestRunner
import subprocess
from time import sleep
import requests
class UnitTest(object):
    def __init__(self):
        pass
    def run(self):
        # url = 'https://mtl4.alibaba-inc.com/scheduler/jobs/705920/artifacts/7c7c3f9bbc494c9990794ce5c3b044b9/download/600000%40aliAuction_android_release_1.0.2.5.5269.apk'
        # try:
        #     headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) '
        #                              'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        #                'Connection': 'keep-alive', }
        #     file = requests.get(url, headers=headers, timeout=10)
        #     filename = 'pm.apk'
        #     with open(filename, 'wb') as apk:
        #         apk.write(file.content)
        #
        #     cmd = "adb  -s 7HX0219920018573 install pm.apk"
        #     subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        #
        # except Exception as e:
        #     print(str(e))
        # sleep(10)
        LOG = r'/Users/alen/hwqCode/AppiumDemo/result.html'
        testunit = unittest.defaultTestLoader.discover(start_dir=r'/Users/alen/hwqCode/AppiumDemo', pattern='test01*.py')
        fp = open(LOG, 'wb')  # 定义测试报告存放路径
        runner = HTMLTestRunner(stream=fp, title='拍卖app第一轮测试', tester='wq.hu', description='用例执行情况')  # 定义测试报告
        c = runner.run(testunit)  # 执行测试用例
        all = c.testsRun
        success = c.success_count
        failure = c.failure_count
        fp.close()
        print('执行测试用例总数', all)
        print('成功用例数', success)
        print('失败用例数', failure)

if __name__ == '__main__':
    # cmd = r'python T004.py E:\tcloud\opsService\testdemo\unittest\baidu hello wq.hu'
    d = UnitTest()
    d.run()