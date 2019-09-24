def ToPercentage(decimalTal):
    if tal > 1.0 or tal < 0.0:
        raise ValueError("Fekaktigt tal")
    return decimalTal * 100.0


while True:
    tal = float(input("Mata in decimaltal mellan 0-1"))
    print(ToPercentage(tal))

#diskutera: felhantering/validering - borde ligga I funktionen också eller hur!


s = ToPercentage(10)
