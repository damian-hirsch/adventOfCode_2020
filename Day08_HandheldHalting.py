def get_input() -> list:
    with open(r'Input/Day08_HandheldHalting.txt', 'r') as file:
        file_list = file.read().splitlines()
    return file_list


def get_command(command_string: str) -> str:
    command = command_string[:3]
    return command


def get_operator(command_string: str) -> str:
    operator = command_string[4]
    return operator


def get_count(command_string: str) -> int:
    count = int(command_string[5:])
    return count


def part_one(command_list: list) -> list:
    # Initialization
    accumulator = 0
    used_commands = [False] * len(command_list)
    exec_line = 0
    reached_end = False
    # Check if the command at the current line is still unused
    while not used_commands[exec_line]:
        # Set the current command to used
        used_commands[exec_line] = True
        # Split command
        command = get_command(command_list[exec_line])
        operator = get_operator(command_list[exec_line])
        count = get_count(command_list[exec_line])
        # Command operation
        if command == "acc":
            if operator == "+":
                accumulator = accumulator + count
            else:
                accumulator = accumulator - count
            exec_line = exec_line + 1
        elif command == "nop":
            exec_line = exec_line + 1
        elif command == "jmp":
            if operator == "+":
                exec_line = exec_line + count
            else:
                exec_line = exec_line - count
        # Check if we reached the end and break if yes
        if exec_line == len(command_list):
            reached_end = True
            break
    # Return current accumulator and end was reached
    return [accumulator, reached_end]


def part_two(command_list: list) -> int:
    accumulator = int
    # Cycle through all commands from top, and replace 1 by 1 with new command
    for exec_line in range(len(command_list)):
        # Copy command line
        command_line = command_list[exec_line]
        # Copy the list, cannot use = !!!. It would only reference to the same list
        temp_list = command_list.copy()
        # Exchange commands
        if command_line[:3] == "jmp":
            command_line = "nop" + command_line[3:]
            temp_list[exec_line] = command_line
        elif command_line[:3] == "nop":
            command_line = "jmp" + command_line[3:]
            temp_list[exec_line] = command_line
        elif command_line[:3] == "acc":
            continue
        # Check if we reach end with accumulator value
        [accumulator, reached_end] = part_one(temp_list)
        # If we reached the end, we are done
        if reached_end is True:
            break
    return accumulator


def main():
    command_list = get_input()
    print("Accumulator value part 1:", part_one(command_list)[0])
    print("Accumulator value part 1:", part_two(command_list))


if __name__ == '__main__':
    main()
