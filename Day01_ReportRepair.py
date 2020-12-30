def get_input() -> list:
    with open('Input/Day01_ReportRepair.txt', 'r') as file:
        file_list = file.read().splitlines()
    return list(map(int, file_list))


def part_one(data: list) -> int:
    for i in range(len(data)):
        for j in range(len(data)):
            summation = data[i] + data[j]
            if summation == 2020:
                return data[i] * data[j]


def part_two(data: list) -> int:
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                summation = data[i] + data[j] + data[k]
                if summation == 2020:
                    return data[i] * data[j] * data[k]


def main():
    print("Multiplying two entries gives:", part_one(get_input()))
    print("Multiplying three entries gives:", part_two(get_input()))


if __name__ == '__main__':
    main()
