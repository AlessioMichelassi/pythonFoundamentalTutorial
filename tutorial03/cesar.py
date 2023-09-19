def caesarCipher(text, shift):
    """
    Cifra un testo usando il cifrario di Cesare.

    :param text: testo da cifrare
    :param shift: numero di posizioni da shiftare ogni lettera
    :return: testo cifrato
    """

    encryptedText = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for char in text:
        # Se il carattere fa parte dell'alfabeto calcola il suo indice
        # altrimenti lo lascia invariato
        if char in alphabet:
            index = alphabet.index(char.lower())
            # Se lo shift fa andare fuori dalla lunghezza alfabeto, ricomincia dall'inizio
            if index + shift >= len(alphabet):
                index = (index + shift) - len(alphabet)
            else:
                index += shift
            encryptedText += alphabet[index]

        else:
            encryptedText += char

    return encryptedText


def descript(text, shift):
    decryptedText = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for char in text:
        if char in alphabet:
            index = alphabet.index(char.lower())
            if index - shift < 0:
                index = (index - shift) + len(alphabet)
            else:
                index -= shift
            decryptedText += alphabet[index]
        else:
            decryptedText += char
    return decryptedText


def mainLoop():
    isWannaContinue = True
    while isWannaContinue:
        text = input("Inserisci il testo da cifrare: ")
        if text.lower() == "exit":
            isWannaContinue = False
            break
        elif text.lower() == "decifra":
            text = input("Inserisci il testo da decifrare: ")
            shift = int(input("Inserisci lo shift (numero di posizioni da spostare): "))
            print(f"Testo decifrato: {descript(text, shift)}")
        else:
            shift = int(input("Inserisci lo shift (numero di posizioni da spostare): "))
            encrypted = caesarCipher(text, shift)
            print(f"Testo cifrato: {encrypted}")


if __name__ == "__main__":
    mainLoop()
