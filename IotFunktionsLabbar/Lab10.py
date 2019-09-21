
def isVowel(char):
    lista = ["a", "o", "u", "å", "e", "i", "y", "ä", "ö"]
    return char.lower() in lista

def isKonsonant(char):
    return char.isalpha() and not isVowel(char)

def ToRovarsprak(txt):
    retValue = ""
    for ch in txt:
        if isKonsonant(ch):
            retValue = retValue + ch + "o" + ch
        else:
            retValue = retValue + ch
    return retValue

print(ToRovarsprak("this is fun. Do you also think so?"))