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

pop_msg    = '{}}}-- leaving unmemoized f_k{}({}) final_result: {} <--'
dive_msg   = '{}{{-- in unmemoized f_k {}({}) -->'
loop_start = '{}  [*** start loop k: {} n: {}'
loop_inner = '{}    |   start iter i {}'
loop_short = '{}    |   found shortcut: k={} n={} already discovered. mem_result {} final_result {}'
done_msg   = '{}    |   done  iter i {} of n {} f_k {}({}) new_result: {}'
loop_stop  = '{}  ]**X stop loop k: {} n: {}'
memoizing  = '{}  memoizing k: {} n: {} = {}'
done_memo  = '{}  already memoized: k: {} n: {} = {} done...'
odd_loop   = '{}  n is ODD, do one more iteration. n {} f_k {}({}) new_result: {} final_result: {}'
depth_add  = '  '

memo_dict = {}

# we need to memoize this, but manually, because we can shortcut the inner loop by checking if a previous
# answer has already been found
@memoize
def floors_revenge(k, n, depth=None):
    if depth is not None:
        depth += depth_add
    else:
        depth = ''

    print(dive_msg.format(depth, str(k), str(n)))
    if n == 0:
        print(pop_msg.format(depth, str(k), str(n), '1'))
        return 1

    final_result = 0
    results = []
    i = n
    print(loop_start.format(depth, str(k), str(n)))
    while i >= 0:
        print(loop_inner.format(depth, str(i)))
        mem_result = memo_dict.get((k, i))
        if mem_result:
            final_result += mem_result
            print(loop_short.format(depth, str(k), str(i), str(mem_result), str(final_result)))
            break
        else:
            fraction = math.floor(i / k)
            mem_result = memo_dict.get((k, fraction))
            if mem_result:
                print(loop_short.format(depth, str(k), str(i), str(mem_result), str(final_result)))

            new_result = floors_revenge(k, fraction, depth + '    ')
            t = new_result, i
            results.append(t)
            print(done_msg.format(depth, str(i), str(n), str(k), str(fraction), str(new_result)))
        i -= 1

    print(loop_stop.format(depth, str(k), str(n)))

    while len(results) > 0:
        result_tuple = results.pop()
        final_result += result_tuple[0]
        if memo_dict.get((k, result_tuple[1])):
            print(done_memo.format(depth, k, result_tuple[1], final_result))
            break

        print(memoizing.format(depth, k, result_tuple[1], final_result))
        memo_dict[(k, result_tuple[1])] = final_result

    print(pop_msg.format(depth, str(k), str(n), str(final_result)))
    return final_result


def run_case(k, n):
    print('-----------------------------')
    print('testing: k = {}, n = {}'.format(str(k), str(n)))
    result = floors_revenge(k, n)
    print('result: ' + str(result))
    print('-----------------------------')


def main():

    print('started ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    run_case(5, 10)
    run_case(7, 100)
    run_case(2, pow(10, 3))

    exit(0)

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
