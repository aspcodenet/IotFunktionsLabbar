
def AddStrings(s1, s2,addSpaceBetween = False):
    if addSpaceBetween:
        return s1 + " " + s2
    return s1+s2


print(AddStrings("Stefan", "Holmberg", True))
print(AddStrings("Stefan", "Holmberg"))

#Modifiera - lägg till parameter add space between