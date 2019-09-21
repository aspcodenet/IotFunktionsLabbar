
def HittaLangstaOrdet(ordLista):
    longestSoFar = ""
    for ord in ordLista:
        if len(ord) > len(longestSoFar):
            longestSoFar = ord
    return longestSoFar

lista = ["Stefan", "hej", "Telefonkiosk","apa"]
print(HittaLangstaOrdet(lista))
