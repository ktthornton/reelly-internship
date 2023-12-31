from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from app.application import Application

from support.logger import logger


def browser_init(context):  # pass scenario_name here as well if using BrowserStack)
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
    # bs_user = 'katelynthornton_kiJwM4'
    # bs_key = 'bFNUqxmcjp4EmS1f3qwS'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Big Sur',
    #     'browserName': 'Safari',
    #     'browserVersion': '14.1',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    ###

    ### CHOME MOBILE EMULATION ###
    mobile_emulation = {
        "deviceName": "Pixel 5",
        # "deviceMetrics": {"width": 393, "height": 851},
        # "deviceName": "iPhone SE"
        # "deviceMetrics": {"width": 375, "height": 667},
        # "deviceName": "iPhone XR"
        # "deviceMetrics": {"width": 414, "height": 896},
        # "deviceName": "iPhone 12 Pro"
        # "deviceMetrics": {"width": 390, "height": 844},
        # "deviceName": "Samsung Galaxy S8+"
        # "deviceMetrics": {"width": 360, "height": 740},
        # "deviceName": "Samsung Galaxy S20 Ultra"
        # "deviceMetrics": {"width": 412, "height": 915},
        # "deviceName": "iPad Air"
        # "deviceMetrics": {"width": 820, "height": 1180},
        # "deviceName": "iPad Mini"
        # "deviceMetrics": {"width": 768, "height": 1024},
        # "deviceName": "Surface Pro 7"
        # "deviceMetrics": {"width": 912, "height": 1368},
        # "deviceName": "Surface Duo"
        # "deviceMetrics": {"width": 540, "height": 720},
        # "deviceName": "Galaxy Fold"
        # "deviceMetrics": {"width": 280, "height": 653},
        # "deviceName": "Samsung Galaxy A51/71"
        # "deviceMetrics": {"width": 412, "height": 914},
        # "deviceName": "Nest Hub"
        # "deviceMetrics": {"width": 1024, "height": 600},
        # "deviceName": "Nest Hub Max"
        # "deviceMetrics": {"width": 1280, "height": 800},
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)
    ###

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)  # pass scenario.name here if using BrowserStack


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
