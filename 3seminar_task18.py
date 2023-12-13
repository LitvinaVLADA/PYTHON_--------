# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

border = int(input('Введите количество элементов в массиве: '))
random_list = [random.randint(1, 100) for _ in range(border)]

find_num = int(input('Введите число от 1 до 100 для поиска ближайшего в массиве: '))

closest_element = min(random_list, key=lambda num: abs(num - find_num))

print("Массив:", random_list)
print("Ближайший элемент к числу X:", closest_element)