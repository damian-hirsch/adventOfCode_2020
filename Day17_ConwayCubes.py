import numpy as np


def get_input():
    with open('Input/Day17_ConwayCubes.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def convert_to_matrix(data_list: list, cycles: int) -> np.ndarray:
    rows = len(data_list)
    columns = len(data_list[0])
    data_matrix = np.zeros((2 * cycles + 1, 2 * cycles + rows, 2 * cycles + columns))
    string_dict = {
        ".": 0,
        "#": 1
    }
    for i in range(cycles, rows + cycles):
        data_matrix[cycles, i, cycles:(columns + cycles)] = np.array([string_dict[datapoint] for datapoint in data_list[i-cycles]])
    return data_matrix


def convert_to_matrix_part2(data_list: list, cycles: int) -> np.ndarray:
    rows = len(data_list)
    columns = len(data_list[0])
    data_matrix = np.zeros((2 * cycles + 1, 2 * cycles + 1, 2 * cycles + rows, 2 * cycles + columns))
    string_dict = {
        ".": 0,
        "#": 1
    }
    for i in range(cycles, rows + cycles):
        data_matrix[cycles, cycles, i, cycles:(columns + cycles)] = \
            np.array([string_dict[datapoint] for datapoint in data_list[i-cycles]])
    return data_matrix


def neighbors(data_matrix: np.ndarray, z: int, x: int, y: int) -> int:
    depth = data_matrix.shape[0]
    rows = data_matrix.shape[1]
    columns = data_matrix.shape[2]
    neighbors_count = 0
    # Checking all seats around
    for k in range(z - 1, z + 2):
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                # Check if seat is out of bounds or itself
                if (x != i or y != j or z != k) and 0 <= i <= rows - 1 and 0 <= j <= columns - 1 \
                        and 0 <= k <= depth - 1 and 0 <= x <= rows - 1 and 0 <= y <= columns - 1 and 0 <= z <= depth:
                    # print(seating_matrix[i, j])
                    if data_matrix[k, i, j] == 1:
                        neighbors_count = neighbors_count + 1
    return neighbors_count


def neighbors_part2(data_matrix: np.ndarray, w: int, z: int, x: int, y: int) -> int:
    fourth = data_matrix.shape[0]
    depth = data_matrix.shape[1]
    rows = data_matrix.shape[2]
    columns = data_matrix.shape[3]
    neighbors_count = 0
    # Checking all seats around
    for m in range(w - 1, w + 2):
        for k in range(z - 1, z + 2):
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    # Check if seat is out of bounds or itself
                    if (x != i or y != j or z != k or w != m) and 0 <= i <= rows - 1 and 0 <= j <= columns - 1 and \
                            0 <= k <= depth - 1 and 0 <= m <= fourth - 1 and 0 <= x <= rows - 1 and \
                            0 <= y <= columns - 1 and 0 <= z <= depth and 0 <= w <= fourth:
                        # print(seating_matrix[i, j])
                        if data_matrix[m, k, i, j] == 1:
                            neighbors_count = neighbors_count + 1
    return neighbors_count


def part_one(data_list: list, cycles: int) -> int:
    data_matrix = convert_to_matrix(data_list, cycles)
    data_matrix_old = np.copy(data_matrix)
    depth = data_matrix.shape[0]
    rows = data_matrix.shape[1]
    columns = data_matrix.shape[2]
    for c in range(cycles):
        for k in range(depth):
            for i in range(rows):
                for j in range(columns):
                    if data_matrix_old[k, i, j] == 1:
                        if not 2 <= neighbors(data_matrix_old, k, i, j) <= 3:
                            data_matrix[k, i, j] = 0
                    elif data_matrix_old[k, i, j] == 0:
                        if neighbors(data_matrix_old, k, i, j) == 3:
                            data_matrix[k, i, j] = 1
        data_matrix_old = np.copy(data_matrix)
    return int(np.sum(data_matrix))


def part_two(data_list: list, cycles: int) -> int:
    data_matrix = convert_to_matrix_part2(data_list, cycles)
    data_matrix_old = np.copy(data_matrix)
    fourth = data_matrix.shape[0]
    depth = data_matrix.shape[1]
    rows = data_matrix.shape[2]
    columns = data_matrix.shape[3]
    for c in range(cycles):
        for m in range(fourth):
            for k in range(depth):
                for i in range(rows):
                    for j in range(columns):
                        if data_matrix_old[m, k, i, j] == 1:
                            if not 2 <= neighbors_part2(data_matrix_old, m, k, i, j) <= 3:
                                data_matrix[m, k, i, j] = 0
                        elif data_matrix_old[m, k, i, j] == 0:
                            if neighbors_part2(data_matrix_old, m, k, i, j) == 3:
                                data_matrix[m, k, i, j] = 1
        data_matrix_old = np.copy(data_matrix)
    return int(np.sum(data_matrix))


def main():
    print('Active cubes after the sixth cycle:', part_one(get_input(), 6))
    print('Active cubes after the sixth cycle:', part_two(get_input(), 6))


if __name__ == '__main__':
    main()
