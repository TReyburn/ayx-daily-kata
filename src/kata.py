class Kata:

    @staticmethod
    def reverse_str(src_str: str) -> str:
        rev_str = ""
        if not isinstance(src_str, str):
            return rev_str
        for letter in src_str:
            rev_str = letter + rev_str
        return rev_str
