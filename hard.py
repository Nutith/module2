QUEST_NUMBERS = tuple(range(3, 21))
CYPHER_NUMBERS = tuple(range(1, 21))


def create_cypher_numbers_pairs(quest_number, cypher_numbers):
    result = []

    for i in cypher_numbers:
        for j in cypher_numbers:
            if j == quest_number or i == quest_number:
                continue

            if i == j:
                continue

            if (j, i) in result:
                continue

            result.append((i, j))

    return result


def find_cypher(quest_number, cypher_numbers_pairs):
    result = ''

    for i, j in cypher_numbers_pairs:
        if quest_number % (i + j) == 0:
            result = f'{result}{i}{j}'

    return result


for n in QUEST_NUMBERS:
    pairs = create_cypher_numbers_pairs(n, CYPHER_NUMBERS)
    print(f'{n} - {find_cypher(n, pairs)}')

# while True:
#     n = input('Введите число со вставки или 0 (ноль) для выхода: ')
#
#     if n.isdigit():
#         n = int(n)
#     else:
#         print('-- Нужно вводить только числа. Попробуйте еще раз.')
#         continue
#
#     if n == 0:
#         break
#
#     if n in QUEST_NUMBERS:
#         pairs = create_cypher_numbers_pairs(n, CYPHER_NUMBERS)
#         print(f'Число: {n} Шифр: {find_cypher(n, pairs)}')
#     else:
#         print('-- Не похоже на число со вставки, попробуйте еще раз.')
#         continue
