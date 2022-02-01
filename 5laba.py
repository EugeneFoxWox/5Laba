def sbor():
    while True:
        baschny = int(input('Введите кол-во башен от 3 до 10 --> '))
        if 3 <= baschny <= 10 :
            break
        else:
            print('Введите значение в заданных пределах! \n ', '-'*40)
    return baschny


def sbor2():
    while True:
        rings = int(input('Введите кол-во башен от 3 до 20 --> '))
        if 3 <= rings <= 20:
            break
        else:
            print('Введите значение в заданных пределах! \n ', '-'*40)
    return rings


sbor()
sbor2()
