import pytest
from lib.api_helper import *


class TestClass:
    def test_http_ok_on_default_page(self):
        assert get_form().status_code == 200

    def test_http_ok_on_results_page(self):
        assert post_form('112').status_code == 200

    def test_http_result_page_not_empty(self):
        assert post_form('12121').text != ''

    def test_http_form_page_content_type(self):
        assert get_form().headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_http_result_page_content_type(self):
        assert post_form('231321').headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_num_decoding_two_ways_result(self):
        assert post_form("12").text == '2'

    def test_num_decoding_three_ways_result(self):
        assert post_form("226").text == '3'

    def test_num_decoding_no_ways_result(self):
        assert post_form("06").text == '0'

    def test_num_decoding_two_ways_code(self):
        assert post_form("12").status_code == 200

    def test_num_decoding_three_ways_code(self):
        assert post_form("226").status_code == 200

    def test_num_decoding_no_ways_code(self):
        assert post_form("06").status_code == 200

    def test_num_decoding_with_empty_string(self):
        assert post_form("").status_code == 400

    def test_num_decoding_with_len_101(self):
        data = "6" * 101
        assert post_form(data).status_code == 400

    def test_num_decoding_with_only_digits_result(self):
        assert post_form("6543210").text == '1'

    def test_num_decoding_with_only_digits_code(self):
        assert post_form("6543210").status_code == 200

    def test_num_decoding_with_letters(self):
        assert post_form("abcde").status_code == 400

    def test_num_decoding_with_digits_and_letters(self):
        assert post_form("abcde12345").status_code == 400

    def test_num_decoding_with_ascii_symbols(self):
        assert post_form("@!$%@$^*.").status_code == 400

    def test_num_decoding_with_zero_result(self):
        assert post_form("0").text == '0'

    def test_num_decoding_with_zeros_result(self):
        assert post_form("00000000").text == '0'

    def test_num_decoding_with_zero_code(self):
        assert post_form("0").status_code == 200

    def test_num_decoding_with_zeros_cde(self):
        assert post_form("00000000").status_code == 200

    def test_list_with_symbols_unicode(self):
        strs = ["＄﹩"]
        strs = ", ".join(strs)

        assert post_form(strs).status_code == 400

    def test_list_with_symbols_weird(self):
        strs = ["µþýøåß∂ƒ©˙∆˚¬…ææ≥≤µ˜˜√ç≈Ω``∑´´†¥¨ˆˆπ“ њ"]
        strs = ", ".join(strs)

        assert post_form(strs).status_code == 400

    def test_list_with_emoji(self):
        strs = ["👩🏿‍🍳"]
        strs = ", ".join(strs)

        assert post_form(strs).status_code == 400

    def test_list_with_japanese(self):
        strs = ["お前はもう死んでいる"]
        strs = ", ".join(strs)

        assert post_form(strs).status_code == 400



