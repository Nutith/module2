my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0

while i < len(my_list):
    list_item = my_list[i]
    i = i + 1

    if list_item == 0:
        continue

    if list_item < 0:
        break

    print(list_item)