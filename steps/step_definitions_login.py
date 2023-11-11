from behave import given, when, then
from selenium import webdriver
from pages.login import Login
from selenium.webdriver.edge.service import Service


@given("Visit Site")
def visit_site(context):
    edge_driver_path = "msedgedriver.exe"
    edge_service = Service(edge_driver_path)
    context.driver = webdriver.Edge(service=edge_service)
    context.login_test = Login(context.driver)
    context.driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )
    context.driver.maximize_window()


@when("I Enter Username and Password")
def enter_details(context):
    context.login_test.enter_details()


@then("Click Login")
def click_login(context):
    # context.login_test.click_login()

    context.driver.quit()
