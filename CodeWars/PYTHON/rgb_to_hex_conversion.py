"""
    The rgb function is incomplete. Complete it so that passing in RGB decimal
    values will result in a hexadecimal representation being returned. Valid
    decimal values for RGB are 0 - 255. Any values that fall out of that
    range must be rounded to the closest valid value.

    Note: Your answer should always be 6 characters long, the shorthand with 3
      will not work here.
    Examples (input --> output):

    255, 255, 255 --> "FFFFFF"
    255, 255, 300 --> "FFFFFF"
    0, 0, 0       --> "000000"
    148, 0, 211   --> "9400D3"
"""


def rgb(r, g, b):
    #5 kyu

    res: str = ""
    for j in (r, g, b):
        number = nmb_eq(j)
        hx_number = str(hex(number))[str(hex(number)).index('x')+1:].upper()
        res += hx_number if len(hx_number) > 1 else "0"+hx_number
    return res

def nmb_eq(number: int):
    if number < 0:return 0
    elif number > 255: return 255
    return number