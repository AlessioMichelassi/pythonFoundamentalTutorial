"""
Il Teorema di Pitagora riguarda i lati di un triangolo rettangolo.
Se aa e bb sono le lunghezze dei cateti e cc è la lunghezza dell'ipotenusa,
il Teorema di Pitagora afferma che:
a2+b2=c2

Da cui:
c=radiceQuadrata(a2+b2)

Per calcolare l'ipotenusa basandoci sul Teorema di Pitagora,
 possiamo modificare il tuo codice come segue:
"""
import math  # per la funzione sqrt

isWannaContinue = True

while isWannaContinue:
    cateto1 = input("Inserisci il primo cateto (o 'exit' per uscire): ")
    if cateto1 == "exit":
        break
    cateto2 = input("Inserisci il secondo cateto (o 'exit' per uscire): ")
    if cateto2 == "exit":
        break

    try:
        cateto1 = float(cateto1)
        cateto2 = float(cateto2)
        ipotenusa = math.sqrt(cateto1**2 + cateto2**2)
        print(f"L'ipotenusa del triangolo rettangolo con cateti {cateto1} e {cateto2} è: {ipotenusa:.2f}")
    except ValueError:
        print(f"Sei sicuro che '{cateto1}' o '{cateto2}' siano numeri?")
        continue

exit()