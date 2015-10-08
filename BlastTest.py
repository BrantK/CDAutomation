# Automated blast test

import unittest
import cd_elements.elements as wd
from cd_elements.elements import Home
from selenium.common.exceptions import TimeoutException
from time import sleep

blast_recipient = ""
blast_text = ""


class BlastTest(unittest.TestCase):
    def test_blasts(self):
        h = Home()
        sleep(1)
        h.action_menu().click()
        h.action_menu_media().click()
        h.photo_button().click()
        h.photo_pen().click()
        wd.driver.swipe(200, 450, 500, 800)
        h.photo_add_text().click()
        h.photo_add_text_field().send_keys("Test test test")
        h.done_button().click()
        h.next_button().click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BlastTest)
    unittest.TextTestRunner(verbosity=2).run(suite)