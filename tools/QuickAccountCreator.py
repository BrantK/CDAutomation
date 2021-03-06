# Creates an account

import unittest
from time import sleep
from elements.drivers import WebDriver, SignUp
from appium.webdriver.common.touch_action import TouchAction as ta

driver = WebDriver().driver()

account_name = "blasttest02"
account_pw = "blasttest02"
account_email = "blasttest02@cyberdust.com"


class AccountCreator(unittest.TestCase):
    def test_account_creation(self):
        s = SignUp()
        # Creates username and password
        s.sign_up_button().click()
        s.pick_username().send_keys(account_name)
        s.sign_up_OK().click()
        s.create_password().send_keys(account_pw)
        s.confirm_password().send_keys(account_pw)
        s.password_OK().click()
        s.birthday().click(), sleep(2)

        ta(driver).long_press(x=s.date().location['x'], y=s.date().location['y'], duration=3000).release().perform()
        s.birthday_done().click()
        s.birthday_OK().click()

        # Enters email
        s.email().send_keys(account_email)
        s.email_OK().click()
        s.OK_button().click()

        # Skips remaining on boarding
        for i in range(2):
            s.skip_button().click()
        s.done_button().click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AccountCreator)
    unittest.TextTestRunner(verbosity=2).run(suite)