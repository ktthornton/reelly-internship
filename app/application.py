from pages.settings_page import SettingsPage
from pages.sign_in_page import SignInPage
from pages.base_page import Page
from pages.add_project_page import AddProjectPage
from pages.settings_mobile_page import SettingsMobilePage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.add_project_page = AddProjectPage(driver)
        self.settings_mobile_page = SettingsMobilePage(driver)
