from cpu import *
import time
VIRT = []    #申请的虚拟内存总量
RES = []  #进程使用的物理内存总和
SHR = []  #RES中”映射至文件”的物理内存总和
CPU = []  #CPU占比
MEM = []  #内存占比

udid = udid()
print(udid)
while True:
    cpuText = cpu(udid)
    # VIRT = str(cpuText[0].split()[4]).split("'")[1]  # 申请的虚拟内存总量
    # RES = str(cpuText[0].split()[5]).split("'")[1]  # 进程使用的物理内存总和
    # SHR = str(cpuText[0].split()[6]).split("'")[1]  # RES中”映射至文件”的物理内存总和
    # CPU = str(cpuText[0].split()[8]).split("'")[1]  # CPU占比
    # MEM = str(cpuText[0].split()[9]).split("'")[1]  # 内存占比

    VIRT.append(str(cpuText[0].split()[4]).split("'")[1])   #申请的虚拟内存总量
    RES.append(str(cpuText[0].split()[5]).split("'")[1])  # 进程使用的物理内存总和
    SHR.append(str(cpuText[0].split()[6]).split("'")[1])  # RES中”映射至文件”的物理内存总和
    CPU.append(str(cpuText[0].split()[8]).split("'")[1])  # CPU占比
    MEM.append(str(cpuText[0].split()[9]).split("'")[1])  # 内存占比
    time.sleep(3)
    print('CPU占比')
    print(CPU)
    print('内存占比')
    print(MEM)
