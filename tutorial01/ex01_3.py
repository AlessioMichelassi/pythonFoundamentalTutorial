pi = 3.14159
radius = input("Inserisci il raggio: ")

try:
   radius = float(radius)  # Prova a convertire la stringa in un intero
   area = pi * (radius ** 2)
   print("L'area del cerchio è:", area)
except Exception:
   print(f"Sei sicuro che '{radius}' sia un numero?")