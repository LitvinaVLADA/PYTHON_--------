# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).


N = int(input('Введите количество чисел: '))
def reverse_sequence(N): 
    if N == 0:
        return
    current_element = int(input())
    reverse_sequence(N-1)
    print(current_element)

reverse_sequence(N)