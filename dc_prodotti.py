prodotti = [
    {'id':1, 'nome':'PC', 'prezzo':999.00},
    {'id':2, 'nome':'Monitor', 'prezzo':699.00},
    {'id':3, 'nome': 'Mouse', 'prezzo':99.00},
    {'id':4, 'nome': 'Tastiera', 'prezzo':129.00},
]

#creiamo un dizionario indicizzato per
#prepariamo i dati: creiamo l'indice. boglio avere una truttura per cui alla chiave 1 abbia il prodotto id 1)
indice = {p ['id']: p for p in prodotti}
#abbia come chiave id del prpdotto
print(indice)

#errori tipici: dimenticarsi dei due punti, confondere il comportamento
# di liste e dizionari, la chiave deve essere sempre unvoca