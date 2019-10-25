import unittest, time, HtmlTestRunner, os, sys
from selenium import webdriver
from properties import Properties
from selenium.common.exceptions import NoSuchElementException
from termcolor import colored
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Six20TestCase(unittest.TestCase):
    
    def setUp (self):
        portrait_mode = {
            "deviceName": "Pixel 2 XL"
        }
        landscape_mode = {
            "deviceMetrics": { "width": 823, "height": 411 }
        }
        chrome_options1 = Options()
        chrome_options2 = Options()
        chrome_options3 = Options()
        if sys.platform == 'win32':
            chrome_options1.add_argument("--start-maximized")
        else:
            chrome_options1.add_argument("--kiosk")
        chrome_options1.add_argument("--incognito")
        chrome_options2.add_experimental_option("mobileEmulation", portrait_mode)
        chrome_options3.add_experimental_option("mobileEmulation", landscape_mode)
        self.driver = webdriver.Chrome(Properties.select_driver(), chrome_options=chrome_options1)
        self.driver2 = webdriver.Chrome(Properties.select_driver(), chrome_options=chrome_options2)
        self.driver3 = webdriver.Chrome(Properties.select_driver(), chrome_options=chrome_options3)
    
    def tearDown(self):
        self.driver = None
        self.driver2 = None
      
    def testcase01_Six20HomePage_Desktop(self):
        try:
            self.driver.get("https://six-20.com")
            self.driver.get_screenshot_as_file("screenshots/test0101_header.png") 
            self.driver.execute_script("window.scrollTo(0,841);")
            self.driver.get_screenshot_as_file("screenshots/test0102_websitedesign.png")
            self.driver.execute_script("window.scrollTo(0,1541);")
            self.driver.get_screenshot_as_file("screenshots/test0103_socialmedia.png")
            self.driver.execute_script("window.scrollTo(0,2341);")
            self.driver.get_screenshot_as_file("screenshots/test0104_payperclick.png") 
            self.driver.execute_script("window.scrollTo(0,3041);")
            self.driver.get_screenshot_as_file("screenshots/test0105_seostrategy.png")
            self.driver.execute_script("window.scrollTo(0,3841);")
            self.driver.get_screenshot_as_file("screenshots/test0106_videomarketing.png")
            self.driver.execute_script("window.scrollTo(0,4786);")
            self.driver.get_screenshot_as_file("screenshots/test0107_branding.png")
            self.driver.execute_script("window.scrollTo(0,5600);")
            self.driver.get_screenshot_as_file("screenshots/test0108_ourteam.png")
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.get_screenshot_as_file("screenshots/test0109_itstime.png")
            self.driver.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    
    def testcase02_AboutUs(self):
        try:
            self.driver.get("https://six-20.com/about-us")           
            self.driver.get_screenshot_as_file("screenshots/test0201_header.png")
            self.driver.execute_script("window.scrollTo(0,800);")
            self.driver.get_screenshot_as_file("screenshots/test0202_experience.png")
            self.driver.execute_script("window.scrollTo(0,1300);")
            self.driver.get_screenshot_as_file("screenshots/test0202_experience2.png")
            self.driver.execute_script("window.scrollTo(0,2000);")
            self.driver.get_screenshot_as_file("screenshots/test0203_freeconsultation.png")
            self.driver.execute_script("window.scrollTo(0,2900);")
            self.driver.get_screenshot_as_file("screenshots/test0204_pioneer.png")
            self.driver.execute_script("window.scrollTo(0,4000);")
            self.driver.get_screenshot_as_file("screenshots/test0206_strategic.png")
            self.driver.execute_script("window.scrollTo(0,4800);")
            self.driver.get_screenshot_as_file("screenshots/test0207_people.png")
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//app-about-us/div[9]/div[2]/div[1]/div[1]/div[2]"))).click()
            self.driver.get_screenshot_as_file("screenshots/test0208_mattshow.png")
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//app-about-us/div[9]/div[2]/div[1]/div[2]/div[1]"))).click()
            self.driver.get_screenshot_as_file("screenshots/test0209_mattwide.png")
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.get_screenshot_as_file("screenshots/test0210_dontdelay.png")
            self.driver.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase03_OurServices(self):
        try:
            self.driver.get("https://six-20.com/our-services")
            self.driver.get_screenshot_as_file("screenshots/test0301_header.png")
            self.driver.execute_script("window.scrollTo(0,800);")
            self.driver.get_screenshot_as_file("screenshots/test0302_websitedesign.png")
            self.driver.execute_script("window.scrollTo(0,800);")
            self.driver.get_screenshot_as_file("screenshots/test0303_websitedesign2.png")
            self.driver.execute_script("window.scrollTo(0,1900);")
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//app-our-services/div[5]/div[2]/div[1]/app-mobile-text-expander[1]/div[1]/div[1]/a[1]/span[1]"))).click()
            self.driver.get_screenshot_as_file("screenshots/test0304_websitedesignreadless.png")
            WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//app-our-services/div[5]/div[2]/div[1]/app-mobile-text-expander[1]/div[1]/div[2]/a[1]/span[1]"))).click()
            self.driver.get_screenshot_as_file("screenshots/test0305_websitedesignreadmore.png")
            self.driver.execute_script("window.scrollTo(0,3200);")
            self.driver.get_screenshot_as_file("screenshots/test0306_growthoptimization.png")
            self.driver.execute_script("window.scrollTo(0,3932);")
            self.driver.get_screenshot_as_file("screenshots/test0307_payperclick.png")
            self.driver.execute_script("window.scrollTo(0,4632);")
            self.driver.get_screenshot_as_file("screenshots/test0308_identifykeywords.png")
            self.driver.execute_script("window.scrollTo(0,5332);")
            self.driver.get_screenshot_as_file("screenshots/test0309_seo.png")
            self.driver.execute_script("window.scrollTo(0,6332);")
            self.driver.get_screenshot_as_file("screenshots/test0310_onepagefactors.png")
            self.driver.execute_script("window.scrollTo(0,7232);")
            self.driver.get_screenshot_as_file("screenshots/test0311_videomarketing.png")
            self.driver.execute_script("window.scrollTo(0,8415);")
            self.driver.get_screenshot_as_file("screenshots/test0312_videomarketing2.png")
            self.driver.execute_script("window.scrollTo(0,9300);")
            self.driver.get_screenshot_as_file("screenshots/test0313_branding.png")
            self.driver.execute_script("window.scrollTo(0,10200);")
            self.driver.get_screenshot_as_file("screenshots/test0314_branding2.png")
            self.driver.execute_script("window.scrollTo(0,10800);")
            self.driver.get_screenshot_as_file("screenshots/test0315_letstalkoclock.png")
            self.driver.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase04_Pricing(self): 
        try:
            self.driver.get("https://six-20.com/pricing")
            self.driver.get_screenshot_as_file("screenshots/test0401_header.png")
            self.driver.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def testcase05_ContactUs(self):
        try:
            self.driver.get("https://six-20.com/contact")
            self.driver.get_screenshot_as_file("screenshots/test0501_header.png")
            self.driver.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase06_Six20HomePage_Portrait(self):
        try:
            self.driver2.get("https://six-20.com")
            self.driver2.get_screenshot_as_file("screenshots/test0601_header.png")
            self.driver2.execute_script("window.scrollTo(0,800);")
            self.driver2.get_screenshot_as_file("screenshots/test0602_websitedesign.png")
            self.driver2.execute_script("window.scrollTo(0,1500);")
            self.driver2.get_screenshot_as_file("screenshots/test0603_socialmedia.png")
            self.driver2.execute_script("window.scrollTo(0,2200);")
            self.driver2.get_screenshot_as_file("screenshots/test0604_payperclick.png")
            self.driver2.execute_script("window.scrollTo(0,3200);")
            self.driver2.get_screenshot_as_file("screenshots/test0605_seostrategy.png")
            self.driver2.execute_script("window.scrollTo(0,4000);")
            self.driver2.get_screenshot_as_file("screenshots/test0606_videomarketing.png")
            self.driver2.execute_script("window.scrollTo(0,4700);")
            self.driver2.get_screenshot_as_file("screenshots/test0607_branding.png")
            self.driver2.execute_script("window.scrollTo(0,5613);")
            self.driver2.get_screenshot_as_file("screenshots/test0608_ourteam.png")
            self.driver2.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver2.get_screenshot_as_file("screenshots/test0609_itstime.png")
            self.driver2.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True     

    def testcase07_AboutUs_Portrait(self):
        try:
            self.driver2.get("https://six-20.com/about-us")
            self.driver2.get_screenshot_as_file("screenshots/test0701_header.png")
            self.driver2.execute_script("window.scrollTo(0,800);")
            self.driver2.get_screenshot_as_file("screenshots/test0702_experience.png")
            self.driver2.execute_script("window.scrollTo(0,1800);")
            self.driver2.get_screenshot_as_file("screenshots/test0703_freeconsultation.png")
            self.driver2.execute_script("window.scrollTo(0,2300);")
            self.driver2.get_screenshot_as_file("screenshots/test0704_strategic.png")
            self.driver2.execute_script("window.scrollTo(0,3200);")
            self.driver2.get_screenshot_as_file("screenshots/test0705_people.png")
            WebDriverWait(self.driver2,60).until(EC.presence_of_element_located((By.XPATH,"//app-about-us/div[9]/div[2]/div[1]/div[1]/div[2]"))).click()
            self.driver2.get_screenshot_as_file("screenshots/test0706_mattshow.png")
            WebDriverWait(self.driver2,60).until(EC.presence_of_element_located((By.XPATH,"//app-about-us/div[9]/div[2]/div[1]/div[2]/div[1]"))).click()
            self.driver2.get_screenshot_as_file("screenshots/test0707_mattwide.png")
            self.driver2.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver2.get_screenshot_as_file("screenshots/test0708_dontdelay.png")
            self.driver2.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase08_OurServices_Portrait(self):
        try:
            self.driver2.get("https://six-20.com/our-services")
            self.driver2.get_screenshot_as_file("screenshots/test0801_header.png")
            self.driver2.execute_script("window.scrollTo(0,828);")
            self.driver2.get_screenshot_as_file("screenshots/test0802_experience.png")
            self.driver2.execute_script("window.scrollTo(0,1800);")
            self.driver2.get_screenshot_as_file("screenshots/test0803_socialmedia.png")
            self.driver2.execute_script("window.scrollTo(0,2900);")
            self.driver2.get_screenshot_as_file("screenshots/test0804_payperclick.png")
            self.driver2.execute_script("window.scrollTo(0,3600);")
            self.driver2.get_screenshot_as_file("screenshots/test0805_seo.png")
            self.driver2.execute_script("window.scrollTo(0,4400);")
            self.driver2.get_screenshot_as_file("screenshots/test0806_onepagefactor.png")
            self.driver2.execute_script("window.scrollTo(0,5700);")
            self.driver2.get_screenshot_as_file("screenshots/test0807_videomarketing.png")
            self.driver2.execute_script("window.scrollTo(0,6400);")
            self.driver2.get_screenshot_as_file("screenshots/test0808_carouselvideo.png")
            self.driver2.execute_script("window.scrollTo(0,7180);")
            self.driver2.get_screenshot_as_file("screenshots/test0809_branding.png")
            self.driver2.execute_script("window.scrollTo(0,7578);")
            self.driver2.get_screenshot_as_file("screenshots/test0810_branding2.png")
            self.driver2.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver2.get_screenshot_as_file("screenshots/test0811_letstalkoclock.png")
            self.driver2.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def testcase09_Pricing_Portrait(self):
        try:
            self.driver2.get("https://six-20.com/pricing")
            self.driver2.get_screenshot_as_file("screenshots/test0901_header.png")
            self.driver2.execute_script("window.scrollTo(0,500);")
            self.driver2.get_screenshot_as_file("screenshots/test0902_letsworktogether.png")
            self.driver2.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver2.get_screenshot_as_file("screenshots/test0903_form.png")
            self.driver2.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True 

    def testcase10_ContactUs_Portrait(self):
        try:
            self.driver2.get("https://six-20.com/contact")
            self.driver2.get_screenshot_as_file("screenshots/test1001_header.png")
            self.driver2.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver2.get_screenshot_as_file("screenshots/test1002_form.png")
            self.driver2.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True  

    def testcase11_Six20HomePage_Landscape(self):
        try:
            self.driver3.get("https://six-20.com") 
            self.driver3.get_screenshot_as_file("screenshots/test1101_header.png")
            self.driver3.execute_script("window.scrollTo(0,400);")
            self.driver3.get_screenshot_as_file("screenshots/test1102_websitedesignlaptop.png")
            self.driver3.execute_script("window.scrollTo(0,700);")
            self.driver3.get_screenshot_as_file("screenshots/test1103_websitedesign.png")
            self.driver3.execute_script("window.scrollTo(0,1202);")
            self.driver3.get_screenshot_as_file("screenshots/test1104_socialmediamobile.png")
            self.driver3.execute_script("window.scrollTo(0,1600);")
            self.driver3.get_screenshot_as_file("screenshots/test1105_socialmedia.png")
            self.driver3.execute_script("window.scrollTo(0,2063);")
            self.driver3.get_screenshot_as_file("screenshots/test1106_payperclicktablet.png")
            self.driver3.execute_script("window.scrollTo(0,2459);")
            self.driver3.get_screenshot_as_file("screenshots/test1107_payperclick.png")
            self.driver3.execute_script("window.scrollTo(0,2895);")
            self.driver3.get_screenshot_as_file("screenshots/test1108_seostrategymacdesktop.png")
            self.driver3.execute_script("window.scrollTo(0,3326);")
            self.driver3.get_screenshot_as_file("screenshots/test1109_seostrategy.png")
            self.driver3.execute_script("window.scrollTo(0,3766);")
            self.driver3.get_screenshot_as_file("screenshots/test1110_videomarketingtv.png")
            self.driver3.execute_script("window.scrollTo(0,4160);")
            self.driver3.get_screenshot_as_file("screenshots/test1111_videomarketing.png")
            self.driver3.execute_script("window.scrollTo(0,5560);")
            self.driver3.get_screenshot_as_file("screenshots/test1112_ourteam1.png")
            self.driver3.execute_script("window.scrollTo(0,6307);")
            self.driver3.get_screenshot_as_file("screenshots/test1113_ourteam2.png")
            self.driver3.execute_script("window.scrollTo(0,6800);")
            self.driver3.get_screenshot_as_file("screenshots/test1113_itstime1.png")
            self.driver3.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver3.get_screenshot_as_file("screenshots/test1114_itstime2.png")
            self.driver3.close()
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase12_AboutUs_Landscape(self):
        try:
            self.driver3.get("https://six-20.com/about-us") 
            self.driver3.get_screenshot_as_file("screenshots/test1201_header.png") 
            self.driver3.execute_script("window.scrollTo(0,466);")
            self.driver3.get_screenshot_as_file("screenshots/test1202_experience.png")
            self.driver3.execute_script("window.scrollTo(0,902);")
            self.driver3.get_screenshot_as_file("screenshots/test1203_experience2.png")
            self.driver3.execute_script("window.scrollTo(0,1475);")
            self.driver3.get_screenshot_as_file("screenshots/test1204_experience3.png")
            self.driver3.execute_script("window.scrollTo(0,1884);")
            self.driver3.get_screenshot_as_file("screenshots/test1205_freeconsultation.png")
            self.driver3.execute_script("window.scrollTo(0,2297);")
            self.driver3.get_screenshot_as_file("screenshots/test1206_pioneer.png")
            self.driver3.execute_script("window.scrollTo(0,2971);")
            self.driver3.get_screenshot_as_file("screenshots/test1207_strategicpartnership.png") 
            self.driver3.execute_script("window.scrollTo(0,3853);")
            self.driver3.get_screenshot_as_file("screenshots/test1208_people.png")
            self.driver3.execute_script("window.scrollTo(0,3956);")
            self.driver3.get_screenshot_as_file("screenshots/test1209_matt.png")
            WebDriverWait(self.driver3,60).until(EC.presence_of_element_located((By.XPATH,"//app-about-us/div[9]/div[2]/div[1]/div[1]/div[2]"))).click()
            self.driver3.get_screenshot_as_file("screenshots/test1210_show.png")
            WebDriverWait(self.driver3,60).until(EC.presence_of_element_located((By.XPATH,"//app-about-us/div[9]/div[2]/div[1]/div[2]/div[1]"))).click()
            self.driver3.get_screenshot_as_file("screenshots/test1211_hide.png")
            self.driver3.execute_script("window.scrollTo(0,6056);")
            self.driver3.get_screenshot_as_file("screenshots/test1212_dontdelay.png")
            self.driver3.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver3.get_screenshot_as_file("screenshots/test1213_dontdelay2.png")
            self.driver3.close()    
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase13_OurServices_Landscape(self):
        try:
            self.driver3.get("https://six-20.com/our-services")
            self.driver3.get_screenshot_as_file("screenshots/test1301_header.png")
            self.driver3.execute_script("window.scrollTo(0,408);")
            self.driver3.get_screenshot_as_file("screenshots/test1302_websitedesign.png")
            self.driver3.execute_script("window.scrollTo(0,823);")
            self.driver3.get_screenshot_as_file("screenshots/test1303_websitedesign2.png")
            self.driver3.execute_script("window.scrollTo(0,1367);")
            self.driver3.get_screenshot_as_file("screenshots/test1304_readmore.png")
            WebDriverWait(self.driver3,60).until(EC.presence_of_element_located((By.XPATH,"//app-our-services/div[5]/div[2]/div[1]/app-mobile-text-expander[1]/div[1]/div[1]/a[1]/span[1]"))).click()
            self.driver3.execute_script("window.scrollTo(0,1779);")
            self.driver3.get_screenshot_as_file("screenshots/test1305_readless.png")
            WebDriverWait(self.driver3,60).until(EC.presence_of_element_located((By.XPATH,"//app-our-services/div[5]/div[2]/div[1]/app-mobile-text-expander[1]/div[1]/div[2]/a[1]/span[1]"))).click()
            self.driver3.get_screenshot_as_file("screenshots/test1306_socialmedia.png")
            self.driver3.execute_script("window.scrollTo(0,2284);")
            self.driver3.get_screenshot_as_file("screenshots/test1307_growth.png")
            self.driver3.execute_script("window.scrollTo(0,3147);")
            self.driver3.get_screenshot_as_file("screenshots/test1308_payperclick.png")
            self.driver3.execute_script("window.scrollTo(0,3492);")
            self.driver3.get_screenshot_as_file("screenshots/test1309_identifykeywords.png")
            self.driver3.execute_script("window.scrollTo(0,3942);")
            self.driver3.get_screenshot_as_file("screenshots/test1310_identifykeywords2.png")
            self.driver3.execute_script("window.scrollTo(0,4320);")
            self.driver3.get_screenshot_as_file("screenshots/test1311_seo.png")
            self.driver3.execute_script("window.scrollTo(0,4823);")
            self.driver3.get_screenshot_as_file("screenshots/test1312_rankinggame.png")
            self.driver3.execute_script("window.scrollTo(0,5644);")
            self.driver3.get_screenshot_as_file("screenshots/test1313_factors.png")
            self.driver3.execute_script("window.scrollTo(0,6130);")
            self.driver3.get_screenshot_as_file("screenshots/test1314_factors2.png")
            self.driver3.execute_script("window.scrollTo(0,6580);")
            self.driver3.get_screenshot_as_file("screenshots/test1315_videomarketing.png")
            self.driver3.execute_script("window.scrollTo(0,7894);")
            self.driver3.get_screenshot_as_file("screenshots/test1316_carouselvideo.png")
            self.driver3.execute_script("window.scrollTo(0,8440);")
            self.driver3.get_screenshot_as_file("screenshots/test1317_branding.png")
            self.driver3.execute_script("window.scrollTo(0,8857);")
            self.driver3.get_screenshot_as_file("screenshots/test1318_branding2.png")
            self.driver3.execute_script("window.scrollTo(0,9713);")
            self.driver3.get_screenshot_as_file("screenshots/test1319_letstalkoclock.png")
            self.driver3.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver3.get_screenshot_as_file("screenshots/test1320_letstalkoclock2.png")
            self.driver3.close()    
        except NoSuchElementException as e:
            print (e)
            return False
        return True

    def testcase14_Pricing_Landscape(self):
        try:
            self.driver3.get("https://six-20.com/pricing")
            self.driver3.get_screenshot_as_file("screenshots/test1401_header.png")
            self.driver3.execute_script("window.scrollTo(0,419);")
            self.driver3.get_screenshot_as_file("screenshots/test1402_letsworktogether.png")
            self.driver3.execute_script("window.scrollTo(0,869);")
            self.driver3.get_screenshot_as_file("screenshots/test1403_letsworktogether2.png")
            self.driver3.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver3.get_screenshot_as_file("screenshots/test1404_letsworktogether3.png")
            self.driver3.close()    
        except NoSuchElementException as e:
            print (e)
            return False
        return True
    
    def testcase15_ConnectWithUs_Landscape(self):
        try:
            self.driver3.get("https://six-20.com/contact")
            self.driver3.execute_script("window.scrollTo(0,105);")
            self.driver3.get_screenshot_as_file("screenshots/test1501_connectwithus.png")
            self.driver3.execute_script("window.scrollTo(0,547);")
            self.driver3.get_screenshot_as_file("screenshots/test1502_form.png")
            self.driver3.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver3.get_screenshot_as_file("screenshots/test1503_footer.png")
            self.driver3.close()    
        except NoSuchElementException as e:
            print (e)
            return False
        return True     

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Repository/python/Six-20/Six-20/tests",report_title="Six-20 Test",descriptions="Six-20 Test Cases Results", verbosity=2))