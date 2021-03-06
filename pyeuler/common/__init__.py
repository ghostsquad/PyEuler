import math


def get_proper_divisors_sum(num):
    max_division_num = math.sqrt(num)
    result = 0
    n = 1
    proper_divisors = []
    while n <= max_division_num:
        if num % n == 0:
            result += n
            proper_divisors.append(n)
            if n == max_division_num:
                break

            if n > 1:
                quotient = num / n
                result += int(quotient)
                proper_divisors.append(int(quotient))
        n += 1

    # print('proper_divisors: ' + str(proper_divisors))

    return result


def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """

    class MemoDict(dict):
        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return MemoDict(f)
