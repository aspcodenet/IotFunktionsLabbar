
def isVowel(char):
    lista = ["a", "o", "u", "å", "e", "i", "y", "ä", "ö"]
    return char.lower() in lista

print(isVowel("A"))
print(isVowel("r"))
