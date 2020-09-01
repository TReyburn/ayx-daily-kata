import pytest
from src.kata import Kata


class TestKata:
    valid_rev_str_data = [["abc", "cba"], ["step on no pets", "step on no pets"], ["travis", "sivart"], ["", ""]]
    invalid_rev_str_data = [14, [], True]

    @pytest.mark.parametrize("valid_str, expect_str", valid_rev_str_data)
    def test_reverse_str_valid(self, valid_str: str, expect_str: str):
        assert expect_str == Kata.reverse_str(valid_str)

    @pytest.mark.parametrize("invalid_str", invalid_rev_str_data)
    def test_reverse_str_invalid(self, invalid_str: any):
        assert not Kata.reverse_str(invalid_str)

    def test_fizz_buzz_valid(self):
        assert False

    def test_fizz_buzz_invalid(self):
        assert False
