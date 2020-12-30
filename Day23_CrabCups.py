import numpy as np


def get_input():
    with open('Input/Day23_CrabCups.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def create_successors(order: str) -> list:
    successors = [0] * (len(order) + 1)
    for i in range(len(order)-1):
        successors[int(order[i])] = int(order[i+1])
    successors[int(order[-1])] = int(order[0])
    return successors


def play(main_cup: int, successors: list) -> int:
    cup_1 = successors[main_cup]
    cup_2 = successors[cup_1]
    cup_3 = successors[cup_2]
    next_cup = successors[cup_3]
    destination_cup = main_cup - 1

    found_flag = False
    while not found_flag:
        if destination_cup < 1:
            destination_cup = max(successors)
        if destination_cup not in (cup_1, cup_2, cup_3):
            found_flag = True
        else:
            destination_cup = destination_cup - 1

    successors[main_cup] = next_cup
    successors[cup_3] = successors[destination_cup]
    successors[destination_cup] = cup_1
    return next_cup


def part_one(data: list, rounds: int) -> int:
    successors = create_successors(data[0])
    main_cup = int(data[0][0])
    for i in range(rounds):
        main_cup = play(main_cup, successors)

    cups = []
    cup = successors[1]
    while cup != 1:
        cups.append(str(cup))
        cup = successors[cup]
    solution_string = ''.join(cups)
    return int(solution_string)


def part_two(data: list, rounds: int) -> np.int64:
    successors = create_successors(data[0])
    # Extend successors
    max_entry = max(successors)
    # + 2 needed for the shift between actual and successor
    successors.extend(range(max_entry + 2, 1000000 + 2))
    successors[int(data[0][-1])] = max_entry + 1
    successors[1000000] = int(data[0][0])

    main_cup = int(data[0][0])
    for i in range(rounds):
        main_cup = play(main_cup, successors)

    return np.int64(successors[1] * successors[successors[1]])


def main():
    print('The labels on the cups after cup 1 are:', part_one(get_input(), 100))
    print('Multiplying the labels of the cups clockwise of cup 1 together yields:', part_two(get_input(), 10000000))


if __name__ == '__main__':
    main()
