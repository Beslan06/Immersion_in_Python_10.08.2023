rows = int(input("Введите количество рядов для ёлки: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


# rows = int(input("Введите количество рядов для ёлки: "))

# for i in range(1, rows + 1):
#     spaces = " " * (rows - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)
