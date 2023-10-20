from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from app.application import Application

from support.logger import logger


def browser_init(context, scenario_name):  # pass scenario_name here as well if using BrowserStack)
    """
    :param context: Behave context
    """

    ### CHROME ###
    # service = Service(executable_path=r'C:\Users\ktknu\reelly-internship\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)

    # FIREFOX ###
    # service = Service(executable_path=r'C:\Users\ktknu\reelly-internship\geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    # service = Service(executable_path=r'C:\Users\ktknu\reelly-internship\chromedriver.exe')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    bs_user = 'katelynthornton_kiJwM4'
    bs_key = 'bFNUqxmcjp4EmS1f3qwS'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Big Sur',
        'browserName': 'Safari',
        'browserVersion': '14.1',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)
    ###

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)  # pass scenario.name here if using BrowserStack


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
