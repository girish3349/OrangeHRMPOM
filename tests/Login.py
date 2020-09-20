from selenium import webdriver
import time
import unittest
from pages.PageHome import HomePage
from common.CommonMethods import commonMethods
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
#   import HtmlTestRunner
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\Ammulu\Documents\Selenium drivers\chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.actions = ActionChains(cls.driver)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

    def test_loginTest(self):
        driver = self.driver
        actions = self.actions

        cm = commonMethods(driver, actions)
        cm.login()
        print("Before Try: ", datetime.now())
        # Exception Handling
        try:
            #Explicit Wait
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "spanMessage")))
            # assertion
            self.assertEqual("Invalid credentials", element.text)
            print("Try: ", datetime.now())
        except Exception as e:
            #assertion
            self.assertEqual("Dashboard", driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').text)
            print("Except: ", datetime.now())
            print(e)
        finally:
            print ("Will Execute allways")
            print("Finally: ", datetime.now())




        cm.navigatetoAddEmployee()
        cm.navigatetoJobtitle()

        time.sleep(2)
        #
        # homepage = HomePage(driver)
        # homepage.clkwelcome()
        # homepage.clklogout()
        #
        # time.sleep(5)


if __name__ == "__main__":
    unittest.main()
    #   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
