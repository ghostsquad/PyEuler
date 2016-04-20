# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=546
Define fk(n) = ∑ni=0∑i=0n fk(⌊ik⌋⌊ik⌋) where fk(0) = 1 and ⌊x⌋⌊x⌋ denotes the floor function.

For example, f5(10) = 18, f7(100) = 1003, and f2(103) = 264830889564.

Find (∑10k=2(∑k=210 fk(1014))) mod (109+7).
"""
import datetime
from assertpy import assert_that
from sympy import *

a, b, c, x, y = symbols('a b c x y')
quadratic_equation_expr = Eq(a * x**2 + b * x + c - y)


def extract_parabolic_values(coords):
    """
    returns a tuple with values of (a, b, c)
    from the equation: y = ax^2 + bx + c
    :param coords:
        example: [
            1,1
            2,4
            3,10
        ]
    :return: 3-tuple
    """
    exprs = []
    for coor in coords:
        expr = quadratic_equation_expr.subs([(x, coor[0]), (y, coor[1])])
        exprs.append(expr)

    return solve(exprs, [a, b, c])


def solve_for_y(k, x_val):
    if k == 2:
        av, bv, cv = Rational(3, 2), Rational(-3, 2), 1
    elif k % 2 == 0:
        av, bv, cv = k/2, -(k-1), 0
    else:
        av, bv, cv = Rational(k, 2), Rational(-(k-2)/2), 0

    expr = quadratic_equation_expr.subs([(x, x_val), (a, av), (b, bv), (c, cv)])
    return solve(expr)[0]


def floors_revenge(k, n):
    i = 0
    set_num = 0
    result = 0
    set_mult = 0
    while i <= n:
        i_start = i
        print('--------- {} ---------'.format(i))

        if i % k == 0:
            print('increasing set_num...')
            set_num += 1
            if set_mult % k == 0:
                print('set_mult BUMP!...')
                set_mult = solve_for_y(k, set_num)
            else:
                print('set_mult incr!...')
                set_mult += set_num

        print('set: {} set_mult: {}'.format(set_num, set_mult))

        if i == n:
            k = 1
            print('adj k: {}'.format(k))
        elif i + k > n:
            k = n - i + 1
            print('adj k: {k} because {i} + {k} > {n}'.format(i=i, k=k, n=n))

        temp_sum = k * set_mult
        result += temp_sum
        i += k
        print('{}-{} = sum of {}'.format(i_start, i - 1, temp_sum))
        print('result: {}'.format(result))
        print('---------------------')
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
    run_case(2, pow(10, 3), 264830889564)

    exit(0)

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
