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
    return paros_szam
        
def bekerc(paros_szamok):
    paros_lista=[]
    
