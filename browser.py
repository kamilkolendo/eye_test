from selenium.webdriver import Firefox

# def get_driver():
#     driver = Firefox()
#     driver.implicitly_wait(5)
#     return driver

driver = None

# przyklad singletona:
def get_driver():
    global driver
    if not driver:
        driver = Firefox()
        driver.implicitly_wait(5)
    return driver