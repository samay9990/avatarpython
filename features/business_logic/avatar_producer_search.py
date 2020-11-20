import time

from selenium.webdriver.common.keys import Keys

from features.business_logic.locators.avatar_claim_intakepage_locaters import AvatarClaimIntakePageLocaters
from features.business_logic.locators.avatar_producer_page_locators import AvatarProducerPageLocators
from features.common_utilities.driver_handler import DriverHandle


class AvatarProducerSearchPage:

    def __init__(self):
        self.producer_locaters = AvatarProducerPageLocators()
        self.driver_handler = DriverHandle()



    def select_agent_code(self, pstr_agent_code):
        try:

            self.driver_handler.click_element(self.producer_locaters.producer_select_agencycode.replace("<<header_replace>>", pstr_agent_code))
        except Exception as e:
            raise Exception("Exception occurred while selecting agency code grid from table -->", e)

    def input_search_agecycode(self,pstr_searchagencycode):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_search_agencycode,pstr_searchagencycode)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->",e)

    def input_fein_number(self,pstr_feinnumber):

        try:
            self.driver_handler.send_keys(self.producer_locaters.producer_search_feinnumber,pstr_feinnumber)
        except Exception as e:
            raise Exception("Exception occurrred while sending input agency code field -->",e)

    def click_search_btn(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_search_searchbtn)
        except Exception as e:
            raise Exception("Exception occurrred while clicking search button -->",e)

    def click_search_agency(self):
        try:
            self.driver_handler.click_element(self.producer_locaters.producer_searchagency_btn)
        except Exception as e:
            raise Exception("Exception occurrred while clicking search agency button -->",e)

    def verify_agent_code(self , pstr_agencycode):
        try:
            if self.driver_handler.is_element_present(self.producer_locaters.producer_search_verify_agencycode.replace('<<replace_header>>',pstr_agencycode)):
                return True
            else:
                return False
        except Exception as e:
            raise Exception("Exception occurrred while clicking search agency button -->", e)





