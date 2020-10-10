from selenium import webdriver

chromedriver = 'C:/Selenium/chromedriver.exe'
edgedriver = 'C:/Selenium/msedgedriver.exe'                          # For running in local machine browser
driver = webdriver.Edge(edgedriver)
driver.maximize_window()


# driver = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     desired_capabilities={                                            # To run selenium grid from local
#         'browserName': 'chrome',
#         'platform': 'Windows'
#         }
#     )
# driver.maximize_window()