from features.business_logic.locators.avatar_topnavbar_locaters import AvatarTopnavBarLocaters
from features.common_utilities.yaml_handler import YamlHandler
from features.common_utilities.file_folder_constants import FileFolderConstants
from features.common_utilities.driver_handler import DriverHandle
import time
import pytest

class AvatarTopNavBar():


    def __init__(self):

        self.topnav_locaters = AvatarTopnavBarLocaters()
        self.driver_handler = DriverHandle()

    def click_on_claims(self):
        try:
            self.driver_handler.click_element(self.topnav_locaters.topnav_claims_btn)
        except Exception as e:
            raise Exception("Exception occured while clicking on claims top nav -->",e)

    def click_on_producer(self):
        try:
            self.driver_handler.click_element(self.topnav_locaters.topnav_producer)
        except Exception as e:
            raise Exception("Exception occured while clicking on claims top nav -->",e)

