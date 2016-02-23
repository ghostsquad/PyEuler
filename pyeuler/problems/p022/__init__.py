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
