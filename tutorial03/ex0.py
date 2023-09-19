alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

findChar = "m"
for i in range(len(alphabet)):
    if findChar == alphabet[i]:
        print(f"ho trovato {findChar} alla posizione {i}")
        break

findChar = "m"
for i in alphabet:
    if findChar == i:
        print(f"ho trovato {findChar} alla posizione {alphabet.index(i)}")
        break