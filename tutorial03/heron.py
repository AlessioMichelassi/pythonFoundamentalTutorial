def sqrt_heronsAlgorithm(number, tolerance=0.00001):
    """
    Calcola la radice quadrata di un numero usando l'algoritmo di Erone.

    :param number: Numero di cui calcolare la radice quadrata.
    :param tolerance: Tolleranza per la convergenza dell'algoritmo.
    :return: Radice quadrata approssimata del numero.
    """

    # Stima iniziale
    guess = number / 2.0
    num_guesses = 0
    while True:
        # Calcola una nuova stima
        new_guess = 0.5 * (guess + number / guess)
        # Verifica la convergenza
        if abs(new_guess - guess) < tolerance:
            print(f"Numero di tentativi: {num_guesses}")
            return new_guess

        guess = new_guess
        num_guesses += 1


# Esempio d'uso
number = 15.625
print(sqrt_herons_algorithm(number))