# Требуется найти N-е число Фибоначчи

n = int(input("Введите номер числа Фибоначчи для поиска: "))
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print (fibonacci(n))