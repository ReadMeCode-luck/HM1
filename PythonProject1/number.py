#Задание 1

# name ="Daniel"
# print(name)

#Задание 2
# age = int(input("Enter a year: "))
# current_year = 2025
# birth_year = current_year - age
# print(f"Ваш год рождения: {birth_year}")

#Задание 3
# a = float(input("Введите длину: "))
# b = float(input("Введите ширину: "))
# S = (a*b)
# print(f"Площадь треугольника с длиной {a} и шириной {b} ранва {S}")

#Задание 4
# C = int(input("Введите температуру в градусах Цельсия: "))
# F = (C * 9/5) + 32
# print(f"{C}°C = {F}°F")

#Задание 5
# a = int(input("Введите Первое число: "))
# b = int(input("Введите Второе число: "))
# c = int(input("Введите Третие число: "))
# S = (a + b + c) / 3
# S_int = int(S)
# print(f"Найти среднее арифметическое число из 3 чисел: {a}, {b}, {c}. \nОтвет: {S_int}")

#Задание 6
# a = int(input("Введите целое число: "))
# if a % 2 == 0:
#     print(f"Число {a} является чётным потому-что делется без остатка.")
# else:
#     print(f"Число {a} является нечётным потому-что не делется без остатка.")

#Задание 7
# is_student = True
# has_homework = False

# print("Исходные значения:")
# print(f"is_student = {is_student}")
# print(f"has_homework = {has_homework}")
# print()

# print("Результаты логических выражений:")
# print(f"is_student and has_homework = {is_student and has_homework}")
# print(f"is_student or has_homework = {is_student or has_homework}")
# print(f"not is_student = {not is_student}")

#Задание 8
# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')
#1  print(first_name + ' ' + last_name)
#2  print(f"{first_name} {last_name}")

#Задание 9
# num_str = "123"
# print(f"Исходное значение:{num_str}")
# print(f"Тип исходного значения: {type(num_str)}")

# num_int = int(num_str) + 10
# print(f"После преобразования в число и прибавления 10: {num_int}")
# print(f"Тип результата (число + 10): {type(num_int)}")
#
# num_str_again = str(num_int)
# print(f"После обратного преобразования в строку: {num_str_again}")
# print(f"Тип конечного значения: {type(num_str_again)}")

#Задание 10
# login = "admin"
# password = "123456"
# user_login = input("Enter your login name: ")
# user_password = input("Enter your password: ")
# if user_login == login and user_password == password:
#     print("Доступ разрешён")
# else:
#     print("Неверный логин или пароль")
