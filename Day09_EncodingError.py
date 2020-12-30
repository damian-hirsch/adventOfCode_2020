import numpy as np
from itertools import combinations_with_replacement


def get_input() -> np.ndarray:
    data = np.loadtxt('Input/Day09_EncodingError.txt')
    return data


def get_sums(array: np.ndarray, n: int):
    # Sum all combinations and remove double entries (set)
    sum_list = set(sum(comb) for comb in combinations_with_replacement(array, n))
    return sum_list


def part_one(array: np.ndarray) -> int:
    shift = 25
    entry = int
    for i in range(len(array) - shift):
        entry = int(array[i+shift])
        sum_list = get_sums(array[i:i+shift], 2)
        if entry not in sum_list:
            break
    return entry


def part_two(array: np.ndarray, number: int) -> int:
    n = np.where(array == number)[0][0]
    # Pick a starting point
    for i in range(n):
        curr_sum = array[i]

        # try all sub-arrays starting with 'i'
        j = i + 1
        while j <= n:

            if curr_sum == number:
                print("Sum found between indexes % d and % d" % (i, j-1))
                print(array[i:j])
                min_number = np.min(array[i:j])
                max_number = np.max(array[i:j])
                min_max_sum = int(min_number + max_number)
                return min_max_sum

            if curr_sum > number or j == n:
                break

            curr_sum = curr_sum + array[j]
            j += 1

    print("No sub-array found")
    return -1


def main():
    array = get_input()
    number = part_one(array)
    print("The first number without the encoding property is:", number)
    print("The the encryption weakness in the XMAS-encrypted list is:", part_two(array, number))


if __name__ == '__main__':
    main()
