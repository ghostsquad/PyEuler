"""
https://projecteuler.net/problem=21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from pyeuler.common import get_proper_divisors_sum


def main(num):

    answer = 0

    last_smallest_amicable_number = 0

    while num >= 1:
        if num == last_smallest_amicable_number:
            print('skipping: {}. We already found this pair.'.format(num))
            num -= 1
            continue

        # print('testing: ' + str(num))
        a_sum = get_proper_divisors_sum(num)
        # print('a_sum: ' + str(a_sum))
        if num != a_sum and a_sum > 1:
            b_sum = get_proper_divisors_sum(a_sum)
            # print('b_sum: ' + str(b_sum))

            if b_sum == num:
                # print('num: ' + str(num))
                last_smallest_amicable_number = a_sum
                print('SCORE: adding {} and {} to answer!'.format(b_sum, a_sum))
                answer += a_sum + b_sum

        num -= 1

    print('answer: ' + str(answer))

if __name__ == '__main__':
    main(9999)
