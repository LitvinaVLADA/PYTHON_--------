# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.

# Код Вани

n = int(input())
max_number = 1000
while n != 0:         # ошибка тут. нет проверки на первый встреченный ноль
    n = int(input())
    if max_number > n:
        max_number = n
print(max_number)

# исправленный кода Вани:

max_number = 1000
n = int(input())
while n != 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)

# Код Пети:

n = int(input())
max_number = -1
while n < 0:           # ошибка тут. должно быть while n != 0: 
    n = int(input())
    if max_number < n:   # ошибка тут. должно быть max_number = n, чтобы обновить значение max_number
        n = max_number
print(n)

# Исправленный код Пети:

max_number = -1
n = int(input())
while n != 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)


# у Вани 1 ошибка, помечена комментарием. У Пети 2 ошибки, помечены комментариями. Значит выиграл Ваня. 