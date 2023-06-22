def exclusive_item(*args, key = True):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key == True:
        new_list.sort()

    return new_list


z = [9,8,7]
x = [8,8,5,6,4,3,]
c = [1,3,4,52,4,24,3]

t = exclusive_item(z,x,c, )
print(t)