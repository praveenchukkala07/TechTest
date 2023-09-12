from selenium import webdriver
import time

@given('Open trademe sanbox website')
def launchbrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    driver.get("https://www.tmsandbox.co.nz/")

@when('verify trademe homepage')
def verifyLogo(context):
    verifymainlogo: bool = context.driver.find_element("id", "SiteHeader_SiteTabs_kevin").is_displayed()
    print(verifymainlogo)

@then('search for "{item}"')
def searchItem(context,item):
    query = context.driver.find_element("id", "searchString")
    query.send_keys("Suzuki")
    query.submit()

@And('Close browser')
def close(context):
    context.driver.close()
