a = input("Введіть арифметичний вираз не більше 2 чисел (наприклад, 23+12): ")
for i in "+-*/":
    if i in a:
        num1, num2 = a.split(i)
        num1, num2 = float(num1), float(num2)
        if i == "+":
            result = num1 + num2
        elif i == "-":
            result = num1 - num2
        elif i == "*":
            result = num1 * num2
        elif i == "/":
            if num2 == 0:
                result = "Помилка: ділення на нуль!"
            else:
                result = num1 / num2
        break
else:
    result = "Помилка: неправильний вираз!"
print("Результат:", result)
