a, b, c = sorted(map(float, input("Введите длины сторон через пробел: ").split()))

if a + b > c:
    print("Треугольник существует.")
    if a == b == c:
        print("Треугольник равносторонний.")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный.")
    else:
        print("Треугольник разносторонний.")
else:
    print("Треугольник с такими сторонами не существует.")