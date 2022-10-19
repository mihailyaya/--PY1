list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
h = len(list_numbers) - 1
z = 0
maxim = list_numbers[0]
for i in range(len(list_numbers)):
    if maxim < list_numbers[i]:
        maxim = list_numbers[i]
        z = i
list_numbers[z], list_numbers[h] = list_numbers[h], list_numbers[z]

# TODO Оформить решение

print(list_numbers)
