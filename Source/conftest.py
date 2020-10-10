import time
from datetime import datetime
import pytest
from Drivers.chromedriver import driver
from Pages.Locators import log_out


@pytest.fixture(scope="function", autouse=True)
def logout():
    yield driver
    driver.find_element_by_xpath(log_out.user).click()
    time.sleep(2)
    driver.find_element_by_css_selector(log_out.logout).click()


@pytest.fixture(scope="session", autouse=True)
def posttest(request):
    yield driver
    driver.quit()


def names():
    date = str(datetime.now().date())
    now = datetime.now()
    temp = ('%02d%02d%d' % (now.minute, now.second, now.microsecond))[:-4]
    name = str(date+temp)
    return name