#Задание 1
# numbers = list(range(1,11))
# squares = [x**2 for x in numbers]
# print("Список квадратов", squares)

#Задание 2
# numbers = list(range(1,21))
# even_numbers = [x for x in numbers if x % 2 == 0]
# print("Четные числа:", even_numbers)

#Задание 3
# words = ["python", "java", "c++"]
# for word in words:
#     print(word)

#Задание 4
# words = ("words12", "words2", "words334", "words4456", "words53221")
# length_words = [(word, len(word)) for word in words]
# print(length_words)

#Задание 5
# number = list(range(1,16))
# numberx2 = [x*2 for x in number]
# print("числа от 1 до 15:", number)
# print("умножаются на 2:", numberx2)

#Задание 6
# numbers = [-6, 3, 5, -7, 4, -5, 12, -3]
# number_smile = [x for x in numbers if x > 0]
# print(number_smile)

#Задание 7
# names = ["Alice", "Bob", "Charlie"]
# create_names = [f"Имя:{name}" for name in names]
# print(create_names)

#Задание 8
# numbers = list(range(1,31))
# krat_numbers = [ x for x in numbers if x % 3 == 0]
# print(krat_numbers)

#Задание 9
# numbers = [1,2,3,4,5,6,7,8,9]
# str_numbers = [str(numbers)]
# print (f"Числа: {type(numbers)} {numbers}")
# print (f"Числа привратили в строки: {type(str_numbers)} {str_numbers}")

# Задание 10
# letters = ['a', 'b', 'c']
# numbers = [1,2,3]
# combinations = [letter + str(number) for letter in letters for number in numbers]
# print(combinations)
