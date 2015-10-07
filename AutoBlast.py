# Sends out blasts to specified recipients

import unittest
import cd_elements.elements as myDriver
from cd_elements.elements import Home
from appium.webdriver.common.touch_action import TouchAction

blast_recipient = "bktest01"
blast_type = "photo, video, text" # Use photo, video, text, or a combination of the 3
blast_text = "+bkortman +bktest01 +bktest02 \n www.google.com" # Only works for blast_type = text
number_of_blasts = 3 # Number of blasts per type

h = Home()


class AutoBlast(unittest.TestCase):
    def test_blasts(self):

        def photo_blast():
            h.action_menu().click()
            h.action_menu_media().click()
            h.photo_button().click()
            h.next_button().click()
            h.blast_friends().click()
            h.blast_recipient(blast_recipient).click()
            h.blast_Ok_button().click()

        def video_blast():
            h.action_menu().click()
            h.action_menu_media().click()
            h.video_button().click()
            TouchAction(myDriver.driver).long_press(h.photo_button(), duration=8000).release().perform()
            h.next_button().click()
            h.blast_friends().click()
            h.blast_recipient(blast_recipient).click()
            h.blast_Ok_button().click()

        def text_blast():
            h.action_menu().click()
            h.action_menu_text().click()
            h.dust_blast_field().send_keys(blast_text)
            h.OK_button().click()
            h.blast_friends().click()
            h.blast_recipient(blast_recipient).click()
            h.blast_Ok_button().click()

        for i in range(number_of_blasts):

            if "text" in blast_type:
                text_blast()
                print("Sending text blast #%d" % (i+1))
            if "photo" in blast_type:
                photo_blast()
                print("Sending photo blast #%d" % (i+1))
            if "video" in blast_type:
                video_blast()
                print("Sending video blast #%d" % (i+1))


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AutoBlast)
    unittest.TextTestRunner(verbosity=2).run(suite)