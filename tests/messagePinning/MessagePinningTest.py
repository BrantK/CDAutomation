
from elements.drivers import Home, log
from tests.messagePinning.test_methods import MessagePinning_test

h = Home()
log("Starting message pinning test", "Start")

try:
    MessagePinning_test().test_pinning_messages()
except Exception as e:
    log("When pinning messages", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass