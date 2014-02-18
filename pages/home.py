from holmium.core import Page, Element, Locators

class HomeMain(Page):

    logout_link = Element(Locators.ID, "aLogoutUtility", timeout=1)
