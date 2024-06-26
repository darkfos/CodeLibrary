from typing import List

"""
    You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

    You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
    Return the array ans. Answers within 10-5 of the actual answer will be accepted.
"""


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Easy

        return [273.15 + celsius, celsius * 9 / 5 + 32]