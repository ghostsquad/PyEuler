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
