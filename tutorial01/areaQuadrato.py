isWannaContinue = True

while isWannaContinue:
    base = input("Inserisci la base: (o 'exit' per uscire):")
    altezza = input("Inserisci l'altezza: (o 'exit' per uscire):")
    if base or altezza == "exit":
        isWannaContinue = False
    else:
        try:
            base = float(base)
            altezza = float(altezza)
            area = base * altezza
            print("L'area del cerchio è:", area)
        except Exception:
            print(f"Sei sicuro che '{base}' o {altezza} sia un numero?")
            continue
exit()