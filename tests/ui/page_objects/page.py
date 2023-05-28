import logging

from tests.ui.page_objects.locators import MainPageLocators, ResultsPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self, title):
        return title == self.driver.title


class MainPage(BasePage):
    def fill_input(self, text):
        elem = self.driver.find_element(*MainPageLocators.INPUT_FIELD)
        elem.send_keys(text)

    def click_submit_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def is_header_matches(self, header):
        return header == self.driver.find_element(*MainPageLocators.HEADER).text


class ResultsPage(BasePage):
    def is_results_found(self):
        element = self.driver.find_element(*ResultsPageLocators.RESULT)
        logging.error(element.text)
        return element.text != ""

    def get_result(self):
        element = self.driver.find_element(*ResultsPageLocators.RESULT)
        logging.error(element.text)
        return element.text


class ErrorPage(BasePage):
    pass
