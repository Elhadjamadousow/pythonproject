# EXO3
"""def liste(num = [2,4,7,8,2], nume = [1,3,9,4,6,7]):
    liste = []
    for i in num:
        if i not in nume:
            if i not in liste:
                liste.append(i)
    for i in nume:
        if i not in num:
            if i not in liste:
                liste.append(i)
    return liste
r = liste()
print(r)"""
def mots(mo = "alpha", mot = "mamadou" ):
    nouvo = []
    for i in mo:
        print("saliou")
        print(i)
        for j in mot:
            print("aliou")
            print(j)
            if i == j:
                nouvo.append(i)
                print("resulta")
     print(nouvo)
    return nouvo
resultat = mots()
print(resultat)
