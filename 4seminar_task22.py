# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств

first_set_size = int(input("Введите размер ПЕРВОГО множества: "))
first_set = set()

for i in range(first_set_size):
    numb = int(input("Введите целое число ПЕРВОГО множества номер {}: ".format(i + 1)))
    first_set.add(numb)

second_set_size = int(input("Введите размер ВТОРОГО множества: "))
second_set = set()

for i in range(second_set_size):
    numb = int(input("Введите целое число ВТОРОГО множества номер {}: ".format(i + 1)))
    second_set.add(numb)

intersection_set = first_set.intersection(second_set)
sorted_list = sorted(intersection_set)
print("В обоих наборах встречаются числа: ", sorted_list)