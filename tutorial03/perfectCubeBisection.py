def is_perfect_cube(S, tolerance=1e-10):
    """Verifica se S è un cubo perfetto e restituisce la sua radice cubica se lo è."""

    # Definisci gli estremi dell'intervallo
    lowBoundary = 0
    highBoundary = max(1, S)  # Considera il caso in cui S < 1
    while (highBoundary - lowBoundary) > tolerance:
        guess = (lowBoundary + highBoundary) / 2  # Punto medio dell'intervallo

        if guess ** 3 < S:
            lowBoundary = guess
        else:
            highBoundary = guess

    # Stima della radice cubica
    estimated_root = (lowBoundary + highBoundary) / 2

    # Verifica se il numero S è (approssimativamente) il cubo di estimated_root
    if abs(estimated_root ** 3 - S) < tolerance:
        return True, estimated_root
    else:
        return False, None

# Test della funzione
S = 8
is_cube, root = is_perfect_cube(S)
if is_cube:
    print(f"{S} è un cubo perfetto di {root}.")
else:
    print(f"{S} non è un cubo perfetto.")