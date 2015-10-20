# Automated blast test

from elements.drivers import Home, log
from tests.blasts.test_methods import BlastTest

h = Home()
log("Starting blasts test", "Start")

try:
    BlastTest().test_sending_text_blasts()
except Exception as e:
    log("When sending text blasts", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    BlastTest().test_sending_photo_blasts()
except Exception as e:
    log("When sending photo blasts", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    BlastTest().test_sending_video_blasts()
except Exception as e:
    log("When sending video blasts", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    BlastTest().test_opening_text_blast()
except Exception as e:
    log("When opening text blasts", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    BlastTest().test_opening_photo_blast()
except Exception as e:
    log("When opening photo blasts", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    BlastTest().test_opening_video_blast()
except Exception as e:
    log("When opening video blasts", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    BlastTest().test_reply_to_blast()
except Exception as e:
    log("When replying to blast", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    BlastTest().test_checking_blast_replies()
except Exception as e:
    log("When checking blast replies", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass
