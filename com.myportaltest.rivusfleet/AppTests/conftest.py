import pytest
from selenium import webdriver
from Config.config import SetupConfiguration as scd

@pytest.fixture(params=['firefox'], scope ='function')
def init_driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=scd.FireFoxInstance)
#     if request.param == 'Chrome':
#         driver = webdriver.Chrome(executable_path=r'C:\\Users\\612563313\\BTFleet_2020\\1.Auto_Fleet\\sel_driver\\geckodriver-v0.24.0-win64\\geckodriver.exe')
#     if request.param == 'ie':
#         driver = webdriver.Firefox(executable_path=r'C:\\Users\\612563313\\BTFleet_2020\\1.Auto_Fleet\\sel_driver\\geckodriver-v0.24.0-win64\\geckodriver.exe')
    driver.delete_all_cookies()
    driver.get(scd.base_URL)
    driver.maximize_window()        
    request.cls.driver =  driver
#     yield 
#     driver.close()

# #######################Generate HTML report #######################################################
# def pytest_configure(config):
#     config._metdata['Project Name']:'Fleet Portal'
#  
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA Home", None)
#     metadata.pop("Plugins", None)


            