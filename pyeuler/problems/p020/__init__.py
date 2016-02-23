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
