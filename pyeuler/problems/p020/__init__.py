"""
https://projecteuler.net/problem=20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def main():
    n = 100
    num = 1
    while n >= 1:
        num *= n
        n -= 1

    nums = list(str(num))

    answer = 0
    for v in nums:
        answer += int(v)

    print('answer: ' + str(answer))

if __name__ == '__main__':
    main()
