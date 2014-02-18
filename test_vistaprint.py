from selenium import webdriver
import unittest

class VistaprintTests(unittest.TestCase):

    def test_login(self):
        """
        Test if I can login with valid credentials
        """
        firefox = webdriver.Firefox()
        firefox.get("http://vistaprint.com")
        firefox.find_element_by_id("aLoginUtility").click()
        firefox.find_element_by_id("txtEmail").send_keys("test@sajnikanth.com")
        firefox.find_element_by_id("txtSignInPassword").send_keys("ten20304050")
        firefox.find_element_by_name("btnSignIn").click()
        assert firefox.find_element_by_id("aLogoutUtility").is_displayed()
        firefox.quit()

if __name__ == "__main__":
    unittest.main()
