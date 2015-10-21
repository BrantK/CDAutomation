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
        sleep(5)
        h.sent_text_blast().click()
        try:
            if h.pinned_message(2):
                log("Pinned a message")
        except Exception:
            log("Problem in pinning", "Error")
            pass


        log("Checking if Pinned icon appears")

        if h.tap_to_unpin_button():
            log("Pinned icon appears")
        else:
            log("Pinned icon does not appear")

        h.back_button().click()
        try:
            if h.pinned_message():
                log("Message is not disappered")
        except Exception:
            log("Message is disappeared")
            pass

        log("Checking if new messages appear below pinned messages")

        h.chat_room_text_box().send_keys(text_message)
        h.chat_room_send_button().click()
        h.chat_room_text_box().send_keys(text_message)
        h.chat_room_send_button().click()
        h.chat_room_text_box().send_keys(text_message)
        h.chat_room_send_button().click()
        try:
            if h.tap_to_unpin_button(2):
                log("New messages do not appear below pinned message", "Error")
        except Exception:
            log("New Messages appear below pinned message")
            pass
        h.back_button().click()

        h.tap_to_unpin_button().click()
        try:
            if h.sent_text_blast():
                log("Unpinned the message")
        except Exception:
            log("Unable to unpin" "Error")
            pass
        sleep(16)

        try:
            if h.sent_text_blast():
                log("Countdown did not resume")
        except Exception:
            log("Countdown resumed")
            pass

        h.back_button().click()
        h.back_button().click()
        m.more_button().click()

        driver.scroll(m.followers(), m.back_button())

        m.logout().click()
        m.confirm().click()





















