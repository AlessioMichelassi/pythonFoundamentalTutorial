"""
Ecco un esempio di come funziona il metodo della bisezione per trovare la radice quadrata di un numero SS:

    Seleziona un intervallo [a,b][a,b] tale che a2≤S≤b2a2≤S≤b2.
    Calcola il punto medio mm dell'intervallo: m=a+b2m=(2a+b)/2.
    Se m2m2 è sufficientemente vicino a SS, allora mm è una buona approssimazione della radice quadrata
    di SS e l'algoritmo termina.
    Altrimenti, se m2<Sm2<S, allora la soluzione deve trovarsi nell'intervallo [m,b][m,b]. Se m2>Sm2>S,
    allora la soluzione deve trovarsi nell'intervallo [a,m][a,m].
    Ripeti i passi da 2 a 4 utilizzando il nuovo intervallo.
"""


def bisection_sqrt(S, tolerance=1e-10):
    """Calcola la radice cuba di S usando il metodo della bisezione."""

    # Definisci gli estremi dell'intervallo
    lowBoundary = 0
    highBoundary = max(1, S)  # Considera il caso in cui S < 1
    num_guesses = 0
    while (highBoundary - lowBoundary) > tolerance:
        guess = (lowBoundary + highBoundary) / 2  # Punto medio dell'intervallo

        if guess ** 3 < S:
            lowBoundary = guess
        else:
            highBoundary = guess
        num_guesses += 1
    return (lowBoundary + highBoundary) / 2, num_guesses


# Test della funzione
S = 10000
root, num_guesses = bisection_sqrt(S)
print(f"Radice quadrata di {S} approssimata con bisezione: {root} in {num_guesses}")
