"""
https://projecteuler.net/problem=18
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""
import os


def enumerate_reversed(enumerable):
    for index in reversed(range(len(enumerable))):
        yield index, enumerable[index]


def main(data_file):
    triangle = []

    with open(data_file) as data:
        for line in data:
            line_array = list(map(int, line.split()))
            if len(line_array) >= 1:
                triangle.append(line_array)

    parents = []
    for idx, row in enumerate_reversed(triangle):
        # because we are enumerating the triangle from bottom to top,
        # we can stop looking for parents when we reach index 0
        if idx != 0:
            # what we want to accomplish, is a new triangle, that defines:
            # below me, the highest sum you can get is X
            # the way we do that is by starting at the bottom of the triangle,
            # working our way up, and replacing numbers in rows with:
            # x + max(c1, c2) where x is the current number, and cN are the two possible routes below it (children)
            #
            # # example work to be done
            # 17 47 82
            #  |\ |\ |\
            # 18 35 87 10
            # given the above triangle rows,
            # starting on line 1, each number will have 2 children,
            # p(17) has c(18) and c(35)

            # we are enumerating starting at the bottom, therefore:
            parents = triangle[idx - 1]
            children = triangle[idx]

            for num_idx, value in enumerate(parents):
                parents[num_idx] = value + max([children[num_idx], children[num_idx + 1]])

    answer = parents[0]

    print(answer)

if __name__ == '__main__':
    data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    main(data_file)
