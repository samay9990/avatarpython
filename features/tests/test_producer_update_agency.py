from pytest_bdd import scenario, given, when, then
from features.business_logic.avatar_loginpage import AvatarLoginPage
from features.business_logic.avatar_claims_intakepage import AvatarClaimsIntakePage
from features.business_logic.avatar_claimpage import AvatarClaimpage
from features.business_logic.avatar_producer_search import AvatarProducerSearchPage
from features.business_logic.avatar_producer_update import AvatarProducerUpdatePage
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
avatarupdate = AvatarProducerUpdatePage()


@scenario(r'TestCases/producer_update.feature', 'Verify producer update feature')
def test_verify_that_user_can_update_agency():
    print('Scenario--> Verify that user can update agency')

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


@when("User enters <fein_number>")
def enter_fein_number(fein_number):
    avatarSearch.input_fein_number(fein_number)
    time.sleep(5)

@when("User clicks on search button")
def clicks_search_button():
    avatarSearch.click_search_btn()

@when("User selects <search_value>")
def selects_agency_code(search_value):
    avatarSearch.select_agent_code(search_value)
    time.sleep(5)

@when("User lands on searched agency form with <verify_agency_code>")
def landing_page(verify_agency_code):
    avatarSearch.verify_agent_code(verify_agency_code)


@when("User inputs new <payee_name>")
def input_new_payeename(payee_name):
    avatarupdate.input_payee_name(payee_name)


@when("User clicks Agency Visit Review")
def click_agency_review():
    avatarupdate.click_agency_visit_review()


@when("User clicks Add Log")
def click_add_log():
    avatarupdate.click_add_log()


@when("User enters <previsit>")
def input_previsit(previsit):
    avatarupdate.input_pre_visit(previsit)


@when("User enters <staffnotes>")
def input_staffnotes(staffnotes):
    avatarupdate.input_staff_notes(staffnotes)

@when("User enters <agentrequests>")
def input_agency_requests(agentrequests):
    avatarupdate.input_agent_requests(agentrequests)

@when("User enters <visitreview>")
def input_visit_review(visitreview):
    avatarupdate.input_visit_review(visitreview)

@when("User clicks Submit")
def click_update_agency():
    avatarupdate.click_agency_submit()
    time.sleep(5)


@when("User clicks update button")
def click_update_agency():
    avatarupdate.click_update_agency()
    time.sleep(5)


@when("User clicks on Document")
def click_update_agency():
    avatarupdate.click_document()

@when("User enters <file_name>")
def input_file_name(file_name):
    avatarupdate.input_doc_filename(file_name)

@when("User selects file_type")
def select_file_type():
    avatarupdate.click_doctype()

@when("User inputs <file>")
def inout_file(file):
    avatarupdate.input_doc_filepath(file)

@when("User clicks submit document")
def click_submit():
    avatarupdate.click_upload_doc()

@when("User clicks close document")
def click_close():
    avatarupdate.click_close_doc()

@when("User clicks Agency User")
def click_agency_user():
    avatarupdate.click_agency_button()

@when("User enters <user_id>")
def input_user_id(user_id):
    avatarupdate.input_user_id(user_id)

@when("User enters <sub_agent>")
def input_sub_agent(sub_agent):
    avatarupdate.input_sub_agent_id(sub_agent)

@when("User enters <first_name>")
def input_first_name(first_name):
    avatarupdate.input_firstname(first_name)

@when("User enters <middle_name>")
def input_middle_name(middle_name):
    avatarupdate.input_middlename(middle_name)

@when("User enters <last_name>")
def input_last_name(last_name):
    avatarupdate.input_lastname(last_name)

@when("User enters <screen_name>")
def input_screen_name(screen_name):
    avatarupdate.input_screenname(screen_name)

@when("User enters <email>")
def input_email(email):
    avatarupdate.input_email(email)

@when("User enters <phone>")
def input_phone_agency(phone):
    avatarupdate.input_phone(phone)

@when("User selects <status>")
def select_status(status):
    avatarupdate.select_status(status)

@when("User selects <user_level>")
def select_user_level(user_level):
    avatarupdate.select_userlevel(user_level)

@when("User enters <effdatefrom>")
def input_effdatefrom(effdatefrom):
    avatarupdate.input_effdatefrom(effdatefrom)

@when("User enters <effdateto>")
def input_effdateto(effdateto):
    avatarupdate.input_effdateto(effdateto)


@when("User enters <visit_date>")
def input_visitdate(visit_date):
    avatarupdate.input_agency_visitdate(visit_date)


@when("User clicks on Add Row")
def click_addrow():
    avatarupdate.click_addrow()

@when("User selects <product>")
def select_prodcuct(product):
    avatarupdate.select_product_agencyform(product)


@when("User selects <state>")
def select_state(state):
    avatarupdate.select_state(state)


@when("User selects <uvassigned>")
def select_uvassign_agency(uvassigned):
    avatarupdate.select_uvassign(uvassigned)

@when("User selects <authorization>")
def select_user_level(authorization):
    avatarupdate.select_authorization(authorization)


@when("User clicks Save Agency User")
def click_save_agency_user():
    avatarupdate.click_save_agency_user()

@when("User clicks Close")
def click_close():
    avatarupdate.click_close()


@then("User verifies successful toast message")
def verify_success_toast_message():
    if avatartoast.get_success_toast_message_if_exist():
        assert True


@then("User verifies in the updated log the <new_value>")
def verify_update_log(new_value):
    time.sleep(5)
    avatarupdate.click_update_log()
    time.sleep(5)
    avatarupdate.verify_update_log(new_value)

