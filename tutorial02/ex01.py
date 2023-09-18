isWannaContinue = True
while isWannaContinue:
   nome = input("Inserisci un nome di almeno 5 lettere: ")
   if len(nome) >= 5:
       print(f"Il nome inserito è lungo {len(nome)} lettere.")
       isWannaContinue = False
   else:
       print(f"Il nome inserito è troppo corto. contiene solo {len(nome)} lettere.")
