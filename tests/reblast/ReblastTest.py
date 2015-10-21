# Automated reblast test

from elements.drivers import Home, log
from tests.reblast.test_methods import ReblastTest, driver

h = Home()
log("Starting reblast test", "Start")


def relaunch():
    driver.close_app()
    driver.launch_app()


try:
    ReblastTest().send_text_with_loc()
except Exception as e:
    log("Sending text without location", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().send_text_no_loc()
except Exception as e:
    log("Sending text without location", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().send_photo_with_loc()
except Exception as e:
    log("Sending photo with location", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().send_photo_no_loc()
except Exception as e:
    log("Sending photo without location", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().send_giphy_with_loc()
except Exception as e:
    log("Sending giphy with location", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().send_giphy_no_loc()
except Exception as e:
    log("Sending giphy without location", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().send_video_with_loc()
except Exception as e:
    log("Sending video with location", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().send_video_no_loc()
except Exception as e:
    log("Sending video without location", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_setup()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_text_with_loc()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_text_no_loc()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_photo_with_loc()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_photo_no_loc()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_giphy_with_loc()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_giphy_no_loc()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_video_with_loc()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().reblast_video_no_loc()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    relaunch()
    pass

try:
    ReblastTest().check_reblast_count()
except Exception as e:
    log("Setting up reblast test", "Error")
    log(e, "Expression")
    pass

log("Reblast test finished", "Complete")