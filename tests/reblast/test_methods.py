# Reblast test methods

from time import sleep
from elements.drivers import WebDriver, LoginWith, Home, log
from appium.webdriver.common.touch_action import TouchAction as ta

###############################
account01 = "blasttest01"
password01 = account01

account02 = "blasttest02"
password02 = account02

account03 = "blasttest03"
password03 = account03
################################

h = Home()
driver = WebDriver().driver()
sw = driver.get_window_size()['width']
sh = driver.get_window_size()['height']

LoginWith().user(account01, password01, driver)

class ReblastTest:
    def send_text_with_loc(self):
        log("Sending text blasts with location")
        my_text = {0: "all followers", 1: "blast list", 2: "friend"}
        for i in range(3):
            h.action_menu().click()
            h.action_menu_text().click()
            h.dust_blast_field().send_keys(my_text[i])
            h.text_location_button().click()
            h.current_location().click()
            h.OK_button().click()
            h.blast_friends().click()
            h.username(account02).click()
            h.blast_Ok_button().click()

    def send_text_no_loc(self):
        log("Sending text blasts without location")
        my_text = {0: "all followers", 1: "blast list", 2: "friend"}
        for i in range(3):
            h.action_menu().click()
            h.action_menu_text().click()
            h.dust_blast_field().send_keys(my_text[i])
            h.OK_button().click()
            h.blast_friends().click()
            h.username(account02).click()
            h.blast_Ok_button().click()

    def send_photo_with_loc(self):
        log("Sending photo blasts with location")
        for i in range(3):
            h.action_menu().click()
            h.action_menu_media().click()
            h.photo_button().click()
            h.photo_location_button().click()
            h.current_location().click()
            h.next_button().click()
            h.blast_friends().click()
            h.username(account02).click()
            h.blast_Ok_button().click()

    def send_photo_no_loc(self):
        log("Sending photo blasts without location")
        for i in range(3):
            h.action_menu().click()
            h.action_menu_media().click()
            h.photo_button().click()
            h.next_button().click()
            h.blast_friends().click()
            h.username(account02).click()
            h.blast_Ok_button().click()

    def send_giphy_with_loc(self):
        log("Sending giphy with location")
        for i in range(3):
            h.action_menu().click()
            h.action_menu_text().click()
            h.dust_blast_field().send_keys(":giphy cats")
            h.text_location_button().click()
            h.current_location().click()
            h.OK_button().click()
            h.blast_friends().click()
            h.username(account02).click()
            h.blast_Ok_button().click()

    def send_giphy_no_loc(self):
        log("Sending giphy without location")
        for i in range(3):
            h.action_menu().click()
            h.action_menu_text().click()
            h.dust_blast_field().send_keys(":giphy cats")
            h.OK_button().click()
            h.blast_friends().click()
            h.username(account02).click()
            h.blast_Ok_button().click()

    def send_video_with_loc(self):
        log("Sending video blasts with location")
        for i in range(3):
            h.action_menu().click()
            h.action_menu_media().click()
            h.video_button().click()
            ta(driver).long_press(h.photo_button(), duration=5000).release().perform()
            h.photo_location_button().click()
            h.current_location().click()
            h.next_button().click()
            h.blast_friends().click()
            h.username(account02).click()
            h.blast_Ok_button().click()

    def send_video_no_loc(self):
        log("Sending video blasts without location")
        for i in range(3):
            h.action_menu().click()
            h.action_menu_media().click()
            h.video_button().click()
            ta(driver).long_press(h.photo_button(), duration=5000).release().perform()
            h.next_button().click()
            h.blast_friends().click()
            h.username(account02).click()
            h.blast_Ok_button().click()

    def reblast_setup(self):
        log("Setting up reblast test")
        LoginWith().user(account02, password02, driver)
        h.blast_lists().click(), sleep(2)
        log("Creating a blast list")
        try:
            if driver.find_element_by_id("com.radicalapps.cyberdust:id/blast_groups_list_item_group_indicator"):
                h.blast_list_expand()  # Doesn't need .click() attribute
                h.blast_list_edit().click()
                h.blast_list_more().click()
                log("Deleting pre-existing blast list first")
                h.delete_list().click()
                h.confirm().click()
                h.blast_lists().click()
        except Exception:
            pass
        h.blast_list_field().send_keys("Reblast List")
        h.OK_button().click()
        h.username(account01).click()
        h.username(account03).click()
        h.OK_button().click()

    def reblast_text_with_loc(self):
        h.username(account01).click()
        log("Reblasting text with location to all followers")
        h.swipe_view_reblast().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting text with location to blast list")
        h.swipe_view_reblast().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting text with location to a friend")
        h.swipe_view_reblast().click()
        h.blast_friends().click()
        h.username(account03).click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.press_keycode(4)

    def reblast_text_no_loc(self):
        h.username(account01).click()
        log("Reblasting text blast without location to all followers")
        h.swipe_view_reblast().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting text blast without location to blast list")
        h.swipe_view_reblast().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting text blast without location to a friend")
        h.swipe_view_reblast().click()
        h.blast_friends().click()
        h.username(account03).click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.press_keycode(4)

    def reblast_photo_with_loc(self):
        h.username(account01).click()
        log("Reblasting photo blast with location to all followers")
        h.swipe_view_reblast().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting photo blast with location to blast list")
        h.swipe_view_reblast().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting photo blast with location to a friend")
        h.swipe_view_reblast().click()
        h.blast_friends().click()
        h.username(account03).click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.press_keycode(4)

    def reblast_photo_no_loc(self):
        h.username(account01).click()
        log("Reblasting photo blast without location to all followers")
        h.swipe_view_reblast().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting photo blast without location to blast list")
        h.swipe_view_reblast().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting photo blast without location to a friend")
        h.swipe_view_reblast().click()
        h.blast_friends().click()
        h.username(account03).click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.press_keycode(4)

    def reblast_giphy_with_loc(self):
        h.username(account01).click()
        log("Reblasting giphy with location to all followers")
        h.swipe_view_reblast().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting giphy with location to blast list")
        h.swipe_view_reblast().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting giphy with location to a friend")
        h.swipe_view_reblast().click()
        h.blast_friends().click()
        h.username(account03).click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.press_keycode(4)

    def reblast_giphy_no_loc(self):
        h.username(account01).click()
        log("Reblasting giphy without location to all followers")
        h.swipe_view_reblast().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting giphy without location to blast list")
        h.swipe_view_reblast().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting giphy without location to a friend")
        h.swipe_view_reblast().click()
        h.blast_friends().click()
        h.username(account03).click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.press_keycode(4)

    def reblast_video_with_loc(self):
        h.username(account01).click()
        log("Reblasting video blast with location to all followers")
        h.swipe_view_reblast().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting video blast with location to blast list")
        h.swipe_view_reblast().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting video blast with location to a friend")
        h.swipe_view_reblast().click()
        h.blast_friends().click()
        h.username(account03).click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.press_keycode(4)

    def reblast_video_no_loc(self):
        h.username(account01).click()
        log("Reblasting video blast without location to all followers")
        h.swipe_view_reblast().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting video blast without location to blast list")
        h.swipe_view_reblast().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)
        log("Reblasting video blast without location to a friend")
        h.swipe_view_reblast().click()
        h.blast_friends().click()
        h.username(account03).click()
        h.blast_Ok_button().click()
        h.swipe_view_reply()
        driver.press_keycode(4)

    def check_reblast_count(self):
        LoginWith().user(account03, password03, driver)
        try:
            if h.name("24", 10):
                log("Blast count correct")
                h.blast_more_button().click()
                log("Deleting blasts")
                h.blast_more_delete().click()
        except Exception:
            log("Blast count incorrect", "Warning")

