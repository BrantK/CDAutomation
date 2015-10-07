# Creates an account - test

import unittest
import cd_elements.elements as myDriver
from cd_elements.elements import SignUp
from time import sleep

account_name = "onboardtest01"
account_pw = "testuser01"
account_email = "onboard01@cyberdust.com"


class AccountCreator(unittest.TestCase):
    def test_account_creation(self):
        sign_up = SignUp()
        # Creates username and password
        print("\nCreating new account...")
        sign_up.sign_up_button().click()
        sign_up.pick_username().send_keys(account_name)
        sign_up.sign_up_OK().click()
        sign_up.create_password().send_keys(account_pw)
        sign_up.confirm_password().send_keys(account_pw)
        sign_up.password_OK().click()
        sign_up.birthday().click(), sleep(2)

        # Scrolls through and sets birthday
        for i in range(7):
            myDriver.driver.scroll(sign_up.bday_scroll_1(), sign_up.bday_scroll_2())
        sign_up.birthday_set().click()
        sign_up.birthday_OK().click()

        # Enters email
        sign_up.email().send_keys(account_email)
        sign_up.email_OK().click()
        sign_up.OK_button().click()

        # Skips remaining on boarding
        for i in range(3):
            sign_up.skip_button().click()
        sign_up.done_button().click()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AccountCreator)
    unittest.TextTestRunner(verbosity=2).run(suite)