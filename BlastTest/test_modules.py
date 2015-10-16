# Automated blast test

from time import sleep
from elements.drivers import WebDriver, LoginWith, Home
from appium.webdriver.common.touch_action import TouchAction as ta

###############################
account01 = "blasttest01"
password01 = account01

account02 = "blasttest02"
password02 = account02

account03 = "blasttest03"
password03 = account03

blast_url = "www.cyberdust.com"
blast_username = "+"+account01
################################

h = Home()
driver = WebDriver().driver()
sw = driver.get_window_size()['width']
sh = driver.get_window_size()['height']


class BlastTest:
    def test_sending_text_blasts(self):
        # Logs into blast testing account
        LoginWith().user(account01, password01, driver)

        # Creates a blast list
        print("Creating new blast list")
        h.blast_lists().click()
        h.blast_list_field().send_keys("List from Blasts tab")
        h.OK_button().click()
        h.username(account02).click()
        h.username(account03).click()
        h.OK_button().click()

        # Sends text blast with +username, URL, and location to blast list
        print("Sending text blast to blast list")
        h.action_menu().click()
        h.action_menu_text().click()
        h.dust_blast_field().send_keys(blast_username+" "+blast_url)
        h.text_location_button().click()
        h.current_location().click()
        h.OK_button().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()

        # Edits participants and renames blast list
        print("Editing blast list")
        h.blast_lists().click()
        h.blast_list_expand()
        h.blast_list_edit().click()
        h.username(account03).click()
        h.blast_list_more().click()
        h.rename_list().click()
        h.rename_blast_list().send_keys("Edited blast list")
        h.OK_button().click(), sleep(1)
        h.OK_button().click()
        h.back_button().click()

    def test_sending_photo_blasts(self):
        # Sends photo blast with drawing and URL to all followers
        print("Sending photo blast with drawing and text to all followers")
        h.action_menu().click()
        h.action_menu_media().click()
        h.photo_button().click()
        h.photo_pen().click()
        driver.swipe(h.photo_back_button().location['x']+50, h.photo_back_button().location['y']-50,
                     h.photo_pen().location['x'], h.photo_pen().location['y']+50)
        h.photo_color().click()
        driver.swipe(h.next_button().location['x']+100, h.next_button().location['y']-50,
                     h.location_button().location['x']+50, h.location_button().location['y']+50)
        h.add_text().click()
        h.add_text_field().send_keys(blast_url)
        h.done_button().click()
        h.next_button().click()
        h.blast_all_followers().click()
        h.blast_Ok_button().click()

        # Sends non public photo blast with +username to the new blast list
        print("Sending non public photo blast")
        h.action_menu().click()
        h.action_menu_media().click()
        h.photo_button().click()
        h.add_text().click()
        h.add_text_field().send_keys(blast_username)
        h.done_button().click()
        h.next_button().click()
        h.make_public().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()

        # Deletes blast list
        print("Deleting renamed blast list")
        h.blast_lists().click()
        h.blast_list_expand()
        h.blast_list_edit().click()
        h.blast_list_more().click()
        h.delete_list().click()
        h.confirm().click()

    def test_sending_video_blasts(self):
        # Sends text blast with giphy to a single friend
        print("Sending giphy")
        h.action_menu().click()
        h.action_menu_text().click()
        h.dust_blast_field().send_keys(":giphy cats")
        h.OK_button().click()
        h.blast_friends().click()
        h.username(account02).click()
        h.blast_Ok_button().click()

        # Takes video, adds +username, creates blast list, then sends to that blast list
        print("Sending video to newly created blast list")
        h.action_menu().click()
        h.action_menu_media().click()
        h.video_button().click()
        ta(driver).long_press(h.photo_button(), duration=5000).release().perform()
        h.add_text().click()
        h.add_text_field().send_keys(blast_username)
        h.done_button().click()
        h.next_button().click()
        h.create_blast_list().click()
        h.blast_list_field().send_keys("My Test List")
        h.OK_button().click()
        h.username(account02).click()
        h.username(account03).click()
        h.OK_button().click()
        h.send_to_blast_list().click()
        h.blast_Ok_button().click()

        # Takes video, adds URL, then sends to single friend
        print("Sending video with URL")
        h.action_menu().click()
        h.action_menu_media().click()
        h.video_button().click()
        ta(driver).long_press(h.photo_button(), duration=5000).release().perform()
        h.add_text().click()
        h.add_text_field().send_keys(blast_url)
        h.done_button().click()
        h.next_button().click()
        h.blast_friends().click()
        h.username(account02).click()
        h.blast_Ok_button().click()

        # Sends text blast for reply test on other account
        print("Sending text blast for reply test")
        h.action_menu().click()
        h.action_menu_text().click()
        h.dust_blast_field().send_keys("Reply test")
        h.OK_button().click()
        h.blast_friends().click()
        h.username(account02).click()
        h.blast_Ok_button().click()

        # Deletes blast list
        print("Deleting blast list")
        h.blast_lists().click()
        h.blast_list_expand()
        h.blast_list_edit().click()
        h.blast_list_more().click()
        h.delete_list().click()
        h.confirm().click()

    def test_receiving_blasts(self):
        # Login as account02
        LoginWith().user(account02, password02, driver)

        # Opens text blast with +username, URL, and location
        print("Opening text blast")
        h.name(account01).click(), sleep(2)  # change to account01
        h.swipe_view_location().click(), sleep(3),
        driver.press_keycode(4), sleep(2)
        ta(driver).press(x=sw * .17, y=sh * .23).release().perform()  # clicks +username
        h.swipe_view_add().click(), sleep(2)
        h.swipe_view_url_card().click(), sleep(4)
        h.back_button().click(), sleep(1)

        # swipes to next blast
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)

        # Opens photo with drawing and URL
        try:
            sleep(3)
            if driver.find_element_by_id("com.radicalapps.cyberdust:id/page_frag_image"):
                print("Image loaded successfully")
        except Exception:
            print("! Image did not load")
        h.swipe_view_text().click(), sleep(4)
        h.back_button().click(), sleep(1)

        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)

        # Opens non public photo blast with +username
        try:
            sleep(4)
            if driver.find_element_by_id("com.radicalapps.cyberdust:id/page_frag_reblast"):
                print("! Able to reblast non public blast")
        except Exception:
            print("Not able to reblast non public blast")
        h.swipe_view_text().click()
        h.swipe_view_add().click(), sleep(1)

        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)

        # Checks if giphy was received
        try:
            sleep(3)
            if driver.find_element_by_id("com.radicalapps.cyberdust:id/page_frag_gif_view")and\
                    driver.find_element_by_id("com.radicalapps.cyberdust:id/text_overlay"):
                print("Giphy loaded successfully")
        except Exception:
            print("! Giphy was not found")

        sleep(1)
        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)

        # Opens video with +username
        try:
            sleep(4)
            if driver.find_element_by_id("com.radicalapps.cyberdust:id/overlay_video_view"):
                print("Video loaded successfully")
        except Exception:
            print("! Video did not load")
        h.swipe_view_text().click()
        h.swipe_view_add().click(), sleep(1)

        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)

        # Opens video with URL
        h.swipe_view_text().click(), sleep(4)
        h.back_button().click(), sleep(1)

        driver.swipe(sw*.800, sh*.300, sw*.100, sh*.300, 300)

    def test_reply_to_blast(self):
        # Opens blast and tests reply functionality
        print("Testing reply functionality")
        h.swipe_view_reply().click()
        h.swipe_view_reply().send_keys("Test reply")
        h.swipe_view_reply_send().click()
        h.swipe_view_reply().click()
        h.swipe_view_reply().send_keys(blast_username[:-2])
        h.swipe_view_reblast().click()
        h.swipe_view_reply_send().click()
        h.swipe_view_reply_monkey().click()
        h.swipe_view_monkey().click()
        h.swipe_view_emoji_cancel().click()
        h.swipe_view_reply_media().click()
        h.photo_button().click()
        h.photo_pen().click()
        driver.swipe(h.photo_back_button().location['x']+50, h.photo_back_button().location['y']-50,
                     h.photo_pen().location['x'], h.photo_pen().location['y']+50)
        h.swipe_view_photo_send().click()
        h.swipe_view_reply_media().click()
        h.video_button().click()
        ta(driver).long_press(h.photo_button(), duration=5000).release().perform()
        h.swipe_view_photo_send().click(), sleep(4)
        h.swipe_view_exit().click()

        # Login with account01 to check replies
        LoginWith().user(account01, password01, driver)

        # Opens replies from account02 and does a check to see if they were all received
        h.dusts_tab().click()
        h.username(account02).click()
        print("Checking if all replies were successful")
        try:
            sleep(2)
            driver.save_screenshot("C:\Screenshots\screenshottest01.jpg")
            if driver.find_elements_by_id("com.radicalapps.cyberdust:id/chat_bubble_view_message_text")and\
                    driver.find_element_by_id("com.radicalapps.cyberdust:id/emoji_view_image")and\
                    driver.find_element_by_id("com.radicalapps.cyberdust:id/photo_view_image")and\
                    driver.find_element_by_id("com.radicalapps.cyberdust:id/video_play_button"):
                print("All replies successfully received from %s" % account02)
        except Exception:
            print("! All replies were not received")
        sleep(1)
        driver.press_keycode(4)

        print("Complete")