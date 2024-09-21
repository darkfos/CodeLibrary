class RomanNumerals:
    # 4 kyu
    """
    Write two functions that convert a roman numeral to and from an integer value.
    Multiple roman numeral values will be tested for each function.

    Modern Roman numerals are written by expressing each digit separately starting
    with the left most digit and skipping any digit with a value of zero. In Roman numerals:

    1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
    2008 is written as 2000=MM, 8=VIII; or MMVIII
    1666 uses each Roman symbol in descending order: MDCLXVI.

    Input range : 1 <= n < 4000

    In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
    """

    ROMAN_VALUES: dict[int, str] = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    @classmethod
    def to_roman(cls, val: int) -> str:
        result: str = ""

        while val:
            for el in cls.ROMAN_VALUES.keys():
                if val >= el:
                    result += cls.ROMAN_VALUES.get(el)
                    val -= el
                    break
        return result

    @classmethod
    def from_roman(cls, roman_num: str) -> int:
        result: int = 0
        prev_el: str = 0

        for el in roman_num[::-1]:
            for rome_el in cls.ROMAN_VALUES.items():
                if el == rome_el[-1]:
                    if rome_el[0] >= prev_el:
                        result += rome_el[0]
                    elif rome_el[0] <= prev_el:
                        result -= rome_el[0]
                    prev_el = rome_el[0]
        return result