class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    

def IsMyndig(age):
    return age >= 18


myndig = IsMyndig(int(input("Ange ålder")))
if myndig:
    print("Du är myndig")
else:
    print("Du är inte myndig")


