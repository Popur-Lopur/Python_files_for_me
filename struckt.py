import math
PI = math.pi
def radius():
    r = float(input('Введите радиус: '))
    r = r / 2
    return r

def height():
    h = float(input('Введите высоту цилиндра: '))
    return h

def volume():
    r = radius()
    h = height()
    v = h * PI * r**2
    return v
print('Объем цилиндра равен: ', volume())

    

