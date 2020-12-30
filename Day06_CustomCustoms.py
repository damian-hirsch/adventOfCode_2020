import numpy as np


def get_input() -> list:
    with open('Input/Day06_CustomCustoms.txt', 'r') as file:
        data = file.read().replace("\n", ",").replace(",,", "\n").replace(",", "")
        data = data.split("\n")
    return data


def get_input2() -> list:
    with open('Input/Day06_CustomCustoms.txt', 'r') as file:
        data = file.read().replace("\n", ",").replace(",,", "\n").replace(",", " ")
        data = data.split("\n")
    return data


def part_one(data: list) -> int:
    num_col = len(data)
    counts = np.zeros(num_col)

    for i, line in enumerate(data):
        # Remove double occurrence
        line = set(line)
        counts[i] = len(line)
    return int(np.sum(counts))


def part_two(data: list) -> int:
    num_col = len(data)
    counts = np.zeros(num_col)

    for i, line in enumerate(data):
        # Split data into list
        line = line.split(" ")
        # Split each entry into a set and then intersect all of these sets
        intersect = set.intersection(*map(set, line))
        counts[i] = len(intersect)
    return int(np.sum(counts))


def main():
    print('Number of questions to which anyone answered "yes":', part_one(get_input()))
    print('Number of questions to which everyone answered "yes":', part_two(get_input2()))


if __name__ == '__main__':
    main()
