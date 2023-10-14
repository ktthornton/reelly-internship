from pages.settings_page import SettingsPage
from pages.sign_in_page import SignInPage
from pages.base_page import Page
from pages.add_project_page import AddProjectPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.add_project_page = AddProjectPage(driver)
