
# индекс при вызове из списка начинается с "0",
# также последний элемент списка можно отсчитывать индекс с "-1"
m = [1, 2, 2, 3, 34, 'e', [1,3,'stroka']]

# длина списка 7 несмотря на то, что индексы считаются с "0"
# по номеру длины НЕ вызывают значения в списке только индекс
print(len(m))

# список в списке ВНИМАНИЕ!!! на индексы
print(m[-1][2])

# меняем данные в списке
m[0] = 22
print(m)

n = list('stroka')
print(n)

r = list( range(10))
s = []
for i in r:
    if i == 8:
        continue
    s += [i]

else:        
    print(s)