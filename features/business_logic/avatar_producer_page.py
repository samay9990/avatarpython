import time

from selenium.webdriver.common.keys import Keys

from features.business_logic.locators.avatar_claim_intakepage_locaters import AvatarClaimIntakePageLocaters
from features.business_logic.locators.avatar_producer_page_locators import AvatarProducerPageLocators
from features.common_utilities.driver_handler import DriverHandle


class AvatarProducerPage:

    def __init__(self):
        self.producer_locaters = AvatarProducerPageLocators()
        self.driver_handler = DriverHandle()

    def click_add_agency(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_addagency_btn)
        except Exception as e:
            raise Exception("Exception occured while clicking on add agency button -->", e)

    def click_save_agency(self):
        try:
            self.driver_handler.scroll_to_toppage()
            self.driver_handler.click_element(self.producer_locaters.producer_add_saveagency)
        except Exception as e:
            raise Exception("Exception occured while clicking on save agency button -->", e)

    def input_agecycode(self,pstr_agencycode):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_agencycode,pstr_agencycode)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->",e)

    def input_agecyname(self,pstr_agencyname):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_agencyname,pstr_agencyname)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency name field -->",e)

    def input_payeename(self,pstr_payeename):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_payeename,pstr_payeename)
        except Exception as e:
            raise Exception("Exception occurrred while sending input payee name field -->",e)

    def input_dbaname(self,pstr_dbaname):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_dbaname,pstr_dbaname)
        except Exception as e:
            raise Exception("Exception occurrred while sending input dba name field -->",e)

    def input_feinnumber(self,pstr_feinnumber):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_feinnuber,pstr_feinnumber)
        except Exception as e:
            raise Exception("Exception occurrred while sending input fein number field -->",e)

    def input_mailingaddress(self,pstr_mailingaddress):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_mailingaddress,pstr_mailingaddress)
        except Exception as e:
            raise Exception("Exception occurrred while sending input mailing address field -->",e)

    # def input_zip(self,pstr_zip):
    #
    #     try:
    #         self.driver_handler.send_keys(self.producer_locaters.producer,pstr_zip)
    #     except Exception as e:
    #         raise Exception("Exception occurrred while sending input zip field -->",e)

    def input_locationaddress(self,pstr_locationaddress):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_locationaddress,pstr_locationaddress)
        except Exception as e:
            raise Exception("Exception occurrred while sending input location address field -->",e)

    def input_web(self,pstr_web):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_web,pstr_web)
        except Exception as e:
            raise Exception("Exception occured while sending input to web field -->",e)

    def input_phone(self,pstr_phone):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_phone,pstr_phone)
        except Exception as e:
            raise Exception("Execetion occurred while sending input to phone field -->",e)

    def input_fax(self,pstr_fax):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_fax,pstr_fax)
        except Exception as e:
            raise Exception("Exception occurred while sending input to fax field -->",e)

    def select_direct_deposit(self,pstr_direct_deposit):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_directdeposit,pstr_direct_deposit)
        except Exception as e:
            raise Exception("Exception occurred while selecting dropdown in direct deposit -->",e)

    def input_manager(self,pstr_manager):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_manager,pstr_manager)
        except Exception as e:
            raise Exception("Exception occurred while sending input manager -->",e)

    def input_manager_phone(self,pstr_manager_phone):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_managerphone,pstr_manager_phone)
        except Exception as e:
            raise  Exception("Exception occurred while sending input to manager phone -->",e)

    def input_manager_email(self,pstr_manager_email):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_manageremail,pstr_manager_email)
        except Exception as e:
            raise Exception("Exception occurred while sending input to manager email -->",e)

    def input_principal(self,pstr_manager_principal):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_principal,pstr_manager_principal)
        except Exception as e:
            raise Exception("Exception occurred while sending input to manager principal -->",e)

    def input_principal_phone(self,pstr_principal_phone):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_principalphone,pstr_principal_phone)
        except Exception as e:
            raise Exception("Exception occurred while sending input to principal phone -->",e)

    def input_principal_email(self,pstr_principal_email):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_principalemail,pstr_principal_email)
        except Exception as e:
            raise Exception("Exception occurred while sending input to principal email -->",e)

    def click_add_row(self):
        try:
            time.sleep(4000)
            self.driver_handler.click_element(self.producer_locaters.producer_add_addrow)
            time.sleep(4000)
        except Exception as e:
            raise Exception("Exception occurred while clicking on add row -->",e)

    def select_licenseinfromation_license_type(self,pstr_license_type):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_licenseinformation_grid.replace("<<header_replace>>","LICENSE TYPE"),pstr_license_type)
        except Exception as e:
            raise Exception("Exception occurred while selecting license type -->",e)

    def select_licenseinfromation_license_no(self,pstr_license_no):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_licenseinformation_grid.replace("<<header_replace>>","LICENSE_NO."),pstr_license_no)
        except Exception as e:
            raise Exception("Exception occurred while input license number in license information grid -->",e)

    def select_licenseinfromation_state(self,pstr_state):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_licenseinformation_grid.replace("<<header_replace>>","STATE"),pstr_state)
        except Exception as e:
            raise Exception("Exception occurred while selecting state in license informaton grid from dropdown -->",e)

    # def select_licenseinfromation_appointed(self, pstr_appointed):
    #     try:
    #         self.driver_handler.select_visible_text_from_dropdown(
    #
    #     except Exception as e:
    #         raise Exception("Exception occurred while selecting state in license informaton grid from dropdown -->", e)

    def select_licenseinfromation_issuedate(self, pstr_issuedate):
        try:
            self.driver_handler.send_keys(
                self.producer_locaters.producer_licenseinformation_grid.replace("<<header_replace>>", "ISSUE DATE"),
                pstr_issuedate)
        except Exception as e:
            raise Exception("Exception occurred while selecting state in license informaton grid from dropdown -->", e)

    def select_licenseinfromation_expdate(self, pstr_expdate):
        try:
            self.driver_handler.send_keys(
                self.producer_locaters.producer_licenseinformation_grid.replace("<<header_replace>>", "EXP.DATE"),
                pstr_expdate)
        except Exception as e:
            raise Exception("Exception occurred while selecting state in license informaton grid from dropdown -->", e)

    def select_licenseinfromation_appdate(self, pstr_appdate):
        try:
            self.driver_handler.select_visible_text_from_dropdown(
                self.producer_locaters.producer_licenseinformation_grid.replace("<<header_replace>>", "APP.DATE"),
                pstr_appdate)
        except Exception as e:
            raise Exception("Exception occurred while selecting state in license informaton grid from dropdown -->", e)


    def select_select_group(self,pstr_select_group):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_selectgrup,pstr_select_group)
        except Exception as e:
            raise Exception("Exception occurred while selecting dropdown in select group -->",e)

    def select_uv_assign(self,pstr_select_group):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_uv,pstr_select_group)
        except Exception as e:
            raise Exception("Exception occurred while selecting dropdown in uv group -->",e)

    def select_agency_status(self,pstr_agency_status):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_agencystatus,pstr_agency_status)
        except Exception as e:
            raise Exception("Exception occurred while selecting dropdown in agency status -->",e)

    def select_service_rep(self,pstr_service_rep):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_servicerep,pstr_service_rep)
        except Exception as e:
            raise Exception("Exception occurred while selecting dropdown in service rep -->",e)

    def select_zip_code(self,pstr_zipcpde):
        try:
            time.sleep(5)
            self.driver_handler.send_keys(self.producer_locaters.producer_add_zip, pstr_zipcpde)
            self.driver_handler.send_keys(self.producer_locaters.producer_add_zip, Keys.TAB)
            self.driver_handler.click_element(self.producer_locaters.producer_add_selectzip)
        except Exception as e:
            raise Exception("Exception occurred while selecting zip  -->", e)

    def click_checkbox(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.prducer_add_checkbox)
            time.sleep(10)
        except Exception as e:
            raise Exception("Exception occurred while selecting zip  -->", e)

    def input_bankacc(self,pstr_bank_acc):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_bankacc,pstr_bank_acc)
        except Exception as e:
            raise Exception("Exception occurred while sending input to bank acc field -->",e)

    def input_bank_name(self,pstr_bank_name):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_bankname,pstr_bank_name)
        except Exception as e:
            raise Exception("Exception occurred while sending input to bank name field -->",e)

    def input_routing_num(self,pstr_routing):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_routingno,pstr_routing)
        except Exception as e:
            raise Exception("Exception occurred while sending input to routing no field -->",e)

    def input_license_no(self,pstr_license_no):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_licenseno,pstr_license_no)
        except Exception as e:
            raise Exception("Exception occured while sending input to license number" , e)

    def input_issuedate(self,pstr_issuedate):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_issuedate,pstr_issuedate)
        except Exception as e:
            raise Exception("Exception occured while sending issue date" , e)

    def input_expdate(self,pstr_expdate):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_expdate,pstr_expdate)
        except Exception as e:
            raise Exception("Exception occured while inputing exp date" , e)

    def input_appdate(self,pstr_appdate):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_add_appdate,pstr_appdate)
        except Exception as e:
            raise Exception("Exception occured while inputing app date" , e
                            )

    def select_license_type(self,pstr_licensetype):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_licensetype,pstr_licensetype)
        except Exception as e:
            raise Exception("Exception while selecting license type --->" ,e )

    def select_state(self,pstr_license_state):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_state,pstr_license_state)
        except Exception as e:
            raise Exception("Exception while selecting license state --->" ,e )

    def select_appointed(self,pstr_appointed):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_appointed,pstr_appointed)
        except Exception as e:
            raise Exception("Exception while selecting license appointed --->" ,e )

    def click_products(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_products_button)
        except Exception as e:
            raise Exception("Exception while clicking product button --->", e)

    def click_add_row(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_add_addrow)
        except Exception as e:
            raise Exception("Exception while clicking product button --->", e)

    def click_add_row_license(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_addrow_license)
        except Exception as e:
            raise Exception("Exception while clicking product button --->", e)


    def select_policy_product(self,pstr_policyproduct):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_policyproduct,pstr_policyproduct)
        except Exception as e:
            raise Exception("Exception while selecting policy product  --->" ,e )

    def select_policy_product(self,pstr_policyproduct):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_add_policyproduct,pstr_policyproduct)
        except Exception as e:
            raise Exception("Exception while selecting policy product  --->" ,e )

    def click_close_product(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_add_buttonclose)
            time.sleep(5)
        except Exception as e:
            raise Exception("Exception raised while clicking close button")