try:
    numero = int(input('Inserisci un numero:'))
    numero_2 = int(input('Inserisci un altro numero:'))
    print('Risultato:',numero/ numero_2)
except ValueError:
    print('numero invalido')
except ZeroDivisionError:
    print('non puoi dividere per 0')
#es. 9-0
else:
    print("Divisione completata con successo")
finally:
    print("Qualsiasi cosa succede io vengo eseguito")