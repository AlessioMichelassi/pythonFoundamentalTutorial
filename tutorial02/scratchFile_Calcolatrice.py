
def checkOperation(splitCharacter, question):
    """
    Controlla l'operazione da fare.
    :param splitCharacter: il carattere da usare per dividere la domanda.
    :param question: la domanda da controllare.
    :return: il risulta dell'operazione o un messaggio di errore.
    """
    splitQuestion = question.split(splitCharacter)
    if len(splitQuestion) <= 2:
        try:
            if splitCharacter == "+":
                return f"{float(splitQuestion[0].strip()) + float(splitQuestion[1].strip())}"
            elif splitCharacter == "-":
                return f"{float(splitQuestion[0].strip()) - float(splitQuestion[1].strip())}"
            elif splitCharacter == "*":
                return f"{float(splitQuestion[0].strip()) * float(splitQuestion[1].strip())}"
            elif splitCharacter == "/":
                return f"{float(splitQuestion[0].strip()) / float(splitQuestion[1].strip())}"
            elif splitCharacter == "^":
                return f"{float(splitQuestion[0].strip()) ** float(splitQuestion[1].strip())}"
            else:
                return "operazione non valida"
        except ValueError:
            return f"L'input non è un numero valido. {question}"

isWannaContinue = True
while isWannaContinue:
    question = input("Inserisci il calcolo: ")
    if question.lower() == "exit":
        isWannaContinue = False
        break
    elif "+" in question:
        print(checkOperation("+", question))
    elif "-" in question:
        print(checkOperation("-", question))
    elif "*" in question:
        print(checkOperation("*", question))
    elif "/" in question:
        print(checkOperation("/", question))
    elif "^" in question:
        print(checkOperation("^", question))
