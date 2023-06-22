# n = list( range(10))
# m = []
# for i in n:
#     if i == 8:
#         continue
#     m += [i]

# else:        
#     print(m)

x = [9, 8, 6, 5]
x.append(4)
x.insert(1, 7)
print(x.count(7))
x.sort()
x.reverse()
y = x.pop(0)
print(y)
x.remove(7)
x.clear()
x.extend(['a', 'd'])
h = x.copy()
print(h)
print(x)