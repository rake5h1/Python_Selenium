from behave import given, when, then
from selenium import webdriver
from pages.login import Login

@given('Visit Site')
def visit_site(context):
    context.driver=webdriver.Edge()
    context.login_test=Login(context.driver)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()

@when('I Enter Username and Password')
def enter_details(context):
    context.login_test.enter_details()

@then('Click Login')
def click_login(context):
    # context.login_test.click_login()

    context.driver.quit()
