# Cyber Dust Elements organized by class

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium import webdriver

# Desired capabilities and driver
desired_caps = {
    'platformName'   : 'Android',
    'platformVersion': '',
    'deviceName'     : '',
    'appPackage'     : 'com.radicalapps.cyberdust',
    'appActivity'    : 'com.radicalapps.cyberdust.activities.LauncherActivity'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


class SignUp:
    def sign_up_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/splash_screen_signup_button")))

    def pick_username(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_1_username_edit_text")))

    def create_password(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_2_password_edit_text")))

    def confirm_password(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_2_password_confirm_edit_text")))

    def birthday(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_3_date_edit_text")))

    def birthday_set(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def email(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_4_email_edit_text")))

    def sign_up_OK(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_1_ok_button")))

    def password_OK(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_2_ok_button")))

    def birthday_OK(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_3_ok_button")))

    def email_OK(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_4_ok_button")))

    def OK_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "OK")))

    def skip_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "skip")))

    def done_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "done")))

    def bday_scroll_1(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.NumberPicker[@index='2'][android.widget.Button[@index='0']]")))

    def bday_scroll_2(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))


class Login:
    def login_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/splash_screen_login_button")))

    def login_username(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_username_edit_text")))

    def login_password(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_password_edit_text")))

    def login_OK(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_ok_button")))
