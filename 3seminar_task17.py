# Дан список чисел. Определите, сколько в нем встречается различных чисел.

numb_input = input("Введите числа через пробел: ")
numb_list = numb_input.split()

result = set(numb_list)

print(len(result))
