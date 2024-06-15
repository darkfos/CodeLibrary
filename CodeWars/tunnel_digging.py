"""
    Given a list r, return how long it would take a tunnel boring machine to excavate a tunnel through r.
    r is a list that contain the following sections made of combinations of the following:

        Very hard rock []: this section takes 60 minutes to excavate
        Hard Rock {}: this section takes 50 minutes to excavate
        Somewhat Hard Rock (): this section takes 40 minutes to excavate
        Somewhat Soft Rock ||: this section takes 30 minutes to excavate
        Soft Rock ::: this section takes 20 minutes to excavate
        Broken Rock   : this section only needs to be cleared (see below)

    After every 3 sections it excavates, the machine needs to stop for 30 minutes so workers can remove the excavated rock.
    Notes:

        The returned time should be in minutes
        'r' may contain sections with only one half. Example: [ should equal 30

    Examples

    tunnel_digging(['()', ')']) # returns 60
    tunnel_digging([': ', '  ', ': ']) # returns 50
    tunnel_digging(['|)', '{ ', '{ ', '|]', '{ ', ' }']) # returns 240
    tunnel_digging(['( ', '()', '(}', '[]', '{ ', '{ ']) # returns 275
    tunnel_digging(['  ', '{ ', '[ ', '[)', '[}']) # returns 190
    tunnel_digging(['{ ', ' }', '[}', ': ', '[ ', ':|']) # returns 230
"""


def tunnel_digging(r):
    # 7 kyu

    result: int = 0
    time_stop: int = 0
    dct_tunnel: dict = {
        "[": 30,
        "]": 30,
        "{": 25,
        "}": 25,
        "(": 20,
        ")": 20,
        "|": 15,
        ":": 10
    }

    for strings in r:
        local_string: str = strings.strip()

        time_stop += 1

        if time_stop % 3 == 0 and time_stop != 0:
            result += 30

        while local_string:

            if local_string[0] in dct_tunnel:
                result += dct_tunnel.get(local_string[0])
                local_string = local_string.replace(local_string[0], "", 1)

    return result