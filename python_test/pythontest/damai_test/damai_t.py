import os
# os.popen("adb shell am start cn.damai/cn.damai.launcher.splash.SplashMainActivity")
print(os.popen("adb shell uiautomator dump /sdcard/ui.xml"))