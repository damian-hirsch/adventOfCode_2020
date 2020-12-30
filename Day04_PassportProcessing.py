import re


def get_input() -> list:
    with open('Input/Day04_PassportProcessing.txt', 'r') as file:
        data = file.read().replace("\n", ",").replace(",,", "\n").replace(",", " ")
        data = data.split("\n")
    return data


def part_one(data: list) -> int:
    column_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    valid = 0
    for line in data:
        # cid doesn't need to be checked
        for j in range(len(column_names) - 1):
            pos = line.find(column_names[j])
            if pos == -1:
                break
            # cid doesn't need to be checked
            elif j == len(column_names) - 2:
                valid = valid + 1
    return valid


def part_two(data: list) -> int:
    column_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    valid = 0
    for line in data:
        string_array = line.split(" ")
        count = 0
        for j in range(len(string_array)):
            check = string_array[j]
            if check[0:3] == column_names[0]:
                byr = int(check[4:])
                if 1920 <= byr <= 2020:
                    count = count + 1
                else:
                    break
            elif check[0:3] == column_names[1]:
                iyr = int(check[4:])
                if 2010 <= iyr <= 2020:
                    count = count + 1
                else:
                    break
            elif check[0:3] == column_names[2]:
                eyr = int(check[4:])
                if 2020 <= eyr <= 2030:
                    count = count + 1
                else:
                    break
            elif check[0:3] == column_names[3]:
                measurement = check[-2:]
                if measurement == "cm":
                    hgt = int(check[4:-2])
                    if 150 <= hgt <= 193:
                        count = count + 1
                    else:
                        break
                elif measurement == "in":
                    hgt = int(check[4:-2])
                    if 59 <= hgt <= 76:
                        count = count + 1
                    else:
                        break
                else:
                    break
            elif check[0:3] == column_names[4]:
                hcl = check[4:]
                matcher = re.match("^[#][a-f0-9]{6}$", hcl)
                if bool(matcher):
                    count = count + 1
                else:
                    break
            elif check[0:3] == column_names[5]:
                ecl = check[4:]
                matcher = re.match("(amb|blu|brn|gry|grn|hzl|oth)", ecl)
                if bool(matcher):
                    count = count + 1
                else:
                    break
            elif check[0:3] == column_names[6]:
                pid = check[4:]
                matcher = re.match("^[0-9]{9}$", pid)
                if bool(matcher):
                    count = count + 1
                else:
                    break
        if count == 7:
            valid = valid + 1
    return valid


def main():
    print('Valid passports for part 1:', part_one(get_input()))
    print('Valid passports for part 2:', part_two(get_input()))


if __name__ == '__main__':
    main()
