# coding=utf-8
import subprocess
import os
import time
from argparse import ArgumentParser
import sys



# 获取手机系统版本
def getAndroidVersion():
    ret = subprocess.check_output("adb shell getprop ro.build.version.release",shell=True)
    retStr = str(ret, encoding="utf-8")
    if "." in retStr:
        print("手机系统版本："+retStr)
        return int(retStr.split('.')[0])
    else:
        print("手机系统版本："+retStr)
        return int(retStr)
        # raise Exception(u'获取设备的安卓版本号失败.')

# 获取手机品牌
def getBrand():
    brand = str(subprocess.check_output("adb -d shell getprop ro.product.brand",shell=True), encoding="utf-8")
    return brand

# 获取手机型号
def getModel():
    model = str(subprocess.check_output("adb -d shell getprop ro.product.model",shell=True), encoding="utf-8")
    return model

# 获取手机序列号
def getSerialNo():
    serialno = str(subprocess.check_output("adb shell getprop ro.serialno",shell=True), encoding="utf-8")
    return serialno

# 设置代理
def setProxy(host,port,package):
    os.system('adb shell settings put global http_proxy {}:{}'.format(host, port))
    time.sleep(2)
    os.system('adb shell am force-stop ' + package)
    time.sleep(2)
    print("设置的IP:PORT为："+host+":"+port)

# 清除代理
def clearProxy(package):
    os.system('adb shell settings put global http_proxy :0')
    time.sleep(2)
    os.system('adb shell am force-stop ' + package)
    time.sleep(2)
    print("代理已清除")


def main():
    status = int(sys.argv[1])
    host = sys.argv[2]
    port = sys.argv[3]
    package = sys.argv[4]
    if status==1:
        print("开始设置代理......")
        print("")
        print("手机品牌："+getBrand())
        print("手机型号："+getModel())
        print("手机序列号："+getSerialNo())
        if getAndroidVersion()<=4:
            print("手机系统版本过低(小于等于4），请手动设置代理")
        else:
            setProxy(host,port,package)
    elif status==2:
        print("开始清除代理......")
        print("")
        print("手机品牌："+getBrand())
        print("手机型号："+getModel())
        print("手机序列号："+getSerialNo())
        if getAndroidVersion()<=4:
            print("手机系统版本过低（小于等于4），请手动设置")
        else:
            clearProxy(package)




if __name__=="__main__":
    main()