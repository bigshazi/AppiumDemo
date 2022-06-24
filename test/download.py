import urllib.request
import requests
import subprocess
import os
# url= 'https://mtl4.alibaba-inc.com/scheduler/jobs/446552/artifacts/1e4f9c10462b4637bb19e35a9b303214/download/600000%40aliAuction_android_release_0.9.0.0.648.apk'
#
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) '
#                           'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
#             'Connection': 'keep-alive', }
# file = requests.get(url, headers=headers, timeout=10)
# filename = 'pm.apk'
# with open(filename, 'wb') as apk:
#     apk.write(file.content)


# cmd="adb  -s 7HX0219920018573 install pm.apk"
# data = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
cmd="adb  install pm.apk"
os.system(cmd)
# subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
