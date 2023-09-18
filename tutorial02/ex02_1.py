isWannaContinue = True
while isWannaContinue:
    question = input("Inserisci il calcolo: ")
    if question.lower() == "exit":
        isWannaContinue = False
        break
    elif "+" in question:
        splitQuestion = question.split("+")
        if len(splitQuestion) == 2:
            try:
                returnString = f"{float(splitQuestion[0].strip()) + float(splitQuestion[1].strip())}"
                print(f"Il risultato di {question} = {returnString}")
            except ValueError:
                print(f"L'input non è un numero valido. {question}")
    elif "-" in question:
        splitQuestion = question.split("-")
        if len(splitQuestion) == 2:
            try:
                returnString = f"{float(splitQuestion[0].strip()) - float(splitQuestion[1].strip())}"
                print(f"Il risultato di {question} = {returnString}")
            except ValueError:
                print(f"L'input non è un numero valido. {question}")

    elif "*" in question:
        splitQuestion = question.split("*")
        if len(splitQuestion) == 2:
            try:
                returnString = f"{float(splitQuestion[0].strip()) * float(splitQuestion[1].strip())}"
                print(f"Il risultato di {question} = {returnString}")
            except ValueError:
                print(f"L'input non è un numero valido. {question}")

    elif "/" in question:
        splitQuestion = question.split("/")
        if len(splitQuestion) == 2:
            try:
                returnString = f"{float(splitQuestion[0].strip()) / float(splitQuestion[1].strip())}"
                print(f"Il risultato di {question} = {returnString}")
            except ValueError:
                print(f"L'input non è un numero valido. {question}")

    elif "^" in question:
        splitQuestion = question.split("^")
        if len(splitQuestion) == 2:
            try:
                returnString = f"{float(splitQuestion[0].strip()) ** float(splitQuestion[1].strip())}"
                print(f"Il risultato di {question} = {returnString}")
            except ValueError:
                print(f"L'input non è un numero valido. {question}")
