# Automated on boarding test....

import unittest
from time import sleep
from elements.drivers import WebDriver, SignUp, More
from appium.webdriver.common.touch_action import TouchAction as ta

account_name = "onboardtest001"
account_pw = "onboardtest001"
account_email = "onboard001@cyberdust.com"


class OnBoardingTest(unittest.TestCase):
    def test_on_boarding(self):
        m = More()
        s = SignUp()
        driver = WebDriver().driver()
        print("\nStarting on boarding test")

        # Creates a new account and tests if special characters can be used
        s.sign_up_button().click()
        s.pick_username().send_keys(account_name + "!@#$")
        try:
            s.sign_up_OK().click()
            print("\nWarning: special characters used in username")
        except Exception:
            print("\nCould not use special characters in username")
        s.pick_username().send_keys(account_name)
        s.sign_up_OK().click()
        s.create_password().send_keys(account_pw)
        s.confirm_password().send_keys(account_pw)
        s.password_OK().click()
        s.birthday().click(), sleep(2)

        # Sets birthday
        ta(driver).long_press(x=s.date().location['x'], y=s.date().location['y'], duration=3000).release().perform()
        s.birthday_done().click()
        s.birthday_OK().click()

        # Enters email
        s.email().send_keys(account_email)
        s.email_OK().click()
        s.OK_button().click()

        # Takes a picture with camera and sets as profile picture
        s.profile_picture().click()
        s.camera_button().click(), sleep(3)
        driver.press_keycode(25), sleep(1), driver.press_keycode(27), sleep(5)  # Takes picture using Android keycode
        try:
            driver.find_element_by_id("com.motorola.camera:id/review_approve").click()  # For Moto phones
        except Exception:
            pass
        try:
            driver.find_element_by_id("com.android.camera:id/select_this").click()  # For older HTC one phones
        except Exception:
            pass
        try:
            ta(driver).press(x=1660, y=530).release().perform()  # For new HTC One phones
        except Exception:
            pass
        try:
            driver.find_element_by_name("OK").click()  # For Galaxy phones
        except Exception:
            pass
        try:
            m.profile_picture_done().click(), sleep(3)
        except Exception:
            for i in range(2):
                driver.press_keycode(4), sleep(1)  # If none of the above works, go back
            s.skip_button()
        s.OK_button().click()
        s.skip_button().click()
        s.done_button().click()

        print("\nAccount created")

        # Changes profile picture
        m.more_button().click()
        m.profile_picture().click()
        m.change_profile_picture().click()
        s.camera_button().click(), sleep(3)
        driver.press_keycode(25), driver.press_keycode(27), sleep(5)  # Takes picture using Android keycode
        try:
            driver.find_element_by_id("com.motorola.camera:id/review_approve").click()  # For Moto phones
        except Exception:
            pass
        try:
            driver.find_element_by_id("com.android.camera:id/select_this").click()  # For older HTC one phones
        except Exception:
            pass
        try:
            ta(driver).press(x=1660, y=530).release().perform()  # For new HTC One phones
        except Exception:
            pass
        try:
            driver.find_element_by_name("OK").click()  # For Galaxy phones
        except Exception:
            pass
        m.profile_picture_done().click(), sleep(3)

        print("\nProfile picture updated")

        # Logout and login
        driver.scroll(m.friends(), m.back_button())
        m.logout().click()
        m.confirm().click()
        m.login_button().click()
        m.login_username().send_keys(account_name.upper())
        m.login_password().send_keys(account_pw)
        m.login_OK().click()
        print("\nUsername is not case sensitive")

        # Deletes account
        m.more_button().click(), sleep(1)
        driver.scroll(m.friends(), m.back_button())
        m.delete_account().click()
        m.confirm().click()
        print("\nAccount deleted")
        print("\nOn boarding test completed")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OnBoardingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)