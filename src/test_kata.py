import pytest
from src.kata import Kata


class TestKata:
    valid_rev_str_data = [["abc", "cba"], ["step on no pets", "step on no pets"], ["travis", "sivart"], ["", ""]]
    invalid_rev_str_data = [14, [], True]
    valid_fizzbuzz_data = [[1, "1"], [2, "2"], [3, "fizz"], [5, "buzz"]]
    invalid_fizzbuzz_data = []

    @pytest.mark.parametrize("valid_str, expect_str", valid_rev_str_data)
    def test_reverse_str_valid(self, valid_str: str, expect_str: str):
        assert expect_str == Kata.reverse_str(valid_str)

    @pytest.mark.parametrize("invalid_str", invalid_rev_str_data)
    def test_reverse_str_invalid(self, invalid_str: any):
        assert not Kata.reverse_str(invalid_str)

    @pytest.mark.parametrize("valid_int, expect_str", valid_fizzbuzz_data)
    def test_fizz_buzz_valid(self, valid_int, expect_str):
        assert Kata.fizzbuzz(valid_int) == expect_str

    @pytest.mark.parametrize("invalid_int, expect_str", invalid_fizzbuzz_data)
    def test_fizz_buzz_invalid(self, invalid_int, expect_str):
        assert False
