pi = 3.14159
isWannaContinue = True

while isWannaContinue:
    radius = input("Inserisci il raggio: (o 'exit' per uscire):")
    if radius == "exit":
        isWannaContinue = False
    else:
        try:
            radius = float(radius)
            area = pi * (radius ** 2)
            print("L'area del cerchio è:", area)
        except Exception:
            print(f"Sei sicuro che '{radius}' sia un numero?")
            continue
exit()
