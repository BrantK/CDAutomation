# Elements organized by class

import sys
from sys import argv
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Desired capabilities
desired_caps = {
    'platformName'   : 'Android',
    'platformVersion': '',
    'deviceName'     : '',
    'appPackage'     : 'com.radicalapps.cyberdust',
    'appActivity'    : 'com.radicalapps.cyberdust.activities.LauncherActivity'}


# Set the port and unique device id from the command line with -p and -udid or set it inside the test script
class WebDriver:
    def __init__(self, DefaultPort=4723):
        self.DefaultPort = DefaultPort

    def driver(self, port=sys.argv):
        port = self.DefaultPort
        if len(sys.argv) == 1:
            port = self.DefaultPort
        elif len(sys.argv) == 3 and sys.argv[1] == '-p':
            port = sys.argv[2]
        elif len(sys.argv) == 3 and sys.argv[1] == '-udid':
            desired_caps.update({'udid': str(sys.argv[2])})
            port = self.DefaultPort
        elif len(sys.argv) == 5 and sys.argv[1] == '-p' and sys.argv[3] == '-udid':
            desired_caps.update({'udid': str(sys.argv[4])})
            port = sys.argv[2]
        global driver
        driver = webdriver.Remote('http://127.0.0.1:'+str(port)+'/wd/hub', desired_caps)
        return driver


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

    def birthday_done(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def email(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_4_email_edit_text")))

    def profile_picture(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_screen_4_1_profile_pic_layout")))

    def sign_up_OK(self):
        return WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_1_ok_button")))

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

    def profile_picture_done(self):
        return WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/activity_profile_pic_crop_btn")))

    def camera_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "Camera")))

    def date(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.NumberPicker[@index='2'][android.widget.Button]")))


class Home:
    def login_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/splash_screen_login_button")))

    def login_username(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_username_edit_text")))

    def login_password(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_password_edit_text")))

    def login_OK(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_ok_button")))

    def dusts_tab(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "DUSTS")))

    def new_dust(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/tap_to_compose_button")))

    def blasts_tab(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, 'BLASTS')))

    def blast_lists(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "Blast Lists")))

    def blast_list_field(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/name_edit_text")))

    def blast_list_expand(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "WebDriverWait com.radicalapps.cyberdust:id/blast_groups_list_item_group_indicator")))

    def blast_list_edit(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_groups_list_item_edit_action")))

    def blast_list_more(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton")))

    def rename_list(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "Rename list")))

    def rename_blast_list(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.EditText")))

    def delete_list(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "Delete list")))

    def groups_tab(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, 'GROUPS')))

    def card_view(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/card_view")))

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

    def photo_flip(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_flip_camera")))

    def photo_pen(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/pen")))

    def photo_color(self):
        return  WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/picker")))

    def photo_back_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_back")))

    def video_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "VIDEO")))

    def location_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/location")))

    def text_location_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/actionbar_blast_pin")))

    def current_location(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "Current Location")))

    def add_text(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_add_text")))

    def add_text_field(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/edit_text_overlay")))

    def next_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_next")))

    def make_public(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_public_button_check")))

    def blast_all_followers(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_followers_button_plus")))

    def blast_all_friends(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_friends_button_plus")))

    def create_blast_list(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "Create Blast List")))

    def send_to_blast_list(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_check")))

    def blast_friends(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_tab_friends")))

    def username(self, user):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, user)))

    def blast_Ok_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "Ok")))

    def OK_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "OK")))

    def done_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "done")))

    def back_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "android:id/home")))

    def confirm(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def cancel(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button2")))


class More:
    def login_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/splash_screen_login_button")))

    def login_username(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_username_edit_text")))

    def login_password(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_password_edit_text")))

    def login_OK(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_ok_button")))

    def more_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='2'][android.widget.ImageView[@index='0']]")))

    def back_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/home")))

    def profile_picture(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_picture")))

    def remove_profile_picture(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button2")))

    def change_profile_picture(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def camera_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "Camera")))

    def profile_picture_done(self):
        return WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/activity_profile_pic_crop_btn")))

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

    def OK_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.NAME, "OK")))

    def confirm(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def cancel(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "android:id/button2")))

