# Automated blast test

import BlastTest.test_modules
from BlastTest.test_modules import BlastTest
from time import sleep
from elements.drivers import WebDriver, LoginWith, Home
from appium.webdriver.common.touch_action import TouchAction as ta

h = Home()


try:
    BlastTest().test_sending_text_blasts()
except Exception:
    print("Failed: sending text blasts")
    h.back_button().click()
    pass

try:
    BlastTest().test_sending_photo_blasts()
except Exception:
    print("Failed: sending photo blasts")
    h.back_button().click()
    pass

try:
    BlastTest().test_sending_video_blasts()
except Exception:
    print("Failed: sending video blasts")
    h.back_button().click()
    pass

try:
    BlastTest().test_receiving_blasts()
except Exception:
    print("Failed: sending receiving blasts")
    h.back_button().click()
    pass

try:
    BlastTest().test_reply_to_blast()
except Exception:
    print("Failed: Replying to blast")
    h.back_button().click()
    pass
