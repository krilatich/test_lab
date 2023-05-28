from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'go')
    INPUT_FIELD = (By.NAME, 'data')
    HEADER = (By.TAG_NAME, 'h1')


class ResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    RESULT = (By.TAG_NAME, 'body')
