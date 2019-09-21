def ToPercentage(decimalTal):
    return decimalTal * 100.0


while True:
    tal = float(input("Mata in decimaltal mellan 0-1"))
    if tal <= 1.0 and tal >= 0.0:
        print(ToPercentage(tal))

#diskutera: felhantering/validering - borde ligga I funktionen också eller hur!
