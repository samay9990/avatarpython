from pathlib import Path
from features.common_utilities.file_folder_constants import FileFolderConstants
import os
class PathProperties:

    def __get_project_root(self):
        try:
            project_root_path = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent  # This is your Project Root
            return project_root_path
        except Exception as e:
            raise Exception("Exception occured while getting the project root path -->",e)

    def get_config_path(self):
        try:
            config_path = os.path.join(self.__get_project_root(), FileFolderConstants.CONFIG_FILE)
            return config_path
        except Exception as e:
            raise Exception("Exception occured while getting the config path -->",e)

    def __get_browsers_root_path(self):
        try:
            browsers_root_path = os.path.join(self.__get_project_root(), FileFolderConstants.BROWSERS_FOLDER)
            return browsers_root_path
        except Exception as e:
            raise Exception("Exception occured while getting the browsers root path --> ",e)

    def get_chromedriver_path(self):
        try:
            chromedriver_path = os.path.join(self.__get_browsers_root_path(), FileFolderConstants.CHROMEDRIVER)
            return chromedriver_path
        except Exception as e:
            raise Exception("Exception occured while getting the chromedriver path --> ",e)

    def get_firefoxdriver_path(self):
        try:
            firefoxdriver_path = os.path.join(self.__get_browsers_root_path(), FileFolderConstants.FIREFOXDRIRVER)
            return firefoxdriver_path
        except Exception as e:
            raise Exception("Exception occured while getting the firefoxdriver path -->",e)

