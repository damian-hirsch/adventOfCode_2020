import numpy as np
import re
import math


def get_input() -> list:
    with open('Input/Day20_JurassicJigsaw.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def convert_data(data: list) -> (list, np.ndarray):
    tile_numbers = [0] * int(len(data)/12 + 1)
    tile_matrix = np.ones((int(len(data)/12) + 1, 10, 10)) * -1
    string_dict = {
        '.': 0,
        '#': 1
    }
    for i, data_line in enumerate(data):
        if i % 12 == 0:
            tile_numbers[int(i/12)] = int(re.search(r'(\d+)', data[i]).group(0))
        elif 1 <= i % 12 <= 10:
            for j, data_point in enumerate(data_line):
                tile_matrix[math.floor(i/12), (i % 12) - 1, j] = string_dict[data_point]
            # Write tile number in the middle, does not matter for alignment
            # tile_matrix[math.floor(i/12), 4, 4] = tile_numbers[math.floor(int(i/12))]
    return tile_numbers, tile_matrix


def find_tile(tile_solution: np.ndarray, tile_matrix: np.ndarray, direction: str) -> (np.ndarray, int):
    for i in range(tile_matrix.shape[0]):
        test_tile = tile_matrix[i, :, :]
        if direction == 'right':
            # Right side to right side
            if np.array_equal(tile_solution[:, -1], test_tile[:, -1]):
                return np.fliplr(test_tile), i
            # Right side to right side flipped
            elif np.array_equal(tile_solution[:, -1], np.flipud(test_tile[:, -1])):
                return np.flipud(np.fliplr(test_tile)), i
            # Right side to left side
            elif np.array_equal(tile_solution[:, -1], test_tile[:, 0]):
                return test_tile, i
            # Right side to left side flipped
            elif np.array_equal(tile_solution[:, -1], np.flipud(test_tile[:, 0])):
                return np.flipud(test_tile), i
            # Right side to top side
            elif np.array_equal(tile_solution[:, -1], np.rot90(test_tile, -1)[:, -1]):
                return np.fliplr(np.rot90(test_tile, -1)), i
            # Right side to top side flipped
            elif np.array_equal(tile_solution[:, -1], np.flipud(np.rot90(test_tile, -1)[:, -1])):
                return np.flipud(np.fliplr(np.rot90(test_tile, -1))), i
            # Right side to bottom side
            elif np.array_equal(tile_solution[:, -1], np.rot90(test_tile, -1)[:, 0]):
                return np.rot90(test_tile, -1), i
            # Right side to bottom side flipped
            elif np.array_equal(tile_solution[:, -1], np.flipud(np.rot90(test_tile, -1)[:, 0])):
                return np.flipud(np.rot90(test_tile, -1)), i

        elif direction == 'top':
            # Top side to right side
            if np.array_equal(np.rot90(tile_solution, -1)[:, -1], test_tile[:, -1]):
                return np.flipud(np.rot90(test_tile, 1)), i
            # Top side to right side flipped
            elif np.array_equal(np.rot90(tile_solution, -1)[:, -1], np.flipud(test_tile[:, -1])):
                return np.rot90(test_tile, -1), i
            # Top side to left side
            elif np.array_equal(np.rot90(tile_solution, -1)[:, -1], test_tile[:, 0]):
                return np.rot90(test_tile, 1), i
            # Top side to left side flipped
            elif np.array_equal(np.rot90(tile_solution, -1)[:, -1], np.flipud(test_tile[:, 0])):
                return np.fliplr(np.rot90(test_tile, 1)), i
            # Top side to top side
            elif np.array_equal(np.rot90(tile_solution, -1)[:, -1], np.rot90(test_tile, -1)[:, -1]):
                return np.flipud(test_tile), i
            # Top side to top side flipped
            elif np.array_equal(np.rot90(tile_solution, -1)[:, -1], np.flipud(np.rot90(test_tile, -1)[:, -1])):
                return np.flipud(np.fliplr(test_tile)), i
            # Top side to bottom side
            elif np.array_equal(np.rot90(tile_solution, -1)[:, -1], np.rot90(test_tile, -1)[:, 0]):
                return test_tile, i
            # Top side to bottom side flipped
            elif np.array_equal(np.rot90(tile_solution, -1)[:, -1], np.flipud(np.rot90(test_tile, -1)[:, 0])):
                return np.fliplr(test_tile), i

        elif direction == 'left':
            # Left side to right side
            if np.array_equal(tile_solution[:, 0], test_tile[:, -1]):
                return test_tile, i
            # Left side to right side flipped
            elif np.array_equal(tile_solution[:, 0], np.flipud(test_tile[:, -1])):
                return np.flipud(test_tile), i
            # Left side to left side
            elif np.array_equal(tile_solution[:, 0], test_tile[:, 0]):
                return np.fliplr(test_tile), i
            # Left side to left side flipped
            elif np.array_equal(tile_solution[:, 0], np.flipud(test_tile[:, 0])):
                return np.flipud(np.fliplr(test_tile)), i
            # Left side to top side
            elif np.array_equal(tile_solution[:, 0], np.rot90(test_tile, -1)[:, -1]):
                return np.rot90(test_tile, -1), i
            # Left side to top side flipped
            elif np.array_equal(tile_solution[:, 0], np.flipud(np.rot90(test_tile, -1)[:, -1])):
                return np.flipud(np.rot90(test_tile, -1)), i
            # Left side to bottom side
            elif np.array_equal(tile_solution[:, 0], np.rot90(test_tile, -1)[:, 0]):
                return np.fliplr(np.rot90(test_tile, -1)), i
            # Left side to bottom side flipped
            elif np.array_equal(tile_solution[:, 0], np.flipud(np.rot90(test_tile, -1)[:, 0])):
                return np.rot90(test_tile, 1), i

        elif direction == 'bottom':
            # Bottom side to right side
            if np.array_equal(np.rot90(tile_solution, -1)[:, 0], test_tile[:, -1]):
                return np.rot90(test_tile, 1), i
            # Bottom side to right side flipped
            elif np.array_equal(np.rot90(tile_solution, -1)[:, 0], np.flipud(test_tile[:, -1])):
                return np.fliplr(np.rot90(test_tile, 1)), i
            # Bottom side to left side
            elif np.array_equal(np.rot90(tile_solution, -1)[:, 0], test_tile[:, 0]):
                return np.fliplr(np.rot90(test_tile, -1)), i
            # Bottom side to left side flipped
            elif np.array_equal(np.rot90(tile_solution, -1)[:, 0], np.flipud(test_tile[:, 0])):
                return np.rot90(test_tile, -1), i
            # Bottom side to top side
            elif np.array_equal(np.rot90(tile_solution, -1)[:, 0], np.rot90(test_tile, -1)[:, -1]):
                return test_tile, i
            # Bottom side to top side flipped
            elif np.array_equal(np.rot90(tile_solution, -1)[:, 0], np.flipud(np.rot90(test_tile, -1)[:, -1])):
                return np.fliplr(test_tile), i
            # Bottom side to bottom side
            elif np.array_equal(np.rot90(tile_solution, -1)[:, 0], np.rot90(test_tile, -1)[:, 0]):
                return np.flipud(test_tile), i
            # Bottom side to bottom side flipped
            elif np.array_equal(np.rot90(tile_solution, -1)[:, 0], np.flipud(np.rot90(test_tile, -1)[:, 0])):
                return np.fliplr(np.flipud(test_tile)), i
    return np.array([]), -1


def cut_borders(solution_all: np.ndarray) -> np.ndarray:
    num_rows = solution_all.shape[0]
    num_cols = solution_all.shape[1]
    first_rows = list(range(0, num_rows, 10))
    first_cols = list(range(0, num_cols, 10))
    last_rows = list(range(9, num_rows, 10))
    last_cols = list(range(9, num_cols, 10))
    rows = first_rows + last_rows
    cols = first_cols + last_cols
    solution_all = np.delete(solution_all, rows, 0)
    solution_all = np.delete(solution_all, cols, 1)

    return solution_all


def part_one(data: list) -> (int, np.ndarray):
    tile_keys, tile_matrix = convert_data(data)
    num_tiles = tile_matrix.shape[0]
    solution = tile_matrix[0, :, :]
    solution_keys = np.ones((1, 1)) * tile_keys[0]
    current_tile = tile_matrix[0, :, :]
    core_tile = tile_matrix[0, :, :]
    tile_matrix = np.delete(tile_matrix, 0, axis=0)
    del tile_keys[0]

    # Check right
    while current_tile.size != 0:
        current_tile, idx = find_tile(current_tile, tile_matrix, 'right')
        if current_tile.size != 0:
            solution = np.concatenate((solution, current_tile), axis=1)
            solution_keys = np.concatenate((solution_keys, np.ones((1, 1)) * tile_keys[idx]), axis=1)
            tile_matrix = np.delete(tile_matrix, idx, axis=0)
            del tile_keys[idx]

    # Check left
    current_tile = core_tile
    while current_tile.size != 0:
        current_tile, idx = find_tile(current_tile, tile_matrix, 'left')
        if current_tile.size != 0:
            solution = np.concatenate((current_tile, solution), axis=1)
            solution_keys = np.concatenate((np.ones((1, 1)) * tile_keys[idx], solution_keys), axis=1)
            tile_matrix = np.delete(tile_matrix, idx, axis=0)
            del tile_keys[idx]
            core_tile = current_tile

    solution_all = solution
    solution_keys_all = solution_keys
    primary_tile = core_tile

    # --------------------------------------

    while tile_matrix.shape[0] > 0:
        core_tile, idx = find_tile(core_tile, tile_matrix, 'top')
        if core_tile.size == 0:
            break
        solution = core_tile
        solution_keys = np.ones((1, 1)) * tile_keys[idx]
        tile_matrix = np.delete(tile_matrix, idx, axis=0)
        del tile_keys[idx]
        current_tile = core_tile
        for i in range(int(math.sqrt(num_tiles)) - 1):
            current_tile, idx = find_tile(current_tile, tile_matrix, 'right')
            solution = np.concatenate((solution, current_tile), axis=1)
            solution_keys = np.concatenate((solution_keys, np.ones((1, 1)) * tile_keys[idx]), axis=1)
            tile_matrix = np.delete(tile_matrix, idx, axis=0)
            del tile_keys[idx]
        solution_all = np.concatenate((solution, solution_all), axis=0)
        solution_keys_all = np.concatenate((solution_keys, solution_keys_all), axis=0)

    # -------------------------------------

    core_tile = primary_tile

    while tile_matrix.shape[0] > 0:
        core_tile, idx = find_tile(core_tile, tile_matrix, 'bottom')
        if core_tile.size == 0:
            break
        solution = core_tile
        solution_keys = np.ones((1, 1)) * tile_keys[idx]
        tile_matrix = np.delete(tile_matrix, idx, axis=0)
        del tile_keys[idx]
        current_tile = core_tile
        for i in range(int(math.sqrt(num_tiles)) - 1):
            current_tile, idx = find_tile(current_tile, tile_matrix, 'right')
            solution = np.concatenate((solution, current_tile), axis=1)
            solution_keys = np.concatenate((solution_keys, np.ones((1, 1)) * tile_keys[idx]), axis=1)
            tile_matrix = np.delete(tile_matrix, idx, axis=0)
            del tile_keys[idx]
        solution_all = np.concatenate((solution_all, solution), axis=0)
        solution_keys_all = np.concatenate((solution_keys_all, solution_keys), axis=0)

    # -------------------------------------

    # Find corner pieces
    top_left = int(solution_keys_all[0, 0])
    top_right = int(solution_keys_all[0, -1])
    bottom_left = int(solution_keys_all[-1, 0])
    bottom_right = int(solution_keys_all[-1, -1])

    return top_left * top_right * bottom_left * bottom_right, solution_all


def part_two(solution_all: np.ndarray) -> int:
    monster = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    separator = ''
    regex_monster = separator.join(monster).replace(' ', '.')
    count_hashes = regex_monster.count('#')
    monster_width = len(monster)
    monster_len = len(monster[0])
    solution_clean = cut_borders(solution_all)
    solution_rows = solution_clean.shape[0]
    solution_cols = solution_clean.shape[1]
    d = {
        0: '.',
        1: '#'
    }
    monster_count = 0
    while monster_count == 0:
        for i in range(solution_rows - monster_width):
            for j in range(solution_cols - monster_len):
                monster_candidate = solution_clean[i:i+monster_width, j:j+monster_len]
                monster_candidate = monster_candidate.flatten()
                monster_candidate = separator.join([d[char_monster_check] for char_monster_check in monster_candidate])
                matched = bool(re.match(regex_monster, monster_candidate))
                if matched:
                    monster_count = monster_count + 1
        solution_clean = np.rot90(solution_clean, -1)
    return int(np.sum(solution_clean) - monster_count * count_hashes)


def main():
    data = get_input()
    sol1, solution_all = part_one(data)
    sol2 = part_two(solution_all)
    print('If you multiply together the IDs of the four corner tiles you get:', sol1)
    print('# that are not part of sea monsters:', sol2)


if __name__ == '__main__':
    main()
