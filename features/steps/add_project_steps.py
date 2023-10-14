from behave import given, when, then


@given('User signs in to Reelly site')
def open_add_project(context):
    context.app.base_page.open_url()
    context.app.sign_in_page.sign_in_username()
    context.app.sign_in_page.sign_in_password()
    context.app.sign_in_page.click_signin()


@when('Click Settings')
def click_settings(context):
    context.app.settings_page.click_settings()


@when('Click Add a Project')
def click_add_project(context):
    context.app.settings_page.click_add_project()


@then('Verify Send an application button is clickable')
def verify_send_application_clickable(context):
    context.app.add_project_page.verify_send_application_clickable()


@then('Verify user is brought to the correct page')
def verify_add_project_url(context):
    context.app.add_project_page.verify_add_project_url()


@when('Text is input into fields')
def input_expected_text(context):
    context.app.add_project_page.input_expected_text()


@then('Verify text displays correctly')
def verify_expected_text(context):
    context.app.add_project_page.verify_expected_text()


