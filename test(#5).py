
money = float(input("Сколько денег зачисляем на счет: "))
years = float(input("На сколько лет делаем счет: "))
days = float(years * 365)
    
result = float(money * 1,1 * days / 365 / 100)
print(result)


