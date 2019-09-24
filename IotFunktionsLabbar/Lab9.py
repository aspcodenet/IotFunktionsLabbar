
def isVowel(character):
    lista = ["a", "o", "u", "å", "e", "i", "y", "ä", "ö"]
    return character.lower() in lista

print(isVowel("A"))
print(isVowel("r"))
