# Trova se un numero è un cubo perfetto

def findPerfectCube(cube):
    """
    Trova se un numero è un cubo perfetto elevando al cubo
    tutti i numeri da 0 al numero passato nei parametri.
    :param cube: numero da controllare
    :return: nothing
    """
    try:
        cube = float(cube)
        for guess in range(int(cube) + 1):
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
        else:
            findPerfectCube(cube)
    exit()


if __name__ == "__main__":
    mainApp()
