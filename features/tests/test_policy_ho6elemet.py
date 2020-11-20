# coding=utf-8
"""Avatar Policy Create Quote feature tests."""

from features.business_logic.avatar_loginpage import AvatarLoginPage
from features.business_logic.avatar_claims_intakepage import AvatarClaimsIntakePage
from features.business_logic.avatar_claimpage import AvatarClaimpage
from features.business_logic.avatar_topnavbar import AvatarTopNavBar
from features.business_logic.avatar_claims_homepage import AvatarClaimsHomepage
from features.business_logic.avatar_toast_messages import AvatarToastMessages
from features.business_logic.avatar_createquote import AvatarCreateQuote
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
avatarCreatequote = AvatarCreateQuote()
avatarClaimPage = AvatarClaimpage()
avatarTopNavBar = AvatarTopNavBar()
avatarClaimsHomepage = AvatarClaimsHomepage()
avatartoast = AvatarToastMessages()


@scenario('TestCases\policy_createquote_elementho6select.feature', 'Verify the HO6 Element fields under policy')
def test_verify_the_ho6_element_fields_under_policy():
    """Verify the HO6 Element fields under policy."""


@given('User is on Avatars login page')
def user_is_on_avatars_login_page():
    """User is on Avatars login page."""
    avatarLoginPage.open_avatar()


@when('User clicks HO6 Elements card')
def user_clicks_mdp_direct_card():
    """User clicks HO3 Homeowners card."""
    avatarCreatequote.click_elements_ho6()


@when('User clicks Property Details')
def user_clicks_property_details():
    """User clicks Property Details."""
    avatarCreatequote.click_propertydetails()



@when('User clicks Rate button')
def user_clicks_rate_button():
    """User clicks Rate button."""
    avatarCreatequote.click_rate()
    time.sleep(5)


@when('User clicks coverage tab')
def user_clicks_coverage_tab():
    """User clicks coverage tab."""
    avatarCreatequote.click_coverages()



@when('User clicks on create quote from left hand navigation bar')
def user_clicks_on_create_quote_from_left_hand_navigation_bar():
    """User clicks on create quote from left hand navigation bar."""
    avatarCreatequote.click_create_quote()


@when('User clicks on policy on top navigation bar')
def user_clicks_on_policy_on_top_navigation_bar():
    """User clicks on policy on top navigation bar."""
    avatarCreatequote.click_policy_tab()

@when('User enters <dob>')
def user_enters_dob(dob):
    """User enters <dob>."""
    avatarCreatequote.input_dob(dob)


@when('User enters <dwelling>')
def user_enters_dwelling(dwelling):
    """User enters <dwelling>."""
    avatarCreatequote.input_dwelling(dwelling)



@when('User enters <first_name>')
def user_enters_first_name(first_name):
    """User enters <first_name>."""
    avatarCreatequote.input_firstname(first_name)


@when('User enters <house_number>')
def user_enters_house_number(house_number):
    """User enters <house_number>."""
    avatarCreatequote.input_houseno(house_number)


@when('User enters <last_name>')
def user_enters_last_name(last_name):
    """User enters <last_name>."""
    avatarCreatequote.input_lastname(last_name)


@when('User enters <occupation>')
def user_enters_occupation(occupation):
    """User enters <occupation>."""
    avatarCreatequote.input_occupation(occupation)


@when('User enters <street_name>')
def user_enters_street_name(street_name):
    """User enters <street_name>."""
    avatarCreatequote.input_streetname(street_name)


@when('User enters <year_built>')
def user_enters_year_built(year_built):
    """User enters <year_built>."""
    avatarCreatequote.input_yearbuilt(year_built)


@when('User enters <zip_code>')
def user_enters_zip_code(zip_code):
    """User enters <zip_code>."""
    avatarCreatequote.input_zipcode(zip_code)

@when(parsers.cfparse("User logs in with user '{user}'"))
def click_on_login_btn(user):
    avatarLoginPage.login(user)
    print("User clicked on item")

@when('User selects <bceg>')
def user_selects_bceg(bceg):
    """User selects <bceg>."""
    avatarCreatequote.select_bceg(bceg)


@when('User selects <construction_type>')
def user_selects_construction_type(construction_type):
    """User selects <construction_type>."""
    avatarCreatequote.select_construction_type(construction_type)


@when('User selects <ppc>')
def user_selects_ppc(ppc):
    """User selects <ppc>."""
    avatarCreatequote.select_ppc(ppc)


@then('User should be able to see error msg window')
def user_should_be_able_to_see_error_msg_window():
    """User should be able to                                                                                                                                                                                                                                                                                                                                                                                                                 see error msg window."""
    avatarCreatequote.error_exist()


@when('User selects <cvg_limit>')
def user_selects_cvg_limit(cvg_limit):
    """User selects <cvg_limit>."""
    avatarCreatequote.select_coverage_limit(cvg_limit)

@when('User selects <cvg_liability>')
def user_selects_cvg_limit(cvg_liability):
    """User selects <cvg_limit>."""
    avatarCreatequote.select_coverage_limit2(cvg_liability)


@when('User selects <hurricane>')
def user_selects_hurricane(hurricane):
    """User selects <hurricane>."""
    avatarCreatequote.select_hurricane(hurricane)
    time.sleep(5)


@when('User selects <medical_payments>')
def user_selects_medical_payments(medical_payments):
    """User selects <medical_payments>."""
    avatarCreatequote.select_medical_payments(medical_payments)


@when('User selects <non_hurricane>')
def user_selects_non_hurricane(non_hurricane):
    """User selects <non_hurricane>."""
    avatarCreatequote.select_nonhurricane(non_hurricane)


@when('User selects <personal_liability>')
def user_selects_personal_liability(personal_liability):
    """User selects <personal_liability>."""
    avatarCreatequote.input_personal_property(personal_liability)

@when('User clicks on deductible tab')
def user_clicks_on_deductible_tab():
    """User clicks on deductible tab."""
    avatarCreatequote.click_deductibles()

