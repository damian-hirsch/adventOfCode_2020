import numpy as np


def get_input() -> np.ndarray:
    data = np.loadtxt('Input/Day10_AdapterArray.txt')
    # data = np.array([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7,
    #                  9, 4, 2, 34, 10, 3])
    return data


def build_series(n: int) -> np.ndarray:
    func = np.array([1, 1, 2])
    for i in range(3, n):
        func = np.append(func, func[i-3]+func[i-2]+func[i-1])
    return func


def part_one(array: np.ndarray) -> int:
    array = np.insert(array, 0, 0)
    array = np.sort(array)

    diff = np.zeros(len(array)-1)
    for i in range(len(array)-1):
        diff[i] = array[i+1] - array[i]
    diff = np.append(diff, 3)
    unique, counts = np.unique(diff, return_counts=True)
    occurrence_dict = dict(zip(unique, counts))
    count_ones = occurrence_dict[1]
    count_threes = occurrence_dict[3]
    return count_ones * count_threes


def part_two(array: np.ndarray) -> int:
    # Repeat part 1
    array = np.insert(array, 0, 0)
    array = np.sort(array)

    diff = np.zeros(len(array) - 1)
    for i in range(len(array) - 1):
        diff[i] = array[i + 1] - array[i]
    diff = np.append(diff, 3)

    # Start of part 2
    distinct_ways = 1
    factor_array = np.ones(len(diff))
    # If 10 is not enough it throws an index error, then increase it
    series = build_series(10)
    counter = 0
    for i in range(len(diff)):
        if diff[i] == 1:
            counter = counter + 1
        elif diff[i] == 3:
            factor_array[i-1] = series[counter]
            counter = 0
        else:
            print("Error")
            return -1
    for x in factor_array:
        distinct_ways = distinct_ways * x
    return int(distinct_ways)


def main():
    array = get_input()
    print("The number of 1-jolt differences multiplied by the number of 3-jolt differences is:", part_one(array))
    print("The total number of distinct ways you can arrange the adapters to connect the charging outlet to your "
          "device is:", part_two(array))


if __name__ == '__main__':
    main()
