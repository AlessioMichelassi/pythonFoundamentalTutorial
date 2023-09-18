# Creare una calcolatrice che esegua le 4 operazioni base (+, -, *, /) e la potenza (^).
# La calcolatrice deve essere in grado di memorizzare dei valori e di richiamarli con un nome.
# Ad esempio, se inserisco "x = 5", la calcolatrice deve memorizzare il valore 5 con il nome "x".
# Se poi scrivo "x + 3", la calcolatrice deve restituire 8.
# Per memorizzare un valore, l'utente deve scrivere "mem" e seguire le istruzioni.
# Per uscire, l'utente deve scrivere "exit".
memories = {}


def checkOperation(question):
    # sourcery skip: assign-if-exp
    """
    Controllo se l'operazione è una somma, sottrazione, moltiplicazione, divisione o potenza.
    :param question:
    :return:
    """
    try:
        if "+" in question:
            parts = question.split("+")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            return operandA + operandB
        elif "-" in question:
            parts = question.split("-")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            return operandA - operandB
        elif "*" in question:
            parts = question.split("*")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            return operandA * operandB
        elif "/" in question:
            parts = question.split("/")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            if operandB != 0:
                return operandA / operandB
            else:
                return "Divisione per zero!"
        elif "^" in question:
            parts = question.split("^")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            return operandA ** operandB
        else:
            return "Operazione non riconosciuta."
    except ValueError:
        return f"Valore non valido in '{question}'"


def putInMemories():
    mem = input("Inserisci il nome della memoria ad es: x = 5 o pi = 3.14: ")
    parts = mem.split("=")
    if len(parts) == 2:
        try:
            memories[parts[0].strip()] = float(parts[1].strip())
        except ValueError:
            print(f"Il valore {parts[1]} non è un numero.")


def getValueFromInputOrMemory(value):
    """
    Controlla se il valore è presente nella memoria, altrimenti lo restituisce come float.
    :param value:
    :return:
    """
    if value in memories:
        return memories[value]
    else:
        return float(value)


isWannaContinue = True
while isWannaContinue:
    question = input("Inserisci il calcolo: ")
    if question.lower() == "exit":
        isWannaContinue = False
    elif question.lower() == "mem":
        putInMemories()
    else:
        print(checkOperation(question))
