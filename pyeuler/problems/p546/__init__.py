# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=546
Define fk(n) = ∑ni=0∑i=0n fk(⌊ik⌋⌊ik⌋) where fk(0) = 1 and ⌊x⌋⌊x⌋ denotes the floor function.

For example, f5(10) = 18, f7(100) = 1003, and f2(103) = 264830889564.

Find (∑10k=2(∑k=210 fk(1014))) mod (109+7).
"""
import math
from pyeuler.common import memoize


@memoize
def floor_fraction(i, k):
    return math.floor(i / k)


@memoize
def floors_revenge(k, n):
    print('-----> dive into unmemoized instance k: {} n: {}'.format(str(k), str(n)))
    if n == 0:
        print('<-- pop from unmemoized instance k: {} n: {} result: {}'.format(str(k), str(n), '1'))
        return 1

    result = 0
    for i in range(0, n+1):
        fract = floor_fraction(i, k)
        new_result = floors_revenge(k, fract)
        result += new_result
        print('done: k: {} n: {} result: {}'.format(str(k), str(fract), str(new_result)))

    print('<-- pop from unmemoized instance k: {} n: {} result: {} <----'.format(str(k), str(n), str(result)))
    return result


def run_case(k, n):
    print('testing: k = {}, n = {}'.format(str(k), str(n)))
    result = floors_revenge(k, n)
    print('result: ' + str(result))


def main():
    # run_case(5, 10)
    # run_case(7, 100)
    # run_case(2, pow(10, 3))

    print('running the real thing...')
    answer = 0
    for k in range(2, 11):
        answer += floors_revenge(k, pow(10, 14))

    answer %= pow(10, 9) + 7
    print('answer: ' + str(answer))

if __name__ == '__main__':
    main()
