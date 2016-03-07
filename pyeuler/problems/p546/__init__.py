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

memo_dict = {}

depth = 0


def floors_revenge(k, n):
    result = memo_dict.get((k, n))

    if result is not None:
        return result

    global depth
    depth += 2

    #print((' ' * depth) + '{{ in unmemoized instance of f {k}({n})'.format(k=k, n=n))

    if n == 0:
        #print((' ' * depth + '}} end f {k}({n}) res {r}'.format(k=k, n=n, r=1)))
        depth -= 2
        return 1

    results = []
    final_result = 0
    odd_result = 0
    shortcut_result = 0
    main_index = n

    depth += 2

    odd_loop_count = (n+1) % k
    main_index -= odd_loop_count
    if odd_loop_count > 0:
        fraction = math.floor(n / k)
        result = floors_revenge(k, fraction)
        odd_result = result * odd_loop_count
        final_result += odd_result
        #print((' ' * depth + 'odd_ct {c} odd_r {r} starting_final {f}'.format(c=odd_loop_count, r=odd_result, f=1)))

    while main_index >= 0:
        mem_result = memo_dict.get((k, main_index))
        if main_index != n and mem_result is not None:
            #print((' ' * depth + '{k}, {n} already memoized as {r}, shortcut!'.format(k=k, n=main_index, r=mem_result)))
            shortcut_result = mem_result
            final_result += mem_result
            break

        fraction = math.floor(main_index / k)
        #print((' ' * depth + '{{ working on i {i}, f {k}({f})!'.format(i=main_index, k=k, f=fraction)))
        result = floors_revenge(k, fraction)
        new_result = result * k
        final_result += new_result
        results.append((main_index, new_result))
        #print((' ' * depth + '}} done with i {i}, f {k}({f}) = {r} final {fin}'.format(i=main_index, k=k, f=fraction, r=new_result, fin=final_result)))
        main_index -= k
    depth -= 2

    mem_result_final = shortcut_result
    while len(results) > 0:
        result = results.pop()
        mem_num = result[0]
        mem_result_final += result[1]
        #print((' ' * depth + '  memoizing f {k}({t}) as {r}'.format(k=k, t=mem_num, r=mem_result_final)))
        memo_dict[(k, mem_num)] = mem_result_final

    memo_dict[(k, n)] = final_result
    #print((' ' * depth + '}} end f {k}({n}) res {r}'.format(k=k, n=n, r=final_result)))
    depth -= 2
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
    run_case(2, 61)
    run_case(2, pow(10, 3))

    #exit(0)

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
