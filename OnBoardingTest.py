# Automated on boarding test

import unittest
import cd_elements.elements as myDriver
from cd_elements.elements import SignUp, More, Login
from selenium.common.exceptions import TimeoutException
from time import sleep

account_name = "onboardtest001"
account_pw = "onboardtest001"
account_email = "onboard001@cyberdust.com"


class OnBoardingTest(unittest.TestCase):
    def test_on_boarding(self):
        s = SignUp()
        m = More()
        l = Login()
        print("\nStarting on boarding test")

        # Creates a new account and tests if special characters can be used
        s.sign_up_button().click()
        s.pick_username().send_keys(account_name + "!@#$")
        try:
            s.sign_up_OK().click()
            print("\nWarning: special characters used in username.")
        except TimeoutException:
            print("\nCould not use special characters in username.")
        s.pick_username().send_keys(account_name)
        s.sign_up_OK().click()
        s.create_password().send_keys(account_pw)
        s.confirm_password().send_keys(account_pw)
        s.password_OK().click()
        s.birthday().click(), sleep(2)

        # Scrolls through and sets birthday
        for i in range(7):
            myDriver.driver.scroll(s.bday_scroll_1(), s.bday_scroll_2())
        s.birthday_set().click()
        s.birthday_OK().click()

        # Enters email
        s.email().send_keys(account_email)
        s.email_OK().click()
        s.OK_button().click()

        # Takes a picture with camera and sets as profile picture (Works for Note 4)
        s.profile_picture().click()
        s.camera_button().click(), sleep(2)
        # For the Moto X and Moto G - self.driver.find_element_by_id("com.motorola.camera:id/preview_surface").click()
        myDriver.driver.press_keycode(27)  # Takes picture using Android keycode and not tapping a button
        s.OK_button().click()
        s.profile_picture_done().click(), sleep(3)
        s.OK_button().click()

        # Skips adding contacts and phone number validation
        for i in range(2):
            s.skip_button().click()
        s.done_button().click()
        print("\nStarting logout and login test")

        # Changes profile picture
        m.more_button().click()
        m.profile_picture().click()
        m.change_profile_picture().click()
        s.camera_button().click(), sleep(2)
        myDriver.driver.press_keycode(27)
        m.OK_button().click()
        m.profile_picture_done().click(), sleep(3)

        # Logout and login
        myDriver.driver.scroll(m.add_friends(), m.back_button())
        m.logout().click()
        m.confirm().click()
        l.login_button().click()
        l.login_username().send_keys(account_name.upper())
        l.login_password().send_keys(account_pw)
        l.login_OK().click()

        # Deletes account
        m.more_button().click(), sleep(1)
        myDriver.driver.scroll(m.add_friends(), m.back_button())
        print("\nDeleting account")
        m.delete_account().click()
        m.confirm().click()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OnBoardingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)