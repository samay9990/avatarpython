from features.common_utilities.yaml_handler import YamlHandler
from features.common_utilities.file_folder_constants import FileFolderConstants
from features.common_utilities.driver_handler import DriverHandle
from features.business_logic.locators.avatar_toast_locaters import AvatarToastLocaters
from features.common_utilities.path_properties import PathProperties
import time
import pytest
import os

class AvatarToastMessages:

    def __init__(self):
        self.toast_locaters = AvatarToastLocaters()
        self.config_data = YamlHandler(PathProperties().get_config_path())
        self.driver_handler = DriverHandle()
        self.all_toasts_visible = None

    def verify_successful_toast_message(self,pstr_expected_messsage):
        '''
        This method is used to verify toast message
        :param pstr_expected_messsage: Expected message
        :return:
        '''
        try:
            actual_message = self.driver_handler.get_element_text(self.toast_locaters.successful_toast_alert)
            if actual_message.strip() == pstr_expected_messsage.strip():
                return True
            else:
                print("ACTUAL MESSAGE :",actual_message,",EXPECTED MESSAGE:",pstr_expected_messsage)
                return False
        except Exception as e:
            raise Exception("Exception occured while verifying successsful toast message -->",e)


    def is_error_toast_present(self):
        '''
        Checks weather error toast is displayed
        :return:  True if Yes else false
        '''
        try:
       #     self.driver_handler.turn_off_implicit_wait()
            if self.driver_handler.is_element_present(self.toast_locaters.error_toast_alert):
                print("ERROR TOAST PRESENT. MESSAGE IS :",self.driver_handler.get_element_text(self.toast_locaters.error_toast_alert,0))
                self.driver_handler.turn_on_implicit_wait()
                return True
            else:
                print("ERROR TOAST IS NOT PRESENT")
                self.driver_handler.turn_on_implicit_wait()
                return False
        except Exception as e:
            raise Exception("Exception occured while checking if error toast is present -->",e)

    def get_error_toast_message(self):
        '''
        Returns the error toast message
        :return:
        '''
        try:
            return self.driver_handler.get_element_text(self.toast_locaters.error_toast_alert)
        except Exception as e:
            raise Exception("Exception occurred while getting text from error toast -->",e)

    def get_all_toasts(self):
        '''
        Returns all toasts
        :return:
        '''
        try:
            all_toasts = self.driver_handler.get_elements(self.toast_locaters.all_toast_alert)
            self.all_toasts_visible = all_toasts
            return all_toasts
        except Exception as e:
            raise Exception("Exception occured while getting all toasts -->",e)

    def get_error_toast_message_if_exist(self):
        try:
            self.get_all_toasts()
            all_toasts = self.all_toasts_visible;
            for toast in all_toasts:
                if "error" in toast.find_element_by_xpath("..").get_attribute("class"):
                    return toast.get_attribute("innerHTML")
                else:
                    return None
        except Exception as e:
            raise Exception("Exception occurred while checking if error toast exists --> ",e)

    def get_success_toast_message_if_exist(self):
        try:
            self.get_all_toasts()
            all_toasts = self.all_toasts_visible;
            for toast in all_toasts:
                if "success" in toast.find_element_by_xpath("..").get_attribute("class"):
                    return toast.get_attribute("innerHTML")
            return None
        except Exception as e:
            raise Exception("Exception occurred while checking if Success toast exists --> ", e)

