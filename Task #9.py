for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(i, i + 4):
            if k <= 9:
                print(f"{k} * {j} = {k * j}", end="\t")
        print()  # Переход на следующую строку
    print()  # Пустая строка между группами