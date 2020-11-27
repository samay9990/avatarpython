import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from features.common_utilities.path_properties import PathProperties
from features.common_utilities.yaml_handler import YamlHandler
import allure
class Annotations:

    config_properties = YamlHandler(PathProperties().get_config_path())

    def common_config(self):
        """
        Description:
        	|  this method is to initialize the common_config

        """
        pytest.driver = None

    def before_scenario(self):
        """
        Description:
               	|  this method is to initialize webdriver and open browser
        """
        try:
            browser = self.config_properties.get_browser_config().lower()
            if browser == 'chrome':
                driver_path = PathProperties().get_chromedriver_path()
                print("Browser Path:", driver_path)
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument("--window-size=1920x1080")
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                pytest.driver = webdriver.Chrome(driver_path,chrome_options=chrome_options)
            elif browser == 'firefox':
                driver_path = PathProperties().get_firefoxdriver_path()
                print("Browser Path:", driver_path)
                pytest.driver = webdriver.Firefox()
            pytest.driver.maximize_window()
            pytest.driver.implicitly_wait(20)
        except Exception as e:
            print('Error in before_scenario-->' + str(e))

    def pytest_take_screenshot(self):

        try:
            allure.attach(pytest.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print('Error in AFTER STEP-->' + str(e))

    def after_scenario(self):
        """
        Description:
                | This method is to initialize webdriver and open browser
        """
        pytest.driver.close()