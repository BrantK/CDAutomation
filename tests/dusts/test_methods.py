
from time import sleep
from elements.drivers import WebDriver, LoginWith, Home, log, More, SignUp
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction as ta
from selenium.webdriver.support import expected_conditions as ec

##############################################
account_name = "existing02"
account_pw = "password"
account_new_pw = "new password"
account_email = "testuser_02@cyberdust.com"
account_new_email = "new_testuser_02@cyberdust.com"
##############################################

h = Home()
m = More()
s = SignUp()
driver = WebDriver().driver()
tbc = ec.element_to_be_clickable

class Dusts_tests:
    def test_dust_from_dustRoom(self):
        # Logs into existing testing account
        LoginWith().user(account_name, account_pw, driver)
        log("Logged In")
        #Changes passwrord

        h.action_menu().click()
        h.action_menu_dust().click()
        h.action_menu()