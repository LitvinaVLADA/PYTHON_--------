# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

N = int(input('Введите число-границу: '))

i = 1
result = []

while i < 1000000:
    step = 2 ** i
    if step <= N:
        result.append(step)
        i += 1
    else:
        break

print(result)