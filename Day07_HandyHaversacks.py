def get_input() -> list:
    with open('Input/Day07_HandyHaversacks.txt', 'r') as file:
        file_list = file.read().splitlines()
    return file_list


def get_bag_dict(bag_list: list) -> dict:
    bag_dict = {}
    for bag in bag_list:
        sep = bag.find(' bags contain')
        dict_key = bag[:sep]
        content = bag[sep+14:]
        bag_instance = []
        if content[-14:] != 'no other bags.':
            content_list = content.split(' ')
            for i in range(0, len(content_list), 4):
                number = int(content_list[i])
                bag_type = f'{content_list[i+1]} {content_list[i+2]}'
                bag_instance.append([number, bag_type])
        bag_dict[dict_key] = bag_instance
    return bag_dict


def part_one(bag_list: list, looking_for: str) -> list:
    found_bags = []
    for bag in bag_list:
        sep = bag.find(' bags contain')
        if looking_for in bag[sep:]:
            found_bags.append(bag[:sep])
            found_bags.extend(part_one(bag_list, bag[:sep]))
    return found_bags


def part_two(bag_dict: dict, looking_for: str) -> int:
    bag_count = 1
    for bag in bag_dict[looking_for]:
        bag_count = bag_count + bag[0] * part_two(bag_dict, bag[1])
    return bag_count


def main():
    # Set is used to find the distinct elements
    print(f'Bag colors that contain at least one shiny gold bag: {len(set(part_one(get_input(), "shiny gold")))}')
    print(f'Shiny gold bags contain this number of other bags: {part_two(get_bag_dict(get_input()), "shiny gold") - 1}')


if __name__ == '__main__':
    main()
