# Automated blast test

import logging
import unittest
from time import sleep
from elements.drivers import WebDriver, LoginWith, Home
from appium.webdriver.common.touch_action import TouchAction as ta

account01 = "blasttest01"
password01 = account01

account02 = "blasttest02"
password02 = account02

account03 = "blasttest03"
password03 = account03

blast_text = "+blasttest01\n\nwww.cyberdust.com"


class BlastTest(unittest.TestCase):
    def test_blasts(self):
        h = Home()
        driver = WebDriver().driver()

        # # Logs into blast testing account
        # LoginWith().user(account01, password01, driver)
        #
        # # Creates a blast list
        # print("Creating new blast list")
        # h.blast_lists().click()
        # h.blast_list_field().send_keys("List from Blasts tab")
        # h.OK_button().click()
        # h.username(account02).click()
        # h.username(account03).click()
        # h.OK_button().click()
        #
        # # Sends text blast with URL, +username, and location to blast list
        # print("Sending text blast to blast list")
        # h.action_menu().click()
        # h.action_menu_text().click()
        # h.dust_blast_field().send_keys(blast_text)
        # h.text_location_button().click()
        # h.current_location().click()
        # h.OK_button().click()
        # h.send_to_blast_list().click()
        # h.blast_Ok_button().click()
        #
        # # Edits participants and renames blast list
        # print("Editing blast list")
        # h.blast_lists().click()
        # h.blast_list_expand()
        # h.blast_list_edit().click()
        # h.username(account02).click()
        # h.blast_list_more().click()
        # h.rename_list().click()
        # h.rename_blast_list().send_keys("Edited blast list")
        # h.OK_button().click(), sleep(1)
        # h.OK_button().click()
        # h.back_button().click()
        #
        # # Sends text blast to new blast list and makes it not public
        # print("Sending non public text blast")
        # h.action_menu().click()
        # h.action_menu_text().click()
        # h.dust_blast_field().send_keys("Should not be able to reblast this!")
        # h.OK_button().click()
        # h.make_public().click()
        # h.send_to_blast_list().click()
        # h.blast_Ok_button().click()
        #
        # # Deletes blast list
        # print("Deleting renamed blast list")
        # h.blast_lists().click()
        # h.blast_list_expand()
        # h.blast_list_edit().click()
        # h.blast_list_more().click()
        # h.delete_list().click()
        # h.confirm().click()
        #
        # # Sends text blast with giphy to a single friend
        # print("Sending giphy")
        # h.action_menu().click()
        # h.action_menu_text().click()
        # h.dust_blast_field().send_keys(":giphy cats")
        # h.OK_button().click()
        # h.blast_friends().click()
        # h.username(account02).click()
        # h.blast_Ok_button().click()
        #
        # # Sends photo blast with drawing and text to all followers
        # print("Sending photo blast with drawing and text to all followers")
        # h.action_menu().click()
        # h.action_menu_media().click()
        # h.photo_button().click()
        # h.photo_pen().click()
        # driver.swipe(h.photo_back_button().location['x']+50, h.photo_back_button().location['y']-50,
        #              h.photo_pen().location['x'], h.photo_pen().location['y']+50)
        # h.photo_color().click()
        # driver.swipe(h.next_button().location['x']+100, h.next_button().location['y']-50,
        #              h.location_button().location['x']+50, h.location_button().location['y']+50)
        # h.add_text().click()
        # h.add_text_field().send_keys(blast_text)
        # h.done_button().click()
        # h.next_button().click()
        # h.blast_all_followers().click()
        # h.blast_Ok_button().click()
        #
        # # Takes video with text, creates blast list, then sends to that blast list
        # print("Taking video then creating a blast list")
        # h.action_menu().click()
        # h.action_menu_media().click()
        # h.video_button().click()
        # ta(driver).long_press(h.photo_button(), duration=8000).release().perform()
        # h.add_text().click()
        # h.add_text_field().send_keys(blast_text)
        # h.done_button().click()
        # h.next_button().click()
        # h.create_blast_list().click()
        # h.blast_list_field().send_keys("My Test List")
        # h.OK_button().click()
        # h.username(account02).click()
        # h.username(account03).click()
        # h.OK_button().click()
        # h.send_to_blast_list().click()
        # h.blast_Ok_button().click()
        #
        # # Deletes blast list
        # print("Deleting blast list")
        # h.blast_lists().click()
        # h.blast_list_expand()
        # h.blast_list_edit().click()
        # h.blast_list_more().click()
        # h.delete_list().click()
        # h.confirm().click()

        # Logout and then login to the recipient account
        #LoginWith().user(account02, password02, driver)

        # Opens blast from the sending account
        # print("Opening blasts")
        # h.blast_preview_card().click()
        # # click to follow user
        # h.swipe_view_add().click()
        # h.swipe_view_location().click(), sleep(2),
        # driver.press_keycode(4)
        # h.swipe_view_url_card().click(), sleep(2)
        # h.back_button().click()

        # swipe to next blast

        # Checks if giphy was received
        h.name("bktest01").click()
        try:
            sleep(3)
            if driver.find_element_by_id("com.radicalapps.cyberdust:id/page_frag_gif_view") and\
                    driver.find_element_by_id("com.radicalapps.cyberdust:id/text_overlay"):
                print("Giphy successfully found")
        except Exception:
            print("! Giphy was not found")


        # swipe to next blast


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BlastTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
