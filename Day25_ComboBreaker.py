def get_input() -> list:
    with open('Input/Day25_ComboBreaker.txt', 'r') as file:
        data = file.read().splitlines()
    return data


def decrypt(key: int, subject_number: int, divisor: int) -> int:
    value = 1
    counter = 0
    while value != key:
        value = (value * subject_number) % divisor
        counter = counter + 1
    return counter


def encrypt(loops: int, subject_number: int, divisor: int) -> int:
    value = 1
    for i in range(loops):
        value = (value * subject_number) % divisor
    return value


def part_one(data: list) -> int:
    subject_number = 7
    divisor = 20201227
    card_key = int(data[0])
    door_key = int(data[1])
    loops1 = decrypt(card_key, subject_number, divisor)
    loops2 = decrypt(door_key, subject_number, divisor)
    encryption_key1 = encrypt(loops1, door_key, divisor)
    encryption_key2 = encrypt(loops2, card_key, divisor)
    if encryption_key1 == encryption_key2:
        return encryption_key1
    else:
        print('Error: Encryption')


def main():
    print('The handshake encryption key is:', part_one(get_input()))


if __name__ == '__main__':
    main()
