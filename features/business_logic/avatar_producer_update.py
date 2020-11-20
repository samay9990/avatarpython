import time

from selenium.webdriver.common.keys import Keys

from features.business_logic.locators.avatar_claim_intakepage_locaters import AvatarClaimIntakePageLocaters
from features.business_logic.locators.avatar_producer_page_locators import AvatarProducerPageLocators
from features.common_utilities.driver_handler import DriverHandle


class AvatarProducerUpdatePage:

    def __init__(self):
        self.producer_locaters = AvatarProducerPageLocators()
        self.driver_handler = DriverHandle()

    def input_payee_name(self,pstr_payeename):
        try:
            self.driver_handler.clear_field(self.producer_locaters.producer_add_payeename)
            self.driver_handler.send_keys(self.producer_locaters.producer_add_payeename,pstr_payeename)
        except Exception as e:
            raise Exception("Exception occurrred while sending input payee name code field -->",e)



    def click_update_agency(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_updateagency_btn)

        except Exception as e:
            raise Exception("Exception occured while clicking on save agency button -->", e)

    def verify_update_log(self,pstr_updated_value):
        try:
            if self.driver_handler.is_element_present(
                    self.producer_locaters.producer_update_log_value.replace('<<header_replace>>',
                                                                                     pstr_updated_value)):
                return True
            else:
                return False
        except Exception as e:
            raise Exception("Exception occurred while searching updated value -->", e)

    def click_update_log(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_updatedlogs_button)
        except Exception as e:
            raise Exception("Exception occurred while clicking updated value -->", e)

    def click_agency_visit_review(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_agency_visit_review)
        except Exception as e:
            raise Exception("Exception occurred while clicking agency visit review  -->", e)

    def input_pre_visit(self, pstr_previsit):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agency_previsit_note, pstr_previsit)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_staff_notes(self, pstr_staffnotes):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agency_staff_note, pstr_staffnotes)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_agent_requests(self, pstr_agent_requests):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agency_agent_requests, pstr_agent_requests)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_visit_review(self, pstr_visitreview):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agency_visit_notes, pstr_visitreview)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def click_agency_submit(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_agency_submit)
            time.sleep(5)
            self.driver_handler.scroll_to_toppage()
            self.driver_handler.click_element(self.producer_locaters.producer_agency_close)
            self.driver_handler.click_element(self.producer_locaters.producer_add_buttonclose)
        except Exception as e:
            raise Exception("Exception occurred while clicking agency visit review  -->", e)

    def click_add_log(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_agency_addlog)

        except Exception as e:
            raise Exception("Exception occurred while clicking agency visit review  -->", e)

    def click_document(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_documents_button)

        except Exception as e:
            raise Exception("Exception occurred while clicking document button  -->", e)

    def click_document_submit(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_document_submit)

        except Exception as e:
            raise Exception("Exception occurred while clicking document button  -->", e)

    def click_document_close(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_document_close)

        except Exception as e:
            raise Exception("Exception occurred while clicking document button  -->", e)

    def input_document_filename(self, pstr_filename):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_document_file_name, pstr_filename)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_document_file(self, pstr_file):

        try:
            self.driver_handler.send_keys_without_dispaly(self.producer_locaters.producer_document_file_name, pstr_file)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def select_file_type(self, pstr_filetype):

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_document_file_type, pstr_filetype)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_user_id(self, pstr_userid):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_userid, pstr_userid)
        except Exception as e:
            raise Exception("Exception occurrred while sending input user id field -->", e)

    def input_sub_agent_id(self, pstr_sub_agent):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_subagentid, pstr_sub_agent)
        except Exception as e:
            raise Exception("Exception occurrred while sending sub agent id code field -->", e)

    def input_firstname(self, pstr_firstname):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_firstname, pstr_firstname)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_middlename(self, pstr_middlename):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_middlename, pstr_middlename)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_lastname(self, pstr_lastname):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_lastname, pstr_lastname)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_screenname(self, pstr_screenname):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_screenname, pstr_screenname)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_email(self, pstr_email):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_email, pstr_email)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_phone(self, pstr_phone):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_phonenumber, pstr_phone)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def select_status(self, pstr_status):

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_agencyuserform_userstatus, pstr_status)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def select_userlevel(self, pstr_userlevel):

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_agencyuserform_userlevel, pstr_userlevel)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_effdatefrom(self, pstr_effdate):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_efffrom, pstr_effdate)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)


    def input_effdateto(self, pstr_effdateto):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agencyuserform_effto, pstr_effdateto)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def click_save_agency_user(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_agency_save_agency)

        except Exception as e:
            raise Exception("Exception occurred while clicking document button  -->", e)

    def click_close(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_agency_user_close)

        except Exception as e:
            raise Exception("Exception occurred while clicking document button  -->", e)


    def click_agency_button(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_agencyusers_button)

        except Exception as e:
            raise Exception("Exception occurred while clicking agency user button  -->", e)

    def click_addrow(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_agencyuserform_addrow)

        except Exception as e:
            raise Exception("Exception occurred while clicking document button  -->", e)

    def click_upload_doc(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_doc_uploadbtn)

        except Exception as e:
            raise Exception("Exception occurred while clicking document button  -->", e)

    def click_close_doc(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_doc_closebtn)

        except Exception as e:
            raise Exception("Exception occurred while clicking document button  -->", e)

    def select_product_agencyform(self, pstr_product):

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_agency_product, pstr_product)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def select_state(self, pstr_state):

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_agency_state, pstr_state)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def select_uvassign(self, pstr_uvassign):

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_agency_uvassign, pstr_uvassign)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)


    def select_authorization(self, pstr_authorization):

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.producer_locaters.producer_agency_authorization, pstr_authorization)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)


    def input_agency_visitdate(self,pstr_visitdate):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_agency_visit_date, pstr_visitdate)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->", e)

    def input_doc_filename(self,pstr_filename):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_doc_filename,pstr_filename)

        except Exception as e:
            raise Exception("Exception occured while inputing file name-->" , e)


    def input_doc_filepath(self,pstr_doc_filepath):
        try:
            self.driver_handler.send_keys_without_dispaly(self.producer_locaters.producer_dragdrop_file,pstr_doc_filepath)

        except Exception as e:
            raise Exception("Exception occured while inputing file name-->" , e)

    def input_date_doc(self,pstr_date_doc):
        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_doc_uploaddate,pstr_date_doc)

        except Exception as e:
            raise Exception("Exception occured while inputing file name-->" , e)

    def click_doctype(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_doc_doctype)
            self.driver_handler.click_element(self.producer_locaters.producer_doc_selectdoctype)

        except Exception as e:
            raise Exception("Exception occured while inputing file name-->" , e)


