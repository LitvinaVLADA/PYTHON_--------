# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.


numb_list = input("Введите числа через пробел: ").split()
border = int(input('Введите количество сдвигаемых символов: '))
print ('Изначальный список ',numb_list)

help_list = numb_list[:border]
numb_list = numb_list[border:]
numb_list += help_list
print('Итоговый список ',numb_list)
