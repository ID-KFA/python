"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

t = 1


def sum_row(i, s=1):
    """Считает сумму элементов ряда"""
    global t
    if i < 2:
        return print(f", их сумма - {t}")
    s *= -0.5
    t += s
    sum_row(i - 1, s)
    return None


n = int(input("Введите количество элементов ряда: "))
print(f"Количество элементов -{n}", end="")
sum_row(n)
