"""
Задание 2.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
number = int(input("Ведите целое положительное число: "))
max_number = 0
while number > 0:
    if max_number < number % 10:
        max_number = number % 10
    number //= 10
print(f"Самая большая цифра в числе: {max_number}")