"""
PREPOCESSING
fate un modello per predire se un cliente puo accedere a un prestito o no.
variabili da tenere in cosniderazione (colonne):
- eta
-reddito annuo
- numero debiti
- credit score
-approvazione
dobbiamo estrarre il dato che ci servira per dire al nostro algoritmo
'guarda che approvi il credito solo in questi casi'
'impara a capire quando un finanziamneto viene autorizzato e decidi in autonomia'
feature: sono le prime 4
target(esito)(dato sul quale devo lavorare): l'ultima colonna
"""

import numpy as np
np.random.seed(42)

dataset = np.array([
    [25,30000, 2,650, 1],
    [45,80000, 1,720, 1],
    [35,50000, 5,580, 0],
    [23,25000, 3, 600, 0],
    [52, 120000, 0, 800, 1],
    [40, 70000, 4, 610, 0]
])

#separiamo il dataset in x e y
x = dataset[:, :-1]   #prediamo tutte le righe e tutte le colonne tranne l'ultima (tutte le feature)
y = dataset[:,-1]   #tutte le righe e solo l'ultima colonna (il target)

#calcoliamo minimo e massimo di ogni colonna, solo su x
minimo = np.min(x, axis=0)
massimo = np.max(x, axis=0)
#si adattano a x che ha sape 6 x4

X_norm = (x - minimo) / (massimo - minimo)
print(X_norm)
#feature normalizzate, stiamo creando una sorta di dataset sui quali i pattern decisionali
# del nostro modello potrebbe iniziare a leggere meglio i dati e capire,
# in base ai valori normalizzati, quali potrebbe essere un pattern ideale
# affichè possa decidere se concedere o meno il prestito

#deve capire che piu sono alti ral e credit score, piu è probabile che esce 1.

"""
1--> separazione feature e target
2 --> normalizzare feature
3 --> creare 
estraiamo una colonna relativa al reddito [colonna 1] estriamo pure colonna debiti [2], e creiamo 
una nuova feature che mia dia il rapporto di debiti/reddito
"""

reddito = x[:, 1]  #tutte le righe tranne la colonna numero 1
debito = x[:, 2]

rapporto_debiti = debito / reddito  #otteniamo un vettore
print(rapporto_debiti)

#inizia a capire che nel caso in cui siamo prossimi allo zero, abbiamo dei risultati molto vicini a 1
#aggiungiamo una feature per creare nuova colonna, con reshape: mi faccio 6 righe e 1 colonna

rapporto_debiti = rapporto_debiti.reshape(-1,1)  #aggiungimo questa colonna alla nostra matrice

x_enhanced = np.hstack(( X_norm,rapporto_debiti)) #matrice che passsa per ml
print(x_enhanced)

indices = np.arange(len(x_enhanced))#per creare un array da utilizzare come indici
#train test split simulati
np.random.shuffle(indices) #randomizziamo il dataset

train_size = int(len(indices) * 0.8) # calcolare quanti elementi vanno in training, che sono l'80%.
# 80% viene preso come train, il restane 20% come test per confrontare

train_idx = indices[:train_size]
test_idx = indices[train_size:] #primi 8 sono per i training, ultimi 2 sono di test

#0,1,5,2 dataset di train
# colonne 4 e 3 formano la matrice di test

x_train = x_enhanced[train_idx] #mi sono diviso il dataset passando gli indici quello che va in train e quello che va in test
x_test = x_enhanced[test_idx]

y_train = y[train_idx]
y_test = y[test_idx]
print(y_train)

#abbiamo creato 4 dataset

#ora dobbiamo passare questi dati inun modello di machine learnijg in corso di addestramento che deve cercare di capire
#perche con questi dati escono quelli risultati, e poi prova. Se i risultati del test sono corretti, allra
#hai trovato un modello attraverso cui posso decidere se dare a un soggetto un finanziamento, in base ai dati che abbiamo.

"""
matrice numerica --> features
il modello moltpilica le feature per un peso, somma il tutto e arriva al risultato. 
Noi interveniamo nel punto in cui deve decidere quali sono i pesi da utilizzare.

normalizzazione = viene utilizzata quando il modello si sbilancia, cosi viene normalizzato tra 0 e 1 in modo 
tale che le feature abbiano lo stesso peso. 
"""