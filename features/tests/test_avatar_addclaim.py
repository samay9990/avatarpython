# coding=utf-8
"""Avatar Add Claim feature tests."""
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
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

avatarLoginPage = AvatarLoginPage()
avatarClaimsIntakePage = AvatarClaimsIntakePage()
avatarClaimPage = AvatarClaimpage()
avatarTopNavBar = AvatarTopNavBar()
avatarClaimsHomepage = AvatarClaimsHomepage()
avatartoast = AvatarToastMessages()
@scenario('TestCases\claim_add.feature', 'Verify that user can add new claim')
def test_verify_that_user_can_add_new_claim():
    """Verify that user can add claim - 2."""


@given('User is on Avatar Insurance Login Page')
def user_is_on_avatar_insurance_login_page():
    avatarLoginPage.open_avatar()
    print("User navigated to Home Page")
    """User is on Avatar Insurance Login Page."""
    #raise NotImplementedError


@when(parsers.cfparse("User logs in with user '{user}'"))
def click_on_login_btn(user):
    avatarLoginPage.login(user)
    print("User clicked on item")


@when("User clicks on claim in top navigation bar")
def click_on_claim_in_top_navigation_bar():
    avatarTopNavBar.click_on_claims()


@when('User clicks Add Claim button')
def user_clicks_on_update_claim_button():
    """User clicks on Update Claim button."""
    avatarClaimsHomepage.click_add_button()
    time.sleep(10)

@when(parsers.cfparse("User enters policy number <policynumber>"))
@when(parsers.cfparse("User enters policy number '{policynumber}'"))
def user_enters_policy_number_hofl200163690(policynumber):
    """User enters policy number 'HOFL200163690'."""
    avatarClaimsHomepage.add_policy_number(policynumber)


@when('User clicks Search button')
def user_clicks_search_button():
    """User clicks Search button."""
    #raise NotImplementedError
    avatarClaimsHomepage.click_search_button()
    time.sleep(5)

@when(parsers.cfparse("User clicks on the Policy number '{policynumber}' from the table"))
@when(parsers.cfparse('User clicks on the Policy number <policynumber> from the table'))
def user_clicks_on_the_policy_number_hofl200163690_from_the_table(policynumber):
    """User clicks on the Policy number 'HOFL200163690' from the table."""
    avatarClaimsHomepage.click_on_policy_number_in_search_grid(policynumber)
    time.sleep(5)
    #raise NotImplementedError

@when(parsers.cfparse("User selects '{select_location}' from the dropdown"))
@when(parsers.cfparse('User selects <select_location> from the dropdown'))

def user_selects_select_location_from_the_dropdown(select_location):
    """User selects <select_location> from the dropdown."""
    #raise NotImplementedError
    avatarClaimsIntakePage.select_location(select_location)

@when(parsers.cfparse("User changes the claim type to '{claim_type}'"))
@when(parsers.cfparse('User selects the claim type to <claim_type>'))
def user_selects_the_claim_type_to_claim_type(claim_type):
    """User selects the claim type to <claim_type>."""
    avatarClaimsIntakePage.select_claim_type(claim_type)


@when(parsers.cfparse("User selects the type of loss to <loss_type>"))
@when(parsers.cfparse("User selects the type of loss to '{loss_type}'"))
def selects_loss_type_on_claim_intake_page(loss_type):
    """User selects the claim type to <loss_type>."""
    avatarClaimsIntakePage.select_type_of_loss(loss_type)


@when(parsers.cfparse("User selects the service rep to <service_rep>"))
@when(parsers.cfparse("User selects the service rep to '{service_rep}'"))
def selects_service_rep_on_claim_intake_page(service_rep):
    """User selects the claim type to <service_rep>."""
    avatarClaimsIntakePage.select_service_rep(service_rep)

@when(parsers.cfparse("User selects '{date_of_loss}'"))
@when(parsers.cfparse('User selects <date_of_loss>'))
def selects_date_of_loss(date_of_loss):
    """User selects <date_of_loss>."""
    avatarClaimsIntakePage.input_date_loss(date_of_loss)

@when(parsers.cfparse("User selects the event name to <event_name>"))
@when(parsers.cfparse("User selects the event name to '{event_name}'"))
def selects_the_event_name(event_name):
    """User selects the <event_name>."""
    avatarClaimsIntakePage.select_event_type(event_name)

@when(parsers.cfparse("User enters the <email_id>"))
@when(parsers.cfparse("User enters the '{email_id}'"))
def user_enters_the_email_id(email_id):
    """User enters the <email_id>."""
    avatarClaimsIntakePage.input_email_id(email_id)


@when(parsers.cfparse("User selects <claim_reported_by>"))
@when(parsers.cfparse("User selects '{claim_reported_by}'"))

def user_selects_claim_reported_by(claim_reported_by):
    """User selects <claim_reported_by>."""
    avatarClaimsIntakePage.select_claim_rep(claim_reported_by)


@when(parsers.cfparse("User selects <claim_sub_status>"))
@when(parsers.cfparse("User selects '<claim_sub_status>'"))
def user_selects_claim_sub_status(claim_sub_status):
    """User selects <claim_sub_status>."""
    avatarClaimsIntakePage.select_claim_substatus(claim_sub_status)

@when('User clicks on Save Claim button')
def user_clicks_on_save_claim_button():
    """User clicks on save Claim button."""
    #raise NotImplementedError
    avatarClaimsIntakePage.click_saveclaim_btn()
    time.sleep(20)

@when('User clicks Payment tab')
def user_clicks_on_payment_tab():
    avatarClaimsIntakePage.click_payments_tab()

@when(parsers.cfparse("User enters '{date}' in payment tab"))
@when(parsers.cfparse('User enters <date> in payment tab'))
def user_selects_date(date):
    """User selects <date> in payment tab."""
    avatarClaimsIntakePage.input_payments_date(date)

@when(parsers.cfparse("User selects <Transaction_sub_type> in payment tab"))
@when(parsers.cfparse('User selects <Transaction_sub_type> in payment tab'))
def selects_transaction_subtype(Transaction_sub_type):
    """User selects <Transaction_sub_type> in payment tab."""
    avatarClaimsIntakePage.select_payments_transaction_sub_type(Transaction_sub_type)


@when(parsers.cfparse("User selects <TransactionType> in payment tab"))
@when(parsers.cfparse('User selects <TransactionType> in payment tab'))
def selects_transaction(TransactionType):
    """User selects <TransactionType> in payment tab"""
    avatarClaimsIntakePage.select_payments_transaction_type(TransactionType)

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

@when('User click on Add Attachment button in attachment tab')
def user_clicks_add_attachement():
    avatarClaimsIntakePage.click_add_attachment()

@when('User clicks Claim View Tab from attachment tab')
def user_clicks_on_claimvew_tab():
    avatarClaimsIntakePage.click_payments_tab()




@then('User should not see the red toast message')
def user_should_not_see_the_red_toast_message():
    """User should not see the red toast message."""
    #raise NotImplementedError


@then('User should see green toast having message \'Claim details stored successfully\'')
def user_should_see_green_toast_having_message_claim_details_stored_successfully():
    """User should see green toast having message 'Claim details stored successfully'."""
    #raise NotImplementedError

