# Elements organized by class

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


class Standard:
    def OK_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "OK")))

    def next_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "next")))

    def back_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "android:id/home")))

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


class Home:
    def dusts_tab(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/actionbar_tab_text[@text='DUSTS']")))

    def blasts_tab(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/actionbar_tab_text[@text='BLASTS']")))

    def groups_tab(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/actionbar_tab_text[@text='GROUPS']")))

    def more_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='2'][android.widget.ImageView[@index='0']]")))

    def action_menu(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='1'][android.widget.ImageView[@index='0']]")))

    def action_menu_dust(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='6'][android.widget.ImageView[@index='1']]")))

    def action_menu_group(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='2'][android.widget.ImageView[@index='1']]")))

    def action_menu_text(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='3'][android.widget.ImageView[@index='1']]")))

    def action_menu_media(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='4'][android.widget.ImageView[@index='1']]")))

    def action_menu_discover(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='5'][android.widget.ImageView[@index='1']]")))

    def action_menu_search(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='8'][android.widget.ImageView[@index='1']]")))

    def action_menu_close(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='7'][android.widget.ImageView[@index='0']]")))

    def dust_blast_field(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/dust_blast_text_edit_text")))

    def photo_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_take_picture")))

    def video_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "VIDEO")))

    def blast_friends(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_tab_friends")))

    def blast_recipient(self, recipient):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, recipient)))

    def OK_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "OK")))

    def next_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "next")))

    def back_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "android:id/home")))

class More:
    def back_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/home")))

    def profile_picture(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_picture")))

    def enter_bio(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_bio")))

    def enter_website(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_url")))

    def share_twitter(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_share_twitter")))

    def share_facebook(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_share_facebook")))

    def share_instagram(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_share_instagram")))

    def share_email(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_share_email")))

    def followers(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/browse_followers_row")))

    def friends(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/browse_friends_row")))

    def add_friends(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/add_friends_row")))

    def invite_friends(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/invite_friends_row")))

    def notification_settings(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_push_notification_row")))

    def easy_search(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_searchable_switch")))

    def default_to_blasts_tab(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_default_tab_switch")))

    def sort_dust_list(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_sort_list_switch")))

    def show_blast_previews(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_show_preview_switch")))

    def logout(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_logout_row")))

    def change_email_address(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_email_row")))

    def change_password(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_password_row")))

    def validate_mobile(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_mobile_number_row")))

    def muted_blocked_users(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_blocked_users_row")))

    def user_guides(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_guide_row")))

    def tutorial(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_tutorial_row")))

    def delete_account(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_delete_account_row")))