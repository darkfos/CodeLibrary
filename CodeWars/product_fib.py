def product_fib(_prod):
    """
    5 kyu

    Given a number, say prod (for product), we search two Fibonacci numbers
    F(n) and F(n+1) verifying
    Your function productFib takes an integer (prod) and returns an array
    If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return
    """

    fib_1, fib_2 = 0, 1

    while True:
        if fib_1 * fib_2 == _prod:
            return [fib_1, fib_2, True]
        elif fib_1 * fib_2 > _prod:
            return [fib_1, fib_2, False]

        time_fib2 = fib_2
        fib_2 = fib_1 + fib_2
        fib_1 = time_fib2