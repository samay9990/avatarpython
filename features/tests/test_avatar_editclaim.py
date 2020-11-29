import os
import sys

from pytest_bdd import scenario, given, when, then
from features.business_logic.avatar_loginpage import AvatarLoginPage
from features.business_logic.avatar_claims_intakepage import AvatarClaimsIntakePage
from features.business_logic.avatar_claimpage import AvatarClaimpage
from features.business_logic.avatar_topnavbar import AvatarTopNavBar
from features.business_logic.avatar_claims_homepage import AvatarClaimsHomepage
from features.business_logic.avatar_toast_messages import AvatarToastMessages
import time
from pytest_bdd import parsers
import pytest



avatarLoginPage = AvatarLoginPage()
avatarClaimsIntakePage = AvatarClaimsIntakePage()
avatarClaimPage = AvatarClaimpage()
avatarTopNavBar = AvatarTopNavBar()
avatarClaimsHomepage = AvatarClaimsHomepage()
avatartoast = AvatarToastMessages()


@scenario(r'TestCases/claim_edit.feature', 'Verify that user can edit claim')
def test_verify_that_user_can_edit_claim():
    print('Scenario--> Verify that user can edit claim')


@scenario(r'TestCases/claim_edit.feature', 'Verify that user can edit claim by changing values in all tabs')
def test_verify_that_user_can_edit_claim_2():
    print('Scenario--> Verify that user can edit claim 2')


@given("User is on Avatar Insurance Login Page")
def go_to_homepage():
    avatarLoginPage.open_avatar()
    print(sys.path[0])


@when(parsers.cfparse("User logs in with user '{user}'"))
def click_on_login_btn(user):
    avatarLoginPage.login(user)
    print("User clicked on item")



@when("User clicks on claim in top navigation bar")
def click_on_claim_in_top_navigation_bar():
    avatarTopNavBar.click_on_claims()


@when(parsers.cfparse("User searches for claim number <claim_number>"))
@when(parsers.cfparse("User searches for claim number '{claim_number}'"))
def search_for_claim_number(claim_number):
    avatarClaimsHomepage.enter_claim_number(claim_number)

@when("User clicks on search button on claim home page")
def click_on_search_button_on_claim_homepage():
    avatarClaimsHomepage.click_search_button()

@when(parsers.cfparse("User clicks on claim <claim_number> in the results table"))
@when(parsers.cfparse("User clicks on claim '{claim_number}' in the results table"))
def click_on_claim_number_in_results_table(claim_number):
    avatarClaimsHomepage.click_on_claim_number_in_search_grid(claim_number)


@when("User clicks on edit button on claim page")
def click_on_edit_button_on_claim_page():
    time.sleep(10)
    avatarClaimPage.click_on_edit_button()
    time.sleep(10)


@when(parsers.cfparse("User changes the claim type to <claim_type>"))
@when(parsers.cfparse("User changes the claim type to '{claim_type}'"))
def change_claim_type_on_claim_intake_page(claim_type):
    avatarClaimsIntakePage.select_claim_type(claim_type)


@when(parsers.cfparse("User changes the type of loss to <loss_type>"))
@when(parsers.cfparse("User changes the type of loss to '{loss_type}'"))
def change_loss_type_on_claim_intake_page(loss_type):
    avatarClaimsIntakePage.select_type_of_loss(loss_type)

@when(parsers.cfparse("User changes the service rep to <service_rep>"))
@when(parsers.cfparse("User changes the service rep to '{service_rep}'"))
def change_service_rep_on_claim_intake_page(service_rep):
    avatarClaimsIntakePage.select_service_rep(service_rep)


@when(parsers.cfparse("User changes the event name to <event_name>"))
@when(parsers.cfparse("User changes the event name to '{event_name}'"))
def change_the_event_name(event_name):
    avatarClaimsIntakePage.select_event_type(event_name)


@when(parsers.cfparse("User changes the claim status open to <claim_status>"))
@when(parsers.cfparse("User changes the claim status open to '{claim_status}'"))
def change_claim_status(claim_status):
    avatarClaimsIntakePage.select_claimstatusopen(claim_status)

@when('User clicks Payment tab')
def user_clicks_on_payment_tab():
    avatarClaimsIntakePage.click_payments_tab()

@when(parsers.cfparse("User enters '{date}' in payment tab"))
@when(parsers.cfparse('User enters <date> in payment tab'))
def user_selects_date(date):
    """User selects <date> in payment tab."""
    avatarClaimsIntakePage.input_payments_date(date)

@when(parsers.cfparse("User selects <TransactionType> in payment tab"))
@when(parsers.cfparse('User selects <TransactionType> in payment tab'))
def selects_transaction(TransactionType):
    """User selects <TransactionType> in payment tab"""
    avatarClaimsIntakePage.select_payments_transaction_type(TransactionType)


@when(parsers.cfparse("User selects <Transaction_sub_type> in payment tab"))
@when(parsers.cfparse('User selects <Transaction_sub_type> in payment tab'))
def selects_transaction_subtype(Transaction_sub_type):
    """User selects <Transaction_sub_type> in payment tab."""
    avatarClaimsIntakePage.select_payments_transaction_sub_type(Transaction_sub_type)

@when(parsers.cfparse("User enters <Description> in payment tab"))
@when(parsers.cfparse('User enters <Description> in payment tab'))
def user_enter_description(Description):
    """User enters <Description> in payment tab"""
    avatarClaimsIntakePage.input_payment_description(Description)

@when('User clicks on Claim Deductible button in payment tab')
def user_clicks_claimdectible_button():
    avatarClaimsIntakePage.click_claim_deductible()

@when('User selects Attachment tab')
def user_selects_attachment_tab():
    avatarClaimsIntakePage.click_attachments_tab()

@when(parsers.cfparse('User enter <Filename> in attachment tab'))
def user_enter_filenemae(Filename):
    avatarClaimsIntakePage.input_attachment_filename(Filename)

@when(parsers.cfparse('User selects <Authorisation> in attachment tab'))
def user_selects_authorisation(Authorisation):
    avatarClaimsIntakePage.select_attachment_authorisation(Authorisation)

@when(parsers.cfparse('User select <Attachment_type> in attachment tab'))
def user_selects_attachmenttype(Attachment_type):
    avatarClaimsIntakePage.select_attachment_attachmentype(Attachment_type)

@when(parsers.cfparse('User selects <document_type> in attachment tab'))
def user_selects_documenttype(document_type):
    avatarClaimsIntakePage.select_attachment_documenttype(document_type)

@when(parsers.cfparse('User enters <description> in attachment tab'))
def user_enters_description(description):
    avatarClaimsIntakePage.input_attachment_description(description)

@when('User attaches file <file_path> in attachment tab')
def user_attaches_file(file_path):
    avatarClaimsIntakePage.input_attachment_documentattach(file_path)

@when('User click on Add Attachment button in attachment tab')
def user_clicks_add_attachement():
    avatarClaimsIntakePage.click_add_attachment()

@when('User clicks Asso party tab')
def user_clicks_assoparty():
    avatarClaimsIntakePage.click_asso_party_tab()

@when('User clicks Add row button')
def user_clicks_addrow():
    avatarClaimsIntakePage.click_add_row()


@when('User clicks Add Info tab')
def user_clicks_add_info():
    avatarClaimsIntakePage.click_add_info_tab()

@when('User enters <total_estimate>')
def user_enters_total_estimate(total_estimate):

    avatarClaimsIntakePage.input_addinfo_totalestimate(total_estimate)

@when('User enters <release_amount>')

def user_enters_releaseamount(release_amount):
    avatarClaimsIntakePage.input_addinfo_releaseamount(release_amount)

@when('User clicks update button on Add info tab')
def user_clicks_update():
    avatarClaimsIntakePage.click_addinfo_update()

@when('User clicks Claim view button')
def user_clicks_claimview():
    avatarClaimsIntakePage.click_claimview_tab()

@when("User clicks on Update Claim button")
def click_update_claim_button():
    avatarClaimsIntakePage.click_updateclaim_btn()

@then(parsers.cfparse("User should see green toast having message '{expected_message}'"))
def verify_green_toast_message(expected_message):
    message = avatartoast.get_success_toast_message_if_exist()
    if message is not None:
        print("SUCCESS TOAST MESSAGE IS: ",message)
        if message.strip() == expected_message.strip():
            assert True
        else:
            print("EXPECTED MESSAGE:",expected_message,",ACTUAL MESSAGE:",message)
            assert False
    else:
        print("SUCCESS TOAST DOES NOT EXIST")
        assert False

   # assert avatartoast.verify_successful_toast_message(expected_message)

@then(parsers.cfparse("User should not see the red toast message"))
def verify_user_should_not_see_error_toast_message():
    message = avatartoast.get_error_toast_message_if_exist()
    if message is not None:
        print("ERROR TOAST MESSAGE IS: ",message)
        assert False
    else:
        print("ERROR TOAST DOES NOT EXIST")
        assert True
   # assert avatartoast.is_error_toast_present() is False




