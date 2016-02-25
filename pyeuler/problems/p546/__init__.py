# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=546
Define fk(n) = ∑ni=0∑i=0n fk(⌊ik⌋⌊ik⌋) where fk(0) = 1 and ⌊x⌋⌊x⌋ denotes the floor function.

For example, f5(10) = 18, f7(100) = 1003, and f2(103) = 264830889564.

Find (∑10k=2(∑k=210 fk(1014))) mod (109+7).
"""
import datetime
import math
from pyeuler.common import memoize

done_msg = 'done: i: {} k: {} n: {} new_result: {} result_multiplied_k: {} final_result: {}'
pop_msg = '<-- pop from unmemoized instance k: {} n: {} final_result: {} <----'
dive_msg = '-----> dive into unmemoized instance k: {} n: {}'


@memoize
def floor_fraction(i, k):
    return math.floor(i / k)


@memoize
def floors_revenge(k, n):
    #print(dive_msg.format(str(k), str(n)))
    if n == 0:
        #print(pop_msg.format(str(k), str(n), '1'))
        return 1

    final_result = 0
    i = 0
    while i <= n:
        fract = floor_fraction(i, k)
        new_result = floors_revenge(k, fract)
        result_multiplied_k = new_result * k
        final_result += result_multiplied_k
        i += k
        #print(done_msg.format(str(i), str(k), str(fract), str(new_result), str(result_multiplied_k), str(final_result)))

    #print(pop_msg.format(str(k), str(n), str(final_result)))
    return final_result


def run_case(k, n):
    print('testing: k = {}, n = {}'.format(str(k), str(n)))
    result = floors_revenge(k, n)
    print('result: ' + str(result))


def main():
    print('started ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    # run_case(5, 10)
    # run_case(7, 100)
    # run_case(2, pow(10, 3))

    print('running the real thing...')
    answer = 0
    for k in range(2, 11):
        answer += floors_revenge(k, pow(10, 14))

    answer %= pow(10, 9) + 7
    print('answer: ' + str(answer))
    print('done ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

if __name__ == '__main__':
    main()
