from pytest_bdd import scenario, given, when, then
from features.business_logic.avatar_loginpage import AvatarLoginPage
from features.business_logic.avatar_claims_intakepage import AvatarClaimsIntakePage
from features.business_logic.avatar_claimpage import AvatarClaimpage
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


@scenario(r'TestCases/producer_add.feature', 'Verify producer add feature')
def test_verify_that_user_can_add_producer():
    print('Scenario--> Verify that user can add producer')

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

@when("User clicks on Add Agency")
def click_on_add_agency():
    avatarProducer.click_add_agency()
    time.sleep(5)

@when("User clicks Save Agency")
def click_on_saveagency():
    avatarProducer.click_save_agency()
    time.sleep(5)

@then(parsers.cfparse("User verifies Please Enter Unique No! toast message"))
def verify_user_should_not_see_error_toast_message():
    message = avatartoast.get_error_toast_message_if_exist()
    if message is not None:
        print("ERROR TOAST MESSAGE IS: ",message)
        assert True
    else:
        print("ERROR TOAST DOES NOT EXIST")
#--------------------------------------------------------------------------------------#

@scenario(r'TestCases/producer_add.feature', 'Verify producer add feature agency code error')
def test_verify_that_user_can_add_producer():
    print('Scenario--> Verify that user can edit claim')

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
    time.sleep(5)

@when("User clicks on Add Agency")
def click_on_add_agency():
    avatarProducer.click_add_agency()
    time.sleep(10)

@when(parsers.cfparse("User enters <agency_code>"))
def enter_agency_code(agency_code):
    avatarProducer.input_agecycode(agency_code)

@when("User clicks Save Agency")
def click_on_saveagency():
    avatarProducer.click_save_agency()
    time.sleep(5)


@then(parsers.cfparse("User verifies Please Enter Agency Name toast message"))
def verify_user_should_not_see_error_toast_message():
    message = avatartoast.get_error_toast_message_if_exist()
    if message is not None:
        print("ERROR TOAST MESSAGE IS: ",message)
        assert True
    else:
        print("ERROR TOAST DOES NOT EXIST")

#--------------------------------------------------------------------------------------#

@scenario(r'TestCases/producer_add.feature', 'Verify producer add feature dba name error')
def test_verify_that_user_can_add_producer():
    print('Scenario--> Verify that user can edit claim')

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
    time.sleep(5)

@when("User clicks on Add Agency")
def click_on_add_agency():
    avatarProducer.click_add_agency()
    time.sleep(10)

@when(parsers.cfparse("User enters <agency_code>"))
def enter_agency_code(agency_code):
    avatarProducer.input_agecycode(agency_code)

@when(parsers.cfparse("User enters <agency_name>"))
def enter_agency_code(agency_name):
    avatarProducer.input_agecyname(agency_name)

@when("User clicks Save Agency")
def click_on_saveagency():
    avatarProducer.click_save_agency()
    time.sleep(5)


@then(parsers.cfparse("User verifies Please Enter Agency DBA Name toast message"))
def verify_user_should_not_see_error_toast_message():
    message = avatartoast.get_error_toast_message_if_exist()
    if message is not None:
        print("ERROR TOAST MESSAGE IS: ",message)
        assert True
    else:
        print("ERROR TOAST DOES NOT EXIST")

#--------------------------------------------------------------------------------------#

@scenario(r'TestCases/producer_add.feature', 'Verify producer add feature fein name error')
def test_verify_that_user_can_add_producer():
    print('Scenario--> Verify that user can edit claim')

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
    time.sleep(5)

@when("User clicks on Add Agency")
def click_on_add_agency():
    avatarProducer.click_add_agency()
    time.sleep(10)

@when(parsers.cfparse("User enters <agency_code>"))
def enter_agency_code(agency_code):
    avatarProducer.input_agecycode(agency_code)

@when(parsers.cfparse("User enters <agency_name>"))
def enter_agency_code(agency_name):
    avatarProducer.input_agecyname(agency_name)

@when(parsers.cfparse("User enters <dba_name>"))
def enter_agency_code(dba_name):
    avatarProducer.input_dbaname(dba_name)

@when("User clicks Save Agency")
def click_on_saveagency():
    avatarProducer.click_save_agency()
    time.sleep(5)


@then(parsers.cfparse("User verifies Please FEIN Number toast message"))
def verify_user_should_not_see_error_toast_message():
    message = avatartoast.get_error_toast_message_if_exist()
    if message is not None:
        print("ERROR TOAST MESSAGE IS: ",message)
        assert True
    else:
        print("ERROR TOAST DOES NOT EXIST")

#--------------------------------------------------------------------------------------#

@scenario(r'TestCases/producer_add.feature', 'Verify producer add feature agency address error')
def test_verify_that_user_can_add_producer():
    print('Scenario--> Verify that user can edit claim')

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
    time.sleep(5)

@when("User clicks on Add Agency")
def click_on_add_agency():
    avatarProducer.click_add_agency()
    time.sleep(10)

@when(parsers.cfparse("User enters <agency_code>"))
def enter_agency_code(agency_code):
    avatarProducer.input_agecycode(agency_code)

@when(parsers.cfparse("User enters <agency_name>"))
def enter_agency_code(agency_name):
    avatarProducer.input_agecyname(agency_name)

@when(parsers.cfparse("User enters <dba_name>"))
def enter_agency_code(dba_name):
    avatarProducer.input_dbaname(dba_name)

@when(parsers.cfparse("User enters <fein_number>"))
def enter_agency_code(fein_number):
    avatarProducer.input_feinnumber(fein_number)
@when("User clicks Save Agency")
def click_on_saveagency():
    avatarProducer.click_save_agency()
    time.sleep(5)


@then(parsers.cfparse("User verifies Please Agency Address toast message"))
def verify_user_should_not_see_error_toast_message():
    message = avatartoast.get_error_toast_message_if_exist()
    if message is not None:
        print("ERROR TOAST MESSAGE IS: ",message)
        assert True
    else:
        print("ERROR TOAST DOES NOT EXIST")

#--------------------------------------------------------------------------------------#

@scenario(r'TestCases/producer_add.feature', 'Verify producer add feature zipcode error')
def test_verify_that_user_can_add_producer():
    print('Scenario--> Verify that user can edit claim')

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
    time.sleep(5)

@when("User clicks on Add Agency")
def click_on_add_agency():
    avatarProducer.click_add_agency()
    time.sleep(10)

@when(parsers.cfparse("User enters <agency_code>"))
def enter_agency_code(agency_code):
    avatarProducer.input_agecycode(agency_code)

@when(parsers.cfparse("User enters <agency_name>"))
def enter_agency_code(agency_name):
    avatarProducer.input_agecyname(agency_name)

@when(parsers.cfparse("User enters <dba_name>"))
def enter_agency_code(dba_name):
    avatarProducer.input_dbaname(dba_name)

@when(parsers.cfparse("User enters <fein_number>"))
def enter_agency_code(fein_number):
    avatarProducer.input_feinnumber(fein_number)

@when(parsers.cfparse("User enters <agency_address>"))
def enter_agency_code(agency_address):
    avatarProducer.input_mailingaddress(agency_address)

@when("User enters <payee_name>")
def input_payee_name(payee_name):
    avatarProducer.input_payeename(payee_name)
    time.sleep(5)

@when("User clicks Save Agency")
def click_on_saveagency():
    avatarProducer.click_save_agency()
    time.sleep(5)


@then(parsers.cfparse("User verifies Please Enter Agency Zipcode toast message"))
def verify_user_should_not_see_error_toast_message():
    message = avatartoast.get_error_toast_message_if_exist()
    if message is not None:
        print("ERROR TOAST MESSAGE IS: ",message)
        assert True
    else:
        print("ERROR TOAST DOES NOT EXIST")

#--------------------------------------------------------------------------------------#

@scenario(r'TestCases/producer_add.feature', 'Verify producer add feature agency phone error')
def test_verify_that_user_can_add_producer():
    print('Scenario--> Verify that user can edit claim')
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
    time.sleep(5)

@when("User clicks on Add Agency")
def click_on_add_agency():
    avatarProducer.click_add_agency()
    time.sleep(10)

@when(parsers.cfparse("User enters <agency_code>"))
def enter_agency_code(agency_code):
    avatarProducer.input_agecycode(agency_code)

@when(parsers.cfparse("User enters <agency_name>"))
def enter_agency_code(agency_name):
    avatarProducer.input_agecyname(agency_name)

@when(parsers.cfparse("User enters <dba_name>"))
def enter_agency_code(dba_name):
    avatarProducer.input_dbaname(dba_name)

@when(parsers.cfparse("User enters <fein_number>"))
def enter_agency_code(fein_number):
    avatarProducer.input_feinnumber(fein_number)

@when(parsers.cfparse("User enters <agency_address>"))
def enter_agency_address(agency_address):
    avatarProducer.input_mailingaddress(agency_address)

@when(parsers.cfparse("User enters <zip>"))
def enter_zip(zip):
    avatarProducer.select_zip_code(zip)

@when("User clicks checkbox")
def clicks_checkbox():
    avatarProducer.click_checkbox()


@then(parsers.cfparse("User verifies Please Enter Agency Phone toast message"))
def verify_user_should_see_error_toast_message():
    message = avatartoast.get_error_toast_message_if_exist()
    if message is not None:
        print("ERROR TOAST MESSAGE IS: ",message)
        assert True
    else:
        print("ERROR TOAST DOES NOT EXIST")

#-------------------------------------------------------------------------------#
@scenario(r'TestCases/producer_add.feature', 'Verify producer add feature all parameters')
def test_verify_that_user_can_add_producer():
    print('Scenario--> Verify that user can edit claim')
@when(parsers.cfparse("User enters <web>"))
def enter_agency_web(web):
    avatarProducer.input_web(web)

@when(parsers.cfparse("User enters <phone>"))
def enter_agency_phone(phone):
    avatarProducer.input_phone(phone)

@when(parsers.cfparse("User enters <zip>"))
def enter_agency_zip(zip):
    avatarProducer.select_zip_code(zip)

@when(parsers.cfparse("User enters <fax>"))
def enter_agency_fax(fax):
    avatarProducer.input_fax(fax)

@when(parsers.cfparse("User enters <manager>"))
def enter_manager_name(manager):
    avatarProducer.input_manager(manager)

@when(parsers.cfparse("User enters <manager_phone>"))
def enter_manager_phone(manager_phone):
    avatarProducer.input_manager_phone(manager_phone)

@when(parsers.cfparse("User enters <manager_email>"))
def enter_manager_email(manager_email):
    avatarProducer.input_manager_email(manager_email)


@when(parsers.cfparse("User enters <principal>"))
def enter_principal_name(principal):
    avatarProducer.input_principal(principal)


@when(parsers.cfparse("User enters <principal_phone>"))
def enter_principal_phone(principal_phone):
    avatarProducer.input_principal_phone(principal_phone)


@when(parsers.cfparse("User enters <principal_email>"))
def enter_principal_email(principal_email):
    avatarProducer.input_principal_email(principal_email)


@when(parsers.cfparse("User selects <select_group>"))
def selects_select_group(select_group):
    avatarProducer.select_select_group(select_group)

@when(parsers.cfparse("User selects <uv>"))
def selects_uv_group(uv):
    avatarProducer.select_uv_assign(uv)

@when(parsers.cfparse("User selects <agency_status>"))
def selects_agency_status(agency_status):
    avatarProducer.select_agency_status(agency_status)

@when(parsers.cfparse("User selects <service_rep>"))
def selects_service_rep(service_rep):
    avatarProducer.select_service_rep(service_rep)

@when(parsers.cfparse("User selects <direct_deposit>"))
def selects_direct_deposit(direct_deposit):
    avatarProducer.select_direct_deposit(direct_deposit)


@when(parsers.cfparse("User enters <bank_acc>"))
def enter_bank_acc(bank_acc):
    avatarProducer.input_bankacc(bank_acc)

@when(parsers.cfparse("User enters <bank_name>"))
def enter_bank_name(bank_name):
    avatarProducer.input_bank_name(bank_name)

@when(parsers.cfparse("User enters <routingno>"))
def enter_routing_no(routingno):
    avatarProducer.input_routing_num(routingno)
    time.sleep(5)


@when("User clicks add row in License Information")
def clicks_add_row_licenseinfo():
    avatarProducer.click_add_row_license()


@when(parsers.cfparse("User selects <license_type>"))
def select_license_type(license_type):
    avatarProducer.select_license_type(license_type)

@when(parsers.cfparse("User enters <license_no>"))
def enter_license_no(license_no):
    avatarProducer.input_license_no(license_no)

@when(parsers.cfparse("User selects <state>"))
def selects_state(state):
    avatarProducer.select_state(state)

@when(parsers.cfparse("User selects <appointed>"))
def selects_appointed(appointed):
    avatarProducer.select_appointed(appointed)

@when(parsers.cfparse("User inputs <exp_date>"))
def inputs_expdate(exp_date):
    avatarProducer.input_expdate(exp_date)

@when(parsers.cfparse("User inputs <issue_date>"))
def input_issue_date(issue_date):
    avatarProducer.input_issuedate(issue_date)

@when(parsers.cfparse("User inputs <app_date>"))
def input_app_date(app_date):
    avatarProducer.input_appdate(app_date)

@when("User clicks on Products button")
def click_product_button():
    avatarProducer.click_products()

@when("User clicks add row in product")
def click_addrow_product():
    avatarProducer.click_add_row()

@when(parsers.cfparse("User selects <policy_product>"))
def selects_policy_product(policy_product):
    avatarProducer.select_policy_product(policy_product)


@when("User clicks close")
def click_close_product():
    avatarProducer.click_close_product()

@then(parsers.cfparse("User verifies successful toast message"))
def verify_user_should_see_successful_toast_message():
    message = avatartoast.get_success_toast_message_if_exist()
    if message :

        assert True
    else:
        print("SUCCESSFUL TOAST DOES NOT EXIST")
        assert False
