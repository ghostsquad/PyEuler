"""
https://projecteuler.net/problem=24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

With some help from:
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""


def find_non_increasing_suffix(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return None

    return i


def find_successor_to_pivot(arr, suffix_idx):
    i = len(arr) - 1
    while arr[i] <= arr[suffix_idx - 1]:
        i -= 1

    return i


def reverse_suffix(arr, suffix_idx):
    arr[suffix_idx:] = arr[len(arr) - 1: suffix_idx - 1: -1]


def get_next_permutation(arr):
    suffix_idx = find_non_increasing_suffix(arr)
    if suffix_idx is None:
        return None

    successor = find_successor_to_pivot(arr, suffix_idx)
    # swap places
    arr[suffix_idx - 1], arr[successor] = arr[successor], arr[suffix_idx - 1]

    reverse_suffix(arr, suffix_idx)
    return arr


def main(arr, target):
    # first permutation is 0123456789
    permutation_idx = 2
    last_permutation = None
    while permutation_idx <= target:
        next_permutation = get_next_permutation(arr)
        if next_permutation is None:
            print('LAST PERMUTATION!')
            break
        last_permutation = next_permutation
        # print('found perm {}: {}'.format(str(permutation_idx), ''.join(map(str, last_permutation))))

        permutation_idx += 1

    print('answer: ' + ''.join(map(str, last_permutation)))

if __name__ == '__main__':
    arr = list(range(0, 10))
    target = pow(10, 6)
    main(arr, target)
