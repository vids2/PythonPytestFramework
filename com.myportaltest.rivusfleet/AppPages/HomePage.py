'''
Created on 28 Oct 2020

@author: 612563313
'''

from AppPages.WebdriverExtensions import WebdriverExtensions
from selenium.webdriver.common.by import By
from AppTestData.HomePage_TestData import HomePage_TestData as hptd
from AppTestData.LoginPage_TestData import LoginPage_TestData as lptd
from AppPages.MyVehicles_HomePage import MyVehicles_Homepage
import time

class HomePage(WebdriverExtensions):
    
    UsrSIelemval= "//a[text()='"+hptd.HP_UsrSI+"']"
    LogdUsr = (By.XPATH, UsrSIelemval)
#     HeaderElemnts =  {
#                     'Home':(By.XPATH,""),
#                     'MyLinks':(By.XPATH,"//ul[@class='navbar-nav flex-row float-left']//a[@class='nav-link'][contains(text(),'My Links')]"),
#                     'MyCommunities':(By.XPATH,"//ul[@class='navbar-nav flex-row float-left']//a[@class='nav-link'][contains(text(),'My Communities')]"),
# #                     'MISReports':(By.XPATH,""),
# #                     'NetworkGarageLocator':(By.XPATH,""),
#                     'VehicleAppointmentBooking':(By.XPATH,"//ul[@class='navbar-nav flex-row float-left']//a[@class='nav-link'][contains(text(),'Vehicle Appointment Booking')]")
# #                     'FleetInsights':(By.XPATH,""),
# #                     'ContactUs':(By.XPATH,"")
#                 }
    VehicleAppointmentBooking=(By.XPATH,"//ul[@class='navbar-nav flex-row float-left']//a[@class='nav-link'][contains(text(),'Vehicle Appointment Booking')]")
    MyLinks=(By.XPATH,"//ul[@class='navbar-nav flex-row float-left']//a[@class='nav-link'][contains(text(),'My Links')]"),

    def __init__(self,driver):
        super().__init__(driver)
        
 
    def getHeaderElements(self,Locator,title):
        self.ClickElement(Locator)
        time.sleep(1)
        self.SwapToSecondWindow()
        self.getPageTitle(title)
        self.GetScreenShot(lptd.SSpath, title)
        
    def getMyVehicles(self):
        return MyVehicles_Homepage(self.driver)
        