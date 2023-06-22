d1 = {'tomato': 1, 'bread': 2}
d2 = dict(tomato = 3, bread = 4, water = 1)
d3 = dict([['tomato', 5],['bread', 6]])
d4 = dict.fromkeys(['tomato', 'bread'], 7)

print(d1)
print(d2)
print(d3)
print(d4)


users = {
    'Vova': {'password': 1234, 'id': 4325},
    'Tolik': {'password': 5643, 'id': 4534},
    'Dima': {'password': 3256, 'id': 9806}
    }

print(users['Dima']['password'])

print(d1.items())
print(d1.keys())
print(d1.values())
d1.update(d2)
print(d1)
