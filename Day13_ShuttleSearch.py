import numpy as np


def get_input_part_one() -> list:
    with open('Input/Day13_ShuttleSearch.txt', 'r') as file:
        file_list = file.read().replace("x,", "").replace("\n", ",").split(",")
    # Convert strings to int
    return list(map(int, file_list))


def get_input_part_two() -> list:
    with open('Input/Day13_ShuttleSearch.txt', 'r') as file:
        file_list = file.read().replace("x", "1").replace("\n", ",").split(",")
    # First value is not used
    file_list = file_list[1:]
    # Convert strings to int
    return list(map(int, file_list))


# This function gets the least common multiplier with an offset
def get_lcm(number1: int, number2: int, offset: int, step: int, max_iter: int) -> int:
    counter = 0
    # Make sure we quit if we cannot find a solution
    while counter < max_iter:
        number = number1 + counter * step
        # print(counter, ":", number)
        if (number + offset) % number2 == 0:
            return number
        counter = counter + 1
    print("Error: Couldn't find a solution!")
    return -1


def part_one(timetable: list) -> int:
    time = timetable[0]
    buses = timetable[1:]
    is_zero = False
    waiting_time = 0
    while not is_zero:
        for bus in buses:
            if (time + waiting_time) % bus == 0:
                return bus * waiting_time
        waiting_time = waiting_time + 1


def part_two(timetable: list, max_iter: int) -> int:
    num1 = timetable[0]
    # The step can get very large, np uses int32 by default, make sure it is initialized as int64
    step = np.int64(num1)
    counter = 0
    for num2 in timetable:
        # Find the LCM with offset for the previous aggregated number and the new one
        num1 = get_lcm(num1, num2, counter, step, max_iter)
        # Calculate the step for the next LCM calculation (major speed-up)
        step = np.lcm(step, num2)
        counter = counter + 1
    return num1


def main():
    print("ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait:",
          part_one(get_input_part_one()))
    print("Earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the "
          "list:", part_two(get_input_part_two(), 10000))


if __name__ == '__main__':
    main()
