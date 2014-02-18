from holmium.core import Page, Element, Locators

class CorpMain(Page):

    login_link = Element(Locators.ID, "aLoginUtility", timeout=1)
