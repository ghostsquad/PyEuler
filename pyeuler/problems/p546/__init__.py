# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=546
Define fk(n) = ∑ni=0∑i=0n fk(⌊ik⌋⌊ik⌋) where fk(0) = 1 and ⌊x⌋⌊x⌋ denotes the floor function.

For example, f5(10) = 18, f7(100) = 1003, and f2(103) = 264830889564.

Find (∑10k=2(∑k=210 fk(1014))) mod (109+7).
"""
import datetime
import logging
from assertpy import assert_that

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

log = logging.getLogger(__name__)


class Revenger(object):
    def __init__(self, k):
        self.log = logging.getLogger(self.__class__.__name__)
        self.k = k
        self.iteration = 0
        self.result = 0
        self.next_result = 0
        self.incr_list = [k, 1]

    def next_result(self, prev_result, incr):
        return incr * self.k + prev_result

    def next(self):
        self.iteration += 1
        self.log.info('iteration: %s', self.iteration)

        self.log.info('list before: %s', self.incr_list)

        if self.iteration % self.k == 0:
            self.log.debug('iteration %s is evenly divisable by %s', self.iteration, self.k)
            if self.incr_list[-1] % 5 == 0:
                self.incr_list.append(1)

        for idx in reversed(range(len(self.incr_list))):
            if idx + 1 == len(self.incr_list):
                incr_by = 1
            else:
                incr_by = self.incr_list[idx + 1]

            if idx == 0:
                break

            self.log.debug('incrementing idx: %s of value %s by %s',
                           idx,
                           self.incr_list[idx],
                           incr_by)

            self.incr_list[idx] += incr_by

        self.incr_list[0] += (self.incr_list[1] * self.k)

        self.log.info('list after: %s', self.incr_list)

        return self.incr_list[0]


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
