"""
    Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should
    be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
    Valid inputs examples:

    Examples of valid inputs:
    1.2.3.4
    123.45.67.89

    Invalid input examples:

    1.2.3
    1.2.3.4.5
    123.456.78.90
    123.045.067.089

    Notes:

        Leading zeros (e.g. 01.02.03.04) are considered invalid
        Inputs are guaranteed to be a single string
"""


def is_valid_IP(strng):
    #6 kyu

    data_ip: list = strng.split(".")
    if len(data_ip) == 4:
        all_integers_data = all([number.isdigit() and (number[0] != "0" if len(number) > 1 else True) and int(number) <= 255 for number in data_ip])
        return all_integers_data
    return False