import  unittest
import HtmlTestRunner
import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class AmazonSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
         cls.driver= Chrome('F:\Softwares\Python\Lib\site-packages\selenium\Chrome\chromedriver.exe')
    def  amazonSearch(self):
         self.driver.get("https://www.amazon.com")
         self.driver.maximize_window()
         a=self.ActionChains(driver)
         e=self.driver.find_element_by_xpath(".//*[@id='nav-link-accountList']")
         self.a.move_to_element(e).perform();
         self.driver.find_element_by_class_name("nav-action-button").click()
         self.driver.find_element_by_id("ap_email").send_keys("samalshudi@gmail.com")
         self.driver.find_element_by_id("ap_password").send_keys("shudi12345")
         self.driver.find_element_by_id("signInSubmit").click()
         dept=self.driver.find_element_by_xpath(".//*[@id='nav-link-shopall']").click()
         self.driver.find_element_by_link_text("Headphones").click()
         self.driver.find_element_by_xpath("//div[@class='sg-col-inner']/div[1]").click()#-----headphone
         self.driver.find_element_by_id("add-to-cart-button").click()
         self.driver.find_element_by_class_name("a-link-normal close-button").click()
         self.driver.find_element_by_id("twotabsearchtextbox").send_keys("Macbook Pro",Keys.ENTER)
         self.driver.find_element_by_xpath("//div[@class='block desktopSparkle__asinContainer block--direction-column']/div[2]").click()#-----Macbook Pro
         Qty_ddl=self.driver.find_element_by_class_name("a-icon a-icon-dropdown")
         Qty_sct= self.Select(Qty_ddl)
         self.Qty_sct.select_by_value(2)
         self.driver.find_element_by_id("add-to-cart-button").click()
         self.driver.find_element_by_class_name("a-link-normal close-button").click()
         cart=self.driver.find_element_by_id("hlb-view-cart-announce")
         self.a.move_to_element(cart).perform()
         if (element==(driver.find_element_by_xpath("//span[@class='a-size-medium sc-product-title a-text-bold']"))):
               Qty_ddl=self.driver.find_element_by_class_name("a-icon a-icon-dropdown")
               Qty_sct= self.Select(Qty_ddl)
               self.Qty_sct.select_by_value(1)
         if (element==(driver.find_element_by_xpath("//span[@class='a-size-medium sc-product-title a-text-bold']"))):
               self.driver.find_element_by_xpath(("//input[@value='Delete'")).click()
               self.driver.find_element_by_xpath(("//input[@name='proceedToCheckout'")).click()
    @classmethod
    def tearDownClass(cls):
    cls.driver.close()
