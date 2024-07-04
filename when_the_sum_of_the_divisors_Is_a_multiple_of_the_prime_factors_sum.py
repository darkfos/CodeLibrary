"""
    The numbers 12, 63 and 119 have something in common related with their divisors and
    their prime factors, let's see it.

    Numbers PrimeFactorsSum(pfs)        DivisorsSum(ds)              Is ds divisible by pfs
    12         2 + 2 + 3 = 7         1 + 2 + 3 + 4 + 6 + 12 = 28            28 / 7 = 4,  Yes
    63         3 + 3 + 7 = 13        1 + 3 + 7 + 9 + 21 + 63 = 104         104 / 13 = 8, Yes
    119        7 + 17 = 24           1 + 7 + 17 + 119 = 144                144 / 24 = 6, Yes

    There is an obvius property you can see: the sum of the divisors of a number
    is divisible by the sum of its prime factors.

    We need the function ds_multof_pfs() that receives two arguments: nMin and nMax,
    as a lower and upper limit (inclusives), respectively, and outputs a sorted list
    with the numbers that fulfill the property described above.
    We represent the features of the described function:
    ds_multof_pfs(nMin, nMax) -----> [n1, n2, ....., nl] # nMin ≤ n1 < n2 < ..< nl ≤ nMax
"""


class PrimeFactorSum:
    def ds_multof_pfs(self, nMin, nMax):
        # 5 kyu

        return [
            numb
            for numb in range(nMin, nMax + 1)
            if (self.divisors_sum(numb) % self.prime_factors_sum(numb) == 0)
        ]  # sorted list

    def prime_factors_sum(self, number: int) -> int:

        factor_numbers: list = []
        nmb: int = 2

        while nmb * nmb <= number:
            if number % nmb == 0:
                factor_numbers.append(nmb)
                number //= nmb
            else:
                nmb += 1
        if number > 2:
            factor_numbers.append(number)

        return sum(factor_numbers)

    def divisors_sum(self, number: int) -> int:
        res: set = set()

        for nmb in range(1, int(number ** 0.5) + 1):
            if number % nmb == 0:
                res.add(nmb)
                res.add(number // nmb)

        return sum(res)


ds_multof_pfs = PrimeFactorSum().ds_multof_pfs