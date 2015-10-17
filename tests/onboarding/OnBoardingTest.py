# Automated on boarding test....

from elements.drivers import Home,log
from tests.onboarding.test_methods import OnBoardingTest


h = Home()
log("Starting on boarding test", "Start")

OnBoardingTest().check_if_logged_out()

try:
    OnBoardingTest().test_sign_up()
except Exception as e:
    log("When signing up", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    OnBoardingTest().test_profile_picture()
except Exception as e:
    log("When taking a profile picture during on boarding", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    OnBoardingTest().test_updating_profile_picture()
except Exception as e:
    log("When updating profile picture", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    OnBoardingTest().test_logout_login()
except Exception as e:
    log("When testing logout and login", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass
