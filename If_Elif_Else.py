import os
while True:
    sayt = input("Введите адресс сайта: ")

    if sayt == "завершить":
        break

    if 'https://' in sayt:
        os.system('start ' + sayt)
        print('if')
    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system ('start ' + sayt)
        print('elif')
    else:
        sayt = 'https://www.' + sayt
        os.system('start ' + sayt)
        print('else')


