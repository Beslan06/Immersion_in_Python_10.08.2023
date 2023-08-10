def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))

try:
    number = int(input("Введите число (от 2 до 100000): "))
    if 2 <= number <= 100000:
        print(f"{number} - {'простое' if is_prime(number) else 'составное'} число.")
    else:
        print("Число должно быть от 2 до 100000.")
except ValueError:
    print("Ошибка ввода. Введите целое число.")