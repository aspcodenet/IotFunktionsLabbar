
def sum(talLista):
    sum = 0
    for tal in ordLista:
        sum = sum + tal
    return sum

def multiply(talLista):
    mult = 1
    for tal in ordLista:
        mult = mult  * tal
    return mult


lista = [1,6,3,4]
print(sum(lista))
print(multiply(lista))
