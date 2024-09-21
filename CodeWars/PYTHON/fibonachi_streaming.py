"""
    You're going to provide a needy programmer a utility method that
    generates an infinite amount of sequential fibonacci numbers.
    to do this write a 'generator' starting with 1

    A fibonacci sequence starts with two 1s. Every element afterwards is the sum of the two previous elements.
"""


def all_fibonacci_numbers():
    #5 kyu
    n1, n2 = 0, 1
    
    while True:
        n3 = n2
        n2 = n1+n2
        n1 = n3
        yield n1