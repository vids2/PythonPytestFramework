'''
Created on 28 Oct 2020

@author: 612563313
'''

from AppPages.WebdriverExtensions import WebdriverExtensions
from selenium.webdriver.common.by import By
from AppTestData.LoginPage_TestData import LoginPage_TestData as lptd
from AppPages.HomePage import HomePage
import time

class LaunchFP(WebdriverExtensions):
    
    email = (By.ID, 'i0116')
    SI_btn = (By.ID, 'idSIButton9')
    pwd = (By.ID, 'passwordInput')
    Submit_btn = (By.ID, 'submitButton')    
#     back_btn = (By.ID, '')
#     SI_opts = (By.ID, '')
#     CantAccess = (By.ID, '') 
#     Cancel_link = (By.ID, '')   

    def __init__(self,driver):
        super().__init__(driver)
        
 
    def chk_SIsupportLnkExists(self):
        SIOptsLink = self.IsElementVisible(self.SI_opts)
        AccAccess = self.IsElementVisible(self.CantAccess)
        return(SIOptsLink,AccAccess)
    
    def LoginToFP(self,UsrN,UsrP):        
        fp = lptd.SSpath
        fn = lptd.LP_ssName
        self.ClearAndTypeValueInto(self.email,UsrN)
#         SI_1 = self.getPageTitle(FPTestData.LP_title1)
        self.GetScreenShot(fp,fn)
        self.ClickElement(self.SI_btn)
        self.ClearAndTypeValueInto(self.pwd,UsrP)
        self.GetScreenShot(fp,fn)
        print('\n----------------------------\n')
#         SI_2 = self.getPageTitle(FPTestData.LP_title2)
        self.ClickElement(self.Submit_btn)
        time.sleep(5)
#         x = self.getPageTitle(FPTestData.HP_title)
#         assert x == FPTestData.HP_title
#         print("Login Succesfull")
        return HomePage(self.driver)
      
        