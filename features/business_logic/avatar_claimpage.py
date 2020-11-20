from features.business_logic.locators.avatar_claimpage_locaters import AvatarClaimPageLocaters
from features.common_utilities.yaml_handler import YamlHandler
from features.common_utilities.file_folder_constants import FileFolderConstants
from features.common_utilities.driver_handler import DriverHandle
import time
import pytest

class AvatarClaimpage:

    def __init__(self):

        self.claimpage_locaters = AvatarClaimPageLocaters()
        self.driver_handler = DriverHandle()

    def click_on_edit_button(self):
        '''
        This method is used to click on edit button in claim page
        :return:
        '''
        try:
            self.driver_handler.click_element(self.claimpage_locaters.editclaim_btn)
            time.sleep(15)
        except Exception as e:
            raise Exception("Exception occured while clicking on edit button on claims page -->",e)



