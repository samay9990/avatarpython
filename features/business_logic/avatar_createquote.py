
import time

from selenium.webdriver.common.keys import Keys

from features.business_logic.locators.avatar_claim_intakepage_locaters import AvatarClaimIntakePageLocaters
from features.common_utilities.driver_handler import DriverHandle
from features.business_logic.locators.avatar_createquote_locators import AvatarCreateQuoteLocators

class AvatarCreateQuote:

    def __init__(self):
        self.createquote_locaters = AvatarCreateQuoteLocators()
        self.driver_handler = DriverHandle()

    def click_create_quote(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_createquote)
        except Exception as e:
            raise Exception("Exception occured while clicking on create quote -->", e)

    def input_firstname(self , pstr_firstname):
        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_firstname , pstr_firstname)
        except Exception as e:
            raise Exception("Exception occured while inputing first name -->", e)

    def input_lastname(self, pstr_lastname):

        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_lastname, pstr_lastname)
        except Exception as e:
            raise Exception("Exception occurrred while inputing last name -->", e)

    def input_dob(self, pstr_dob):

        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_dob, pstr_dob)
        except Exception as e:
            raise Exception("Exception occurrred while input of dob-->", e)

    def input_occupation(self, pstr_occupation):

        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_occupation, pstr_occupation)
        except Exception as e:
            raise Exception("Exception occurred while entering occupation-->", e)

    def input_houseno(self,pstr_houseno):
        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_house_no,pstr_houseno)

        except Exception as e:
            raise Exception("Exception occurred while entering house number-->", e)



    def error_exist(self):
        try:
            return self.driver_handler.is_element_present(self.createquote_locaters.policy_errors)

        except Exception as e:
            raise Exception("Exception occurred while verifying error --->" , e)

    def click_cancel(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_cancel)

        except Exception as e:
            raise Exception("Exception occurred while clicking cancel button --->", e)

    def click_rate(self):
        try:
            self.driver_handler.scroll_to_bottom()
            self.driver_handler.click_element(self.createquote_locaters.policy_rate)

        except Exception as e:
            raise Exception("Exception occurred while clicking rate button --->", e)

    def click_ho3_owner(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_ho3_homeowners)

        except Exception as e:
            raise Exception("Exception occurred while clicking ho3 owner button --->", e)

    def click_ho6_owner(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_ho6_homeowners)

        except Exception as e:
            raise Exception("Exception occurred while clicking ho6 owner button --->", e)

    def click_mdp_direct(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_mdp_direct)

        except Exception as e:
            raise Exception("Exception occurred while clicking mdp direct button --->", e)

    def click_mho_direct(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_mho_direct)

        except Exception as e:
            raise Exception("Exception occurred while clicking mdp direct button --->", e)



    def click_elements_ho6(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_elements_ho6_select)

        except Exception as e:
            raise Exception("Exception occurred while clicking mdp direct button --->", e)

    def click_elements_ho3(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_elements_ho3_select)

        except Exception as e:
            raise Exception("Exception occurred while clicking mdp direct button --->", e)


    def click_ho3_diamond(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_ho3_diamond)

        except Exception as e:
            raise Exception("Exception occurred while clicking mdp direct button --->", e)

    def click_policy_tab(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_tab)

        except Exception as e:
            raise Exception("Exception occurred while clicking policy tab --->", e)

    def input_streetname(self, pstr_streetname):

        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_streetname, pstr_streetname)
        except Exception as e:
            raise Exception("Exception occurred while entering street name-->", e)

    def input_zipcode(self, pstr_zipcode):

        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_postalcode, pstr_zipcode)
            self.driver_handler.send_keys(self.createquote_locaters.policy_postalcode,Keys.TAB)
            if self.driver_handler.is_element_present(self.createquote_locaters.policy_select_city):
                self.driver_handler.click_element(self.createquote_locaters.policy_city)
        except Exception as e:
            raise Exception("Exception occurred while entering postal code-->", e)


    def select_ppc(self,pstr_ppc):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_ppc,pstr_ppc)

        except Exception as e:
            raise Exception("Exception occured while selecting ppc --->" ,e)

    def select_bceg(self,pstr_bceg):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_bceg,pstr_bceg)

        except Exception as e:
            raise Exception("Exception occurred while selecting bceg --->" , e)

    def select_construction_type(self, pstr_constructiontype):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_constrcution_type,pstr_constructiontype)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)

    def input_yearbuilt(self, pstr_yearbuilt):

        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_yearbuilt, pstr_yearbuilt)
        except Exception as e:
            raise Exception("Exception occurred while entering postal code-->", e)

    def click_propertydetails(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_propertydetails)

        except Exception as e:
            raise Exception("Exception occurred while clicking property details " , e)

    def click_coverages(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_coverages_tab)

        except Exception as e:
            raise Exception("Exception occurred while clicking coverages tab -->", e )

    def click_deductibles(self):
        try:
            self.driver_handler.click_element(self.createquote_locaters.policy_deductibles_tab)

        except Exception as e:
            raise Exception("Exception occurred while clicking coverages tab -->", e)

    def input_dwelling(self,pstr_dwelling):
        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_dwelling,pstr_dwelling)

        except Exception as e:
            raise Exception("Exception occurred sending input to dwelling field -->" , e)

    def input_nor(self,pstr_nor):
        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_nor,pstr_nor)

        except Exception as e:
            raise Exception("Exception occurred sending input to nor field -->" , e)


    def input_firestn(self,pstr_firestn):
        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_firestn,pstr_firestn)

        except Exception as e:
            raise Exception("Exception occurred sending input to nor field -->" , e)

    def input_hydrant(self,pstr_hydrant):
        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_hydrant,pstr_hydrant)

        except Exception as e:
            raise Exception("Exception occurred sending input to nor field -->" , e)

    def input_areasqft(self,pstr_areasqft):
        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_area_sqft,pstr_areasqft)

        except Exception as e:
            raise Exception("Exception occurred sending input to area sqft field -->" , e)

    def input_personal_property(self,pstr_personal_property):
        try:
            self.driver_handler.send_keys(self.createquote_locaters.policy_personal_property, pstr_personal_property)

        except Exception as e:
            raise Exception("Exception occurred sending input to dwelling field -->", e)

    def select_personal_liability(self, pstr_perosnal_liability):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_personal_liability,pstr_perosnal_liability)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)

    def select_medical_payments(self, pstr_medical_payments):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_medical_payments,pstr_medical_payments)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)

    def select_nonhurricane(self, pstr_nonhurricane):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_nonhurricane,pstr_nonhurricane)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)

    def select_coverage_limit(self, pstr_covglimt):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_covergae_limit,pstr_covglimt)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)

    def select_coverage_limit2(self, pstr_covglimt2):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_coverage_limit2,pstr_covglimt2)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)





    def select_hurricane(self, pstr_hurricane):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_hurricane,pstr_hurricane)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)

    def select_roof(self, pstr_roof):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_roof_type,pstr_roof)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)

    def select_roofsubtype(self, pstr_roofsubtype):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_roof_subtype,pstr_roofsubtype)

        except Exception as e:
            raise Exception("Exception occurred while selection construction type-->" , e)

    def select_structure_type(self, pstr_structure_type):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_structure_type,pstr_structure_type)

        except Exception as e:
            raise Exception("Exception occurred while selection structure type-->" , e)


    def verify_errortext_exists(self,pstr_errortext):
        try:
            self.driver_handler.is_element_present(self.createquote_locaters.policy_error_in_text.replace('<<replace_header>>',pstr_errortext))
            print("Error containing keyword "+ pstr_errortext+" exists")
        except Exception as e:
            raise Exception("Exception occurred while verifying the text in error",e)

    def verify_errortext_notpresent(self,pstr_errornotpresent):

        try:
            if self.driver_handler.is_element_present(self.createquote_locaters.policy_error_in_text.replace('<<replace_header>>',pstr_errornotpresent)):
                return False
            else:
                return True
        except Exception as e:
            raise Exception("Exception occurred while verifying the text in error",e)

    def select_occupancy_type(self, pstr_occupancy_type):
        try:
            self.driver_handler.select_visible_text_from_dropdown(self.createquote_locaters.policy_occupancy_type,pstr_occupancy_type)

        except Exception as e:
            raise Exception("Exception occurred while selection occupancy type-->" , e)


    def verify_premium_value(self):
        try:
            str_premium_value = self.driver_handler.get_element_text(self.createquote_locaters.policy_premium_value)
            if (str_premium_value == ''):
                return False

            else:
                print("Value of the premium is--->"+ str_premium_value)
                return True

        except Exception as e:
            raise Exception("Exception occurred while verifying premiun value-->" , e)


