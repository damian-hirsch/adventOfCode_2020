import re


def get_input() -> list:
    with open('Input/Day02_PasswordPhilosophy.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def part_one(data: list) -> int:
    valid = 0
    for line in data:
        for letter_min, letter_max, letter, pw_string in re.findall(r'(\d+)-(\d+)\s([a-z]):\s(\w+)', line):
            letter_count = pw_string.count(letter)
            if int(letter_min) <= letter_count <= int(letter_max):
                valid = valid + 1
    return valid


def part_two(data: list) -> int:
    valid = 0
    for line in data:
        for letter_first, letter_second, letter, pw_string in re.findall(r'(\d+)-(\d+)\s([a-z]):\s(\w+)', line):
            if (pw_string[int(letter_first) - 1] == letter or pw_string[int(letter_second) - 1] == letter) \
                    and pw_string[int(letter_first) - 1] != pw_string[int(letter_second) - 1]:
                valid = valid + 1
    return valid


def main():
    print('Number of passwords that are valid for part 1:', part_one(get_input()))
    print('Number of passwords that are valid for part 2:', part_two(get_input()))


if __name__ == '__main__':
    main()
