from random import randint

NUM_ATTEMPTS = 10
target_number = randint(0, 1000)

for attempt in range(NUM_ATTEMPTS):
    guess = int(input(f"Попытка {attempt + 1}/{NUM_ATTEMPTS}: Введите предположение: "))
    
    if guess < target_number:
        print("Больше.")
    elif guess > target_number:
         print("Меньше.")
    else:
        print("Поздравляем! Вы угадали число!")
        break
else:
    print("Попытки закончились. Загаданное число:", target_number)






# from random import randint

# n, t = randint(0, 1000), 10

# for _ in range(t):
#     g = int(input(f"Попытка {_ + 1}/{t}: "))
#     print(["Больше.", "Меньше.", f"Поздравляем! Вы угадали число! {n}"][g < n] if g != n else f"Попытки закончились. Загаданное число: {n}")
#     if g == n: break
