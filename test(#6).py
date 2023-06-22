def first_info():
     num = int(input("Введите число от 0 до 1000: "))
     return num
     
def symple():
          
          k = 0  
          for i in range(2, num // 2 + 1):
               if (num % i == 0):
                    k = k + 1
          if (k <= 0) :  
            # print('True')                                                         
             return True
          else:
            #print('False')                  
            return False

while True:
    num = first_info()
    print(type(num))
    if num > int(1000) or num < int(0):
         print("Error")
         first_info()
    
    
    symple()

    result = symple()

    if result == True:
         print("Число простое")
    elif result == False:
         print ("Число не простое")
    
         




