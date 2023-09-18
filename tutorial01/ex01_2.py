pi = 3.14159
radius = input("inserisci il raggio")
if type(radius) == int:
   area = pi * (radius ** 2)
   print(f"L'area del cerchio è:{area}" )
else:
   print(f"sei sicuro che: {radius} - sia un numero?")