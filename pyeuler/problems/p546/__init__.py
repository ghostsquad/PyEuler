# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=546
Define fk(n) = ∑ni=0∑i=0n fk(⌊ik⌋⌊ik⌋) where fk(0) = 1 and ⌊x⌋⌊x⌋ denotes the floor function.

For example, f5(10) = 18, f7(100) = 1003, and f2(103) = 264830889564.

Find (∑10k=2(∑k=210 fk(1014))) mod (109+7).
"""
import datetime
import math
from assertpy import assert_that
from pyeuler.common import memoize

memo_dict = {}

depth = 0


def floors_revenge(k, n):
    i = 0
    mult = 1
    result = 0
    while i <= n:
        print("---------------")
        i_start = i
        print('mult: {} k: {}'.format(mult, k))
        extra = (mult - k) * k
        extra_msg = 'extra: ({} - {k}) * {k} = {}'.format(mult, extra, k=k)
        if extra < 0:
            extra = 0

        if i == n:
            k = 1
            print('adj k: {}'.format(k))
        elif i + k > n:
            k = n - i + 1
            print('adj k: {}'.format(k))

        before_extra = k * mult
        temp_sum = before_extra + extra
        result += temp_sum
        i += k
        print(extra_msg)
        print('{}-{} = sum of {} + {} = {}'.format(i_start, i - 1, before_extra, extra, temp_sum))
        print('result: {}'.format(result))
        mult += 1

    return result


def run_case(k, n, expected_result):
    print('-----------------------------')
    print('testing: k = {}, n = {}'.format(str(k), str(n)))
    result = floors_revenge(k, n)
    print('final result: ' + str(result))
    print('-----------------------------')

    assert_that(result).is_equal_to(expected_result)


def main():

    print('started ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    run_case(5, 10, 18)
    run_case(7, 100, 1003)
    run_case(2, 61, 264830889564)
    # run_case(2, pow(10, 3))

    # exit(0)

    print('  samples done at ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

    print('============================================')
    print('running the real thing...')
    answer = 0
    for k in range(2, 11):
        answer += floors_revenge(k, pow(10, 14))

    answer %= (pow(10, 9) + 7)
    print('answer: ' + str(answer))
    print('done ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    print('============================================')

if __name__ == '__main__':
    main()
