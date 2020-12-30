import numpy as np
import re


def get_input() -> list:
    with open('Input/Day16_TicketTranslation.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def ticket_definitions(data: list) -> (str, int, int, int, int):
    definition_name = []
    a_1 = []
    b_1 = []
    a_2 = []
    b_2 = []
    for line in data:
        for definition, a1, b1, a2, b2 in re.findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line):
            definition_name.append(definition)
            a_1.append(int(a1))
            b_1.append(int(b1))
            a_2.append(int(a2))
            b_2.append(int(b2))
    return definition_name, a_1, b_1, a_2, b_2


def get_my_ticket(data: list) -> np.ndarray:
    ind = data.index('your ticket:')
    number_list = data[ind + 1].split(',')
    my_ticket_numbers = np.array(number_list, dtype=np.int)
    return my_ticket_numbers


def get_nearby_tickets(data: list) -> np.ndarray:
    rows_start = data.index('nearby tickets:') + 1
    rows_end = len(data)
    rows = rows_end - rows_start
    columns = len(data[rows_start].split(','))
    nearby_tickets_list = np.zeros(shape=(rows, columns), dtype=np.int)
    for i in range(rows_start, rows_end):
        nearby_tickets_list[i - rows_start, :] = data[i].split(',')
    return nearby_tickets_list


def get_valid_set(a_1: list, b_1: list, a_2: list, b_2: list) -> set:
    valid_set = set()
    for i in range(len(a_1)):
        set_1 = list(range(a_1[i], b_1[i] + 1))
        set_2 = list(range(a_2[i], b_2[i] + 1))
        valid_set.update(set_1)
        valid_set.update(set_2)
    return valid_set


def part_one(data: list) -> (np.ndarray, int):
    definition_name, a_1, b_1, a_2, b_2 = ticket_definitions(data)
    nearby_tickets = get_nearby_tickets(data)
    valid_set = get_valid_set(a_1, b_1, a_2, b_2)
    rows = nearby_tickets.shape[0]
    cols = nearby_tickets.shape[1]
    valid_tickets_idx = []
    invalid_sum = 0
    for i in range(rows):
        valid_flag = True
        for j in range(cols):
            if nearby_tickets[i, j] not in valid_set:
                invalid_sum = invalid_sum + nearby_tickets[i, j]
                valid_flag = False
        if valid_flag:
            valid_tickets_idx.append(i)
    valid_tickets = nearby_tickets[valid_tickets_idx, :]
    return valid_tickets, invalid_sum


def part_two(data: list, valid_tickets: np.ndarray) -> np.int64:
    definition_name, a_1, b_1, a_2, b_2 = ticket_definitions(data)
    my_ticket = get_my_ticket(data)

    # Build validity array
    rows = valid_tickets.shape[0]
    cols = valid_tickets.shape[1]
    validity = np.ones(shape=(cols, cols), dtype=np.int)
    for k in range(cols):
        valid_set = set()
        set_1 = list(range(a_1[k], b_1[k] + 1))
        set_2 = list(range(a_2[k], b_2[k] + 1))
        valid_set.update(set_1)
        valid_set.update(set_2)
        for j in range(cols):
            for i in range(rows):
                if valid_tickets[i, j] not in valid_set:
                    validity[k, j] = 0
                    break
    del i, j, k, a_1, b_1, a_2, b_2, cols, data, rows, set_1, set_2, valid_set, valid_tickets

    # Find which columns correspond to which fields
    field_order = []
    columns_order = []
    definition_name_copy = definition_name.copy()
    columns = list(range(0, len(validity)))
    while len(validity) > 0:
        for i in range(len(validity)):
            if sum(validity[:, i]) == 1:
                columns_order.append(columns[i])
                idx = np.where(validity[:, i] == 1)[0][0]
                field_order.append(definition_name_copy[idx])
                del columns[i]
                del definition_name_copy[idx]
                validity = np.delete(validity, i, axis=1)
                validity = np.delete(validity, idx, axis=0)
                break
    field_column = dict(zip(field_order, columns_order))
    del i, idx, validity, field_order, columns_order, definition_name_copy, columns

    # Find departure fields of own tickets and multiply them together
    field_multiplier: np.int64 = 1
    for name in definition_name:
        if 'departure' in name:
            idx = field_column[name]
            field_multiplier = np.int64(field_multiplier * my_ticket[idx])
    return field_multiplier


def main():
    valid_tickets, invalid_sum = part_one(get_input())
    print('The ticket scanning error rate is:', invalid_sum)
    print('If you multiply all six departure values together you get:', part_two(get_input(), valid_tickets))


if __name__ == '__main__':
    main()
