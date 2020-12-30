import numpy as np
import re


def get_input() -> list:
    with open('Input/Day14_DockingData.txt', 'r') as file:
        file_list = file.read().splitlines()
    return file_list


def apply_mask(bit: str, mask: str) -> int:
    result = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            result = result + bit[i]
        elif mask[i] == "1":
            result = result + mask[i]
        elif mask[i] == "0":
            result = result + mask[i]
        else:
            print("Error with mask!")
            return result
    # Convert result to integer
    return int(result, 2)


def apply_mask_to_memory(bit: str, mask: str) -> str:
    result = ""
    for i in range(len(mask)):
        if mask[i] == "0":
            result = result + bit[i]
        elif mask[i] == "1":
            result = result + "1"
        elif mask[i] == "X":
            result = result + "X"
        else:
            print("Error with mask!")
            return "-1"
    return result


def memory_expand_float(memory_floating: str) -> list:
    count_x = memory_floating.count("X")
    result_array = [-1] * (2 ** count_x)
    for i in range(2 ** count_x):
        result = ""
        bit_string = f'{i:0{count_x}b}'
        counter = 0
        for j in range(len(memory_floating)):
            if memory_floating[j] == "1" or memory_floating[j] == "0":
                result = result + memory_floating[j]
            elif memory_floating[j] == "X":
                result = result + bit_string[counter]
                counter = counter + 1
        result_array[i] = int(result, 2)
    return result_array


def part_one(command_list: list) -> int:
    memory_list = np.zeros(1000000)
    mask = ""
    for command in command_list:
        if command[:2] == "ma":
            # Split and take the second part
            mask = command.split("= ", 1)[1]
        elif command[:2] == "me":
            # Find memory number between the square brackets using regex
            memory = int(re.search('\\[(.*)]', command).group(1))
            # Split and take the second part
            number = int(command.split("= ", 1)[1])
            # 036 pads 36 zeros to the left, b is binary representation
            bit_string = f'{number:036b}'
            memory_list[memory] = apply_mask(bit_string, mask)
        else:
            print("Error in command list")
            return -1
    return int(sum(memory_list))


def part_two(command_list) -> int:
    memory_list = np.zeros((1000000, 2))
    mask = ""
    counter = 0
    for command in command_list:
        print(command)
        if command[:2] == "ma":
            # Split and take the second part
            mask = command.split("= ", 1)[1]
        elif command[:2] == "me":
            # Find memory number between the square brackets using regex
            memory = int(re.search('\\[(.*)]', command).group(1))
            # Split and take the second part
            number = int(command.split("= ", 1)[1])
            # 036 pads 36 zeros to the left, b is binary representation
            bit_memory = f'{memory:036b}'
            # Apply mask to memory
            memory_floating = apply_mask_to_memory(bit_memory, mask)
            # Translate floating points to memory positions
            memory_pos = memory_expand_float(memory_floating)
            for memory_entry in memory_pos:
                # Check if memory position already exists
                if memory_entry in memory_list[:, 0]:
                    # If yes, overwrite it
                    index = np.where(memory_list[:, 0] == memory_entry)
                    memory_list[index, 1] = number

                else:
                    # If no, create new entry
                    memory_list[counter, 0] = memory_entry
                    memory_list[counter, 1] = number
                    counter = counter + 1
        else:
            print("Error in command list")
            return -1
    return int(sum(memory_list[:, 1]))


def main():
    print("Sum of all values left in memory after Part 2 completes is:", part_two(get_input()))
    print("Sum of all values left in memory after Part 1 completes is:", part_one(get_input()))


if __name__ == '__main__':
    main()
