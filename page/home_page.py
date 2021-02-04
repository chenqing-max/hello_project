from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    close_button = By.XPATH, '//*[@content-desc="关闭对话框"]'
    click_me = By.XPATH, '//*[@text="我"]'

    def click_close_button(self):
        self.click(self.close_button)

    def click_me_button(self):
        self.click(self.click_me)
