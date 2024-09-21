"""
    Input

    You’ll receive a list of lists, representing all the jobs Bear the Freelancer
    carried out for the month. Each array within the outer list is comprised of the
    number of hours worked, and the proximity to the client as a string, the possible
    values being 'Close Friend', 'Friend', 'Acquaintance', or any other string for the rest
    of his clients. The recognition of those three strings ('Close Friend', 'Friend', and 'Acquaintance')
    should be case insensitive.
"""


def bear_dollars(jobs):
    #7 kyu

    friends_money: dict = {
        "Close Friend": 25,
        "Friend": 50,
        "Acquaintance": 100,
    }
    
    return sum((job[0] * friends_money.get(job[-1].title()) if job[-1].title() in friends_money else job[0]*125 for job in jobs))