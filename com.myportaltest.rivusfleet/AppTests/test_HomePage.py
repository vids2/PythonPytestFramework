'''
Created on 28 Oct 2020

@author: 612563313
'''

import pytest
import time
from AppTests.test_InitWebdriver import BaseTest
from Config.config import SetupConfiguration as scd
from AppPages.aFPLaunch import LaunchFP
from AppPages.HomePage import HomePage
from AppTestData.HomePage_TestData import HomePage_TestData as hptd

class XTest_HomePage(BaseTest):      

# SSAB: PASSED
    def test_HeaderLinks_VAB(self):
        self.LaunchFP = LaunchFP(self.driver)
        HmePg = self.LaunchFP.LoginToFP(scd.UsrName,scd.UsrPwd)
        HmePg.getHeaderElements(HomePage.VehicleAppointmentBooking,hptd.VAB_title)
        HdrLnk_title = self.driver.title
        assert hptd.VAB_title == HdrLnk_title
        

#         HmePg.getHeaderElements(HomePage.VehicleAppointmentBooking,hptd.VAB_title)
#         HdrLnk_title = self.driver.title
#         assert hptd.VAB_title == HdrLnk_title    
    
                
        
    

    

        
        