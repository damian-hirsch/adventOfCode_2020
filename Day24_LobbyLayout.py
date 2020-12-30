import numpy as np


def get_input() -> list:
    with open('Input/Day24_LobbyLayout.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def tile_finder(tile: str) -> (int, int):
    x = 0
    y = 0
    while len(tile) > 0:
        char1 = tile[0]
        if char1 == 's':
            char2 = tile[1]
            if char2 == 'e':
                x = x + 1
                y = y - 1
                tile = tile[2:]
            elif char2 == 'w':
                x = x - 1
                y = y - 1
                tile = tile[2:]
        elif char1 == 'n':
            char2 = tile[1]
            if char2 == 'e':
                x = x + 1
                y = y + 1
                tile = tile[2:]
            elif char2 == 'w':
                x = x - 1
                y = y + 1
                tile = tile[2:]
        elif char1 == 'e':
            x = x + 2
            tile = tile[1:]
        elif char1 == 'w':
            x = x - 2
            tile = tile[1:]
        else:
            print('Error: tile_finder')
    return x, y


def neighbor_counter(floor: np.ndarray, x: int, y: int) -> int:
    rows = floor.shape[0]
    columns = floor.shape[1]
    neighbors = 0

    # E tile
    if 0 <= x + 2 < rows and floor[x + 2, y] == 1:
        neighbors = neighbors + 1
    # NE tile
    if 0 <= x + 1 < rows and 0 <= y + 1 < columns and floor[x + 1, y + 1] == 1:
        neighbors = neighbors + 1
    # NW tile
    if 0 <= x - 1 < rows and 0 <= y + 1 < columns and floor[x - 1, y + 1] == 1:
        neighbors = neighbors + 1
    # W tile
    if 0 <= x - 2 < rows and floor[x - 2, y] == 1:
        neighbors = neighbors + 1
    # SW tile
    if 0 <= x - 1 < rows and 0 <= y - 1 < columns and floor[x - 1, y - 1] == 1:
        neighbors = neighbors + 1
    # SE tile
    if 0 <= x + 1 < rows and 0 <= y - 1 < columns and floor[x + 1, y - 1] == 1:
        neighbors = neighbors + 1

    return neighbors


def part_one(data: list) -> (int, np.ndarray):
    floor = np.zeros((81, 81))
    center_x = 40
    center_y = 40
    for data_line in data:
        x, y = tile_finder(data_line)
        if floor[center_x + x, center_y + y] == 1:
            floor[center_x + x, center_y + y] = 0
        else:
            floor[center_x + x, center_y + y] = 1
    return int(np.sum(floor)), floor


def part_two(floor: np.ndarray) -> int:
    floor_old = np.copy(floor)
    for k in range(100):
        for i in range(0, floor.shape[0] - 1, 1):
            for j in range(0, floor.shape[1] - 1, 2):
                if i % 2 == 1:
                    j = j + 1
                neighbors = neighbor_counter(floor_old, i, j)
                if (neighbors == 0 or neighbors > 2) and floor_old[i, j] == 1:
                    floor[i, j] = 0
                elif neighbors == 2 and floor_old[i, j] == 0:
                    floor[i, j] = 1
        floor = np.pad(floor, pad_width=1, mode='constant', constant_values=0)
        floor_old = np.copy(floor)
        # print(k, ':', int(np.sum(floor)))
    return int(np.sum(floor))


def main():
    part1, floor = part_one(get_input())
    print('Tiles that are left with the black side up:', part1)
    print('Tiles thar are black after 100 days:', part_two(floor))


if __name__ == '__main__':
    main()
