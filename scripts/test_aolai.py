import random

import pytest
from appium import webdriver
from time import sleep

from base.base_analyze import analyze_data
from page.fourth_page import FourthPage
from page.home_page import HomePage
from page.sce_page import SecPage
from page.third_page import ThirdPage


class TestAoLai:

    def setup(self):
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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.home_page = HomePage(self.driver)
        self.sec_page = SecPage(self.driver)
        self.third_page = ThirdPage(self.driver)
        self.fourth_page = FourthPage(self.driver)

    def teardown(self):
        sleep(1)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("date", "test_ao"))
    def test_ao(self, args):
        name = args["name"]
        tel = args["tel"]
        location = args["location"]
        # 关闭更新
        self.home_page.click_close_button()
        # 点击右下角的我
        self.home_page.click_me_button()
        # 点击右上角的设置按钮
        self.sec_page.click_settings_button()
        # 点击地址管理
        self.third_page.click_manger_location()
        # 点击新增地址
        self.third_page.click_new_location()
        # # 输入收件人
        self.fourth_page.input_receive_people(name)
        # 输入手机号
        self.fourth_page.input_tel_number(tel)
        # 随机选择地区
        self.fourth_page.click_your_location()
        self.fourth_page.choose()
        # 输入详细地址
        self.fourth_page.input_edit_your_location(location)
        # 设为默认值
        self.fourth_page.click_default()
        # 点击保存
        self.fourth_page.click_saved_btn()








