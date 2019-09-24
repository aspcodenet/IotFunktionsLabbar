import enum

class VatCalculation(enum.Enum):
    INK_MOMS = 1
    EX_MOMS = 2


def CalculateVat(belopp, inkEllerExMoms):
    if inkEllerExMoms == VatCalculation.INK_MOMS:
        return belopp * 0.20
    return belopp *0.25






print(CalculateVat(1000, VatCalculation.EX_MOMS))



#Modifiera - lägg till parameter ink/exkl
#               - as string then enum











































