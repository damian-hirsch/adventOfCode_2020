import numpy as np


def get_input():
    with open('Input/Day11_SeatingSystem.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def convert_to_matrix(seating_list: list) -> np.ndarray:
    rows = len(seating_list)
    columns = len(seating_list[0])
    seating_matrix = np.zeros((rows, columns))
    string_dict = {
        ".": -1,
        "L": 0,
        "#": 1
    }
    for i in range(rows):
        seating_matrix[i, :] = np.array([string_dict[chair] for chair in seating_list[i]])
    return seating_matrix


def neighbors_full(seating_matrix: np.ndarray, x: int, y: int) -> (bool, bool):
    rows = seating_matrix.shape[0]
    columns = seating_matrix.shape[1]
    neighbors_empty = False
    neighbors_four = False
    neighbors_count = 0
    # Checking all seats around
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            # Check if seat is out of bounds or itself
            if (x != i or y != j) and 0 <= i <= rows - 1 and 0 <= j <= columns - 1 and 0 <= x <= rows - 1 \
                    and 0 <= y <= columns - 1:
                # print(seating_matrix[i, j])
                if seating_matrix[i, j] == 1:
                    neighbors_count = neighbors_count + 1
    if neighbors_count >= 4:
        neighbors_four = True
    elif neighbors_count == 0:
        neighbors_empty = True
    return neighbors_four, neighbors_empty


def neighbors_full_part2(seating_matrix: np.ndarray, x: int, y: int) -> (bool, bool):
    rows = seating_matrix.shape[0]
    columns = seating_matrix.shape[1]
    neighbors_empty = False
    neighbors_five = False
    neighbors_count = 0

    # Check left
    for n in range(y - 1, -1, -1):
        # Check if it's occupied, if yes break
        if seating_matrix[x, n] == 1:
            neighbors_count = neighbors_count + 1
            break
        # Check if it's an empty seat, if yes break
        elif seating_matrix[x, n] == 0:
            break

    # Check right
    for n in range(y + 1, columns, 1):
        # Check if it's occupied, if yes break
        if seating_matrix[x, n] == 1:
            neighbors_count = neighbors_count + 1
            break
        # Check if it's an empty seat, if yes break
        elif seating_matrix[x, n] == 0:
            break

    # Check up
    for m in range(x - 1, -1, -1):
        # Check if it's occupied, if yes break
        if seating_matrix[m, y] == 1:
            neighbors_count = neighbors_count + 1
            break
        # Check if it's an empty seat, if yes break
        elif seating_matrix[m, y] == 0:
            break

    # Check down
    for m in range(x + 1, rows, 1):
        # Check if it's occupied, if yes break
        if seating_matrix[m, y] == 1:
            neighbors_count = neighbors_count + 1
            break
        # Check if it's an empty seat, if yes break
        elif seating_matrix[m, y] == 0:
            break

    # Check top-left
    m = x - 1
    n = y - 1
    while m >= 0 and n >= 0:
        # Check if it's occupied, if yes break
        if seating_matrix[m, n] == 1:
            neighbors_count = neighbors_count + 1
            break
        # Check if it's an empty seat, if yes break
        elif seating_matrix[m, n] == 0:
            break
        m = m - 1
        n = n - 1

    # Check top-right
    m = x - 1
    n = y + 1
    while m >= 0 and n < columns:
        # Check if it's occupied, if yes break
        if seating_matrix[m, n] == 1:
            neighbors_count = neighbors_count + 1
            break
        # Check if it's an empty seat, if yes break
        elif seating_matrix[m, n] == 0:
            break
        m = m - 1
        n = n + 1

    # Check bottom-left
    m = x + 1
    n = y - 1
    while m < rows and n >= 0:
        # Check if it's occupied, if yes break
        if seating_matrix[m, n] == 1:
            neighbors_count = neighbors_count + 1
            break
        # Check if it's an empty seat, if yes break
        elif seating_matrix[m, n] == 0:
            break
        m = m + 1
        n = n - 1

    # Check bottom_right
    m = x + 1
    n = y + 1
    while m < rows and n < columns:
        # Check if it's occupied, if yes break
        if seating_matrix[m, n] == 1:
            neighbors_count = neighbors_count + 1
            break
        # Check if it's an empty seat, if yes break
        elif seating_matrix[m, n] == 0:
            break
        m = m + 1
        n = n + 1

    if neighbors_count >= 5:
        neighbors_five = True
    elif neighbors_count == 0:
        neighbors_empty = True
    return neighbors_five, neighbors_empty


def part_one(seating_list: list, iterations: int) -> int:
    seating_matrix = convert_to_matrix(seating_list)
    seating_matrix_old = np.copy(seating_matrix)
    rows = seating_matrix.shape[0]
    columns = seating_matrix.shape[1]
    iter_count = 0
    while iter_count < iterations:
        # print(iter_count)
        iter_count = iter_count + 1
        for i in range(rows):
            for j in range(columns):
                if seating_matrix[i, j] == -1:
                    continue
                elif seating_matrix[i, j] == 1:
                    if neighbors_full(seating_matrix_old, i, j)[0]:
                        seating_matrix[i, j] = 0
                elif seating_matrix[i, j] == 0:
                    if neighbors_full(seating_matrix_old, i, j)[1]:
                        seating_matrix[i, j] = 1
        comparison = seating_matrix == seating_matrix_old
        # print(comparison.all())
        if comparison.all():
            unique, counts = np.unique(seating_matrix, return_counts=True)
            occurrence_dict = dict(zip(unique, counts))
            count_ones = occurrence_dict[1]
            return count_ones
        seating_matrix_old = np.copy(seating_matrix)
    print("Solution not converged, please increase iterations.")


def part_two(seating_list: list, iterations: int) -> int:
    seating_matrix = convert_to_matrix(seating_list)
    seating_matrix_old = np.copy(seating_matrix)
    rows = seating_matrix.shape[0]
    columns = seating_matrix.shape[1]
    iter_count = 0
    while iter_count < iterations:
        # print(iter_count)
        iter_count = iter_count + 1
        for i in range(rows):
            for j in range(columns):
                if seating_matrix[i, j] == -1:
                    continue
                elif seating_matrix[i, j] == 1:
                    if neighbors_full_part2(seating_matrix_old, i, j)[0]:
                        seating_matrix[i, j] = 0
                elif seating_matrix[i, j] == 0:
                    if neighbors_full_part2(seating_matrix_old, i, j)[1]:
                        seating_matrix[i, j] = 1
        comparison = seating_matrix == seating_matrix_old
        # print(comparison.all())
        if comparison.all():
            unique, counts = np.unique(seating_matrix, return_counts=True)
            occurrence_dict = dict(zip(unique, counts))
            count_ones = occurrence_dict[1]
            return count_ones
        seating_matrix_old = np.copy(seating_matrix)
    print("Solution not converged, please increase iterations.")


def main():
    seating_map = get_input()
    # seating_map = ["L.LL.LL.LL", "LLLLLLL.LL", "L.L.L..L..", "LLLL.LL.LL", "L.LL.LL.LL", "L.LLLLL.LL", "..L.L.....",
    #                "LLLLLLLLLL", "L.LLLLLL.L", "L.LLLLL.LL"]
    print("Occupied seats part 1:", part_one(seating_map, 100))
    print("Occupied seats part 2:", part_two(seating_map, 100))


if __name__ == '__main__':
    main()
