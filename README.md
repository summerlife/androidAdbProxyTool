# androidAdbProxyTool
用于安卓手机快速设置IP代理。eg：Charles代理


1.支持5.x及以上的Android设备快速设置代理和端口号。
2.使用python3执行，执行后无需重启手机。
3.请务必保证手机处于链接状态且adb devices只能有此一台设备
4.设置代理：python3  ./androidAdbProxyTool.py  1  <IP>  <PORT>  <packageName>
5.清除代理：python3  ./androidAdbProxyTool.py  2  <IP>  <PORT>  <packageName>
6.如果出现问题，请尝试如下命令解决：adb shell settings delete global http_proxy  adb reboot
