string1 = "E' una bella giornata!"

string2 = 'Lui ha detto: "Ciao!"'

string3 = '''Questo è un esempio
di una stringa
su più righe.'''

string4 = """Un altro esempio
di una stringa
su più righe."""

def checkOperation(stringOperation):
    """
    Controllo se l'operazione è una somma, sottrazione, moltiplicazione, divisione o potenza.
    :param stringOperation:
    :return:
    """
    try:
        if "+" in stringOperation:
            parts = stringOperation.split("+")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            return operandA + operandB
        elif "-" in stringOperation:
            parts = stringOperation.split("-")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            return operandA - operandB
        elif "*" in stringOperation:
            parts = stringOperation.split("*")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            return operandA * operandB
        elif "/" in stringOperation:
            parts = stringOperation.split("/")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            if operandB != 0:
                return operandA / operandB
            else:
                return "Divisione per zero!"
        elif "^" in stringOperation:
            parts = stringOperation.split("^")
            operandA = getValueFromInputOrMemory(parts[0].strip())
            operandB = getValueFromInputOrMemory(parts[1].strip())
            return operandA ** operandB
        else:
            return "Operazione non riconosciuta."
    except ValueError:
        return f"Valore non valido in '{stringOperation}'"

























