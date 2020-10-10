from selenium.webdriver.common.by import By
from Drivers.chromedriver import driver
from Pages.Locators import login_page, dashboard
import time
import pytest
from pytest_bdd import scenario, given, when, then
from Source.conftest import names
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


wait = WebDriverWait(driver, 200)


@pytest.mark.login
@scenario('../Feature/Twitter.feature','User logs into twitter with username and password')
def test_login_page():
    pass


@pytest.mark.search
@scenario('../Feature/Twitter.feature','User searches for celebrity and logs his followings into csv file')
def test_search():
    pass


@given("User navigates to twitter login page")
def logging_in():
    driver.get("https://twitter.com/login?lang=en")


@when("User enters username, password and clicks sign-in button")
def username_password():
    driver.find_element_by_name(login_page.txt_username).send_keys("Shankar88463029")
    driver.find_element_by_name(login_page.txt_password).send_keys("#SS_automation")
    driver.find_element_by_css_selector(login_page.btn_submit).click()


@when("User searches for his/her favourite celebrity")
def search():
    driver.find_element_by_css_selector(dashboard.txt_search).send_keys("@reliancegroup")
    element = wait.until(EC.element_to_be_clickable((By.XPATH, dashboard.first_element)))
    options = driver.find_elements_by_xpath(dashboard.first_element)
    time.sleep(5)
    if (len(options) != 0):
        options[1].click()


@when("User is taken to Celebrity page and clicks on following")
def celebrity():
    driver.implicitly_wait(10)
    name = "@reliancegroup"             #"@msdhoni"
    Profile_name = driver.find_element_by_xpath(dashboard.name).text
    if Profile_name == name:
        driver.find_element_by_xpath(dashboard.link_following).click()
    else:
        print("Wrong profile!!!")


@then("User Copies all people in the following list to csv file")
def csv_write():
    time.sleep(5)
    i = 0
    path = "../Source/csvfiles/" + names() + ".csv"
    file = open(path, "a")
    list = driver.find_elements_by_xpath(dashboard.following_list)
    while i < len(list):
        value = list[i].text
        file.write(value.replace("Follow","")+'\n')
        i = i+1
    file.close()


@then("User is taken to dashboard")
def assert_dashboard():
    assert driver.find_element_by_css_selector(dashboard.txt_search).is_displayed()


