# # Функция 1
numbers = [1, 5, 3, 9, 2]
def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)
print(find_max(numbers))

# # Функция 2
numbers = [1, 2, 3, 4, 5, 6]
def filter_even(numbers):
    return [x for x in numbers if x % 2 == 0]
print(filter_even(numbers))

# # Функция 3
words = ['a', 'b', 'b', 'a']
def is_palindrome(words):
    return words == words[::-1]
print(is_palindrome(words))

# # Функция 4
def count_vowels(text):
    vowels = "аеёиоуыэюя"
    text = text.lower()
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Программирование"))

# Функция 5
list1 = [1, 2, 3]
list2 = [3, 4, 5]
def merge_lists_unique(list1, list2):
    return list(set(list1 + list2))
print(merge_lists_unique(list1, list2))
