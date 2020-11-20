from features.common_utilities.yaml_handler import YamlHandler
from features.common_utilities.file_folder_constants import FileFolderConstants
from features.common_utilities.driver_handler import DriverHandle
from features.business_logic.locators.avatar_loginpage_locaters import AvatarLoginPageLocaters
from features.common_utilities.path_properties import PathProperties
import time
import pytest
import os

class AvatarLoginPage:


    def __init__(self):

        self.loginpage_locaters = AvatarLoginPageLocaters()
        self.config_data = YamlHandler(PathProperties().get_config_path())
        self.driver_handler = DriverHandle()

    def open_avatar(self):
        try:
            self.driver_handler.get_url(self.config_data.get_base_url())
        except Exception as e:
            raise Exception("Expcetion occured while opening the home page -->",e)

    def login(self,pstr_user="default_user"):
        try:
            time.sleep(3)
            username,password = self.config_data.get_user_credentials(pstr_user)
            self.driver_handler.send_keys(self.loginpage_locaters.username_textbox, username)
            self.driver_handler.send_keys(self.loginpage_locaters.password_textbox, password)
            self.driver_handler.click_element(self.loginpage_locaters.login_button)
        except Exception as e:
            raise Exception("Exception occured while login -->",e)
