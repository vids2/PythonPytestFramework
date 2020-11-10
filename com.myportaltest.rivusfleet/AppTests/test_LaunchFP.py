'''
Created on 28 Oct 2020

@author: 612563313
'''

import pytest
import time
from selenium.webdriver.common.by import By


from AppTests.test_InitWebdriver import BaseTest
from Config.config import SetupConfiguration as scd
from AppPages.aFPLaunch import LaunchFP
from AppTestData.LoginPage_TestData import LoginPage_TestData as lptd
from AppTestData.HomePage_TestData import HomePage_TestData as hptd

class XTest_LaunchFP(BaseTest):
    
    def test_ValidateUserLogin(self):
        self.LaunchFP = LaunchFP(self.driver)
        self.LaunchFP.LoginToFP(scd.UsrName,scd.UsrPwd)
        time.sleep(3)
        HmePgTitle = self.LaunchFP.getCurrentPgTitle()
        self.LaunchFP.GetScreenShot(lptd.SSpath, hptd.HP_ssName) 
        exp_LogInUsr = scd.UsrName[:-7].replace('.', ' ').title()
        locVal = "//a[contains(text(),'"+exp_LogInUsr+"')]"
        LoggedInUsr = self.driver.find_element(By.XPATH,locVal).text
        assert HmePgTitle == hptd.HP_title
        assert LoggedInUsr == exp_LogInUsr
        print('LoggedInUsr:{} matches exp_LogInUsr:{} '.format(LoggedInUsr,exp_LogInUsr))
          
    @pytest.mark.parametrize("Usr,Pwd",
                              [ pytest.param(scd.UsrName,scd.UsrPwd, id = "valid creds"),
                               pytest.param("Usrabc","Pwdqdfe",marks = pytest.mark.xfail,id="invalid creds")]
                              )   
    def test_ValidateUserLogin_withMultipleInput(self,Usr,Pwd):
        self.LaunchFP = LaunchFP(self.driver)
        self.LaunchFP.LoginToFP(Usr,Pwd)       
        


        
        
    
    

