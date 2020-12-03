from pytest_bdd import scenario, given, when, then
from features.business_logic.avatar_loginpage import AvatarLoginPage
from features.business_logic.avatar_claims_intakepage import AvatarClaimsIntakePage
from features.business_logic.avatar_claimpage import AvatarClaimpage
from features.business_logic.avatar_producer_search import AvatarProducerSearchPage
from features.business_logic.avatar_topnavbar import AvatarTopNavBar
from features.business_logic.avatar_claims_homepage import AvatarClaimsHomepage
from features.business_logic.avatar_toast_messages import AvatarToastMessages
from features.business_logic.avatar_producer_page import AvatarProducerPage
import time
from pytest_bdd import parsers


avatarLoginPage = AvatarLoginPage()
avatarClaimsIntakePage = AvatarClaimsIntakePage()
avatarProducer = AvatarProducerPage()
avatarClaimPage = AvatarClaimpage()
avatarTopNavBar = AvatarTopNavBar()
avatarClaimsHomepage = AvatarClaimsHomepage()
avatartoast = AvatarToastMessages()
avatarSearch = AvatarProducerSearchPage()


@scenario(r'TestCases/producer_search.feature', 'Verify producer search feature')
def test_verify_that_user_can_search_producer():
    print('Scenario--> Verify that user can search producer')

@given("User is on Avatar Insurance Login Page")
def go_to_homepage():
    avatarLoginPage.open_avatar()
    print("User navigated to Home Page")

@when(parsers.cfparse("User logs in with user '{user}'"))
def click_on_login_btn(user):
    avatarLoginPage.login(user)
    print("User clicked on item")

@when("User clicks on producer in top navigation bar")
def click_on_claim_in_top_navigation_bar():
    avatarTopNavBar.click_on_producer()


@when("User clicks on Search Agency button")
def click_on_search_agency_button():
    avatarSearch.click_search_agency()


@when("User enters <agency_code>")
def enters_agency_code(agency_code):
    avatarSearch.input_search_agecycode(agency_code)
    time.sleep(5)

@when("User clicks on search button")
def clicks_search_button():
    avatarSearch.click_search_btn()

@when("User selects <search_value>")
def selects_agency_code(search_value):
    avatarSearch.select_agent_code(search_value)
    time.sleep(5)

@then("User lands on searched agency form with <verify_agency_code>")
def landing_page(verify_agency_code):
    avatarSearch.verify_agent_code(verify_agency_code)
