from behave import given, when, then
from selenium import webdriver

from pages.login import Login


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")


def browser():
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@given("a browser")
def get_browser(context):
    context.browser = browser()


@given("Visit Site")
def visit_site(context):
    # edge_driver_path = os.environ.get("EDGE_DRIVER_PATH")
    context.login_test = context.browser
    context.browser.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )
    context.browser.maximize_window()


@when("I Enter Username and Password")
def enter_details(context):
    Login(context.login_test).enter_details()


@then("Click Login")
def click_login(context):
    # context.login_test.click_login()

    context.browser.quit()
