# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

def same_by(characteristic, objects):
    if not objects:
        return True
    
    first_value = characteristic(objects[0])

    return all(characteristic(obj) == first_value for obj in objects)

values = [0, 2, 10, 6] 

if same_by(lambda x: x > 9, values):
    print('same')   
else:
    print('different')
