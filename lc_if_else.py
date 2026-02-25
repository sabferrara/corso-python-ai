numeri = [1,2,3,4,5,6,7,8,9]

#quando voglio fare una scelta tra due trasformazioni, la struttura cambia.


#es. voglio stampare una cllection che mi dica se il numero è pari o dispari.
#poste le due condizioni a(pari) e b(dispari) [A if condizione else B for elemento in sequenza]

risultato =["pari" if numero % 2 == 0 else "dispari" for numero in numeri] #metto la mia trasformazione
print(risultato)

#non la usiamo quando la logica è complessa, quando il codice e difficile da leggere e
#se serve fare bandling riga per riga. in questo caso servono le funzioni
