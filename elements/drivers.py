# Testing methods and elements organized by class

import os
import sys
import time
import logging
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.touch_action import TouchAction as ta

# Desired capabilities
desired_caps = {
    'platformName'   : 'Android',
    'platformVersion': '',
    'deviceName'     : '',
    'appPackage'     : 'com.radicalapps.cyberdust',
    'appActivity'    : 'com.radicalapps.cyberdust.activities.LauncherActivity'}


# Use log("text_here") to print a log to the console and to a log file in the root directory
def log(msg, mod=os.path.basename(sys.argv[0])[:-3]):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Prints to console
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s ['+mod+']: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(msg)
    logger.removeHandler(handler)

    # Prints log to folder that module is in
    handler = logging.FileHandler(os.path.basename(sys.argv[0])[:-3]+str(time.strftime('_%m-%d-%Y'))+".log")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s ['+mod+']: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug(msg)
    logger.removeHandler(handler)

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


# Checks to see if a specified account is logged in, then logs in or continues script
class LoginWith:
    def user(self, account, password, driver):
        m = More()
        tbc = ec.element_to_be_clickable
        already_logged_in = False

        try:
            WebDriverWait(driver, 5).until(tbc((By.ID, "com.radicalapps.cyberdust:id/splash_screen_login_button")))
            logged_out = True
        except Exception:
            logged_out = False

        if logged_out is False:
            m.more_button().click()
            try:
                WebDriverWait(driver, 1).until(tbc((By.NAME, account)))
                already_logged_in = True
            except Exception:
                already_logged_in = False
                pass

        if already_logged_in is True and logged_out is False:
            log("Already logged in as %s" % account, "Login")
            m.back_button().click()
        elif already_logged_in is False and logged_out is False:
            logged_out = True
            driver.scroll(m.followers(), m.back_button())
            m.logout().click()
            m.confirm().click()

        if already_logged_in is False and logged_out is True:
            log("Logging in as %s" % account, "Login")
            m.login_button().click()
            m.login_username().send_keys(account)
            m.login_password().click()
            m.login_password().send_keys(password)
            m.login_OK().click()


# Elements for on boarding
class SignUp:
    def sign_up_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/splash_screen_signup_button")))

    def pick_username(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_1_username_edit_text")))

    def create_password(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_2_password_edit_text")))

    def confirm_password(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_2_password_confirm_edit_text")))

    def birthday(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_3_date_edit_text")))

    def birthday_done(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def email(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_4_email_edit_text")))

    def profile_picture(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_screen_4_1_profile_pic_layout")))

    def sign_up_OK(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_1_ok_button")))

    def password_OK(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_2_ok_button")))

    def birthday_OK(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_3_ok_button")))

    def email_OK(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/onboarding_4_ok_button")))

    def OK_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "OK")))

    def skip_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "skip")))

    def done_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "done")))

    def profile_picture_done(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/activity_profile_pic_crop_btn")))

    def camera_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Camera")))

    def date(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.NumberPicker[@index='2'][android.widget.Button]")))

    def name(self, name, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, name)))


# Elements for the "Home" page of the app
class Home:
    def login_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/splash_screen_login_button")))

    def login_username(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_username_edit_text")))

    def login_password(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_password_edit_text")))

    def login_OK(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_ok_button")))

    def dusts_tab(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "DUSTS")))

    def new_dust(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/tap_to_compose_button")))

    def blasts_tab(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, 'BLASTS')))

    def blast_preview_card(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/preview_text")))

    def blast_more_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_button")))

    def blast_more_mute(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "mute blasts")))

    def blast_more_delete(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "delete blast")))

    def blast_more_block(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "block user")))

    def blast_more_cancel(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "cancel")))

    def blast_lists(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Blast Lists")))

    def create_new_blast_list(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/create_button")))

    def blast_list_field(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/name_edit_text")))

    def blast_list_expand(self, wait=30):
        el = WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.ExpandableListView[@index='0'][android.widget.RelativeLayout]")))
        ta(driver).press(x=el.location['x'], y=el.location['y']).release().perform()

    def blast_list_edit(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_groups_list_item_edit_action")))

    def blast_list_more(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton")))

    def rename_list(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Rename list")))

    def rename_blast_list(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.EditText")))

    def delete_list(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Delete list")))

    def groups_tab(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, 'GROUPS')))

    def card_view(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/card_view")))

    def more_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='2'][android.widget.ImageView[@index='0']]")))

    def action_menu(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='1'][android.widget.ImageView[@index='0']]")))

    def action_menu_dust(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='6'][android.widget.ImageView[@index='1']]")))

    def action_menu_group(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='2'][android.widget.ImageView[@index='1']]")))

    def action_menu_text(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='3'][android.widget.ImageView[@index='1']]")))

    def action_menu_media(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='4'][android.widget.ImageView[@index='1']]")))

    def action_menu_discover(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='5'][android.widget.ImageView[@index='1']]")))

    def action_menu_search(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='8'][android.widget.ImageView[@index='1']]")))

    def action_menu_close(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='7'][android.widget.ImageView[@index='0']]")))

    def dust_blast_field(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/dust_blast_text_edit_text")))

    def photo_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_take_picture")))

    def photo_flip(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_flip_camera")))

    def photo_pen(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/pen")))

    def photo_color(self, wait=30):
        return  WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/picker")))

    def photo_back_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_back")))

    def video_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "VIDEO")))

    def photo_location_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/location")))

    def text_location_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/actionbar_blast_pin")))

    def current_location(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Current Location")))

    def add_text(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_add_text")))

    def add_text_field(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/edit_text_overlay")))

    def next_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_next")))

    def make_public(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_public_button_check")))

    def blast_all_followers(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_followers_button_plus")))

    def blast_all_friends(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_friends_button_plus")))

    def create_blast_list(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Create blasts List")))

    def send_to_blast_list(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_check")))

    def blast_friends(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/blast_tab_friends")))

    def swipe_view_add(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/add_friend")))

    def swipe_view_cancel(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/cancel")))

    def swipe_view_url_card(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.LinearLayout[@index='0'][android.widget.LinearLayout[@index='1']]")))

    def swipe_view_location(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/page_frag_location")))

    def swipe_view_text(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/text_overlay")))

    def swipe_view_reblast(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/page_frag_reblast")))

    def swipe_view_reply(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/reply_box")))

    def swipe_view_reply_send(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/reply_send")))

    def swipe_view_reply_media(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/reply_media")))

    def swipe_view_reply_monkey(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/reply_monkey")))

    def swipe_view_monkey(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/emoji_image")))

    def swipe_view_emoji_cancel(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/emoji_cancel")))

    def swipe_view_photo_send(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/action_next")))

    def swipe_view_exit(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/exit_button")))

    def name(self, name, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, name)))

    def username(self, user, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, user)))

    def blast_Ok_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Ok")))

    def OK_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "OK")))

    def done_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "done")))

    def back_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/home")))

    def confirm(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def cancel(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/button2")))

    def chat_room_text_box(self, wait = 30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/chat_room_fragment_text_box")))

    def chat_room_send_button(self, wait = 30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/chat_room_fragment_send_button")))

    def sent_text_blast(self, wait = 30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/chat_bubble_view_message_text")))

    def pinned_message(self, wait = 30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/pinned_message_text")))

    def tap_to_unpin_button(self, wait = 30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Tap message to unpin")))



# Elements for the "More" page of the app
class More:
    def login_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/splash_screen_login_button")))

    def login_username(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_username_edit_text")))

    def login_password(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_password_edit_text")))

    def login_OK(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/login_frag_ok_button")))

    def more_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@index='2'][android.widget.ImageView[@index='0']]")))

    def back_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/home")))

    def profile_picture(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_picture")))

    def remove_profile_picture(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/button2")))

    def change_profile_picture(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def camera_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "Camera")))

    def profile_picture_done(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/activity_profile_pic_crop_btn")))

    def enter_bio(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_bio")))

    def enter_website(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_url")))

    def share_twitter(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_share_twitter")))

    def share_facebook(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_share_facebook")))

    def share_instagram(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_share_instagram")))

    def share_email(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_share_email")))

    def followers(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/browse_followers_row")))

    def friends(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/browse_friends_row")))

    def add_friends(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/add_friends_row")))

    def invite_friends(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/invite_friends_row")))

    def notification_settings(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_push_notification_row")))

    def easy_search(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_searchable_switch")))

    def default_to_blasts_tab(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_default_tab_switch")))

    def sort_dust_list(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_sort_list_switch")))

    def show_blast_previews(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_show_preview_switch")))

    def logout(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_logout_row")))

    def change_email_address(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_email_row")))

    def change_password(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_password_row")))

    def validate_mobile(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_mobile_number_row")))

    def muted_blocked_users(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_blocked_users_row")))

    def user_guides(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_guide_row")))

    def tutorial(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_tutorial_row")))

    def delete_account(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/more_fragment_delete_account_row")))

    def OK_button(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.NAME, "OK")))

    def confirm(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/button1")))

    def cancel(self, wait=30):
        return WebDriverWait(driver, wait).until(ec.element_to_be_clickable((By.ID, "android:id/button2")))

    def enter_old_password(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/change_password_fragment_oldpass_edit_text")))

    def enter_new_password(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/change_password_fragment_newpass_edit_text")))

    def confirm_new_password(self):
       return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/change_password_fragment_newpass_confirm_edit_text")))

    def change_password_ok_button(self):
        return WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, "com.radicalapps.cyberdust:id/spinner_button_text_view")))