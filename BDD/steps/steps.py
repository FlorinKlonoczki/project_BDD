from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'I am on autocomplete page')
def step_impl(context):
    print(u'STEP: Given I am on autocomplete page')
    context.driver.get('https://formy-project.herokuapp.com/autocomplete')


@when(u'I type cj in address field')
def step_impl(context):
    print(u'STEP: When I type cj in address field')
    #context.driver.find_element(By.ID, 'autocomplete').send_keys('cj')


@then(u'Cluj should be display')
def step_impl(context):
    print(u'STEP: Then Cluj should be display')


@when(u'I type Dorobantilor on street field')
def step_impl(context):
    print(u'STEP: When I type Dorobantilor on street field')


@when(u'I click on search button')
def step_impl(context):
    print(u'STEP: When I click on search button')


@then(u'Dorobantilor should be display')
def step_impl(context):
    print(u'STEP: Then Dorobantilor should be display')


@when(u'I type "{city}" in address field')
def step_impl(context, city):
    print(f'STEP: When I type "{city}" in address field')


@then(u'"{expected_results}"should be display')
def step_impl(context, expected_results):
    print(f'STEP: Then "{expected_results}"should be display')
