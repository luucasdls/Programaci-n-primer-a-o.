def comun():
    a = [1,2,3,4,5,6,7,8,9]
    b = [2,4,6,8,10,12,14,16]
    comunes = set(a).intersection(b)

    print(comunes)

comun()