"""
Задание 1.®

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
name = input("Введите ваше имя: ")
age = input("Сколько вам лет? ")
password = input("Введите пароль: ")
print(f"Ваши данные для входа в аккаунт: Имя — {name}, Возраст — {age}, "
      f"Пароль — {password}")
