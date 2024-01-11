import random

def beker():
    paros_szam: int= int(input("Kérek egy páros számot! "))
    while not(paros_szam % 2 == 0):
            paros_szam: int= int(input("Ez nem páros! PÁROS számot kérek! "))
    return paros_szam

    """while not(paros_szam % 2 == 0) == 3:"""
def bekerb():
    i: int= 1
    paros_szam: int= int(input(f"Kérem az {i}. páros számot! "))
    while not(paros_szam % 2 == 0) == 3:
        if paros_szam % 2 == 0:
            paros_szam: int= int(input(f"Kérem az {i+1}. páros számot! "))
            i += 1
        else:
             paros_szam: int= int(input(f"Ez nem PÁROS! Kérem az {i}. páros számot! "))
    return paros_szam.append(paros_lista)

paros_lista=[]
def bekerc(paros_lista):
    min = 0
    for i in range(0, len(paros_lista), 1):
        if paros_lista[i] <= paros_lista[min]:
            min = i
    print(f"{i}. lépésben adta meg a legkisebb páros számot, melynek értéke {min}")
    return paros_lista[i]

def veletlen():
    veletlen_lista=[]
    for i in range(0, 13, 1):
        szam: int= random.randint(-40,150)
        veletlen_lista.append(szam)
    return veletlen_lista

def ketjegyuek_szama(lista):
    ketjegyuek: int= 0
    for i in range(0, len(lista), 1):
        if 100 > lista[i] > 9 or lista[i] < (-9):
            ketjegyuek += 1
    return ketjegyuek

def paros_osszege(lista):
    parosok: int= 0
    ossz: int= 0
    for i in range(0, len(lista), 1):
        if lista[i] % 2 == 0:
            parosok += 1
            ossz += lista[i]
    return ossz

def paratlan_osszege(lista):
    paratlanok: int= 0
    ossz: int= 0
    for i in range(0, len(lista), 1):
        if lista[i] % 2 != 0:
            paratlanok += 1
            ossz += lista[i]
    return ossz

def nagyobb(lista):
    paros= lista
    paratlan= lista
    if paros > paratlan:
        print(">")
    else:
        print("<")
    
def stadionok():
    """"""