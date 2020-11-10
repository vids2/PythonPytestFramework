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
from AppTestData.MyVehicles_TestData import MyVehicles_TestData as mvtd 

class Test_HPMyVehicles(BaseTest):        

    @pytest.mark.parametrize("InRegNo,InOptVal",
                              mvtd.MyVehicleDetails_td()
                              )   
    def test_MyVehicleDetails(self,InRegNo,InOptVal):
        self.LaunchFP = LaunchFP(self.driver)
        self.HomePage = HomePage(self.driver)        
        HmePg = self.LaunchFP.LoginToFP(scd.UsrName,scd.UsrPwd)        
        HP_MyVeh = self.HomePage.getMyVehicles()
        Title,VRN,actVehOptSel = HP_MyVeh.get_vehiclesdetails(InRegNo,InOptVal)
        actVRN = VRN[-7:] 
        assert mvtd.VP_title == Title
        assert actVRN == InRegNo        
        assert actVehOptSel == InOptVal

    
                
        
    

    

        
        