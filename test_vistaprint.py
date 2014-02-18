import unittest
import pages


class VistaPrintTests(unittest.TestCase):

    def test_login(self):
        """
        Test if I can login with valid credentials
        """
        # instantiate corp page object and click on login link
        corp_site = pages.corp.CorpMain(self.driver, "http://vistaprint.com")
        corp_site.login_link.click()

        # instantiate login page object and login (function defined in pages/login.py)
        login_page = pages.login.LoginMain(self.driver)
        login_page.do_login("test@sajnikanth.com", "ten20304050")

        # instantiate home page object and assert if you see a logout link
        home_page = pages.home.HomeMain(self.driver)
        assert home_page.logout_link.is_displayed()

if __name__ == "__main__":
    unittest.main()
