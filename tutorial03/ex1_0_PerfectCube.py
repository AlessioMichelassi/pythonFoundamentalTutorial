# Trova se un numero è un cubo perfetto
cube = 27
for guess in range(cube + 1):
    print(f"guess = {guess} cube of guess = {guess ** 3}")
    if guess ** 3 == cube:
        print(f"Cube root of {cube} is {guess}")
        break
    elif guess ** 3 > cube:
        print(f"{cube} is not a perfect cube")
        break