import random
lst = [random.randint(-10, 10) for _ in range(20)]
min = lst[0]
max = lst[0]
for num in lst:
    if num < min:
        min = num
    if num > max:
        max = num
negative = 0
positive = 0
zero = 0
for num in lst:
    if num < 0:
        negative += 1
    elif num > 0:
        positive += 1
    else:
        zero += 1
print(f"Список: {lst}")
print(f"Мінімальний елемент: {min}")
print(f"Максимальний елемент: {max}")
print(f"Кількість від'ємних елементів: {negative}")
print(f"Кількість додатних елементів: {positive}")
print(f"Кількість нулів: {zero}")

