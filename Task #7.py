def process_number(num):
    if 1 <= num <= 9:
        return f"{num} - {num ** 2}"
    elif 10 <= num <= 99:
        return f"{num} - {(num // 10) * (num % 10)}"
    elif 100 <= num <= 999:
        return f"{num} - {int(str(num)[::-1])}"
    return "Число не в диапазоне от 1 до 999."

try:
    num = int(input("Введите число от 1 до 999: "))
    print(process_number(num))
except ValueError:
    print("Ошибка ввода. Введите целое число.")