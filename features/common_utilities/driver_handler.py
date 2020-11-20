import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from features.common_utilities.yaml_handler import YamlHandler
from selenium.webdriver.remote.webdriver import WebDriver
from features.common_utilities.file_folder_constants import FileFolderConstants
from itertools import count
from features.common_utilities.path_properties import PathProperties
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import sys
import time
import pytest


class DriverHandle():
    # config_file_properties = YamlHandler(PathProperties().get_config_path())
    # def __init(self, pdriver=None):
    #     if pdriver is None:
    #         self.driver: 'WebDriver' = self.get_driver()
    def get_driver(self):

        driver: 'WebDriver' = pytest.driver
        return driver;

    def get_url(self, pstr_url):
        '''
        Open URL
        :param pstr_url: URL
        :return:
        '''
        try:
            self.get_driver().get(pstr_url)
        except Exception as e:
            raise Exception("Error occured while opening the url " + pstr_url + "-->", e)

    def send_keys(self, locater, pstr_text_to_send):
        '''
        Send keys to element
        :param locater: locater of element
        :param pstr_text_to_send: text to send to elemenet
        :return:
        '''
        try:
            self.wait_for_element_to_dispaly(locater)
            self.get_element(locater).send_keys(pstr_text_to_send)
        except Exception as e:
            raise Exception("Exception occured while sending text to element :", locater, "-->", e)

    def get_by(self, locater_type):
        try:
            if locater_type.lower() == 'xpath':
                locater_by = by.By.XPATH
            elif locater_type.lower() == 'id':
                locater_by = by.By.ID
            elif locater_type.lower() == 'css':
                locater_by = by.By.CSS_SELECTOR
            elif locater_type.lower() == 'link':
                locater_by = by.By.LINK_TEXT
            else:
                raise Exception("By of Locater not found for -->", locater_type)
            return locater_by
        except Exception as e:
            raise Exception("Error occurred while getting the by -->", e)

    def get_element(self, pstr_element_locater):
        try:
            split_locater = pstr_element_locater.split("=", 1)
            locater_type_by = self.get_by(split_locater[0])
            locater_identifer = split_locater[1]
            return self.get_driver().find_element(by=locater_type_by, value=locater_identifer)
        except Exception as e:
            raise Exception("Error occurred while getting the element :" + pstr_element_locater + "-->", e)

    def get_title(self):
        try:
            return self.get_driver().title
        except Exception as e:
            raise Exception("Error occured while getting the title of the page-->", e)

    def wait_for_element_to_dispaly(self, pstr_locater, pint_time_to_wait=20):
        try:
            count = 0
            while not self.get_element(pstr_locater).is_displayed():
                time.sleep(1)
                count+=1
                if count > pint_time_to_wait:
                    break;

            WebDriverWait(self.get_driver(), pint_time_to_wait).until(EC.visibility_of(self.get_element(pstr_locater)))
        except Exception as e:
            raise Exception("Exception occured while waiting for element to be located :", pstr_locater, " --> ", e)

    def click_element(self, pstr_locater):
        try:
            self.wait_for_element_to_dispaly(pstr_locater)
            self.get_element(pstr_locater).click()
        except Exception as e:
            raise Exception("Exception occured while clicking element :", pstr_locater, "-->", e)

    def get_elements(self, pstr_element_locater):
        #   time.sleep(5)
        try:
            split_locater = pstr_element_locater.split("=", 1)
            locater_type_by = self.get_by(split_locater[0])
            locater_identifer = split_locater[1]
            return self.get_driver().find_elements(by=locater_type_by, value=locater_identifer)
        except Exception as e:
            raise Exception("Error occurred while getting the element :" + pstr_element_locater + "-->", e)

    def verify_alert_message(self, expected_alert_message):
        time.sleep(5)
        try:
            alert_obj = self.get_driver().switch_to.alert
            message = alert_obj.text
            alert_obj.accept()
            if expected_alert_message in message:
                return True
            else:
                return False
        except Exception as e:
            raise Exception("Exception occured while verifying alert message -->", e)

    def select_visible_text_from_dropdown(self, pstr_locater, pstr_visibletext):
        try:
            self.wait_for_element_to_dispaly(pstr_locater)
            select_dropdown = Select(self.get_element(pstr_locater))
            select_dropdown.select_by_visible_text(pstr_visibletext)
        except Exception as e:
            raise Exception("Exception occured while selecting visible text from dropdown -->", e)

    def get_element_text(self, pstr_locater, pint_wait_for_element=20):
        try:
            self.wait_for_element_to_dispaly(pstr_locater, pint_wait_for_element)
            return self.get_element(pstr_locater).text
        except Exception as e:
            raise Exception("Exception occured while fetching element text -->", e)

    def is_element_present(self, locater):
        try:
        #    self.wait_for_element_to_dispaly(locater)
            split_locater = locater.split("=", 1)
            locater_type_by = self.get_by(split_locater[0])
            locater_identifer = split_locater[1]
            element = self.get_element(locater)
        #    element = WebDriverWait(self.get_driver(), 20).until(EC.presence_of_element_located((locater_type_by, locater_identifer)))
            if element is not None:
                return True
            else:
                return False
        except Exception as e:
            raise Exception("Exception occrued while checking if element is present -->",e)

    def turn_off_implicit_wait(self):
        try:
            self.get_driver().implicitly_wait(0)
        except Exception as e:
            raise Exception("Exception occurred while turning off implicit wait -->", e)

    def turn_on_implicit_wait(self):
        try:
            self.get_driver().implicitly_wait(20)
        except Exception as e:
            raise Exception("Exception occurred while turning on implicit wait -->", e)

    def scroll_to_element(self,pstr_locater):
        actions = ActionChains(self.get_driver())
        actions.move_to_element(self.get_element(pstr_locater)).perform()


    def send_keys_without_dispaly(self,pstr_locator,pstr_text_to_send):
        try:

            self.get_element(pstr_locator).send_keys(pstr_text_to_send)
        except Exception as e:
            raise Exception("Exception occured while sending text to element without display :", pstr_locator, "-->", e)

    def scroll_to_toppage(self):
        try:
            actions = ActionChains(self.get_driver())
            self.get_driver().find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

        except Exception as e:
            raise Exception("Exception occured while scrolling to top of the page ")

    def scroll_to_bottom(self):
        try:
            actions = ActionChains(self.get_driver())
            self.get_driver().find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)

        except Exception as e:
            raise Exception("Exception occured while scrolling to end of the page ")

    def clear_field(self, locater):
        '''
        Send keys to element
        :param locater: locater of element
        :param pstr_text_to_send: text to send to elemenet
        :return:
        '''
        try:
            self.wait_for_element_to_dispaly(locater)
            self.get_element(locater).clear()
        except Exception as e:
            raise Exception("Exception occured while clearing the element :", locater, "-->", e)
