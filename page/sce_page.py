from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SecPage(BaseAction):

    click_settings = By.XPATH, '//*[@resource-id="com.yunmall.lc:id/ymtitlebar_left_btn_image"]'

    def click_settings_button(self):
        self.click(self.click_settings)

