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

class Account_Management_test:
    def test_changing_password(self):
        # Logs into existing testing account
        LoginWith().user(account_name, account_pw, driver)
        log("Logged In")
        #Changes passwrord

        m.more_button().click()
        driver.scroll(m.friends(), m.back_button())
        m.change_password().click()
        m.enter_old_password().click()
        m.enter_old_password().send_keys(account_pw)
        m.enter_new_password().click()
        m.enter_new_password().send_keys(account_new_pw)
        m.confirm_new_password().click()
        m.confirm_new_password().send_keys(account_new_pw)
        m.change_password_ok_button().click()

        #Resets Password
        m.change_password().click()
        m.enter_old_password().send_keys(account_new_pw)
        m.enter_new_password().click()
        m.enter_new_password().send_keys(account_pw)
        m.confirm_new_password().click()
        m.confirm_new_password().send_keys(account_pw)
        m.change_password_ok_button().click()
        log("Password reset")


    def test_changing_email(self):
        m.change_email_address().click()
        m.new_email_text_box().send_keys(account_new_email)
        m.change_password_ok_button().click()

        #Reset email address
        m.change_email_address().click()
        try:
            if WebDriver.WebDriverWait(driver, 1).until(tbc((By.NAME, account_new_email))):
                log("Email adress changed")
        except Exception:
            log("Email adress is not changed", "Error")
        m.new_email_text_box().send_keys(account_email)
        m.change_password_ok_button().click()
        log("Email address reset")

    def test_account_deleting(self):
        log("Deleting")
        driver.scroll(m.change_email_address(), m.back_button())
        m.delete_account().click()
        m.confirm().click()
        log("Account Deleted")

        try:
            if LoginWith().user(account_name, account_pw, driver):
                ("Logged into deleted account")
        except Exception:
            log("Can not login into deleted account")

        #Recreating the account

        s.pick_username().send_keys(account_name)
        s.sign_up_OK(5).click()
        s.create_password().send_keys(account_pw)
        s.confirm_password().send_keys(account_pw)
        s.password_OK().click()
        s.birthday().click(), sleep(2)

        log("Entering birthday")
        ta(driver).long_press(x=s.date().location['x'], y=s.date().location['y'], duration=3000).release().perform()
        s.birthday_done().click()
        s.birthday_OK().click()
        log("Entering email")
        s.email().send_keys(account_email)
        s.email_OK().click()
        s.OK_button().click()






