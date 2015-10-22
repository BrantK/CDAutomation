from elements.drivers import Home, log
from tests.accountManagement.test_methods import Account_Management_test


h = Home()
log("Starting account management test", "Start")

try:
    Account_Management_test().test_changing_password()
except Exception as e:
    log("When changing password", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    Account_Management_test().test_changing_email()
except Exception as e:
    log("When changing email address", "Error")
    log(e, "Expression")
    h.back_button().click()
    pass

try:
    Account_Management_test().test_account_deleting()
except Exception as e:
    log("When deleting account","Error")
    log(e, "Expression")
    h.back_button().click()
    pass
