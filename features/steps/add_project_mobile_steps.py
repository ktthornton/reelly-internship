from behave import given, when, then
from time import sleep


@when('Click Settings/Menu')
def click_settings(context):
    context.app.settings_mobile_page.click_menu_mobile()