from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ThirdPage(BaseAction):

    click_location_manger = By.XPATH, '//*[@text="地址管理"]'
    add_new_location = By.XPATH, '//*[@text="新增地址"]'

    def click_manger_location(self):
        self.click(self.click_location_manger)

    def click_new_location(self):
        self.click(self.add_new_location)



