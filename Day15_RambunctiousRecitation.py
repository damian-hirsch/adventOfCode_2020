import numpy as np


def get_input() -> np.ndarray:
    with open('Input/Day15_RambunctiousRecitation.txt', 'r') as file:
        file_list = np.array(file.read().replace(',', '\n').splitlines(), dtype=int)
    return file_list


def part_one(starting_numbers: np.ndarray, spoken_number: int) -> int:
    start = len(starting_numbers)-1
    counter = list(range(start))
    d = dict(zip(starting_numbers[:start], counter))

    last_number = int(starting_numbers[-1:])
    for i in range(start, spoken_number-1):
        # if i % 1000000 == 0:
        #     print(i)
        if last_number in d:
            new_number = i - d[last_number]
            d[last_number] = i
            last_number = new_number
        else:
            d[last_number] = i
            last_number = 0
    return int(last_number)


def main():
    print('The 2020th number spoken is:', part_one(get_input(), 2020))
    print('The 30000000th number spoken is:', part_one(get_input(), 30000000))


if __name__ == '__main__':
    main()
