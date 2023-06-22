price = {'tomato': 3.2, 'meat': 5, 'bread': 6}
new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 1)

print(new_price)
# print(new_price)
# new = {}
# for key, value in price.items():
#     print(key)
#     print(value)
#     new[value] = key
# print(new)


for val in price.values():
    print(val)
for ke in price.keys():
    print(ke)    