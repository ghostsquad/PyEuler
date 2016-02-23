"""
https://projecteuler.net/problem=22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import csv
import os


def main(data_file):
    names = []
    with open(data_file) as f:
        for row in csv.reader(f, delimiter=','):
            names = names + row

    names.sort()

    answer = 0

    list_position = 1
    for name in names:
        print("eval: " + name)
        alphabetical_value = 0
        for c in name:
            alphabetical_value += ord(c) - 64

        name_score = list_position * alphabetical_value
        answer += name_score
        list_position += 1

    print('answer: ' + str(answer))

if __name__ == '__main__':
    data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    main(data_file)
