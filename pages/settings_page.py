from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SettingsPage(Page):
    ADD_PROJECT_BTN = (By.CSS_SELECTOR, 'a.page-setting-block.w-inline-block[href*="add-a-project"]')
    SETTINGS_MENU = (By.CSS_SELECTOR, 'div.logo-menu-block [href*="settings"]')

    def click_add_project(self, *locator):
        self.click(*self.ADD_PROJECT_BTN)

    def click_settings(self, *locator):
        sleep(3)  # need to add a sleep here if using Safari in BS or mobile emulation
        self.click(*self.SETTINGS_MENU)


