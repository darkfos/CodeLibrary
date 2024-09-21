"""
    Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
"""


from typing import Dict


class Solution:
    def dayOfYear(self, date: str) -> int:
        #Easy

        date = date.split("-")
        month, days = int(date[1]), int(date[-1])

        month_days: Dict[int, int] = {
            1: 31,
            2: 29 if self.check_year(year=int(date[0])) else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        for month_d in range(1, month + 1):
            if month_d == month:
                continue
            days += month_days[month_d]

        return days

    def check_year(self, year: int):
        """
        Check year
        :param year:
        :return:
        """

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False