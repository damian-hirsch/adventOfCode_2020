import re


def get_input():
    with open('Input/Day18_OperationOrder.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def eval_str(string: str) -> int:
    res = 0
    not_done = True
    while not_done:
        re_num = re.search(r'(\d+)[\s](\D+)[\s](\d+)', string)
        num1 = re_num.group(1)
        operator = re_num.group(2)
        num2 = re_num.group(3)
        pos = re_num.end(3)
        if pos == len(string):
            not_done = False
        if operator == '+':
            res = int(num1) + int(num2)
        elif operator == '*':
            res = int(num1) * int(num2)
        # only replace first occurrence!
        string = string.replace(string[:pos], str(res), 1)
    return res


def eval_str2(string: str) -> int:
    res = 0
    not_done = True
    while not_done:
        re_num = re.search(r'(\d+)[\s](\+)[\s](\d+)', string)
        if re_num is None:
            re_num = re.search(r'(\d+)[\s](\*)[\s](\d+)', string)
        num1 = re_num.group(1)
        operator = re_num.group(2)
        num2 = re_num.group(3)
        start = re_num.start(1)
        end = re_num.end(3)
        if operator == '+':
            res = int(num1) + int(num2)
        elif operator == '*':
            res = int(num1) * int(num2)
        # only replace first occurrence!
        string = string.replace(string[start:end], str(res), 1)
        if len(string) == len(str(res)):
            not_done = False
    return res


def parenthesis(string: str) -> int:
    check = string.find('(')
    while check != -1:
        in_parenthesis = re.search(r'(\(([^()]+)\))', string)
        substring = in_parenthesis.group(0)[1:-1]
        start = in_parenthesis.start(0)
        end = in_parenthesis.end(0)
        str_result = str(eval_str(substring))
        string = string.replace(string[start:end], str_result)
        check = string.find('(')
    result = eval_str(string)
    return result


def parenthesis2(string: str) -> int:
    check = string.find('(')
    while check != -1:
        in_parenthesis = re.search(r'(\(([^()]+)\))', string)
        substring = in_parenthesis.group(0)[1:-1]
        start = in_parenthesis.start(0)
        end = in_parenthesis.end(0)
        str_result = str(eval_str2(substring))
        string = string.replace(string[start:end], str_result)
        check = string.find('(')
    result = eval_str2(string)
    return result


def part_one(operations: list) -> list:
    results = [0] * len(operations)
    for idx, operation in enumerate(operations):
        results[idx] = parenthesis(operation)
    return results


def part_two(operations: list) -> list:
    results = [0] * len(operations)
    for idx, operation in enumerate(operations):
        results[idx] = parenthesis2(operation)
    return results


def main():
    print('The homework result for part 1 is:', sum(part_one(get_input())))
    print('The homework result for part 2 is:', sum(part_two(get_input())))


if __name__ == '__main__':
    main()
