from holmium.core import Element, Page, Locators

class LoginMain(Page):

    username = Element(Locators.ID, "txtEmail", timeout=1)
    password = Element(Locators.ID, "txtSignInPassword", timeout=1)
    sign_in = Element(Locators.NAME, "btnSignIn", timeout=1)

    def do_login(self, username, password):
        self.username.clear()
        self.username.send_keys(username)
        self.password.clear()
        self.password.send_keys(password)
        self.sign_in.click()
