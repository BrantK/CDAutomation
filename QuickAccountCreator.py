# Creates an account

import unittest
import cd_elements.elements as eDriver
from cd_elements.elements import SignUp
from time import sleep

account_name = "testuser999"
account_pw = "testuser999"
account_email = "testuser999@cyberdust.com"


class AccountCreator(unittest.TestCase):
    def test_account_creation(self):
        s = SignUp()
        # Creates username and password
        print("\nCreating new account...")
        s.sign_up_button().click()
        s.pick_username().send_keys(account_name)
        s.sign_up_OK().click()
        s.create_password().send_keys(account_pw)
        s.confirm_password().send_keys(account_pw)
        s.password_OK().click()
        s.birthday().click(), sleep(2)

        # Scrolls through and sets birthday
        for i in range(7):
            eDriver.driver.scroll(s.bday_scroll_1(), s.bday_scroll_2())
        s.birthday_set().click()
        s.birthday_OK().click()

        # Enters email
        s.email().send_keys(account_email)
        s.email_OK().click()
        s.OK_button().click()

        # Skips remaining on boarding
        for i in range(3):
            s.skip_button().click()
        s.done_button().click()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AccountCreator)
    unittest.TextTestRunner(verbosity=2).run(suite)