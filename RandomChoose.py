import random

from appium import webdriver
# 创建一个字典，包装相应的启动参数
desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '5.1'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = 'huawei p30'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.yunmall.lc'
# 需要启动的程序的界面名
desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
# 不重置
desired_caps['noReset'] = True
# 可以输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_xpath('//*[@content-desc="关闭对话框"]').click()
driver.find_element_by_xpath('//*[@text="我"]').click()
driver.find_element_by_xpath('//*[@resource-id="com.yunmall.lc:id/ymtitlebar_left_btn_image"]').click()
driver.find_element_by_xpath('//*[@text="地址管理"]').click()
driver.find_element_by_xpath('//*[@text="新增地址"]').click()
driver.find_element_by_xpath('//*[@text="请选择"]').click()


def random_location():
    while True:
        ret = driver.find_elements_by_id("com.yunmall.lc:id/area_title")
        ret1 = list(set(ret))
        try:
            ret1[random.randint(0, len(ret) - 1)].click()
        except:
            old_page_source = driver.page_source
            driver.swipe(200, 900, 200, 300)
            if driver.page_source == old_page_source:
                break


random_location()






