from features.business_logic.locators.avatar_claims_homepage_locaters import AvatarClaimsHomePageLocaters
from features.common_utilities.yaml_handler import YamlHandler
from features.common_utilities.file_folder_constants import FileFolderConstants
from features.common_utilities.driver_handler import DriverHandle
import time
import pytest

class AvatarClaimsHomepage:

    def __init__(self):

        self.claimshomepage_locaters = AvatarClaimsHomePageLocaters()
        self.driver_handler = DriverHandle()

    def enter_claim_number(self,pstr_claimnumber):

        '''
        This method is used to enter claim number in claim search box
        :param pstr_claimnumber: clam number to search
        :return:
        '''
        try:
            self.driver_handler.send_keys(self.claimshomepage_locaters.claimno_textbox,pstr_claimnumber)
        except Exception as e:
            raise Exception("Exception occurred while entering value in claim number -->",e)
    def add_policy_number(self,pstr_policynumber):

        '''
        This method is used to enter claim number in claim search box
        :param pstr_claimnumber: clam number to search
        :return:
        '''
        try:
            self.driver_handler.send_keys(self.claimshomepage_locaters.policy_textbox,pstr_policynumber)
            print("POLICY NUMBER ADDED")
        except Exception as e:
            raise Exception("Exception occurred while entering value in claim number -->",e)

    def click_search_button(self):
        '''
        This method is used to click on search button
        :return:
        '''
        try:
            self.driver_handler.click_element(self.claimshomepage_locaters.search_btn)
            print("CLICKED ON SEARCH BUTTON")
        except Exception as e:
            raise Exception("Exception occured while clicking on search button on claims page-->",e)

    def click_add_button(self):
        '''
        This method is used to click on search button
        :return:
        '''
        try:
            self.driver_handler.click_element(self.claimshomepage_locaters.addclaim_btn)
            print("CLICKED ON ADD BUTTON")
        except Exception as e:
            raise Exception("Exception occured while clicking on search button on claims page-->",e)

    def click_on_claim_number_in_search_grid(self,pstr_claimnumber):
        '''
        This method is used to click on claim number in search grid
        :param pstr_claimnumber: claim number to click on
        :return:
        '''
        try:
            claim_searchgrid_locater = self.claimshomepage_locaters.searchgrid_claimnumber_link.replace("<<claim_number>>",pstr_claimnumber)
            self.driver_handler.click_element(claim_searchgrid_locater)
        except Exception as e:
            raise Exception("Exception occured while clicking on cliam number in search grid -->",e)

    def click_on_policy_number_in_search_grid(self,pstr_policynumber):
        '''
        This method is used to click on claim number in search grid
        :param pstr_claimnumber: claim number to click on
        :return:
        '''
        try:
            claim_searchgrid_locater = self.claimshomepage_locaters.searchgrid_policynumber_link.replace("<<policynumber>>",pstr_policynumber)
            self.driver_handler.click_element(claim_searchgrid_locater)
        except Exception as e:
            raise Exception("Exception occured while clicking on cliam number in search grid -->",e)