from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('AnnaV would like to open "{pagename}" page')
def open_page(context, pagename):
    if pagename =="Profitolizer":
        context.driver.get("https://profitolizer.com/")
    elif pagename =="Google":
        context.driver.get("https://google.com/")
    elif pagename =="Walmart":
        context.driver.get("https://walmart.com/")
    else:
        assert pagename in context.driver.title, f"Page {pagename} not found"


@then('AnnaV verify page title is "{str_title}"')
def page_title(context, str_title):
    actual_title = context.driver.title
    print(f"Actual title of the page is {actual_title}")
    assert context.driver.title == str_title, f"Title mismatch  {actual_title} != {str_title}"


@step('AnnaV click on "{button_name}" button')
def click_button(context, button_name):
    if button_name == "Login":
        xpath_of_element = "//a[contains(text(),'Login')]"
    elif button_name == "SignUp":
        xpath_of_element = "//a[contains(text(),'Sign Up')]"
    elif button_name == "Submit":
        xpath_of_element = "//button[@type='submit']"
    else:
        raise ValueError(f"No Xpath for {button_name}")

    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_of_element)))
    element.click()


@then('AnnaV type "{text}" to "{xpath}"')
def step_impl(context,text,xpath):
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.clear()
    element.send_keys(text)

