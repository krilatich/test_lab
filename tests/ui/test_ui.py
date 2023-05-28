import pytest

from selenium import webdriver
import page_objects.page as page


class TestAppUI:

    def test_main_page_title_matches(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)

        assert main_page.is_title_matches('This is Test App')

    def test_main_page_header_matches(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)

        assert main_page.is_header_matches('This is Test App')

    def test_result_not_empty_with_nums(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('112121')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.is_results_found()

    def test_result_empty_with_empty_string(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == 'bad request'

    def test_result_with_digits(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('226')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == "3"

    def test_with_list_with_single_digit(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('1')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == "1"

    def test_with_invalid_data(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('@!@#%&"')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == "bad request"

    def test_with_too_long_data(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        string = "6" * 101
        main_page.fill_input(string)
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == "bad request"


