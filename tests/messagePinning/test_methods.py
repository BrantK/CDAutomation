from time import sleep
from elements.drivers import WebDriver, LoginWith, Home, log, More
from appium.webdriver.common.touch_action import TouchAction as ta

#############################################
account_name = "existingTest01"
account_pw = "password"
account_email = "new_existing@cyberdust.com"
text_message = "cyber dust"
#############################################

h = Home()
m = More()
driver = WebDriver().driver()
sw = driver.get_window_size()['width']
sh = driver.get_window_size()['height']

class MessagePinning_test:
    def test_pinning_messages(self):
        # Logs into existing testing account
        LoginWith().user(account_name, account_pw, driver)
        log("Logged In")

        h.action_menu().click()
        h.action_menu_dust().click()
        sleep(5)
        #m.chat_room_first_friend().click()
        h.chat_room_text_box().click()
        h.chat_room_text_box().send_keys(text_message)
        h.chat_room_send_button().click()
        log("Sent a dust")
        sleep(2)
        h.sent_text_blast().click()
        #try:
         #   if h.pinned_message(2):
          #      log("Pinned a message")
        #except Exception:
         #   log("Problem in pinning", "Error")
          #  pass
        if h.pinned_message(2):
            log("pinned a message")
        else:
            log("problem in pinning", "Error")

        log("Checking if Pinned icon appears")

        if h.tap_to_unpin_button():
            log("Pinned icon appears")
        else:
            log("Pinned icon does not appear")

        log("Checking if new messages appear below pinned messages")

        h.chat_room_text_box().send_keys(text_message)
        h.chat_room_text_box().send_keys(text_message)

        if h.pinned_message(1):
            log("New messages do not appear below pinned messages")
        else:
            log("New messages appear below pinned messages")

        log("Checkinng if timer resumes counting down after unpinning")
















