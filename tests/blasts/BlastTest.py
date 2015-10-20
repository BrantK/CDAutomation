# Automated blast test

from elements.drivers import Home, log
from tests.blasts.test_methods import BlastTest, driver

h = Home()
log("Starting Blast test", "Start")


def relaunch():
    driver.close_app()
    driver.launch_app()

try:
    BlastTest().test_sending_text_blasts()
except Exception as e:
    log("Sending text blast", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    BlastTest().test_sending_photo_blast_01()
except Exception as e:
    log("Sending photo blast", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    BlastTest().test_sending_photo_blast_02()
except Exception as e:
    log("Sending photo blast", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    BlastTest().test_sending_giphy_blast()
except Exception as e:
    log("Sending giphy blast", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    BlastTest().test_sending_video_blast_01()
except Exception as e:
    log("Sending video blast", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    BlastTest().test_sending_video_blast_02()
except Exception as e:
    log("Sending video blast", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    BlastTest().test_sending_text_for_replies()
except Exception as e:
    log("Sending text blast for reply test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    BlastTest().test_opening_text_blast()
except Exception as e:
    log("Opening text blast", "Error")
    log(e, "Expression")
    pass

try:
    BlastTest().test_opening_photo_blast()
except Exception as e:
    log("Opening photo blast", "Error")
    log(e, "Expression")
    pass

try:
        BlastTest().test_opening_non_public_blast()
except Exception as e:
    log("Opening non public blast", "Error")
    log(e, "Expression")
    pass

try:
        BlastTest().test_opening_giphy_blast()
except Exception as e:
    log("Opening giphy blast", "Error")
    log(e, "Expression")
    pass

try:
    BlastTest().test_opening_video_blast()
except Exception as e:
    log("When opening video blasts", "Error")
    log(e, "Expression")
    pass

try:
    BlastTest().test_reply_to_blast()
except Exception as e:
    log("When replying to blast", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    BlastTest().test_checking_blast_replies()
except Exception as e:
    log("When checking blast replies", "Error")
    log(e, "Expression")
    relaunch()
    pass
