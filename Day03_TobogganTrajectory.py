import numpy as np


def get_input() -> list:
    with open('Input/Day03_TobogganTrajectory.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def part_one(data: list) -> int:
    number_cols = len(data[0])

    trees = 0
    for i, line in enumerate(data):
        column = 3 * i % number_cols
        if line[column] == "#":
            trees = trees + 1
    return trees


def part_two(data: list) -> np.int64:
    number_rows = len(data)
    number_cols = len(data[0])
    right = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]

    trees = 0
    trees_all = np.zeros(len(right))
    for i in range(len(right)):
        for j in range(0, number_rows, down[i]):
            column = int(right[i] * j / down[i] % number_cols)
            line = data[j]
            if line[column] == "#":
                trees = trees + 1
        trees_all[i] = int(trees)
        trees = 0
    return np.int64(np.prod(trees_all))


def main():
    print('Number of encountered trees for part 1:', part_one(get_input()))
    print('The number of trees encountered on each of the listed slopes multiplied together:', part_two(get_input()))


if __name__ == '__main__':
    main()
