# On boarding test methods

from time import sleep
from elements.drivers import WebDriver, SignUp, More, log
from appium.webdriver.common.touch_action import TouchAction as ta

#############################################
account_name = "onboardtest001"
account_pw = "onboardtest001"
account_email = "onboard001@cyberdust.com"
#############################################

m = More()
s = SignUp()
driver = WebDriver().driver()


class OnBoardingTest:
    # Checks if an account is logged in then logs out
    def check_if_logged_out(self):
        try:
            s.sign_up_button(5)
            logged_out = True
        except Exception:
            logged_out = False

        if logged_out is False:
            m.more_button().click(), sleep(1)
            driver.scroll(m.followers(), m.back_button())
            m.logout().click()
            log("Logging out before starting test")
            m.confirm().click()

    def test_sign_up(self):
        # Creates a new account and tests if special characters can be used
        s.sign_up_button().click()
        s.pick_username().send_keys(account_name + "!@#$")
        try:
            s.sign_up_OK(5).click()
            log("Special characters used in username", "Warning")
        except Exception:
            log("Could not use special characters in username")
        s.pick_username().send_keys(account_name)
        s.sign_up_OK(5).click()
        s.create_password().send_keys(account_pw)
        s.confirm_password().send_keys(account_pw)
        s.password_OK().click()
        s.birthday().click(), sleep(2)

        # Sets birthday
        log("Entering birthday")
        ta(driver).long_press(x=s.date().location['x'], y=s.date().location['y'], duration=3000).release().perform()
        s.birthday_done().click()
        s.birthday_OK().click()

        # Enters email
        log("Entering email")
        s.email().send_keys(account_email)
        s.email_OK().click()
        s.OK_button().click()

    def test_profile_picture(self):
        # Takes a picture with camera and sets as profile picture
        s.profile_picture().click()
        log("Taking a photo and setting it as the profile picture")
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
            driver.find_element_by_id("com.android.camera2:id/done_button").click()  # For Nexus phones
        except Exception:
            pass
        try:
            m.profile_picture_done(5).click(), sleep(3)
        except Exception:
            log("Could not take a photo, going back", "Warning")
            for i in range(2):
                driver.press_keycode(4), sleep(1)  # If none of the above works, go back
            s.skip_button()
        log("Skipping checking contacts and sending text message")
        s.OK_button().click()
        s.skip_button().click()
        s.done_button().click()
        log("New account, %s, created" % account_name)

    def test_updating_profile_picture(self):
        # Changes profile picture
        m.more_button().click()
        m.profile_picture().click()
        m.change_profile_picture().click()
        log("Changing profile picture")
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
        try:
            driver.find_element_by_id("com.android.camera2:id/done_button").click()  # For Nexus phones
        except Exception:
            pass
        m.profile_picture_done().click(), sleep(3)
        log("Profile picture updated")

    def test_logout_login(self):
        # Logout and login
        log("Testing logout and login")
        driver.scroll(m.friends(), m.back_button())
        m.logout().click()
        m.confirm().click()
        m.login_button().click()
        m.login_username().send_keys(account_name.upper())
        m.login_password().send_keys(account_pw)
        m.login_OK().click()
        log("Username is not case sensitive")

        # Deletes account
        m.more_button().click(), sleep(1)
        driver.scroll(m.followers(), m.back_button())
        m.delete_account().click()
        log("Deleting account")
        m.confirm().click()
        log("On boarding test completed", "Complete")