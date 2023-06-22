price = {'tomato': 3.2, 'meat': 5, 'bread': 6}

def buy():
    pay = 0
    while True:
        enter = input('Что будем покупать?\n')

        if enter == 'end':
            break
        pay += price[enter]
    print(pay) 

buy()



        
