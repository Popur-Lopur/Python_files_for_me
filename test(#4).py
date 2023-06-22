def season():
    x = input('Введите месяц года: ')
    if x == 12 or x == 1 or x == 2:
         
         print("winter")
         return 'winter'
    elif x == 3 or x == 4 or x == 5:
         
         print("spring")
         return 'spring'
    elif x == 6 or x == 7 or x == 8:
         
         print("summer")
         return 'summer'
    elif x == 9 or x == 10 or x == 11:
         
         print("autmun")
         return 'autmun'
    else:
         print("Error")
         return 'Error'

season()
