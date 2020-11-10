import time
import os
from Utilities import Utils
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class WebdriverExtensions:
    
    ss_Cnt = 1
    
    def __init__(self, driver):
        self.driver = driver
        
    def NavigateToURL(self,URL):
        self.driver.get(URL)
        
    def getPageTitle(self,title):
        WebDriverWait(self.driver,20).until(EC.title_is(title))
        return self.driver.title 
    
    def getCurrentPgTitle(self):
            time.sleep(1)
            return self.driver.title        
        
    def ClearAndTypeValueInto(self, locatorSelect, inputValue):
        InTxt = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect))
        InTxt.clear()
        InTxt.send_keys(inputValue)  
        
    def ClickElement(self, locatorSelect):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect)).click()      
        
    def IsElementVisible(self,locatorSelect):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect)).is_displayed()
        return bool(element)        
    
    def IsElementEnabled(self,locatorSelect):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect)).is_enabled()
        return bool(element)

    def DoesElementExist(self, locatorSelect):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect))
        return bool(element)
    
    def SelectSelectText(self, locatorSelect, optionText):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect))
        dropDownSelect = Select(element)
        dropDownSelect.select_by_visible_text(optionText)
        
    def getListValues(self,locatorSelect):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect))
        return element.text
    
    def GetElementTxt(self, locatorSelect):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect))
        return element.text            
        
    def GetScreenShot(self,SS_dir, SS_filename):
        lclCnt = self.ss_Cnt
        fn = SS_dir+SS_filename+str(lclCnt)+"_"+Utils.nowTsttime+".png" 
        if not os.path.exists(SS_dir):
            os.makedirs(SS_dir)
        if os.path.isfile(fn):
            lclCnt = lclCnt+1
            fn = SS_dir+SS_filename+str(lclCnt)+"_"+Utils.nowTsttime+".png"
        else:
            lclCnt=1
            fn = SS_dir+SS_filename+str(lclCnt)+"_"+Utils.nowTsttime+".png"
        WebdriverExtensions.ss_Cnt = lclCnt
        self.driver.get_screenshot_as_file(fn)
        
    def SelectRadioButton(self, locatorSelect, elementPosition):
        pass
    
    def SwapToSecondWindow(self):
        CurrWin = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != CurrWin:
#                 print(handle)
                nxtWin = handle
                break
        self.driver.switch_to.window(nxtWin)     
    
    def WaitForElement(self,locatorSelect):
        pass    
  
    def SwapToiframe(self,  locatorSelect):     
        InTxt = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locatorSelect))
        self.driver.switch_to.frame(InTxt)
        
    def getDwnLdFile(self, filepath, locatorSelect):
        ff_opt = webdriver.FirefoxOptions()
        ff_prefs = {"download.default_directory": filepath,"safebrowsing.enabled":"false"}
        ff_opt.add_experimental_option("prefs",ff_prefs)
        self.driver = webdriver.Firefox(firefox_options=ff_opt)
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locatorSelect)).click()
        
                                                               