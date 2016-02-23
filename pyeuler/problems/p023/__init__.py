"""
https://projecteuler.net/problem=23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as
the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from pyeuler.common import get_proper_divisors_sum
from collections import OrderedDict

def main():
    n = 1
    abundant_numbers = OrderedDict()
    # abundant_number_sums = {}
    answer = 0

    while n <= 28123:
        # print('eval: ' + str(n))
        proper_div_sum = get_proper_divisors_sum(n)
        # print('proper_div_sum: ' + str(proper_div_sum))
        if proper_div_sum > n:
            abundant_numbers[n] = True
            # print('found abundant number: ' + str(n))

        is_abundant_sum = False
        for key in abundant_numbers.keys():
            diff = n - key
            # print('diff {} = n {} - key {}'.format(str(diff), str(n), str(key)))
            # print(abundant_numbers.keys())
            if diff == key or abundant_numbers.get(diff):
                # abundant_number_sums[n] = (key, diff)
                print('found abundant sum: ' + str(n))
                is_abundant_sum = True
                break

            if diff < key:
                break

        if not is_abundant_sum:
            answer += n

        n += 1

    print('answer: ' + str(answer))


if __name__ == '__main__':
    main()
