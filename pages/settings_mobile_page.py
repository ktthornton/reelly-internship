from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SettingsMobilePage(Page):
    MOBILE_MENU = (By.CSS_SELECTOR, 'a.menu-button-wrapper.w-inline-block')

    def click_menu_mobile(self, *locator):
        sleep(3)  # need to add a sleep here if using mobile emulation
        self.click(*self.MOBILE_MENU)