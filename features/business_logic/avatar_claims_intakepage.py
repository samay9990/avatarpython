import time

from features.business_logic.locators.avatar_claim_intakepage_locaters import AvatarClaimIntakePageLocaters
from features.common_utilities.driver_handler import DriverHandle


class AvatarClaimsIntakePage:

    def __init__(self):

        self.claimsintakepage_locaters = AvatarClaimIntakePageLocaters()
        self.driver_handler = DriverHandle()

    def select_claim_type(self,pstr_claimtype):
        '''
        Select claim type
        :param pstr_claimtype: claim type to select
        :return:
        '''
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.claimtype_selectbox, pstr_claimtype)
        except Exception as e:
            raise Exception("Exception occured while selecting claim type from dropdown -->",e)

    def select_type_of_loss(self,pstr_losstype):
        '''
        Select type of loss
        :param pstr_losstype: type of loss
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.typeofloss_selectbox, pstr_losstype)
        except Exception as e:
            raise Exception("Exception occured while selecting loss type from dropdown -->",e)

    def input_email_id(self,pstr_emailid):
        '''
        Method to input date in email id tab
        :param pstr_emailid:
        :return:
        '''

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.emailaddress_textbox,pstr_emailid)
        except Exception as e:
            raise Exception("Exception occured while adding date in payments tab -->",e)

    def input_date_loss(self,pstr_dateloss):
        '''
        Method to input date in email id tab
        :param pstr_emailid:
        :return:
        '''

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.dateloss_textbox,pstr_dateloss)
        except Exception as e:
            raise Exception("Exception occured while adding date in payments tab -->",e)

    def select_service_rep(self,pstr_servicerep):
        '''
        Select Service Rep from dropdown
        :param pstr_servicerep: service rep to select
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.servicerep_selectbox,pstr_servicerep)
        except Exception as e:
            raise Exception("Exception occured while selecting rep from dropdown -->",e)

    def select_claim_rep(self,pstr_claimrep):
        '''
        Select Service Rep from dropdown
        :param pstr_servicerep: service rep to select
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.claimreportedtype_selectbox,pstr_claimrep)
        except Exception as e:
            raise Exception("Exception occured while selecting rep from dropdown -->",e)

    def select_claim_substatus(self,pstr_claimsubstatus):
        '''
        Select Service Rep from dropdown
        :param pstr_servicerep: service rep to select
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.claimsubstatus,pstr_claimsubstatus)
        except Exception as e:
            raise Exception("Exception occured while selecting rep from dropdown -->",e)

    def select_location(self,pstr_location):
        '''
        Select Service Rep from dropdown
        :param pstr_servicerep: service rep to select
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.location_selectbox,pstr_location)
        except Exception as e:
            raise Exception("Exception occured while selecting rep from dropdown -->",e)

    def select_event_type(self,pstr_eventname):
        '''
        Select Event name from dropdown
        :param pstr_eventname: Event name to select
        :return:
        '''
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.eventname_selectbox,pstr_eventname)
        except Exception as e:
            raise Exception("Exception occured while selecting event type dropdown -->",e)

    def select_claimstatusopen(self,pstr_claimstatusopentype):
        '''
        Select Claim status open from dropdown
        :param pstr_claimstatusopentype: claim status open to select
        :return:
        '''
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.claimstatusopen_dropdown,pstr_claimstatusopentype)
        except Exception as e:
            raise Exception("Exception occured while selecting claim status open dropdown -->",e)

    def click_updateclaim_btn(self):
        '''
        Method to click on update claim button
        :return:
        '''
        try:
            self.driver_handler.click_element(self.claimsintakepage_locaters.updatecliam_btn)
        except Exception as e:
            raise Exception("Exception occrued while clicking on update claim button -->",e)

    def click_saveclaim_btn(self):
        '''
        Method to click on update claim button
        :return:
        '''
        try:
            self.driver_handler.click_element(self.claimsintakepage_locaters.saveclaim_btn)
        except Exception as e:
            raise Exception("Exception occrued while clicking on save claim button -->",e)



    def click_payments_tab(self):
        '''
        Method to navigat to payments tab
        :return:
        '''

        try:

            self.driver_handler.scroll_to_element(self.claimsintakepage_locaters.payments_button)
            time.sleep(5)
            self.driver_handler.click_element(self.claimsintakepage_locaters.payments_button)
            time.sleep(5)
        except Exception as e:
            raise Exception("Exception occured while clicking on payments tab -->",e)

    def input_payments_date(self,pstr_date):
        '''
        Method to input date in payments tab
        :param pstr_date:
        :return:
        '''

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.payments_date_inputdatebox,pstr_date)
        except Exception as e:
            raise Exception("Exception occured while adding date in payments tab -->",e)

    def select_payments_transaction_type(self,pstr_transaction_type):
        '''
        Method to select transaction type in payments tab
        :param pstr_transaction_type:
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.payments_transactiontype_selectbox,pstr_transaction_type)
        except Exception as e:
            raise Exception("Exception occurred while selecting transaction type in payments tab -->",e)

    def select_payments_transaction_sub_type(self,pstr_transactions_sub_type):
        '''
        Method to selec transactions sub type in payments tab
        :param pstr_transactions_sub_type:
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.payments_transactionsubtype_selectbox,pstr_transactions_sub_type)
        except Exception as e:
            raise Exception("Exception occurred while selecting transaction sub type in payments tab")


    def input_payment_description(self,pstr_description):
        '''
        Method to input description on payments tab
        :param pstr_description: 
        :return: 
        '''

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.payments_description_textarea,pstr_description)
        except Exception as e:
            raise Exception("Exception occurred while sending input to description box on payments page -->",e)

    def clickcheckbox_payment_refund(self):
        '''
        Method to click checkbox of refund on payments tab
        :return:
        '''

        try:
            self.driver_handler.click_element(self.claimsintakepage_locaters.payments_refund_checkbox)
        except Exception as e:
            raise Exception("Exception occurred while clicing on refund checkbox on payment refund page -->",e)

    def clickcheckbox_payment_refundcheck(self):
        '''
        Method to click checkbox of refund check on payments tab
        :return:
        '''

        try:
            self.driver_handler.click_element(self.claimsintakepage_locaters.payments_refundcheck_checkbox)
        except Exception as e:
            raise Exception("Exception occured while clicking on refund check checkbox on payment refund page -->",e)


    def  click_claim_deductible(self):
        '''
        Method to click on attachment tab
        :return:
        '''

        try:
            time.sleep(10)
            self.driver_handler.click_element(self.claimsintakepage_locaters.payments_claim_deductible_button)
        except Exception as e:
            raise Exception("Exception occurred while clicking on claim deductible button -->",e)

    def  click_add_attachment(self):
        '''
        Method to click on attachment tab
        :return:
        '''

        try:
            time.sleep(10)
            self.driver_handler.click_element(self.claimsintakepage_locaters.attachments_add_attachment)
        except Exception as e:
            raise Exception("Exception occurred while clicking on add attachment button -->",e)

    def  click_attachments_tab(self):
        '''
        Method to click on attachment tab
        :return:
        '''

        try:
            time.sleep(10)
            #self.driver_handler.scroll_to_element(self.claimsintakepage_locaters.payments_button)
            self.driver_handler.scroll_to_toppage()
            time.sleep(10)
            self.driver_handler.click_element(self.claimsintakepage_locaters.attachments_button)
        except Exception as e:
            raise Exception("Exception occurred while clicking on attachment tab on claim intake page -->",e)

    def input_attachment_filename(self,pstr_filename):
        '''
        Method to input filename in attachment tab
        :return:
        '''

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.attachments_filename_textbox,pstr_filename)
        except Exception as e:
            raise Exception("Exception occured while sending file name input  on attachment tab -->",e)

    def select_attachment_authorisation(self,pstr_authorisation):
        '''
        Method to select authorisation on attachment tab
        :param pstr_authorisation:
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.attachments_authorisation_selectbox,pstr_authorisation)
        except Exception as e:
            raise Exception("Exception occurred while selecting authorisation on attachment tab -->",e)

    def select_attachment_attachmentype(self,pstr_attachmenttype):
        '''
        Method to select attachment type on attachment tab
        :param pstr_attachmenttype:
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.attachments_attachmenttype_selectbox,pstr_attachmenttype)
        except Exception as e:
            raise Exception("Exception occurred while selecting attachment type on attachment tab -->",e)

    def select_attachment_documenttype(self,pstr_documenttype):
        '''
        Method to select document type on attachment tab
        :param pstr_documenttype:
        :return:
        '''

        try:
            self.driver_handler.select_visible_text_from_dropdown(self.claimsintakepage_locaters.attachments_documenttype_selectbox,pstr_documenttype)
        except Exception as e:
            raise Exception("Exception occurred while selecting document type on attachment tab --> ",e)

    def input_attachment_description(self,pstr_description):
        '''
        Method to input description on attachment tab
        :param pstr_description:
        :return:
        '''

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.attachments_description_textarea,pstr_description)
        except Exception as e:
            raise Exception("Exception occurrred while sending input in description on attachment tab -->",e)

    def input_attachment_documentattach(self,pstr_filepath):
        '''
        Method to input file path in document attach on attachment tab
        :param pstr_filepath:
        :return:
        '''

        try:
            self.driver_handler.send_keys_without_dispaly(self.claimsintakepage_locaters.attachments_documentattach_inputfile,pstr_filepath)
        except Exception as e:
            raise Exception("Exception occurred while inputing file path in document attach on attachment tab -->",e)

    def click_claimview_tab(self):
        '''
        Method to click on claim view tab
        :return:
        '''

        try:
            time.sleep(10)
            self.driver_handler.scroll_to_element(self.claimsintakepage_locaters.claimview_tab)
            self.driver_handler.click_element(self.claimsintakepage_locaters.claimview_tab)
        except Exception as e:
            raise Exception("Exception occurred while clicking on claim view tab -->",e)

    def click_add_info_tab(self):
        try:

            self.driver_handler.scroll_to_element(self.claimsintakepage_locaters.add_infotab)
            time.sleep(5)
            self.driver_handler.click_element(self.claimsintakepage_locaters.add_infotab)
        except Exception as e:
            raise Exception("Exception occured while clicking on addinfo tab -->",e)

    def input_addinfo_totalestimate(self,pstr_totalestimate):
        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.add_info_totalestimate,pstr_totalestimate)
        except Exception as e:
            raise Exception("Exception occurred while inputing total estimate in add info tab -->",e)

    def input_addinfo_releaseamount(self,pstr_releaseamount):
        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.add_info_releaseamount,pstr_releaseamount)
        except Exception as e:
            raise Exception("Exception occurred while inputing release amount in add info tab -->",e)

    def  click_addinfo_update(self):


        try:
            time.sleep(10)
            self.driver_handler.click_element(self.claimsintakepage_locaters.add_info_update)
        except Exception as e:
            raise Exception("Exception occurred while clicking on add info button -->",e)

    def click_asso_party_tab(self):
        try:

            #self.driver_handler.scroll_to_element(self.claimsintakepage_locaters.asso_party_tab)
            self.driver_handler.scroll_to_toppage()
            time.sleep(5)
            self.driver_handler.click_element(self.claimsintakepage_locaters.asso_party_tab)
        except Exception as e:
            raise Exception("Exception occured while clicking on asso party  tab -->",e)

    def click_add_row(self):


        try:
            time.sleep(10)
            self.driver_handler.click_element(self.claimsintakepage_locaters.asso_party_addrow)
        except Exception as e:
            raise Exception("Exception occurred while clicking on add row button in asso party -->",e)

    def input_nameoncheck_payment(self,pstr_nameoncheck):

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.payment_nameoncheck,pstr_nameoncheck)
        except Exception as e:
            raise Exception("Exception occurrred while sending input in name on check field -->",e)

    def input_invoicedate_payment(self, pstr_invoicedate):

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.payment_invoicedate, pstr_invoicedate)
        except Exception as e:
            raise Exception("Exception occurrred while sending input in invoice date field -->", e)

    def input_invoiceduedate_payment(self, pstr_invoiceduedate):

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.payment_invoiceduedatedate, pstr_invoiceduedate)
        except Exception as e:
            raise Exception("Exception occurrred while sending input in invoice due date field -->", e)

    def input_invoice_payment(self, pstr_invoice):

        try:
            self.driver_handler.send_keys(self.claimsintakepage_locaters.payment_invoice, pstr_invoice)
        except Exception as e:
            raise Exception("Exception occurrred while sending input in invoice field -->", e)


