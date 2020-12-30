def get_input() -> list:
    with open('Input/Day12_RainRisk.txt', 'r') as file:
        file_list = file.read().splitlines()
    return file_list


def calc_deg(degree: int) -> int:
    # Degree needs to be < abs(720)
    if abs(degree) <= 720:
        degree = (degree + 360) % 360
        return degree
    else:
        print("Error")
        return -1


def part_one(commands: list) -> int:
    x = 0
    y = 0
    pos = 90
    for command in commands:
        direction = command[0]
        number = int(command[1:])
        if direction == "N":
            y = y + number
        elif direction == "S":
            y = y - number
        elif direction == "E":
            x = x + number
        elif direction == "W":
            x = x - number
        elif direction == "L":
            pos = (pos - number)
            pos = calc_deg(pos)
        elif direction == "R":
            pos = (pos + number)
            pos = calc_deg(pos)
        elif direction == "F":
            if pos == 0:
                y = y + number
            elif pos == 90:
                x = x + number
            elif pos == 180:
                y = y - number
            elif pos == 270:
                x = x - number
            else:
                print("Error")
                exit()
        else:
            print("Error")
            exit()
    return abs(x) + abs(y)


def part_two(commands: list) -> int:
    x = 0
    y = 0
    x_waypoint = 10
    y_waypoint = 1
    for command in commands:
        direction = command[0]
        number = int(command[1:])
        if direction == "N":
            y_waypoint = y_waypoint + number
        elif direction == "S":
            y_waypoint = y_waypoint - number
        elif direction == "E":
            x_waypoint = x_waypoint + number
        elif direction == "W":
            x_waypoint = x_waypoint - number
        elif direction == "L":
            if number == 90:
                x_old = x_waypoint
                x_waypoint = - y_waypoint
                y_waypoint = x_old
            elif number == 180:
                x_waypoint = - x_waypoint
                y_waypoint = - y_waypoint
            elif number == 270:
                x_old = x_waypoint
                x_waypoint = y_waypoint
                y_waypoint = - x_old
            else:
                print("Error: Degree higher than 270!")
        elif direction == "R":
            if number == 90:
                x_old = x_waypoint
                x_waypoint = y_waypoint
                y_waypoint = - x_old
            elif number == 180:
                x_waypoint = - x_waypoint
                y_waypoint = - y_waypoint
            elif number == 270:
                x_old = x_waypoint
                x_waypoint = - y_waypoint
                y_waypoint = x_old
            else:
                print("Error: Degree higher than 270!")
        elif direction == "F":
            x = x + number * x_waypoint
            y = y + number * y_waypoint
        else:
            print("Error")
            exit()
        # print(x)
        # print(y)
        # print(x_waypoint)
        # print(y_waypoint)
        # print("----")
    return abs(x) + abs(y)


def main():
    # coordinates = ["F10", "N3", "F7", "R90", "F11"]
    coordinates = get_input()
    print("The Manhattan distance for Part 1 is:", part_one(coordinates))
    print("The Manhattan distance for Part 2 is:", part_two(coordinates))


if __name__ == '__main__':
    main()
