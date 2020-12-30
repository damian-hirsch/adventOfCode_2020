import re
import numpy as np


def get_input():
    with open('Input/Day19_MonsterMessages.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def transform_data(data: list) -> (list, list):
    index = data.index('')
    instructions = data[:index]
    instructions_order = [0] * len(instructions)
    for idx, instruction in enumerate(instructions):
        colon_idx = instruction.find(':')
        instructions_order[idx] = int(instruction[:colon_idx])
        instructions[idx] = instruction[colon_idx + 2:]
        instructions[idx] = instructions[idx].replace('"', '')
    instructions_order = list(np.argsort(instructions_order))
    instructions = np.array(instructions)
    instructions = list(instructions[instructions_order])
    messages = data[index + 1:]

    return instructions, messages


def update_instructions(instructions: list) -> list:
    instructions[8] = '(?:42)+'

    # Note: PCRE patterns are not possible in Python, thus this "hardcoded" way
    options = []
    for n in range(1, 10):
        options.append('(?:(?:{a}){{{n}}}(?:{b}){{{n}}})'.format(a=42, b=31, n=n))
    instructions[11] = '(?:' + '|'.join(options) + ')'
    return instructions


def regex_builder(instructions: list, regex_string: str) -> str:
    # Find all numbers that are not between {}
    matches = list(re.finditer('[0-9]+(?![^{]*})', regex_string))
    # Non-recursive
    # while len(matches) > 0:
    if len(matches) > 0:
        for m in reversed(matches):
            number = int(m.group())
            num_start = int(m.start())
            num_end = int(m.end())
            if instructions[number] == 'a' or instructions[number] == 'b':
                regex_substring = instructions[number]
            else:
                regex_substring = '(?:' + instructions[number] + ')'
                # Comment below line for non-recursive
                regex_substring = regex_builder(instructions, regex_substring)
            regex_string = regex_string[:num_start] + regex_substring + regex_string[num_end:]
        # Non-recursive
        # matches = list(re.finditer('[0-9]+', regex_string))
    return regex_string


def part_one(data: list) -> int:
    instructions, messages = transform_data(data)
    regex_string = '(?:' + instructions[0] + ')'
    regex_string = regex_builder(instructions, regex_string)
    regex_string = regex_string.replace(' ', '')
    regex_string = '^' + regex_string + '$'
    counter = 0
    for message in messages:
        matched = re.match(regex_string, message)
        if bool(matched):
            counter = counter + 1
    return counter


def part_two(data: list) -> int:
    instructions, messages = transform_data(data)
    instructions = update_instructions(instructions)
    regex_string = '(?:' + instructions[0] + ')'
    regex_string = regex_builder(instructions, regex_string)
    regex_string = regex_string.replace(' ', '')
    regex_string = '^' + regex_string + '$'
    counter = 0
    for message in messages:
        matched = re.match(regex_string, message)
        if bool(matched):
            counter = counter + 1
    return counter


def main():
    print('Messages that completely match rule 0 from part 1:', part_one(get_input()))
    print('Messages that completely match rule 0 from part 2:', part_two(get_input()))


if __name__ == '__main__':
    main()
