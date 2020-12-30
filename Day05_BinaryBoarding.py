import numpy as np


def get_input() -> list:
    with open('Input/Day05_BinaryBoarding.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def part_one(data: list) -> int:
    num_col = len(data)
    row = np.zeros(num_col)
    col = np.zeros(num_col)
    result = np.zeros(num_col)
    row_powers = np.flip(2 ** np.arange(7))
    col_powers = np.flip(2 ** np.arange(3))
    string_dict = {
        "F": 0,
        "B": 1,
        "L": 0,
        "R": 1
    }

    for i, line in enumerate(data):
        row_string = line[0:7]
        col_string = line[7:]
        row_numbers = [string_dict[x] for x in row_string]
        col_numbers = [string_dict[x] for x in col_string]
        row[i] = np.dot(row_numbers, row_powers)
        col[i] = np.dot(col_numbers, col_powers)
        result[i] = 8 * row[i] + col[i]

    max_value = int(np.max(result))
    return max_value


def part_two(data: list) -> int:
    num_col = len(data)
    row = np.zeros(num_col)
    col = np.zeros(num_col)
    result = np.zeros(num_col)
    row_powers = np.flip(2 ** np.arange(7))
    col_powers = np.flip(2 ** np.arange(3))
    string_dict = {
        "F": 0,
        "B": 1,
        "L": 0,
        "R": 1
    }

    for i, line in enumerate(data):
        row_string = line[0:7]
        col_string = line[7:]
        row_numbers = [string_dict[x] for x in row_string]
        col_numbers = [string_dict[x] for x in col_string]
        row[i] = np.dot(row_numbers, row_powers)
        col[i] = np.dot(col_numbers, col_powers)
        result[i] = 8 * row[i] + col[i]

    result = np.sort(result)
    result_compare = np.linspace(np.min(result), np.max(result), num_col + 1)
    missing_seat = set(result_compare).difference(result)
    return int(next(iter(missing_seat)))


def main():
    print('Highest seat ID on a boarding pass:', part_one(get_input()))
    print('ID of my seat:', part_two(get_input()))


if __name__ == '__main__':
    main()
