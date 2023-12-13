# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.


num_list = [int(input()) for _ in range(int(input("Введите количество чисел в списке: ")))]
num_count = {}

for num in num_list:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

pair_count = sum(count // 2 for count in num_count.values())
print("Количество пар: ", pair_count)
