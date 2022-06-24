
import re
import subprocess
def mem(udid):
    memCmd = 'adb -s '+ udid + ' shell dumpsys meminfo com.taobao.aliAuction'
    # print("内存命令",memCmd)
    menTextList = subprocess.Popen(memCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    # print("内存信息",menTextList)
    for memInfo in menTextList:
        if len(memInfo.split())>0 and memInfo.split()[0].decode() == "TOTAL":
            mem = int(memInfo.split()[1].decode())//1024
            print("进程占用的系统总内存",mem, "M")
            # men_list = str(info.split()[1].decode())
    return mem
def cpu(udid):
    # cpuCmd = 'adb -s ' + udid + ' shell top -n 1| grep com.taobao.aliA+'
    cpuCmd = 'adb -s ' + udid + ' shell top -n 1| grep com.taobao.aliA+'
    print(cpuCmd)
    cpuText = subprocess.Popen(cpuCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    if len(cpuText) >= 1:
        VIRT = str(cpuText[0].split()[4]).split("'")[1]    #申请的虚拟内存总量
        RES = str(cpuText[0].split()[5]).split("'")[1]  #进程使用的物理内存总和
        SHR = str(cpuText[0].split()[6]).split("'")[1]  #RES中”映射至文件”的物理内存总和
        CPU = str(cpuText[0].split()[8]).split("'")[1]  #CPU占比
        MEM = str(cpuText[0].split()[9]).split("'")[1]  #内存占比
        # print(VIRT, RES, SHR, CPU, MEM)
        return cpuText

def udid():
    udidCmd = 'adb devices'
    udidText = subprocess.Popen(udidCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    udid = str(udidText[1].split()[0]).split("'")[1]
    return udid

def monkey():
    monkeyCmd = 'adb shell monkey -p com.taobao.aliAuction -s 500 --ignore-crashes --ignore-timeouts --monitor-native-crashes -v -v 10000 > /Users/alen/hwqLog/log.txt'
    subprocess.Popen(monkeyCmd)

if __name__=='__main__':
    udid = udid()
    print(udid)
    cpu(udid)