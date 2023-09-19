# Trova se un numero è un cubo perfetto

def findApproxCube(cube):
    """
    Trova se un numero è un cubo perfetto elevando al cubo
    tutti i numeri da 0 al numero passato nei parametri.
    :param cube: numero da controllare
    :return: nothing
    """
    try:
        # trasformo la stringa in un numero
        cube = float(cube)
        isContinue = True
        # definisco la tolleranza
        acceptableError = 0.1
        # definisco il valore di partenza
        guess = 0.0
        # definisco l'incremento
        increment = 0.01
        # definisco il numero di tentativi
        num_guesses = 0

        # cerca una risposta abbastanza vicina e si assicura
        # di non aver saltato accidentalmente il limite abbastanza vicino
        while abs(guess**3 - cube) >= acceptableError and guess <= cube:
            print(f"{abs(guess ** 3 - cube)} >= {acceptableError} and {guess} <= {cube} = {abs(guess**3 - cube) >= acceptableError and guess <= cube}")
            print(f"guess: {guess} += {increment} = {guess + increment}")
            guess += increment
            num_guesses += 1
        print('num_guesses =', num_guesses)
        if abs(guess**3 - cube) >= acceptableError:
            print('Failed on cube root of', cube, "with these parameters.")
        else:
            print(round(guess, 4), 'is close to the cube root of', cube)
    except ValueError:
        print(f"sei sicuro che {cube} sia un numero?")

def findApprox(cube):
    try:
        cube = float(cube)
        guess = 1.0
        for _ in range(int(cube)):
            guess += 0.01
            print(f"guess = {guess} cube of guess = {guess ** 3}")
            if guess ** 3 == cube:
                print(f"{guess}: Cube root of {cube} is {guess}")
                break
            elif guess ** 3 > cube:
                print(f"{cube} is not a perfect cube")
                break
    except ValueError:
        print(f"sei sicuro che {cube} sia un numero?")


def mainApp():
    isWannaContinue = True
    while isWannaContinue:
        cube = input("Enter an integer: ")
        if cube.lower() == "exit":
            isWannaContinue = False
            break
        else:
            findApproxCube(cube)


if __name__ == "__main__":
    mainApp()
