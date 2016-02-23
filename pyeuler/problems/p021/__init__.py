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
