"""
    Hofstadter sequences are a family of related integer sequences, among which the first ones were described by American professor Douglas Hofstadter in his book Gödel, Escher, Bach.
    Task

    Today we will be implementing the rather chaotic recursive sequence of integers called Hofstadter Q.

    The Hofstadter Q is defined as follows:

    As the author states in the aforementioned book:

    It is reminiscent of the Fibonacci definition in that each new value is a sum of two previous values - but not of the immediately previous two values. Instead, the two immediately previous values tell how far to count back to obtain the numbers to be added to make the new value
    The function produces the sequence
    1, 1, 2, 3, 3, 4, 5, 5, 6, ..

    Test info
    100 random tests ( LC: 20 )
    0 < n <= 5 000 ( Python: 1 000, LC: 500 )
"""


def hofstadter_q(n):
    #6 kyu

    hofstadter_q: list = []
    for numb in range(0, n):
        if numb > 2:
            hofstadter_q.append(
                hofstadter_q[numb - hofstadter_q[numb-1]] + hofstadter_q[numb - hofstadter_q[numb-2]]
            )
        else:
            hofstadter_q.append(numb if numb > 1 else 1)
    return hofstadter_q[-1]