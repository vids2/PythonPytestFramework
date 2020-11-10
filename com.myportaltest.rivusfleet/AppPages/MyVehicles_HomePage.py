'''
Created on 28 Oct 2020

@author: 612563313
'''

from AppPages.WebdriverExtensions import WebdriverExtensions
from selenium.webdriver.common.by import By
from AppTestData.MyVehicles_TestData import MyVehicles_TestData as mvtd
from AppTestData.LoginPage_TestData import LoginPage_TestData as lptd

import time

class MyVehicles_Homepage(WebdriverExtensions):
    
    if_MyVehicles = (By.XPATH, "//*[@src='/myvehicles/']")
    VRN = (By.XPATH, "//*[@class='validate form-control' and @name = 'regno']")
    VehOptSel = (By.XPATH,"//*[@id='searchOption']")
    Search_btn = (By.XPATH,"//*[@class='btn btn-primary btn-sm' and @type='submit']")
    Reset_btn = (By.XPATH,"//*[@class='btn btn-primary btn-sm' and @type='reset']")

    InOptVal1= 'Vehicle Details'
    InOptVal2= 'Service History'
    InOptVal3= 'Vehicle Documents'
    InOptVal4= 'Tyre History'

    vp_outVRN_vde=(By.XPATH,"/html/body/div/ul/li[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]")   #For remaining Vehicle Type: VRN #
    vp_outVRN_sh = (By.XPATH,"/html/body/div/ul/li[9]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]") #For Service History#
    vp_outVRN_vdo= (By.XPATH,"/html/body/div/ul/li[8]/div[2]/form/div[2]/div[1]/div[1]") #For Vehicle Documents#
    vp_outVRN_th = (By.XPATH,"/html/body/div/ul/li[10]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]") #For Tyre History#    
    
    OutOptVal1 = (By.XPATH,"//div[@id='vehicle']") #For Vehicle Details#
    OutOptVal2 = (By.XPATH,"//div[@id='service']") #For Service History#
    OutOptVal3= (By.XPATH, "//div[@id='document']") #For Vehicle Documents#
    OutOptVal4 = (By.XPATH,"//div[@id='tyre']") #For Tyre History#

    dwnld_url1 = (By.XPATH,"/html/body/div/ul/li[1]/div[2]/div[1]/div/img[1]")  #For Vehicle Details#
    dwnld_url2 = (By.XPATH,"(//img[@alt='Download to Excel'])[8]")                     #For Service History#
    dwnld_url3 = (By.XPATH,"/html/body/div/ul/li[8]/div[2]/form/div[1]/div/img[1]")  #For Vehicle Documents#
    dwnld_url4 = (By.XPATH,"/html/body/div/ul/li[10]/div[2]/div[1]/div/img[1]") #For Tyre History#
     
     
    def __init__(self,driver):
        super().__init__(driver)
     
    def get_vehiclesdetails(self,InRegNo,InOptVal):
        ss_fn = mvtd.VP_ssName+ InRegNo+"_"+InOptVal
        print("Test for: My Vehicles")
        print('\nInput Selected: {}-{}'.format(InRegNo,InOptVal))
        self.IsElementVisible(self.if_MyVehicles)
        self.SwapToiframe(self.if_MyVehicles)
        self.ClearAndTypeValueInto(self.VRN, InRegNo)
        self.SelectSelectText(self.VehOptSel,InOptVal)
        self.GetScreenShot(lptd.SSpath ,ss_fn )
        self.ClickElement(self.Search_btn)
        self.SwapToSecondWindow()
        time.sleep(50)        
        if self.InOptVal1 == InOptVal:                       
            self.GetScreenShot(lptd.SSpath ,ss_fn)
            expTitle = self.getPageTitle(mvtd.VP_title)
            actVRN= self.GetElementTxt(self.vp_outVRN_vde)
            actVehOptSel= self.GetElementTxt(self.OutOptVal1)
#             self.ClickElement(self.dwnld_url1)
        elif self.InOptVal2 == InOptVal:
            self.GetScreenShot(lptd.SSpath ,ss_fn)
            expTitle = self.getPageTitle(mvtd.VP_title)
            actVRN= self.GetElementTxt(self.vp_outVRN_sh)
            actVehOptSel= self.GetElementTxt(self.OutOptVal2)
            self.ClickElement(self.dwnld_url2)
        elif self.InOptVal3 == InOptVal:
            self.GetScreenShot(lptd.SSpath ,ss_fn)
            expTitle = self.getPageTitle(mvtd.VP_title)
            actVRN= self.GetElementTxt(self.vp_outVRN_vdo)
            actVehOptSel= self.GetElementTxt(self.OutOptVal3)
#             self.ClickElement(self.dwnld_url3)
        elif self.InOptVal4 == InOptVal:
            self.GetScreenShot(lptd.SSpath ,ss_fn)
            expTitle = self.getPageTitle(mvtd.VP_title)
            actVRN= self.GetElementTxt(self.vp_outVRN_th)
            actVehOptSel= self.GetElementTxt(self.OutOptVal4)
#             self.ClickElement(self.dwnld_url4)
        else:
            print("No Valid Option Selected")
        print('The Result Matched : \ncurrent title: {}; Inputs: {}-{}'.format(expTitle,actVRN[-7:],actVehOptSel))
        return (expTitle,actVRN,actVehOptSel)    
        

         
         
     
     
     