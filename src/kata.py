class Kata:

    @staticmethod
    def reverse_str(src_str: str) -> str:
        rev_str = ""
        if not isinstance(src_str, str):
            return rev_str
        for letter in src_str:
            rev_str = letter + rev_str
        return rev_str

    @staticmethod
    def fizzbuzz(src_int: int) -> str:
        res_str = ""
        if src_int % 3 == 0:
            res_str += "fizz"
        if src_int % 5 == 0:
            res_str += "buzz"
        if not res_str:
            return str(src_int)
        return res_str
