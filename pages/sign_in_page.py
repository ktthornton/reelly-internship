from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_EMAIL = (By.ID, 'email-2')
    SIGNIN_PW = (By.ID, 'field')
    SIGNIN_CONTINUE = (By.CSS_SELECTOR, 'a.login-button.w-button')

    def sign_in_username(self):
        self.input_text('ktlnknutn@gmail.com', *self.SIGNIN_EMAIL)

    def sign_in_password(self):
        self.input_text('ARizonaa16!', *self.SIGNIN_PW)

    def click_signin(self):
        self.click(*self.SIGNIN_CONTINUE)
