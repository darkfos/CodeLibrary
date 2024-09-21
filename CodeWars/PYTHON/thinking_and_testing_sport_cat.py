"""
    No Story
    No Description
    Only by Thinking and Testing
    Look at result of testcase, guess the code!
"""


def testit(act, s):
    # 7 kyu

    result_string: str = ""
    for do, pr in zip(act, s):
        if do == "run":
            if pr == "_":
                result_string += "_"
            else:
                result_string += "/"

        if do == "jump":
            if pr == "|":
                result_string += "|"
            else:
                result_string += "x"

    return result_string