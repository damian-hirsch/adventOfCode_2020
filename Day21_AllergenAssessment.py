import numpy as np
import re


def get_input():
    with open('Input/Day21_AllergenAssessment.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def transform_data(data: list) -> (dict, set):
    foods = {}
    allergens = set()
    for data_line in data:
        allergen_line = re.findall(r'\(contains (.*)\)', data_line)
        allergens_line = allergen_line[0].split(', ')
        allergens.update(allergens_line)

        food_line = re.findall(r'(.*) \(', data_line)
        food_line = food_line[0].split(' ')
        for food_item in food_line:
            foods[food_item] = foods.get(food_item, 0) + 1

    return foods, allergens


def part_one(data: list, foods: dict, allergens: set) -> (int, np.ndarray):
    allergen_food_list = np.ones((len(allergens), len(foods)))
    food_keys = list(foods.keys())
    allergens_keys = list(allergens)
    for data_line in data:
        allergen_line = re.findall(r'\(contains (.*)\)', data_line)
        allergens_line = allergen_line[0].split(', ')
        food_line = re.findall(r'(.*) \(', data_line)
        food_line = food_line[0].split(' ')
        index_food = np.zeros(len(foods))
        for food in food_line:
            indices_food_line = food_keys.index(food)
            index_food[indices_food_line] = 1
        for allergen in allergens_line:
            index_allergen = allergens_keys.index(allergen)
            allergen_food_list[index_allergen, :] = np.multiply(allergen_food_list[index_allergen, :], index_food)

    allergen_food_list_solution = [True] * len(foods)
    food_summation = 0
    for i in range(len(allergen_food_list_solution)):
        allergen_food_list_solution[i] = bool(max(allergen_food_list[:, i]))
        if not allergen_food_list_solution[i]:
            food_summation = food_summation + foods[food_keys[i]]
    return food_summation, allergen_food_list


def part_two(allergen_food_list: np.ndarray, foods: list, allergens: list) -> str:
    # Remove good foods
    for_deletion = []
    for i in range(len(foods)):
        if sum(allergen_food_list[:, i]) == 0:
            for_deletion.append(i)
    for j in sorted(for_deletion, reverse=True):
        del foods[j]
        allergen_food_list = np.delete(allergen_food_list, j, axis=1)
    del i, j, for_deletion

    allergens_final = []
    foods_final = []
    while len(allergens) > 0:
        for k in range(len(allergens)):
            if sum(allergen_food_list[:, k]) == 1:
                foods_final.append(foods[k])
                idx = np.where(allergen_food_list[:, k] == 1)[0][0]
                allergens_final.append(allergens[idx])
                del foods[k]
                del allergens[idx]
                allergen_food_list = np.delete(allergen_food_list, k, axis=1)
                allergen_food_list = np.delete(allergen_food_list, idx, axis=0)
                break
    new_order = list(np.argsort(allergens_final))
    foods_final = np.array(foods_final)
    foods_final = list(foods_final[new_order])
    food_string = ','.join(foods_final)
    return food_string


def main():
    foods, allergens = transform_data(get_input())
    result1, allergen_food_list = part_one(get_input(), foods, allergens)
    print('Number of times ingredients that cannot possibly contain any of the allergens appear:', result1)
    print('Canonical dangerous ingredient list:', part_two(allergen_food_list, list(foods.keys()), list(allergens)))


if __name__ == '__main__':
    main()
