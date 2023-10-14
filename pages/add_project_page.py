from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page


class AddProjectPage(Page):
    SEND_APPLICATION_BTN = (By.CSS_SELECTOR, 'input.purchase-access.w-button')
    YOUR_NAME_FIELD = (By.ID, 'Your-name')
    COMPANY_NAME_FIELD = (By.ID, 'Your-company-name')
    COMPANY_ROLE_FIELD = (By.ID, 'Role')
    COMPANY_AGE_FIELD = (By.ID, 'Age-of-the-company')
    COUNTRY_FIELD = (By.ID, 'Country')
    PROJECT_NAME_FIELD = (By.ID, 'Name-project')
    PHONE_FIELD = (By.ID, 'Phone')
    EMAIL_FIELD = (By.ID, 'Email-add-project')

    expected_text_your_name = 'test name'
    expected_text_company_name = 'test company'
    expected_text_company_role = 'Manager'
    expected_text_company_age = '12 years'
    expected_text_country = 'United States'
    expected_text_project_name = 'Test Project'
    expected_text_phone = '123-456-7890'
    expected_text_email = 'test@email.com'

    def input_expected_text(self):
        self.input_text(self.expected_text_your_name, *self.YOUR_NAME_FIELD)
        self.input_text(self.expected_text_company_name, *self.COMPANY_NAME_FIELD)
        self.input_text(self.expected_text_company_role, *self.COMPANY_ROLE_FIELD)
        self.input_text(self.expected_text_company_age, *self.COMPANY_AGE_FIELD)
        self.input_text(self.expected_text_country, *self.COUNTRY_FIELD)
        self.input_text(self.expected_text_project_name, *self.PROJECT_NAME_FIELD)
        self.input_text(self.expected_text_phone, *self.PHONE_FIELD)
        self.input_text(self.expected_text_email, *self.EMAIL_FIELD)
        sleep(3)

    def verify_expected_text(self):
        actual_your_name = self.find_element(*self.YOUR_NAME_FIELD).get_attribute("value")
        actual_company_name = self.find_element(*self.COMPANY_NAME_FIELD).get_attribute("value")
        actual_company_role = self.find_element(*self.COMPANY_ROLE_FIELD).get_attribute("value")
        actual_company_age = self.find_element(*self.COMPANY_AGE_FIELD).get_attribute("value")
        actual_country = self.find_element(*self.COUNTRY_FIELD).get_attribute("value")
        actual_project_name = self.find_element(*self.PROJECT_NAME_FIELD).get_attribute("value")
        actual_phone = self.find_element(*self.PHONE_FIELD).get_attribute("value")
        actual_email = self.find_element(*self.EMAIL_FIELD).get_attribute("value")

        assert self.expected_text_your_name == actual_your_name, \
            f'Error, expected {self.expected_text_your_name} did not match actual {actual_your_name}'
        assert self.expected_text_company_name == actual_company_name, \
            f'Error, expected {self.expected_text_company_name} did not match actual {actual_company_name}'
        assert self.expected_text_company_role == actual_company_role, \
            f'Error, expected {self.expected_text_company_role} did not match actual {actual_company_role}'
        assert self.expected_text_company_age == actual_company_age, \
            f'Error, expected {self.expected_text_company_age} did not match actual {actual_company_age}'
        assert self.expected_text_country == actual_country, \
            f'Error, expected {self.expected_text_country} did not match actual {actual_country}'
        assert self.expected_text_project_name == actual_project_name, \
            f'Error, expected {self.expected_text_project_name} did not match actual {actual_project_name}'
        assert self.expected_text_phone == actual_phone, \
            f'Error, expected {self.expected_text_phone} did not match actual {actual_phone}'
        assert self.expected_text_email == actual_email, \
            f'Error, expected {self.expected_text_email} did not match actual {actual_email}'

    def verify_send_application_clickable(self, *locator):
        self.wait_for_element_clickable(self.SEND_APPLICATION_BTN)

    def verify_add_project_url(self):
        self.verify_partial_url('add-a-project')
