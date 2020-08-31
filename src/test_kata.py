import pytest
from src.kata import Kata


class TestKata:
    reverse_str_test_data = [["abc", "cba"], ["step on no pets", "step on no pets"], ["travis", "sivart"]]

    @pytest.mark.parametrize("src_str, expect_str", reverse_str_test_data)
    def test_reverse_str(self, src_str: str, expect_str: str):
        assert expect_str == Kata.reverse_str(src_str)
