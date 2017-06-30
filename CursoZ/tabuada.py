# tabuada 1 a 10 #################################
tabuada = 1

while tabuada <= 10:
    print()
    print('Tabuada do %d' % tabuada)
    x = 1
    while x <= 10:
        valor = tabuada * x
        print('%d x %d = %d' % (tabuada, x, valor))
        x = x + 1
    tabuada = tabuada + 1