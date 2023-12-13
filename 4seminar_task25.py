# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

work_list = input("Введите символы через пробел: ").split()

char_count = {}
result = ""

for char in work_list:
    if char in char_count:
        char_count[char] += 1
        result += f"{char}_{char_count[char]} "
    else:
        char_count[char] = 1
        result += char + " "

print(result)