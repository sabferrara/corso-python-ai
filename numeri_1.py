numeri = [5,12,26,30,20,9,14,209]
#creare una nuova lista solo con i numeri maggiori di 10 e divisi per 2 (filtraggio e trasformazione)
risultato =[]

for num in numeri:
    if num > 10:
        risultato.append(num/2)
print(risultato)

#perchè non posso modificare la lista mentre la sto attraversando? il ciclo si basa su una sequnìenza ordinata di elementi.
