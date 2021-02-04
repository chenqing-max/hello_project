import random

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FourthPage(BaseAction):

    receive_people = By.XPATH, '//*[@text="收件人姓名2–15个字符"]'
    tel_number = By.XPATH, '//*[@text="11位手机号"]'

    # 选择地区
    choose_your_location = By.XPATH, '//*[@text="请选择"]'
    # 选择省份
    ramdom_sheng = By.ID, "com.yunmall.lc:id/area_title"
    # 选择城市
    ramdom_city = By.XPATH, '//*[@resource-id="com.yunmall.lc:id/area_title"]'

    edit_your_location = By.XPATH, '//*[@text="5–60个字符"]'
    input_bianma = By.XPATH, '//*[@text="可选填"]'
    click_default_location = By.XPATH, '//*[@resource-id="com.yunmall.lc:id/address_default"]'
    click_saved = By.XPATH, '//*[@text="保存"]'

    def input_receive_people(self, text):
        self.input(self.receive_people, text)

    def input_tel_number(self, text):
        self.input(self.tel_number, text)

    def click_your_location(self):
        self.click(self.choose_your_location)

    def choose(self):
        while True:
            try:
                ret = self.find_elements(self.ramdom_sheng)
                ret1 = random.randint(0, len(ret) - 1)
                ret[ret1].click()
                # ret = random.randint()
            except:
                break

        # ret = random.randint(0, )
        # self.find_elements_with_scroll(self.ramdom_sheng)


    # def random_choose_sheng(self):
    #     self.choose()
    #
    # def random_choose_city(self):
    #     self.choose()

    def input_edit_your_location(self, text):
        self.input(self.edit_your_location, text)

    def click_default(self):
        self.click(self.click_default_location)

    def click_saved_btn(self):
        self.click(self.click_saved)

